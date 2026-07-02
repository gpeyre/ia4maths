"""Numerical invariant checks for the stochastic-interpolant examples."""

from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "python"))

import torch

from stochastic_interpolants import (
    DTYPE,
    SCHEDULES,
    dirac_points,
    gaussian_covariance,
    gaussian_flow_map,
    gaussian_ot_map,
    gaussian_velocity_matrix,
    log_density,
    nearest_labels,
    posterior_weights,
    schedule_values,
    velocity,
)


torch.set_default_dtype(DTYPE)


def require_close(name: str, actual: torch.Tensor, expected: torch.Tensor, tol: float) -> None:
    err = torch.linalg.norm(actual - expected).item()
    if err > tol:
        raise AssertionError(f"{name}: error {err:.3e} exceeds tolerance {tol:.3e}")
    print(f"{name}: {err:.3e}")


def check_schedule_endpoints() -> None:
    print("\nSchedule endpoint checks")
    for info in SCHEDULES:
        a0, b0, _, _ = schedule_values(0.0, info.key)
        a1, b1, _, _ = schedule_values(1.0, info.key)
        values = torch.stack([a0, b0, a1, b1])
        expected = torch.tensor([1.0, 0.0, 0.0, 1.0], dtype=DTYPE)
        require_close(info.label, values, expected, 1.0e-12)


def check_dirac_continuity_equation() -> None:
    print("\nDirac-mixture continuity-equation residuals")
    points = dirac_points()
    base = torch.tensor(
        [
            [-1.25, -0.65],
            [-0.40, 0.90],
            [0.15, -1.10],
            [0.90, 0.30],
            [1.35, 1.05],
        ],
        dtype=DTYPE,
    )

    for info in SCHEDULES:
        residuals = []
        for t_value in (0.2, 0.5, 0.8):
            for row in base:
                x = row.reshape(1, 2).clone().requires_grad_(True)
                t = torch.tensor(t_value, dtype=DTYPE, requires_grad=True)
                logp = log_density(x, t, points, info.key)[0]
                u = velocity(x, t, points, info.key)[0]

                grad_logp = torch.autograd.grad(
                    logp, x, create_graph=True, retain_graph=True
                )[0][0]
                dlogp_dt = torch.autograd.grad(
                    logp, t, create_graph=True, retain_graph=True
                )[0]

                div_u = torch.zeros((), dtype=DTYPE)
                for j in range(2):
                    div_u = div_u + torch.autograd.grad(
                        u[j], x, create_graph=True, retain_graph=True
                    )[0][0, j]

                residuals.append(dlogp_dt + torch.dot(u, grad_logp) + div_u)

        max_residual = torch.max(torch.abs(torch.stack(residuals))).item()
        print(f"{info.label}: {max_residual:.3e}")
        if max_residual > 2.0e-9:
            raise AssertionError(f"{info.label}: continuity residual too large")


def check_dirac_density_and_posteriors() -> None:
    print("\nDirac-mixture density and posterior checks")
    points = dirac_points()
    x = torch.tensor(
        [
            [-1.4, -0.7],
            [0.0, 0.0],
            [1.1, 0.5],
            [2.4, -1.0],
        ],
        dtype=DTYPE,
    )
    raw_weights = torch.tensor([2.0, 5.0, 3.0], dtype=DTYPE)
    norm_weights = raw_weights / raw_weights.sum()
    for info in SCHEDULES:
        gamma = posterior_weights(x, 0.37, points, info.key, raw_weights)
        require_close(
            f"{info.label} posterior row sums",
            gamma.sum(dim=1),
            torch.ones(x.shape[0], dtype=DTYPE),
            1.0e-12,
        )
        require_close(
            f"{info.label} raw-vs-normalized density",
            log_density(x, 0.37, points, info.key, raw_weights),
            log_density(x, 0.37, points, info.key, norm_weights),
            1.0e-12,
        )
        require_close(
            f"{info.label} raw-vs-normalized posterior",
            posterior_weights(x, 0.37, points, info.key, raw_weights),
            posterior_weights(x, 0.37, points, info.key, norm_weights),
            1.0e-12,
        )

    try:
        posterior_weights(x, 0.37, points, "linear", torch.tensor([1.0, -1.0, 1.0], dtype=DTYPE))
    except ValueError:
        print("invalid negative weights rejected")
    else:
        raise AssertionError("negative mixture weights should be rejected")


def check_ot_cells() -> None:
    print("\nSemi-discrete OT cell check")
    points = dirac_points()
    x = torch.tensor(
        [
            [3.0, 0.1],
            [-2.0, 2.5],
            [-2.0, -2.5],
            [0.5, 0.8],
            [0.5, -0.8],
        ],
        dtype=DTYPE,
    )
    nearest = nearest_labels(x, points)
    linear_scores = torch.argmax(x @ points.T, dim=1)
    if not torch.equal(nearest, linear_scores):
        raise AssertionError("nearest-target cells disagree with angular Laguerre cells")
    print("nearest-target labels agree with equal-weight Laguerre cells")


def check_gaussian_maps() -> None:
    print("\nGaussian flow-map checks")
    theta = torch.tensor(58.0 * torch.pi / 180.0, dtype=DTYPE)
    rotation = torch.stack(
        [
            torch.stack([torch.cos(theta), -torch.sin(theta)]),
            torch.stack([torch.sin(theta), torch.cos(theta)]),
        ]
    )
    sigma0 = torch.tensor([[1.75, 0.34], [0.34, 0.55]], dtype=DTYPE)
    sigma1 = rotation @ torch.diag(torch.tensor([0.24, 3.10], dtype=DTYPE)) @ rotation.T

    for info in SCHEDULES:
        for t in (0.0, 1.0):
            transport = gaussian_flow_map(t, sigma0, sigma1, info.key)
            sigma_t = gaussian_covariance(t, sigma0, sigma1, info.key)
            require_close(
                f"{info.label} endpoint covariance push-forward t={t}",
                transport @ sigma0 @ transport.T,
                sigma_t,
                3.0e-12,
            )

        for t in (0.2, 0.5, 0.8):
            transport = gaussian_flow_map(t, sigma0, sigma1, info.key)
            sigma_t = gaussian_covariance(t, sigma0, sigma1, info.key)
            require_close(
                f"{info.label} covariance push-forward t={t}",
                transport @ sigma0 @ transport.T,
                sigma_t,
                2.0e-10,
            )

            h = 1.0e-6
            d_transport = (
                gaussian_flow_map(t + h, sigma0, sigma1, info.key)
                - gaussian_flow_map(t - h, sigma0, sigma1, info.key)
            ) / (2.0 * h)
            generator = d_transport @ torch.linalg.inv(transport)
            velocity_matrix = gaussian_velocity_matrix(t, sigma0, sigma1, info.key)
            require_close(
                f"{info.label} generator t={t}",
                generator,
                velocity_matrix,
                3.0e-8,
            )

    si_endpoint = gaussian_flow_map(1.0, sigma0, sigma1, "cosine")
    ot_endpoint = gaussian_ot_map(sigma0, sigma1)
    gap = torch.linalg.norm(si_endpoint - ot_endpoint).item()
    if gap < 1.0e-2:
        raise AssertionError("noncommuting Gaussian endpoint maps should differ")
    print(f"noncommuting endpoint-map gap: {gap:.3e}")

    diag0 = torch.diag(torch.tensor([0.7, 2.5], dtype=DTYPE))
    diag1 = torch.diag(torch.tensor([3.0, 0.4], dtype=DTYPE))
    require_close(
        "commuting endpoint maps",
        gaussian_flow_map(1.0, diag0, diag1, "cosine"),
        gaussian_ot_map(diag0, diag1),
        1.0e-12,
    )


def main() -> None:
    check_schedule_endpoints()
    check_dirac_continuity_equation()
    check_dirac_density_and_posteriors()
    check_ot_cells()
    check_gaussian_maps()
    print("\nAll mathematical invariant checks passed.")


if __name__ == "__main__":
    main()
