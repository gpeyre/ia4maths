"""Numerical utilities for stochastic interpolants and flow matching.

The functions are intentionally small and notebook-friendly.  PyTorch is used
for the conditional expectations and ODE integration in the discrete-target
experiment; NumPy is only used for plotting helpers.
"""

from __future__ import annotations

import math
import os
from dataclasses import dataclass
from typing import Iterable

os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")

import numpy as np
import torch


DTYPE = torch.float64


@dataclass(frozen=True)
class ScheduleInfo:
    key: str
    label: str
    color: str


SCHEDULES: tuple[ScheduleInfo, ...] = (
    ScheduleInfo("linear", "linear", "#2f6fbb"),
    ScheduleInfo("vp", "variance preserving", "#d08c2f"),
    ScheduleInfo("cosine", "cosine", "#4f9d69"),
)


def schedule_values(
    t: float | torch.Tensor,
    kind: str,
    *,
    eps: float = 1.0e-6,
    dtype: torch.dtype = DTYPE,
    device: torch.device | None = None,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    """Return a(t), b(t), a'(t), b'(t) as scalar tensors.

    The variance-preserving square-root schedule has endpoint-singular
    derivatives.  We clamp only for numerical evaluation in notebooks.
    """

    tau = torch.as_tensor(t, dtype=dtype, device=device)
    if kind == "linear":
        a = 1.0 - tau
        b = tau
        adot = torch.full_like(tau, -1.0)
        bdot = torch.ones_like(tau)
    elif kind == "vp":
        tau01 = tau.clamp(0.0, 1.0)
        s = tau.clamp(eps, 1.0 - eps)
        a = torch.sqrt(torch.clamp(1.0 - tau01, min=0.0))
        b = torch.sqrt(torch.clamp(tau01, min=0.0))
        adot = -0.5 / torch.sqrt(1.0 - s)
        bdot = 0.5 / torch.sqrt(s)
    elif kind == "cosine":
        theta = 0.5 * math.pi * tau
        a = torch.cos(theta)
        b = torch.sin(theta)
        adot = -0.5 * math.pi * torch.sin(theta)
        bdot = 0.5 * math.pi * torch.cos(theta)
    else:
        raise ValueError(f"Unknown schedule '{kind}'")
    return a, b, adot, bdot


def dirac_points(radius: float = 2.4, *, dtype: torch.dtype = DTYPE) -> torch.Tensor:
    """Three equal-weight Dirac locations on an equilateral triangle."""

    pts = torch.tensor(
        [
            [1.0, 0.0],
            [-0.5, math.sqrt(3.0) / 2.0],
            [-0.5, -math.sqrt(3.0) / 2.0],
        ],
        dtype=dtype,
    )
    return radius * pts


def _as_weights(points: torch.Tensor, weights: torch.Tensor | None) -> torch.Tensor:
    if weights is None:
        return torch.full(
            (points.shape[0],),
            1.0 / points.shape[0],
            dtype=points.dtype,
            device=points.device,
        )
    probs = weights.to(dtype=points.dtype, device=points.device)
    if probs.ndim != 1 or probs.shape[0] != points.shape[0]:
        raise ValueError("weights must be a one-dimensional tensor matching the number of points")
    if torch.any(probs < 0):
        raise ValueError("weights must be nonnegative")
    total = torch.sum(probs)
    if total <= 0:
        raise ValueError("at least one mixture weight must be positive")
    return probs / total


def posterior_weights(
    x: torch.Tensor,
    t: float | torch.Tensor,
    points: torch.Tensor,
    kind: str,
    weights: torch.Tensor | None = None,
    *,
    min_scale: float = 1.0e-5,
) -> torch.Tensor:
    """Return P(X1=y_k | X_t=x) for the discrete target experiment."""

    points = points.to(dtype=x.dtype, device=x.device)
    probs = _as_weights(points, weights)
    a, b, _, _ = schedule_values(t, kind, dtype=x.dtype, device=x.device)
    scale2 = torch.clamp(a * a, min=min_scale**2)
    centered = x[:, None, :] - b * points[None, :, :]
    sqdist = torch.sum(centered * centered, dim=-1)
    logp = torch.log(probs)[None, :] - 0.5 * sqdist / scale2
    return torch.softmax(logp, dim=1)


def log_density(
    x: torch.Tensor,
    t: float | torch.Tensor,
    points: torch.Tensor,
    kind: str,
    weights: torch.Tensor | None = None,
    *,
    min_scale: float = 1.0e-5,
) -> torch.Tensor:
    """Closed-form log density of X_t for the Gaussian-to-Dirac mixture."""

    points = points.to(dtype=x.dtype, device=x.device)
    probs = _as_weights(points, weights)
    a, b, _, _ = schedule_values(t, kind, dtype=x.dtype, device=x.device)
    scale2 = torch.clamp(a * a, min=min_scale**2)
    d = x.shape[-1]
    centered = x[:, None, :] - b * points[None, :, :]
    sqdist = torch.sum(centered * centered, dim=-1)
    normalizer = -0.5 * d * torch.log(2.0 * torch.pi * scale2)
    log_components = torch.log(probs)[None, :] + normalizer - 0.5 * sqdist / scale2
    return torch.logsumexp(log_components, dim=1)


def velocity(
    x: torch.Tensor,
    t: float | torch.Tensor,
    points: torch.Tensor,
    kind: str,
    weights: torch.Tensor | None = None,
) -> torch.Tensor:
    """Conditional expectation velocity E[a'X0+b'X1 | X_t=x]."""

    points = points.to(dtype=x.dtype, device=x.device)
    a, b, adot, bdot = schedule_values(t, kind, dtype=x.dtype, device=x.device)
    gamma = posterior_weights(x, t, points, kind, weights)
    ybar = gamma @ points
    alpha = adot / torch.clamp(a, min=1.0e-5)
    beta = bdot - alpha * b
    return alpha * x + beta * ybar


def integrate_trajectories(
    x0: torch.Tensor,
    points: torch.Tensor,
    kind: str,
    *,
    n_steps: int = 500,
    t0: float = 1.0e-4,
    t1: float = 1.0 - 1.0e-4,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Integrate the probability-flow ODE with a fourth-order Runge-Kutta rule."""

    x = x0.clone()
    ts = torch.linspace(t0, t1, n_steps + 1, dtype=x0.dtype, device=x0.device)
    path = torch.empty((n_steps + 1, *x0.shape), dtype=x0.dtype, device=x0.device)
    path[0] = x
    for i in range(n_steps):
        t = ts[i]
        h = ts[i + 1] - ts[i]
        k1 = velocity(x, t, points, kind)
        k2 = velocity(x + 0.5 * h * k1, t + 0.5 * h, points, kind)
        k3 = velocity(x + 0.5 * h * k2, t + 0.5 * h, points, kind)
        k4 = velocity(x + h * k3, t + h, points, kind)
        x = x + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        path[i + 1] = x
    return ts, path


def nearest_labels(x: torch.Tensor, points: torch.Tensor) -> torch.Tensor:
    """Index of the nearest Dirac point."""

    dist2 = torch.sum((x[:, None, :] - points[None, :, :]) ** 2, dim=-1)
    return torch.argmin(dist2, dim=1)


def ot_trajectories(
    x0: torch.Tensor,
    points: torch.Tensor,
    *,
    n_steps: int = 200,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    """Semi-discrete OT trajectories for the symmetric three-Dirac example."""

    labels = nearest_labels(x0, points)
    target = points[labels]
    ts = torch.linspace(0.0, 1.0, n_steps + 1, dtype=x0.dtype, device=x0.device)
    path = (1.0 - ts[:, None, None]) * x0[None, :, :] + ts[:, None, None] * target[None, :, :]
    return ts, path, labels


def path_lengths(path: torch.Tensor) -> torch.Tensor:
    """Arc length of each trajectory in a path tensor with shape T x N x d."""

    increments = path[1:] - path[:-1]
    return torch.sum(torch.linalg.norm(increments, dim=-1), dim=0)


def spd_matrix_sqrt(mat: torch.Tensor, inverse: bool = False) -> torch.Tensor:
    """Symmetric square root or inverse square root of an SPD matrix."""

    evals, evecs = torch.linalg.eigh(mat)
    evals = torch.clamp(evals, min=1.0e-12)
    powers = torch.rsqrt(evals) if inverse else torch.sqrt(evals)
    return (evecs * powers[None, :]) @ evecs.T


def gaussian_covariance(
    t: float,
    sigma0: torch.Tensor,
    sigma1: torch.Tensor,
    kind: str,
) -> torch.Tensor:
    """Covariance a(t)^2 Sigma0 + b(t)^2 Sigma1."""

    a, b, _, _ = schedule_values(t, kind, dtype=sigma0.dtype, device=sigma0.device)
    return (a * a) * sigma0 + (b * b) * sigma1


def gaussian_velocity_matrix(
    t: float,
    sigma0: torch.Tensor,
    sigma1: torch.Tensor,
    kind: str,
) -> torch.Tensor:
    """Matrix B_t such that the Gaussian interpolant velocity is B_t x."""

    a, b, adot, bdot = schedule_values(t, kind, dtype=sigma0.dtype, device=sigma0.device)
    sigma_t = (a * a) * sigma0 + (b * b) * sigma1
    numerator = (a * adot) * sigma0 + (b * bdot) * sigma1
    return numerator @ torch.linalg.inv(sigma_t)


def gaussian_flow_map(
    t: float,
    sigma0: torch.Tensor,
    sigma1: torch.Tensor,
    kind: str,
) -> torch.Tensor:
    """Closed-form flow map for independent Gaussian endpoints."""

    s0_half = spd_matrix_sqrt(sigma0)
    s0_inv_half = spd_matrix_sqrt(sigma0, inverse=True)
    a, b, _, _ = schedule_values(t, kind, dtype=sigma0.dtype, device=sigma0.device)
    a_mat = s0_inv_half @ sigma1 @ s0_inv_half
    m_t = (a * a) * torch.eye(sigma0.shape[0], dtype=sigma0.dtype, device=sigma0.device) + (b * b) * a_mat
    return s0_half @ spd_matrix_sqrt(m_t) @ s0_inv_half


def gaussian_ot_map(sigma0: torch.Tensor, sigma1: torch.Tensor) -> torch.Tensor:
    """Brenier map from N(0,Sigma0) to N(0,Sigma1)."""

    s0_half = spd_matrix_sqrt(sigma0)
    s0_inv_half = spd_matrix_sqrt(sigma0, inverse=True)
    middle = spd_matrix_sqrt(s0_half @ sigma1 @ s0_half)
    return s0_inv_half @ middle @ s0_inv_half


def ellipse_points(cov: np.ndarray, *, level: float = 2.0, n: int = 240) -> np.ndarray:
    """Return points on the covariance ellipse {x: x^T cov^{-1} x = level^2}."""

    evals, evecs = np.linalg.eigh(cov)
    theta = np.linspace(0.0, 2.0 * np.pi, n)
    circle = np.stack([np.cos(theta), np.sin(theta)], axis=0)
    ellipse = evecs @ (np.sqrt(np.maximum(evals, 0.0))[:, None] * circle)
    return level * ellipse.T


def tensor_to_numpy(items: Iterable[torch.Tensor]) -> list[np.ndarray]:
    return [item.detach().cpu().numpy() for item in items]
