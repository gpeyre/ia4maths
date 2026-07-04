#!/usr/bin/env python3
"""Plot a generated unit-distance coordinate JSON file."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import matplotlib.pyplot as plt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="JSON file produced by the Sage prototype")
    parser.add_argument("--output", default=None, help="Output PNG path")
    parser.add_argument("--max-edges", type=int, default=3000)
    parser.add_argument("--point-size", type=float, default=8.0)
    args = parser.parse_args()

    path = Path(args.input)
    data = json.loads(path.read_text())
    points = data["points"]
    edges = data["edges"][: args.max_edges]

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    fig, ax = plt.subplots(figsize=(7.2, 7.2), dpi=180)
    for i, j, _direction_idx in edges:
        x0, y0 = points[i]
        x1, y1 = points[j]
        ax.plot([x0, x1], [y0, y1], color="#8392a7", lw=0.45, alpha=0.42, zorder=1)

    ax.scatter(xs, ys, s=args.point_size, color="#1f2937", linewidths=0, zorder=2)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

    title = f"{data.get('field', 'unit-distance')}, k={data['k']}, n={data['num_points']}, edges={data['num_edges']}"
    if data.get("window_radius") is not None:
        title += f", R={data['window_radius']}"
    if data.get("edge_closure"):
        title += ", edge-closure"
    ax.set_title(title, fontsize=10, color="#111827", pad=8)

    if points:
        pad = 0.06 * max(max(xs) - min(xs), max(ys) - min(ys), 1.0)
        ax.set_xlim(min(xs) - pad, max(xs) + pad)
        ax.set_ylim(min(ys) - pad, max(ys) + pad)

    output = Path(args.output) if args.output else path.with_suffix(".png")
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(output)


if __name__ == "__main__":
    main()
