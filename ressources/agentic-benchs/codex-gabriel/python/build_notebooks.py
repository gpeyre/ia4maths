"""Build the two pedagogical notebooks used by the paper.

The notebooks are generated from this script so their mathematical exposition
and reproducible plotting code remain easy to maintain.
"""

from __future__ import annotations

from pathlib import Path

import nbformat as nbf


ROOT = Path(__file__).resolve().parents[1]
PYTHON_DIR = ROOT / "python"


def md(text: str):
    return nbf.v4.new_markdown_cell(text.strip())


def code(text: str):
    return nbf.v4.new_code_cell(text.strip())


def write_notebook(path: Path, cells: list):
    nb = nbf.v4.new_notebook()
    nb["metadata"] = {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {"name": "python", "pygments_lexer": "ipython3"},
    }
    nb["cells"] = cells
    nbf.write(nb, path)


def dirac_notebook():
    cells = [
        md(
            r"""
# Flow matching from a Gaussian to three Dirac masses

This notebook studies the stochastic interpolant
\[
X_t = a(t)X_0+b(t)X_1,\qquad t\in[0,1],
\]
with \(X_0\sim\mathcal N(0,I_2)\) and \(X_1\), independently of \(X_0\),
uniformly supported on three Dirac masses \(y_1,y_2,y_3\).  The goal is to
visualize the probability-flow velocity
\[
u_t(x)=\mathbb E[\dot a(t)X_0+\dot b(t)X_1\mid X_t=x],
\]
then compare its trajectories with the semi-discrete optimal-transport rays.
"""
        ),
        md(
            r"""
## Closed-form density and conditional velocity

Conditionally on \(X_1=y_k\), the random variable \(X_t\) is Gaussian:
\[
X_t\mid X_1=y_k \sim \mathcal N(b(t)y_k,a(t)^2I_2).
\]
For mixture weights \(\pi_k\), the density is therefore
\[
p_t(x)=\sum_{k=1}^3 \pi_k\,\varphi_{a(t)^2I_2}(x-b(t)y_k).
\]
Bayes' formula gives the posterior responsibility
\[
\gamma_k(x,t)=
\frac{\pi_k\exp\left(-\frac{\|x-b(t)y_k\|^2}{2a(t)^2}\right)}
{\sum_{\ell=1}^3\pi_\ell\exp\left(-\frac{\|x-b(t)y_\ell\|^2}{2a(t)^2}\right)}.
\]
Since \(X_0=(X_t-b(t)X_1)/a(t)\) whenever \(a(t)>0\),
\[
u_t(x)=\frac{\dot a(t)}{a(t)}x+
\left(\dot b(t)-\frac{\dot a(t)b(t)}{a(t)}\right)
\sum_{k=1}^3\gamma_k(x,t)y_k .
\]
All evaluations below use PyTorch tensors, including the posterior weights and
Runge-Kutta integration of the ODE \(\dot x_t=u_t(x_t)\).
"""
        ),
        code(
            r"""
import os
from pathlib import Path
import sys

os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")

PROJECT_ROOT = Path.cwd()
if PROJECT_ROOT.name == "python":
    PROJECT_ROOT = PROJECT_ROOT.parent
sys.path.insert(0, str(PROJECT_ROOT / "python"))

FIG_DIR = PROJECT_ROOT / "paper" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import torch

from stochastic_interpolants import (
    DTYPE,
    SCHEDULES,
    dirac_points,
    integrate_trajectories,
    log_density,
    nearest_labels,
    ot_trajectories,
    path_lengths,
    velocity,
)

torch.set_default_dtype(DTYPE)
torch.manual_seed(7)

plt.rcParams.update({
    "figure.dpi": 140,
    "savefig.dpi": 240,
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.18,
    "legend.frameon": False,
})

palette = np.array(["#3666a6", "#d17c2f", "#4b9a62"])
points = dirac_points()
points_np = points.numpy()
points
"""
        ),
        md(
            r"""
## The three interpolation schedules

We compare three common choices satisfying the same endpoint constraints:
\[
\begin{array}{c|cc}
\text{schedule} & a(t) & b(t)\\
\hline
\text{linear} & 1-t & t\\
\text{variance preserving} & \sqrt{1-t} & \sqrt t\\
\text{cosine} & \cos(\pi t/2) & \sin(\pi t/2).
\end{array}
\]
They induce the same terminal law, but not the same time-dependent velocity
field or sample trajectories.  The square-root schedule has singular endpoint
derivatives, so the numerical ODE is evaluated on
\([10^{-4},1-10^{-4}]\).
"""
        ),
        code(
            r"""
def draw_targets(ax):
    ax.scatter(points_np[:, 0], points_np[:, 1], s=95, c=palette, marker="*", edgecolor="black", linewidth=0.6, zorder=5)
    for k, y in enumerate(points_np):
        ax.text(y[0] + 0.08, y[1] + 0.08, f"$y_{k+1}$", color=palette[k], weight="bold")


def set_equal_panel(ax, title=None):
    ax.set_aspect("equal")
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-3.1, 3.1)
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    if title:
        ax.set_title(title)


grid_1d = torch.linspace(-3.6, 3.6, 135)
xx, yy = torch.meshgrid(grid_1d, grid_1d, indexing="xy")
flat = torch.stack([xx.reshape(-1), yy.reshape(-1)], dim=1)

fig, axes = plt.subplots(1, 3, figsize=(11.8, 3.65), constrained_layout=True)
for ax, t in zip(axes, [0.15, 0.50, 0.85]):
    dens = torch.exp(log_density(flat, t, points, "linear")).reshape(xx.shape).numpy()
    levels = np.linspace(0.0, dens.max(), 18)[1:]
    ax.contourf(xx.numpy(), yy.numpy(), dens, levels=levels, cmap="Blues", alpha=0.86)
    stride = 11
    sample = torch.stack([xx[::stride, ::stride].reshape(-1), yy[::stride, ::stride].reshape(-1)], dim=1)
    vel = velocity(sample, t, points, "linear").numpy()
    ax.quiver(
        sample[:, 0].numpy(),
        sample[:, 1].numpy(),
        vel[:, 0],
        vel[:, 1],
        color="#203040",
        alpha=0.70,
        width=0.0032,
        scale=36,
    )
    draw_targets(ax)
    set_equal_panel(ax, rf"linear schedule, $t={t:.2f}$")

fig.suptitle("Closed-form density and conditional expectation velocity", y=1.04)
fig.savefig(FIG_DIR / "dirac_density_velocity.pdf", bbox_inches="tight")
plt.show()
"""
        ),
        md(
            r"""
The contours above are not kernel estimates. They are the exact Gaussian
mixture density \(p_t\), and the arrows are the conditional expectation
velocity evaluated by PyTorch from the posterior weights \(\gamma_k(x,t)\).
"""
        ),
        code(
            r"""
n_samples = 150
x0 = torch.randn(n_samples, 2, dtype=DTYPE)

paths = {}
stats = []
for info in SCHEDULES:
    ts, path = integrate_trajectories(x0, points, info.key, n_steps=520)
    labels = nearest_labels(path[-1], points)
    lengths = path_lengths(path)
    endpoint_error = torch.linalg.norm(path[-1] - points[labels], dim=1)
    paths[info.key] = (ts, path, labels, lengths, endpoint_error)
    stats.append((info.label, lengths.mean().item(), lengths.std().item(), endpoint_error.mean().item()))

print("schedule                  mean arc length   std arc length   mean endpoint error")
for row in stats:
    print(f"{row[0]:26s} {row[1]:15.4f} {row[2]:16.4f} {row[3]:20.4e}")
"""
        ),
        code(
            r"""
fig, axes = plt.subplots(1, 3, figsize=(12.2, 3.85), constrained_layout=True)
for ax, info in zip(axes, SCHEDULES):
    _, path, labels, _, _ = paths[info.key]
    path_np = path.numpy()
    labels_np = labels.numpy()
    for i in range(n_samples):
        col = palette[labels_np[i]]
        ax.plot(path_np[:, i, 0], path_np[:, i, 1], color=col, alpha=0.34, linewidth=0.9)
        ax.scatter(path_np[0, i, 0], path_np[0, i, 1], color=col, s=5, alpha=0.22)
    draw_targets(ax)
    set_equal_panel(ax, info.label)

legend_handles = [
    Line2D([0], [0], color=palette[k], lw=2, label=rf"converges to $y_{k+1}$")
    for k in range(3)
]
axes[-1].legend(handles=legend_handles, loc="lower right", fontsize=8)
fig.suptitle("Probability-flow trajectories colored by terminal Dirac", y=1.04)
fig.savefig(FIG_DIR / "dirac_schedule_comparison.pdf", bbox_inches="tight")
plt.show()
"""
        ),
        md(
            r"""
Although the endpoint law is identical, the schedules bend time differently.
The linear schedule rapidly contracts noise while translating toward the
posterior mean. The square-root and cosine schedules keep more variance at
intermediate times, producing visibly different curvature before the terminal
collapse.
"""
        ),
        code(
            r"""
ts_ot, path_ot, labels_ot = ot_trajectories(x0, points, n_steps=220)
length_ot = path_lengths(path_ot)

fig, ax = plt.subplots(figsize=(4.7, 4.15), constrained_layout=True)
path_ot_np = path_ot.numpy()
labels_ot_np = labels_ot.numpy()
for i in range(n_samples):
    col = palette[labels_ot_np[i]]
    ax.plot(path_ot_np[:, i, 0], path_ot_np[:, i, 1], color=col, alpha=0.33, linewidth=0.9)
    ax.scatter(path_ot_np[0, i, 0], path_ot_np[0, i, 1], color=col, s=5, alpha=0.22)
draw_targets(ax)
set_equal_panel(ax, "semi-discrete OT rays")
fig.savefig(FIG_DIR / "dirac_ot_trajectories.pdf", bbox_inches="tight")
plt.show()

print(f"OT mean arc length: {length_ot.mean().item():.4f}")
"""
        ),
        md(
            r"""
For this equilateral, equal-weight target, the semi-discrete OT Laguerre cells
have equal dual weights by rotational symmetry.  Because the three targets have
the same norm, these Laguerre cells reduce to the nearest-vertex cones.  OT
therefore sends each source point to its nearest Dirac mass and interpolates
along a straight segment.  The stochastic-interpolant probability flow is
different: it is a deterministic flow with the same marginal endpoints, but it
is not constrained to be the Brenier transport map at \(t=1\).
"""
        ),
        code(
            r"""
names = ["OT"] + [info.label for info in SCHEDULES]
means = [length_ot.mean().item()] + [paths[info.key][3].mean().item() for info in SCHEDULES]
errs = [0.0] + [paths[info.key][3].std().item() for info in SCHEDULES]

fig, ax = plt.subplots(figsize=(6.8, 3.2), constrained_layout=True)
bar_colors = ["#69707a"] + [info.color for info in SCHEDULES]
ax.bar(np.arange(len(names)), means, yerr=errs, color=bar_colors, alpha=0.86, capsize=3)
ax.set_xticks(np.arange(len(names)), names, rotation=12, ha="right")
ax.set_ylabel("mean trajectory arc length")
ax.set_title("Path length contrast with semi-discrete OT")
fig.savefig(FIG_DIR / "dirac_path_length_comparison.pdf", bbox_inches="tight")
plt.show()
"""
        ),
    ]
    write_notebook(PYTHON_DIR / "flow_matching_dirac_mixture.ipynb", cells)


def gaussian_notebook():
    cells = [
        md(
            r"""
# Gaussian covariance paths for stochastic interpolants

This notebook generates the covariance ellipse figures used in the paper and
checks the closed-form map for independent Gaussian endpoints.  Let
\[
X_0\sim\mathcal N(0,\Sigma_0),\qquad
X_1\sim\mathcal N(0,\Sigma_1)
\]
be independent and \(X_t=a(t)X_0+b(t)X_1\).  Then
\[
\Sigma_t=\operatorname{Cov}(X_t)=a(t)^2\Sigma_0+b(t)^2\Sigma_1.
\]
The conditional expectation velocity is linear,
\[
u_t(x)=B_tx,\qquad
B_t=(a\dot a\,\Sigma_0+b\dot b\,\Sigma_1)\Sigma_t^{-1}.
\]
"""
        ),
        md(
            r"""
## Closed-form flow map

Set
\[
A=\Sigma_0^{-1/2}\Sigma_1\Sigma_0^{-1/2},
\qquad
M_t=a(t)^2I+b(t)^2A.
\]
Since \(M_t\) and \(\dot M_t\) commute, the linear flow generated by \(B_t\)
has the explicit solution
\[
T_t=\Sigma_0^{1/2}M_t^{1/2}\Sigma_0^{-1/2}.
\]
At \(t=1\), this map sends \(\Sigma_0\) to \(\Sigma_1\), but it is generally
not symmetric and therefore generally not the Gaussian optimal-transport map.
"""
        ),
        code(
            r"""
import os
from pathlib import Path
import sys

os.environ.setdefault("KMP_DUPLICATE_LIB_OK", "TRUE")

PROJECT_ROOT = Path.cwd()
if PROJECT_ROOT.name == "python":
    PROJECT_ROOT = PROJECT_ROOT.parent
sys.path.insert(0, str(PROJECT_ROOT / "python"))

FIG_DIR = PROJECT_ROOT / "paper" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import torch

from stochastic_interpolants import (
    DTYPE,
    SCHEDULES,
    ellipse_points,
    gaussian_covariance,
    gaussian_flow_map,
    gaussian_ot_map,
)

torch.set_default_dtype(DTYPE)
plt.rcParams.update({
    "figure.dpi": 140,
    "savefig.dpi": 240,
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.18,
    "legend.frameon": False,
})
"""
        ),
        code(
            r"""
theta = np.deg2rad(58.0)
R = torch.tensor(
    [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]],
    dtype=DTYPE,
)

sigma0 = torch.tensor([[1.75, 0.34], [0.34, 0.55]], dtype=DTYPE)
sigma1 = R @ torch.diag(torch.tensor([0.24, 3.10], dtype=DTYPE)) @ R.T

print("Sigma0 =")
print(sigma0.numpy())
print("Sigma1 =")
print(sigma1.numpy())
print("commutator Frobenius norm:", torch.linalg.norm(sigma0 @ sigma1 - sigma1 @ sigma0).item())
"""
        ),
        code(
            r"""
t_values = np.linspace(0.0, 1.0, 6)
fig, axes = plt.subplots(1, 3, figsize=(12.1, 3.7), constrained_layout=True)

for ax, info in zip(axes, SCHEDULES):
    for j, t in enumerate(t_values):
        cov = gaussian_covariance(float(t), sigma0, sigma1, info.key).numpy()
        ell = ellipse_points(cov, level=2.0)
        color = plt.cm.viridis(j / (len(t_values) - 1))
        ax.plot(ell[:, 0], ell[:, 1], color=color, lw=2.0, alpha=0.95)
    ax.set_aspect("equal")
    ax.set_xlim(-4.4, 4.4)
    ax.set_ylim(-4.4, 4.4)
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("$x_2$")
    ax.set_title(info.label)

legend_handles = [
    Line2D([0], [0], color=plt.cm.viridis(j / (len(t_values) - 1)), lw=2, label=f"t={t:.1f}")
    for j, t in enumerate(t_values)
]
axes[-1].legend(handles=legend_handles, loc="upper right", fontsize=8)
fig.suptitle(r"Covariance ellipses for $\Sigma_t=a(t)^2\Sigma_0+b(t)^2\Sigma_1$", y=1.04)
fig.savefig(FIG_DIR / "gaussian_covariance_ellipses.pdf", bbox_inches="tight")
plt.show()
"""
        ),
        code(
            r"""
T_si = gaussian_flow_map(1.0, sigma0, sigma1, "cosine")
T_ot = gaussian_ot_map(sigma0, sigma1)

print("Stochastic-interpolant endpoint map:")
print(T_si.numpy())
print("\nGaussian OT map:")
print(T_ot.numpy())
print("\n||T_si Sigma0 T_si^T - Sigma1||_F =", torch.linalg.norm(T_si @ sigma0 @ T_si.T - sigma1).item())
print("||T_ot Sigma0 T_ot^T - Sigma1||_F =", torch.linalg.norm(T_ot @ sigma0 @ T_ot.T - sigma1).item())
print("||T_si - T_ot||_F =", torch.linalg.norm(T_si - T_ot).item())
print("symmetry defect ||T_si - T_si^T||_F =", torch.linalg.norm(T_si - T_si.T).item())
"""
        ),
        code(
            r"""
angles = torch.linspace(0.0, 2.0 * torch.pi, 33, dtype=DTYPE)[:-1]
ell0 = ellipse_points(sigma0.numpy(), level=2.0)
ell1 = ellipse_points(sigma1.numpy(), level=2.0)

evals0, evecs0 = torch.linalg.eigh(sigma0)
sigma0_sqrt = (evecs0 * torch.sqrt(evals0)[None, :]) @ evecs0.T
unit = torch.stack([torch.cos(angles), torch.sin(angles)], dim=1)
source_curve = 2.0 * (unit @ sigma0_sqrt.T)
si_curve = source_curve @ T_si.T
ot_curve = source_curve @ T_ot.T

fig, ax = plt.subplots(figsize=(5.2, 4.35), constrained_layout=True)
ax.plot(ell0[:, 0], ell0[:, 1], color="#69707a", lw=2, label=r"source ellipse")
ax.plot(ell1[:, 0], ell1[:, 1], color="#202020", lw=2.3, label=r"target ellipse")
ax.plot(si_curve[:, 0], si_curve[:, 1], "o", ms=3.8, color="#d17c2f", alpha=0.82, label=r"$T_1$ from interpolant")
ax.plot(ot_curve[:, 0], ot_curve[:, 1], "x", ms=4.5, color="#3666a6", alpha=0.82, label=r"Gaussian OT map")
for p, q in zip(source_curve[::4].numpy(), si_curve[::4].numpy()):
    ax.plot([p[0], q[0]], [p[1], q[1]], color="#d17c2f", alpha=0.28, lw=0.8)
for p, q in zip(source_curve[2::4].numpy(), ot_curve[2::4].numpy()):
    ax.plot([p[0], q[0]], [p[1], q[1]], color="#3666a6", alpha=0.28, lw=0.8)
ax.set_aspect("equal")
ax.set_xlim(-4.4, 4.4)
ax.set_ylim(-4.4, 4.4)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_title("Endpoint maps both match covariance, but differ as maps")
ax.legend(loc="lower left", fontsize=8)
fig.savefig(FIG_DIR / "gaussian_endpoint_maps.pdf", bbox_inches="tight")
plt.show()
"""
        ),
    ]
    write_notebook(PYTHON_DIR / "gaussian_covariance_ellipses.ipynb", cells)


def main():
    PYTHON_DIR.mkdir(parents=True, exist_ok=True)
    dirac_notebook()
    gaussian_notebook()
    print("Wrote notebooks:")
    print(" - python/flow_matching_dirac_mixture.ipynb")
    print(" - python/gaussian_covariance_ellipses.ipynb")


if __name__ == "__main__":
    main()
