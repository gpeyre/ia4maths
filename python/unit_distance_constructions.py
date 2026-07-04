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
from functools import lru_cache
from pathlib import Path

if "MPLCONFIGDIR" not in os.environ:
    mpl_cache = Path(tempfile.gettempdir()) / "mpl-ia4maths"
    mpl_cache.mkdir(parents=True, exist_ok=True)
    os.environ["MPLCONFIGDIR"] = str(mpl_cache)

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyArrowPatch


METHOD_SLUGS = ["grid", "openai", "sawin", "emmerich"]
SHOWCASE_MIN_N = 64
SHOWCASE_MAX_N = 65536
SHOWCASE_MIN_FRAMES = 28


def shared_n_schedule(frames: int, min_n: int = SHOWCASE_MIN_N, max_n: int = SHOWCASE_MAX_N) -> np.ndarray:
    count = max(frames, SHOWCASE_MIN_FRAMES)
    values = np.rint(np.geomspace(min_n, max_n, count)).astype(int)
    values[0] = min_n
    values[-1] = max_n
    for idx in range(1, len(values)):
        if values[idx] <= values[idx - 1]:
            values[idx] = values[idx - 1] + 1
    return values


def showcase_projection_dim(max_n: int = SHOWCASE_MAX_N) -> int:
    return max(1, int(math.ceil(math.log2(max_n))))


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


def projected_norm_one_graph(k: int, offset: float = 0.17) -> tuple[np.ndarray, np.ndarray]:
    # Deterministic, slightly incommensurable angles avoid too much overlap.
    golden = (math.sqrt(5) - 1) / 2
    angles = np.sort((offset + np.arange(k) * golden * math.pi) % math.pi)
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
    point_scale: float = 1.0,
) -> None:
    pts = normalize_points(points)
    shown_edges = edge_subset(edges, max_edges)
    segs = pts[shown_edges]
    lc = LineCollection(segs, colors=line_color, linewidths=0.52, alpha=0.42, zorder=1)
    ax.add_collection(lc)
    size = point_scale * max(2.0, 7.0 * (90 / len(points)) ** 0.30)
    ax.scatter(
        pts[:, 0],
        pts[:, 1],
        s=size,
        color=point_color,
        edgecolor="white",
        linewidth=0.08,
        alpha=1.0,
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


def progress_labels(language: str) -> dict[str, list[dict[str, str]] | str]:
    if language == "fr":
        return {
            "increase": "n augmente",
            "n_label": "n",
            "methods": [
                {"name": "Grille", "exp": r"$1+\Theta(1/\log\log n)$"},
                {"name": "OpenAI", "exp": r"$1+\varepsilon$"},
                {"name": "Sawin", "exp": r"$1.014$"},
                {"name": "Emmerich", "exp": r"$1.0152$"},
            ],
        }
    return {
        "increase": "n increases",
        "n_label": "n",
        "methods": [
            {"name": "Grid", "exp": r"$1+\Theta(1/\log\log n)$"},
            {"name": "OpenAI", "exp": r"$1+\varepsilon$"},
            {"name": "Sawin", "exp": r"$1.014$"},
            {"name": "Emmerich", "exp": r"$1.0152$"},
        ],
    }


def graph_for_progress(method_index: int, progress: float) -> tuple[np.ndarray, np.ndarray, int, str, str]:
    t = float(np.clip(progress, 0.0, 1.0))
    if method_index == 0:
        m = 10 + int(round(18 * t))
        points, edges = classical_grid_graph(m, 65)
        return points, edges, len(points), "#c9872a", "#263238"

    starts = [5, 6, 7]
    k = starts[method_index - 1] + int(round(3 * t))
    offsets = [0.11, 0.27, 0.43]
    line_colors = ["#4a90a4", "#2e7d71", "#5b65b7"]
    point_colors = ["#34215f", "#193d35", "#20264f"]
    points, edges = projected_norm_one_graph(k, offset=offsets[method_index - 1])
    return points, edges, len(points), line_colors[method_index - 1], point_colors[method_index - 1]


def board_labels(language: str) -> dict[str, object]:
    if language == "fr":
        return {
            "title": r"$n$ augmente",
            "curve_title": r"courbes $n\mapsto u(n)$",
            "cell_label": r"$u(n)\geq{}$",
            "columns": [r"$n_1$", r"$n_2$", r"$n_3$", r"$n_4$"],
            "methods": [
                {
                    "letter": "A",
                    "name": "Grille",
                    "exp": r"$1+\Theta(1/\log\log n)$",
                    "desc": "sommes de deux carres",
                    "color": "#c9872a",
                    "point": "#263238",
                },
                {
                    "letter": "B",
                    "name": "OpenAI",
                    "exp": r"$1+\varepsilon$",
                    "desc": "certificat algebrique",
                    "color": "#4a90a4",
                    "point": "#34215f",
                },
                {
                    "letter": "C",
                    "name": "Sawin",
                    "exp": r"$1.014$",
                    "desc": "version explicite",
                    "color": "#2e7d71",
                    "point": "#193d35",
                },
                {
                    "letter": "D",
                    "name": "Emmerich",
                    "exp": r"$1.0152$",
                    "desc": "optimisation certifiee",
                    "color": "#5b65b7",
                    "point": "#20264f",
                },
            ],
        }
    return {
        "title": r"$n$ increases",
        "curve_title": r"curves $n\mapsto u(n)$",
        "cell_label": r"$u(n)\geq{}$",
        "columns": [r"$n_1$", r"$n_2$", r"$n_3$", r"$n_4$"],
        "methods": [
            {
                "letter": "A",
                "name": "Grid",
                "exp": r"$1+\Theta(1/\log\log n)$",
                "desc": "sums of two squares",
                "color": "#c9872a",
                "point": "#263238",
            },
            {
                "letter": "B",
                "name": "OpenAI",
                "exp": r"$1+\varepsilon$",
                "desc": "algebraic certificate",
                "color": "#4a90a4",
                "point": "#34215f",
            },
            {
                "letter": "C",
                "name": "Sawin",
                "exp": r"$1.014$",
                "desc": "explicit version",
                "color": "#2e7d71",
                "point": "#193d35",
            },
            {
                "letter": "D",
                "name": "Emmerich",
                "exp": r"$1.0152$",
                "desc": "certified optimization",
                "color": "#5b65b7",
                "point": "#20264f",
            },
        ],
    }


def graph_for_cell(method_index: int, column_index: int) -> tuple[np.ndarray, np.ndarray, int, int]:
    if method_index == 0:
        m_values = [8, 12, 16, 22]
        points, edges = classical_grid_graph(m_values[column_index], 65)
        return points, edges, len(points), len(edges)

    k_values = [
        [5, 6, 7, 8],
        [6, 7, 8, 9],
        [7, 8, 9, 10],
    ][method_index - 1]
    offsets = [0.11, 0.27, 0.43]
    points, edges = projected_norm_one_graph(k_values[column_index], offset=offsets[method_index - 1])
    return points, edges, len(points), len(edges)


def add_matching_chords(edges: np.ndarray, n_points: int, k: int, layers: int) -> np.ndarray:
    if layers <= 0:
        return edges

    extra_edges: list[tuple[int, int]] = []
    for layer in range(layers):
        a = layer % k
        b = (layer + 2) % k
        if a == b:
            b = (b + 1) % k
        flip_mask = (1 << a) | (1 << b)
        for source in range(n_points):
            target = source ^ flip_mask
            if source < target:
                extra_edges.append((source, target))

    if not extra_edges:
        return edges
    return np.vstack([edges, np.asarray(extra_edges, dtype=int)])


def exact_grid_graph(n_value: int) -> tuple[np.ndarray, np.ndarray]:
    cols = int(math.ceil(math.sqrt(n_value)))
    idx = np.arange(n_value, dtype=int)
    rows = idx // cols
    cols_idx = idx % cols
    points = np.column_stack([cols_idx, rows]).astype(float)

    right_sources = idx[(cols_idx < cols - 1) & (idx + 1 < n_value)]
    down_sources = idx[idx + cols < n_value]
    edge_parts = []
    if len(right_sources):
        edge_parts.append(np.column_stack([right_sources, right_sources + 1]))
    if len(down_sources):
        edge_parts.append(np.column_stack([down_sources, down_sources + cols]))
    if not edge_parts:
        return points, np.empty((0, 2), dtype=int)
    return points, np.vstack(edge_parts).astype(int)


def projected_prefix_graph(
    n_value: int,
    offset: float = 0.17,
    layers: float = 0.0,
    projection_dim: int = showcase_projection_dim(),
) -> tuple[np.ndarray, np.ndarray]:
    golden = (math.sqrt(5) - 1) / 2
    angles = np.sort((offset + np.arange(projection_dim) * golden * math.pi) % math.pi)
    directions = np.column_stack([np.cos(angles), np.sin(angles)])

    masks = np.arange(n_value, dtype=np.uint64)
    bit_indices = np.arange(projection_dim, dtype=np.uint64)
    bits = ((masks[:, None] >> bit_indices) & 1).astype(float)
    points = bits @ directions

    sources = np.arange(n_value, dtype=np.int64)
    edge_parts: list[np.ndarray] = []
    for bit in range(projection_dim):
        targets = sources ^ (1 << bit)
        valid = (sources < targets) & (targets < n_value)
        if np.any(valid):
            edge_parts.append(np.column_stack([sources[valid], targets[valid]]))

    full_layers = int(math.floor(max(layers, 0.0)))
    fractional_layer = max(layers, 0.0) - full_layers
    for layer in range(full_layers):
        a = layer % projection_dim
        b = (layer + 2) % projection_dim
        if a == b:
            b = (b + 1) % projection_dim
        targets = sources ^ ((1 << a) | (1 << b))
        valid = (sources < targets) & (targets < n_value)
        if np.any(valid):
            edge_parts.append(np.column_stack([sources[valid], targets[valid]]))

    if fractional_layer > 1e-9:
        layer = full_layers
        a = layer % projection_dim
        b = (layer + 2) % projection_dim
        if a == b:
            b = (b + 1) % projection_dim
        targets = sources ^ ((1 << a) | (1 << b))
        valid = (sources < targets) & (targets < n_value)
        if np.any(valid):
            source_subset = sources[valid]
            target_subset = targets[valid]
            take = int(round(fractional_layer * len(source_subset)))
            if take > 0:
                edge_parts.append(np.column_stack([source_subset[:take], target_subset[:take]]))

    if not edge_parts:
        return points, np.empty((0, 2), dtype=int)
    return points, np.vstack(edge_parts).astype(int)


def exact_grid_edge_count(n_value: int) -> int:
    cols = int(math.ceil(math.sqrt(n_value)))
    full_rows = n_value // cols
    remainder = n_value % cols
    horizontal = full_rows * max(cols - 1, 0) + max(remainder - 1, 0)
    vertical = max(n_value - cols, 0)
    return horizontal + vertical


def projected_prefix_edge_count(
    n_value: int,
    layers: float = 0.0,
    projection_dim: int = showcase_projection_dim(),
) -> int:
    sources = np.arange(n_value, dtype=np.int64)
    total = 0
    for bit in range(projection_dim):
        targets = sources ^ (1 << bit)
        total += int(np.count_nonzero((sources < targets) & (targets < n_value)))

    full_layers = int(math.floor(max(layers, 0.0)))
    fractional_layer = max(layers, 0.0) - full_layers
    for layer in range(full_layers):
        a = layer % projection_dim
        b = (layer + 2) % projection_dim
        if a == b:
            b = (b + 1) % projection_dim
        targets = sources ^ ((1 << a) | (1 << b))
        total += int(np.count_nonzero((sources < targets) & (targets < n_value)))
    if fractional_layer > 1e-9:
        layer = full_layers
        a = layer % projection_dim
        b = (layer + 2) % projection_dim
        if a == b:
            b = (b + 1) % projection_dim
        targets = sources ^ ((1 << a) | (1 << b))
        total += int(round(fractional_layer * np.count_nonzero((sources < targets) & (targets < n_value))))
    return total


def showcase_extra_layers(method_index: int, n_value: int) -> float:
    if method_index <= 1:
        return 0

    log_span = math.log2(SHOWCASE_MAX_N / SHOWCASE_MIN_N)
    progress = math.log2(max(n_value, SHOWCASE_MIN_N) / SHOWCASE_MIN_N) / log_span
    progress = float(np.clip(progress, 0.0, 1.0))
    if method_index == 2:
        return 1 + 4 * progress**1.18
    return 2 + 7 * progress**1.28


@lru_cache(maxsize=None)
def shared_edge_count(method_index: int, n_value: int) -> int:
    if method_index == 0:
        return exact_grid_edge_count(n_value)
    return projected_prefix_edge_count(n_value, layers=showcase_extra_layers(method_index, n_value))


def graph_for_shared_n(method_index: int, n_value: int) -> tuple[np.ndarray, np.ndarray, int, int]:
    if method_index == 0:
        points, edges = exact_grid_graph(n_value)
        return points, edges, len(points), len(edges)

    offsets = [0.11, 0.27, 0.43]
    points, edges = projected_prefix_graph(
        n_value,
        offset=offsets[method_index - 1],
        layers=showcase_extra_layers(method_index, n_value),
    )
    return points, edges, len(points), len(edges)


def theory_ratio(method_letter: str, n_values: np.ndarray | float) -> np.ndarray:
    n = np.asarray(n_values, dtype=float)
    if method_letter == "A":
        safe_n = np.maximum(n, math.e**math.e)
        return n ** (0.018 / np.maximum(np.log(np.log(safe_n)), 1.0))
    if method_letter == "B":
        return n**0.006
    if method_letter == "C":
        return n**0.014
    return n**0.0152


def fitted_theory_constant(method_index: int, method_letter: str, schedule: np.ndarray) -> float:
    n_arr, _, ratio_arr = method_numeric_series(method_index, schedule)
    base = np.asarray(theory_ratio(method_letter, n_arr), dtype=float)
    valid = (ratio_arr > 0) & (base > 0)
    if not np.any(valid):
        return 1.0
    return float(np.exp(np.mean(np.log(ratio_arr[valid]) - np.log(base[valid]))))


def fitted_theory_ratio(
    method_index: int,
    method_letter: str,
    n_values: np.ndarray | float,
    schedule: np.ndarray,
) -> np.ndarray:
    return fitted_theory_constant(method_index, method_letter, schedule) * theory_ratio(method_letter, n_values)


def draw_cell_graph(
    ax: plt.Axes,
    points: np.ndarray,
    edges: np.ndarray,
    line_color: str,
    point_color: str,
) -> None:
    draw_graph(ax, points, edges, line_color, point_color, max_edges=1150, point_scale=0.72)


def make_progress_figure(language: str = "fr", progress: float = 1.0) -> plt.Figure:
    labels = board_labels(language)
    methods = labels["methods"]  # type: ignore[index]
    columns = labels["columns"]  # type: ignore[index]

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8,
            "axes.titlesize": 8,
        }
    )

    fig = plt.figure(figsize=(11.8, 5.2), constrained_layout=False)
    fig.patch.set_facecolor("white")
    gs = GridSpec(
        4,
        6,
        figure=fig,
        width_ratios=[1.34, 1, 1, 1, 1, 1.56],
        wspace=0.14,
        hspace=0.36,
        left=0.025,
        right=0.985,
        top=0.86,
        bottom=0.07,
    )

    active_position = float(np.clip(progress, 0.0, 1.0)) * 3.0
    for col, column_label in enumerate(columns):
        fig.text(
            0.226 + col * 0.131,
            0.900,
            column_label,
            ha="center",
            va="center",
            fontsize=10,
            color="#26364F",
            fontweight="bold",
        )

    fig.text(
        0.50,
        0.943,
        labels["title"],  # type: ignore[index]
        ha="center",
        va="center",
        fontsize=12,
        fontweight="normal",
        color="#30343b",
    )
    arrow = FancyArrowPatch(
        (0.44, 0.915),
        (0.56, 0.915),
        transform=fig.transFigure,
        arrowstyle="-|>",
        mutation_scale=10,
        linewidth=0.9,
        color="#6c757d",
    )
    fig.add_artist(arrow)

    for row, method in enumerate(methods):  # type: ignore[assignment]
        label_ax = fig.add_subplot(gs[row, 0])
        label_ax.axis("off")
        label_ax.text(
            0.02,
            0.74,
            f"{method['letter']}. {method['name']}",
            ha="left",
            va="center",
            fontsize=11,
            color="#26364F",
            fontweight="bold",
        )
        label_ax.text(0.02, 0.45, method["exp"], ha="left", va="center", fontsize=8, color="#30343b")
        label_ax.text(0.02, 0.19, method["desc"], ha="left", va="center", fontsize=7, color="#6D7480")

        for col in range(4):
            ax = fig.add_subplot(gs[row, col + 1])
            points, edges, n_points, u_count = graph_for_cell(row, col)
            draw_cell_graph(ax, points, edges, method["color"], method["point"])
            highlight = max(0.0, 1.0 - abs(active_position - col) / 0.55)
            if highlight > 0.0:
                ax.set_facecolor("#fffdf4")
                for spine in ax.spines.values():
                    spine.set_color(method["color"])
                    spine.set_linewidth(0.75 + 1.15 * highlight)
            ax.set_title(f"{method['letter']}{col + 1}", pad=0.5, color="#26364F", fontweight="bold")
            ax.text(
                0.5,
                0.025,
                rf"$n={n_points}$, {labels['cell_label']}{u_count}",
                transform=ax.transAxes,
                ha="center",
                va="bottom",
                fontsize=5.7,
                color="#30343b",
                bbox={"facecolor": "white", "alpha": 0.78, "edgecolor": "none", "pad": 0.8},
            )

    curve_ax = fig.add_subplot(gs[:, 5])
    n_curve = np.logspace(2, 12, 260)
    curves = [
        ("A", n_curve ** (1.0 + 0.018 / np.maximum(np.log(np.log(n_curve)), 1.0))),
        ("B", n_curve**1.006),
        ("C", n_curve**1.014),
        ("D", n_curve**1.0152),
    ]
    for method, (_, y_values) in zip(methods, curves):  # type: ignore[arg-type]
        curve_ax.semilogx(
            n_curve,
            y_values / n_curve,
            color=method["color"],
            linewidth=1.35,
            alpha=0.42,
            label=f"{method['letter']} {method['name']}",
        )
        theory_n = np.logspace(2, 12, 9)
        theory_y = theory_ratio(method["letter"], theory_n)
        curve_ax.semilogx(
            theory_n,
            theory_y,
            linestyle="none",
            marker="o",
            markersize=3.2,
            markerfacecolor=method["color"],
            markeredgecolor="white",
            markeredgewidth=0.45,
            alpha=1.0,
        )
    curve_ax.set_title(labels["curve_title"], fontsize=10, color="#26364F", fontweight="bold")
    curve_ax.set_xlabel(r"$n$", fontsize=8)
    curve_ax.set_ylabel(r"$u(n)/n$", fontsize=8)
    curve_ax.grid(True, which="both", linewidth=0.35, color="#d8dde5", alpha=0.8)
    curve_ax.tick_params(axis="both", which="major", labelsize=6)
    curve_ax.legend(loc="upper left", fontsize=6, frameon=False, handlelength=1.4)
    for spine in curve_ax.spines.values():
        spine.set_color("#d7d8dc")
        spine.set_linewidth(0.75)
    return fig


def make_method_progress_figure(language: str = "fr", method_index: int = 0, stage_index: int = 0) -> plt.Figure:
    labels = board_labels(language)
    methods = labels["methods"]  # type: ignore[index]
    method = methods[method_index]  # type: ignore[index]
    columns = labels["columns"]  # type: ignore[index]
    stage = int(np.clip(stage_index, 0, 3))

    n_values: list[int] = []
    for col in range(4):
        _, _, n_points, u_count = graph_for_cell(method_index, col)
        n_values.append(n_points)

    points, edges, n_points, u_count = graph_for_cell(method_index, stage)

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 8,
            "axes.titlesize": 8,
        }
    )

    fig = plt.figure(figsize=(7.1, 3.35), constrained_layout=False)
    fig.patch.set_facecolor("white")
    gs = GridSpec(
        1,
        2,
        figure=fig,
        width_ratios=[1.05, 1.18],
        wspace=0.25,
        left=0.08,
        right=0.965,
        top=0.70,
        bottom=0.17,
    )

    fig.text(
        0.08,
        0.925,
        f"{method['letter']}. {method['name']}",
        ha="left",
        va="center",
        fontsize=13,
        color="#26364F",
        fontweight="bold",
    )
    fig.text(0.08, 0.848, method["exp"], ha="left", va="center", fontsize=9, color="#30343b")
    fig.text(0.08, 0.778, method["desc"], ha="left", va="center", fontsize=8, color="#6D7480")
    fig.text(
        0.49,
        0.906,
        labels["title"],  # type: ignore[index]
        ha="center",
        va="center",
        fontsize=11,
        fontweight="normal",
        color="#30343b",
    )
    arrow = FancyArrowPatch(
        (0.425, 0.875),
        (0.555, 0.875),
        transform=fig.transFigure,
        arrowstyle="-|>",
        mutation_scale=10,
        linewidth=0.9,
        color="#6c757d",
    )
    fig.add_artist(arrow)

    graph_ax = fig.add_subplot(gs[0, 0])
    draw_graph(graph_ax, points, edges, method["color"], method["point"], max_edges=1500, point_scale=0.82)
    graph_ax.set_facecolor("#fffdf4")
    for spine in graph_ax.spines.values():
        spine.set_color(method["color"])
        spine.set_linewidth(1.55)
    graph_ax.set_title(
        f"{method['letter']}{stage + 1}   {columns[stage]}",
        pad=2,
        color="#26364F",
        fontweight="bold",
    )
    graph_ax.text(
        0.5,
        0.02,
        rf"$n={n_points}$, {labels['cell_label']}{u_count}",
        transform=graph_ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=7,
        color="#30343b",
        bbox={"facecolor": "white", "alpha": 0.86, "edgecolor": "none", "pad": 1.2},
    )

    curve_ax = fig.add_subplot(gs[0, 1])
    n_arr = np.asarray(n_values, dtype=float)
    theory_points = theory_ratio(method["letter"], n_arr)
    n_min = max(3.0, float(n_arr.min()) * 0.82)
    n_max = float(n_arr.max()) * 1.22
    n_curve = np.logspace(np.log10(n_min), np.log10(n_max), 180)
    y_curve = theory_ratio(method["letter"], n_curve)
    curve_ax.semilogx(n_curve, y_curve, color=method["color"], linewidth=1.25, alpha=0.38)
    curve_ax.semilogx(
        n_arr,
        theory_points,
        linestyle="none",
        marker="o",
        markersize=4.0,
        markerfacecolor=method["color"],
        markeredgecolor="white",
        markeredgewidth=0.55,
        alpha=1.0,
        label="theory" if language != "fr" else "theorie",
    )
    curve_ax.semilogx(
        [n_arr[stage]],
        [theory_points[stage]],
        linestyle="none",
        marker="o",
        markersize=7.2,
        markerfacecolor=method["color"],
        markeredgecolor="#26364F",
        markeredgewidth=0.85,
        alpha=1.0,
    )
    curve_ax.axvline(n_arr[stage], color=method["color"], linewidth=0.75, alpha=0.35)
    curve_ax.set_title(r"theory for $u(n)/n$" if language != "fr" else r"theorie pour $u(n)/n$", fontsize=10, color="#26364F", fontweight="bold")
    curve_ax.set_xlabel(r"$n$", fontsize=8)
    curve_ax.set_ylabel(r"$u(n)/n$", fontsize=8)
    y_min = float(theory_points.min())
    y_max = float(theory_points.max())
    y_pad = max(0.002, 0.13 * (y_max - y_min))
    curve_ax.set_ylim(y_min - y_pad, y_max + y_pad)
    curve_ax.grid(True, which="both", linewidth=0.35, color="#d8dde5", alpha=0.8)
    curve_ax.tick_params(axis="both", which="major", labelsize=6)
    curve_ax.legend(loc="upper left", fontsize=6, frameon=False, handlelength=1.1)
    curve_ax.annotate(
        rf"$n={n_values[stage]}$",
        xy=(n_arr[stage], theory_points[stage]),
        xytext=(6, 7),
        textcoords="offset points",
        fontsize=7,
        color="#26364F",
    )
    for spine in curve_ax.spines.values():
        spine.set_color("#d7d8dc")
        spine.set_linewidth(0.75)
    return fig


def method_numeric_series(method_index: int, schedule: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    n_values = []
    u_values = []
    for n_value in schedule:
        n_int = int(n_value)
        n_values.append(n_int)
        u_values.append(shared_edge_count(method_index, n_int))
    n_arr = np.asarray(n_values, dtype=float)
    u_arr = np.asarray(u_values, dtype=float)
    return n_arr, u_arr, u_arr / n_arr


def interpolate_progress(x_values: np.ndarray, y_values: np.ndarray, position: float) -> tuple[float, float]:
    pos = float(np.clip(position, 0.0, 3.0))
    low = int(math.floor(pos))
    high = min(low + 1, 3)
    alpha = pos - low
    x = math.exp((1.0 - alpha) * math.log(float(x_values[low])) + alpha * math.log(float(x_values[high])))
    y = (1.0 - alpha) * float(y_values[low]) + alpha * float(y_values[high])
    return x, y


def smoothstep(t: float) -> float:
    clipped = float(np.clip(t, 0.0, 1.0))
    return clipped * clipped * (3.0 - 2.0 * clipped)


def make_showcase_progress_figure(
    language: str = "fr",
    active_n: int = SHOWCASE_MIN_N,
    n_schedule: np.ndarray | None = None,
) -> plt.Figure:
    labels = board_labels(language)
    methods = labels["methods"]  # type: ignore[index]
    schedule = shared_n_schedule(SHOWCASE_MIN_FRAMES) if n_schedule is None else np.asarray(n_schedule, dtype=int)
    active_n = int(active_n)
    combined_title = (
        r"$u(n)/n$  empirical + fitted theory"
        if language != "fr"
        else r"$u(n)/n$  empirique + theorie ajustee"
    )

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9.0,
            "axes.titlesize": 11,
            "axes.labelsize": 9.0,
            "axes.linewidth": 0.8,
            "lines.solid_capstyle": "round",
            "lines.dash_capstyle": "round",
        }
    )

    fig = plt.figure(figsize=(12.8, 6.85), constrained_layout=False)
    fig.patch.set_facecolor("white")
    gs = GridSpec(
        2,
        4,
        figure=fig,
        height_ratios=[1.28, 1.0],
        hspace=0.27,
        wspace=0.20,
        left=0.038,
        right=0.985,
        top=0.945,
        bottom=0.085,
    )

    for method_index, method in enumerate(methods):  # type: ignore[assignment]
        points, edges, n_points, u_count = graph_for_shared_n(method_index, active_n)
        graph_ax = fig.add_subplot(gs[0, method_index])
        draw_graph(graph_ax, points, edges, method["color"], method["point"], max_edges=1900, point_scale=0.74)
        graph_ax.set_facecolor("#fffdf4")
        for spine in graph_ax.spines.values():
            spine.set_color(method["color"])
            spine.set_linewidth(1.35)
        graph_ax.set_title(
            f"{method['letter']}  {method['name']}",
            pad=4,
            color="#26364F",
            fontweight="bold",
            fontsize=13,
        )
        graph_ax.text(
            0.5,
            0.024,
            rf"$n={n_points}$  $u/n={u_count / n_points:.2f}$",
            transform=graph_ax.transAxes,
            ha="center",
            va="bottom",
            fontsize=8.4,
            color="#26364F",
            bbox={"facecolor": "white", "alpha": 0.88, "edgecolor": "none", "pad": 1.2},
        )

    curve_ax = fig.add_subplot(gs[1, :])
    n_curve = np.logspace(np.log10(float(schedule[0])), np.log10(float(schedule[-1])), 300)

    all_y = []
    for method_index, method in enumerate(methods):  # type: ignore[assignment]
        n_arr, _, ratio_arr = method_numeric_series(method_index, schedule)
        active_ratio = shared_edge_count(method_index, active_n) / active_n
        theory_values = fitted_theory_ratio(method_index, method["letter"], n_curve, schedule)
        theory_points = fitted_theory_ratio(method_index, method["letter"], schedule, schedule)
        active_theory = float(fitted_theory_ratio(method_index, method["letter"], active_n, schedule))
        all_y.extend(ratio_arr.tolist())
        all_y.extend(np.asarray(theory_values).tolist())

        curve_ax.semilogx(
            n_arr,
            ratio_arr,
            color=method["color"],
            linewidth=2.0,
            marker="o",
            markersize=4.4,
            markerfacecolor=method["color"],
            markeredgecolor="white",
            markeredgewidth=0.55,
            alpha=0.94,
            label=f"{method['letter']} emp.",
        )
        curve_ax.semilogx(
            n_curve,
            theory_values,
            color=method["color"],
            linewidth=1.85,
            linestyle=(0, (4.5, 3.0)),
            alpha=0.78,
            label=f"{method['letter']} theory",
        )
        curve_ax.semilogx(
            schedule,
            theory_points,
            linestyle="none",
            marker="o",
            markersize=3.3,
            markerfacecolor=method["color"],
            markeredgecolor="white",
            markeredgewidth=0.45,
            alpha=0.72,
        )
        curve_ax.semilogx(
            [active_n],
            [active_ratio],
            linestyle="none",
            marker="o",
            markersize=10.2,
            markerfacecolor=method["color"],
            markeredgecolor="#26364F",
            markeredgewidth=1.15,
            zorder=5,
        )
        curve_ax.semilogx(
            [active_n],
            [active_theory],
            linestyle="none",
            marker="o",
            markersize=8.0,
            markerfacecolor=method["color"],
            markeredgecolor="white",
            markeredgewidth=1.0,
            zorder=5,
        )

    curve_ax.axvline(active_n, color="#26364F", linewidth=0.75, alpha=0.18, zorder=0)
    curve_ax.set_xlim(float(schedule[0]) * 0.78, float(schedule[-1]) * 1.28)
    curve_ax.set_xlabel(r"$n$")
    curve_ax.set_ylabel(r"$u(n)/n$")
    curve_ax.grid(True, which="both", linewidth=0.38, color="#d8dde5", alpha=0.82)
    curve_ax.tick_params(axis="both", which="major", labelsize=7.5)
    curve_ax.tick_params(axis="both", which="minor", length=2)
    curve_ax.legend(loc="upper left", fontsize=7.1, frameon=False, ncol=4, handlelength=1.8, columnspacing=0.9)
    curve_ax.set_title(combined_title, color="#26364F", fontweight="bold", pad=5)
    y_min = min(all_y)
    y_max = max(all_y)
    curve_ax.set_ylim(max(0.0, y_min - 0.65), y_max + 0.65)
    for spine in curve_ax.spines.values():
        spine.set_color("#d7d8dc")
        spine.set_linewidth(0.78)

    return fig


def figure_to_image(fig: plt.Figure):
    from PIL import Image

    fig.canvas.draw()
    rgba = np.asarray(fig.canvas.buffer_rgba())
    image = Image.fromarray(rgba)
    return image.convert("P", palette=Image.Palette.ADAPTIVE)


def save_showcase_gif_output(outdir: Path, language: str, frames: int) -> None:
    gif_path = outdir / "unit_distance_progress.gif"
    images = []
    durations = []
    schedule = shared_n_schedule(frames)
    total_frames = len(schedule)
    for idx, active_n in enumerate(schedule):
        fig = make_showcase_progress_figure(language=language, active_n=int(active_n), n_schedule=schedule)
        images.append(figure_to_image(fig))
        durations.append(1050 if idx == total_frames - 1 else 80)
        plt.close(fig)
    images[0].save(
        gif_path,
        save_all=True,
        append_images=images[1:],
        duration=durations,
        loop=0,
        optimize=True,
        disposal=2,
    )
    print(f"saved {gif_path}")


def save_method_gif_outputs(outdir: Path, language: str) -> None:
    labels = board_labels(language)
    methods = labels["methods"]  # type: ignore[index]
    for method_index, method in enumerate(methods):  # type: ignore[assignment]
        gif_path = outdir / f"unit_distance_progress_{method['letter']}_{METHOD_SLUGS[method_index]}.gif"
        images = []
        durations = []
        for stage in range(4):
            fig = make_method_progress_figure(language=language, method_index=method_index, stage_index=stage)
            images.append(figure_to_image(fig))
            durations.append(1200 if stage == 3 else 850)
            plt.close(fig)
        images[0].save(
            gif_path,
            save_all=True,
            append_images=images[1:],
            duration=durations,
            loop=0,
            optimize=True,
        )
        print(f"saved {gif_path}")


def save_progress_outputs(outdir: Path, language: str, make_gif: bool, frames: int) -> None:
    png_path = outdir / "unit_distance_progress.png"
    fig = make_progress_figure(language=language, progress=1.0)
    fig.savefig(png_path, dpi=230, bbox_inches="tight", pad_inches=0.02)
    plt.close(fig)
    print(f"saved {png_path}")

    if not make_gif:
        return

    save_showcase_gif_output(outdir, language=language, frames=frames)


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
    parser.add_argument(
        "--gif",
        action="store_true",
        help="Also write a polished animated unit_distance_progress.gif showing all four methods.",
    )
    parser.add_argument(
        "--frames",
        type=int,
        default=36,
        help="Number of frames for --gif.",
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
        plt.close(fig)
        print(f"saved {png_path}")
        print(f"saved {pdf_path}")
        save_progress_outputs(outdir, language=language, make_gif=args.gif, frames=max(args.frames, 2))


if __name__ == "__main__":
    main()
