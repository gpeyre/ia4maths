"""Generate the unit-distance construction figure used in the slides.

The figure is intentionally pedagogical:

- the first row shows the classical integer-grid mechanism;
- the second row sketches the richer norm-one translation strategy behind
  the OpenAI/Sawin/Emmerich line of examples.

It is not meant to reproduce the full arithmetic certificate. The output is a
compact visual for a talk.
"""

from __future__ import annotations

import argparse
import math
import os
import tempfile
from pathlib import Path

if "MPLCONFIGDIR" not in os.environ:
    mpl_cache = Path(tempfile.gettempdir()) / "mpl-ia4maths"
    mpl_cache.mkdir(parents=True, exist_ok=True)
    os.environ["MPLCONFIGDIR"] = str(mpl_cache)

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.patches import FancyArrowPatch


def normalize_points(points: np.ndarray) -> np.ndarray:
    pts = np.asarray(points, dtype=float)
    lo = pts.min(axis=0)
    hi = pts.max(axis=0)
    center = 0.5 * (lo + hi)
    span = max(float((hi - lo).max()), 1e-12)
    return 1.66 * (pts - center) / span


def integer_unit_vectors(q: int) -> list[tuple[int, int]]:
    r = int(math.isqrt(q))
    vectors: list[tuple[int, int]] = []
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1):
            if dx * dx + dy * dy == q and (dx > 0 or (dx == 0 and dy > 0)):
                vectors.append((dx, dy))
    return vectors


def classical_grid_graph(m: int, q: int) -> tuple[np.ndarray, np.ndarray]:
    scale = math.sqrt(q)
    raw = np.array([(i, j) for i in range(m) for j in range(m)], dtype=float) / scale
    index = {(i, j): i * m + j for i in range(m) for j in range(m)}
    edges: list[tuple[int, int]] = []
    for dx, dy in integer_unit_vectors(q):
        for i in range(m):
            for j in range(m):
                p = (i + dx, j + dy)
                if p in index:
                    edges.append((index[(i, j)], index[p]))
                p = (i + dx, j - dy)
                if dy != 0 and p in index:
                    edges.append((index[(i, j)], index[p]))
    return raw, np.asarray(edges, dtype=int)


def projected_norm_one_graph(k: int) -> tuple[np.ndarray, np.ndarray]:
    # Deterministic, slightly incommensurable angles avoid too much overlap.
    golden = (math.sqrt(5) - 1) / 2
    angles = np.sort((0.17 + np.arange(k) * golden * math.pi) % math.pi)
    directions = np.column_stack([np.cos(angles), np.sin(angles)])

    points = np.zeros((2**k, 2))
    for mask in range(2**k):
        bits = np.array([(mask >> j) & 1 for j in range(k)], dtype=float)
        points[mask] = bits @ directions

    edges: list[tuple[int, int]] = []
    for mask in range(2**k):
        for j in range(k):
            if ((mask >> j) & 1) == 0:
                edges.append((mask, mask | (1 << j)))
    return points, np.asarray(edges, dtype=int)


def edge_subset(edges: np.ndarray, max_edges: int | None) -> np.ndarray:
    if max_edges is None or len(edges) <= max_edges:
        return edges
    idx = np.linspace(0, len(edges) - 1, max_edges, dtype=int)
    return edges[idx]


def draw_graph(
    ax: plt.Axes,
    points: np.ndarray,
    edges: np.ndarray,
    line_color: str,
    point_color: str,
    max_edges: int | None = None,
) -> None:
    pts = normalize_points(points)
    shown_edges = edge_subset(edges, max_edges)
    segs = pts[shown_edges]
    lc = LineCollection(segs, colors=line_color, linewidths=0.52, alpha=0.42, zorder=1)
    ax.add_collection(lc)
    size = max(5.0, 13.5 * (90 / len(points)) ** 0.28)
    ax.scatter(
        pts[:, 0],
        pts[:, 1],
        s=size,
        color=point_color,
        edgecolor="white",
        linewidth=0.16,
        alpha=0.94,
        zorder=3,
    )
    ax.set_aspect("equal")
    ax.set_xlim(-1.0, 1.0)
    ax.set_ylim(-1.0, 1.0)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor("#fbfbf8")
    for spine in ax.spines.values():
        spine.set_color("#d7d8dc")
        spine.set_linewidth(0.75)


def make_figure(language: str = "fr") -> plt.Figure:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 12,
            "axes.titlesize": 13,
            "axes.labelsize": 11,
        }
    )

    classical_specs = [(9, 5), (15, 65), (25, 65)]
    human_specs = [5, 6, 7]

    fig, axes = plt.subplots(2, 3, figsize=(6.65, 4.55), constrained_layout=False)
    fig.patch.set_facecolor("white")
    plt.subplots_adjust(left=0.108, right=0.985, top=0.855, bottom=0.08, wspace=0.08, hspace=0.16)

    for ax, (m, q) in zip(axes[0], classical_specs):
        points, edges = classical_grid_graph(m, q)
        draw_graph(ax, points, edges, "#c9872a", "#263238", max_edges=1350)

    for ax, k in zip(axes[1], human_specs):
        points, edges = projected_norm_one_graph(k)
        draw_graph(ax, points, edges, "#1f91b4", "#34215f", max_edges=None)

    labels = {
        "fr": {"grid": "grille", "emmerich": "Emmerich", "increase": "n augmente"},
        "en": {"grid": "grid", "emmerich": "Emmerich", "increase": "n increases"},
    }.get(language, {"grid": "grid", "emmerich": "Emmerich", "increase": "n increases"})

    fig.text(
        0.088,
        0.655,
        labels["grid"],
        ha="center",
        va="center",
        rotation=90,
        fontsize=13,
        fontweight="normal",
        color="#9a681e",
    )
    fig.text(
        0.088,
        0.285,
        labels["emmerich"],
        ha="center",
        va="center",
        rotation=90,
        fontsize=13,
        fontweight="normal",
        color="#1f7894",
    )
    fig.text(
        0.56,
        0.925,
        labels["increase"],
        ha="center",
        va="center",
        fontsize=13,
        fontweight="normal",
        color="#30343b",
    )
    arrow = FancyArrowPatch(
        (0.43, 0.892),
        (0.69, 0.892),
        transform=fig.transFigure,
        arrowstyle="-|>",
        mutation_scale=12,
        linewidth=0.9,
        color="#6c757d",
    )
    fig.add_artist(arrow)
    return fig


def default_output_dirs(repo_root: Path) -> list[Path]:
    slide_root = repo_root / "slides"
    candidates = sorted(slide_root.glob("*/assets/generated"))
    if candidates:
        return candidates
    return [repo_root / "slides" / "fr" / "assets" / "generated"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--language",
        choices=["auto", "fr", "en"],
        default="auto",
        help="Label language. With 'auto', slides/fr uses French and all other decks use English.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        action="append",
        help="Directory where unit_distance_series.{png,pdf} should be written. "
        "Can be passed several times. Defaults to every slides/*/assets/generated directory.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    output_dirs = args.output_dir or default_output_dirs(repo_root)
    for outdir in output_dirs:
        deck_name = outdir.resolve().parents[1].name if len(outdir.resolve().parents) > 1 else ""
        language = "fr" if args.language == "auto" and deck_name == "fr" else args.language
        if language == "auto":
            language = "en"
        fig = make_figure(language=language)
        outdir.mkdir(parents=True, exist_ok=True)
        png_path = outdir / "unit_distance_series.png"
        pdf_path = outdir / "unit_distance_series.pdf"
        fig.savefig(png_path, dpi=260, bbox_inches="tight", pad_inches=0.02)
        fig.savefig(pdf_path, bbox_inches="tight", pad_inches=0.02)
        print(f"saved {png_path}")
        print(f"saved {pdf_path}")


if __name__ == "__main__":
    main()
