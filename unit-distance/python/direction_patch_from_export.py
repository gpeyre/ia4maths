#!/usr/bin/env python3
"""Build a small exact additive patch from exported algebraic directions.

Given exact unit directions u_1, ..., u_m in a number-field basis, this creates
points

    c_1 u_1 + ... + c_m u_m,  0 <= c_i < side.

Edges connect coefficient vectors that differ by one in a single coordinate.
This is a coordinate smoke test built from actual principalized directions.  It
is not yet the proof's denominator-lattice/Minkowski-window construction.
"""

from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path


DEFAULT_INPUT = "unit-distance/output/degree16_openai_principalization_direct.json"
DEFAULT_OUTPUT = "unit-distance/output/degree16_direction_patch_s2.json"


def parse_fraction_vector(values: list[str]) -> tuple[Fraction, ...]:
    return tuple(Fraction(value) for value in values)


def vector_add_scaled(
    acc: tuple[Fraction, ...], direction: tuple[Fraction, ...], scale: int
) -> tuple[Fraction, ...]:
    return tuple(a + scale * b for a, b in zip(acc, direction))


def vector_to_strings(values: tuple[Fraction, ...]) -> list[str]:
    return [str(value) for value in values]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--side", type=int, default=2)
    parser.add_argument("--max-directions", type=int, default=None)
    parser.add_argument("--include-exact-points", action="store_true")
    args = parser.parse_args()

    if args.side < 2:
        raise ValueError("--side must be at least 2")

    data = json.loads(Path(args.input).read_text())
    directions = data["unique_directions"]
    if args.max_directions is not None:
        directions = directions[: args.max_directions]
    if not directions:
        raise ValueError("no directions found in input")

    exact_directions = [
        parse_fraction_vector(direction["u_basis_vector"]) for direction in directions
    ]
    embedding_directions = [
        (
            float(direction["u_embedding"]["real_float"]),
            float(direction["u_embedding"]["imag_float"]),
        )
        for direction in directions
    ]
    dimension = len(exact_directions[0])
    zero = tuple(Fraction(0) for _ in range(dimension))

    coeff_to_index = {}
    exact_point_to_index = {}
    points = []
    coeffs_for_points = []
    exact_points = []

    for coeffs in itertools.product(range(args.side), repeat=len(directions)):
        exact = zero
        x = 0.0
        y = 0.0
        for coeff, exact_direction, emb_direction in zip(
            coeffs, exact_directions, embedding_directions
        ):
            exact = vector_add_scaled(exact, exact_direction, coeff)
            x += coeff * emb_direction[0]
            y += coeff * emb_direction[1]

        if exact in exact_point_to_index:
            idx = exact_point_to_index[exact]
        else:
            idx = len(points)
            exact_point_to_index[exact] = idx
            points.append([x, y])
            coeffs_for_points.append(list(coeffs))
            if args.include_exact_points:
                exact_points.append(vector_to_strings(exact))
        coeff_to_index[coeffs] = idx

    edge_set = set()
    edges = []
    for coeffs in itertools.product(range(args.side), repeat=len(directions)):
        i = coeff_to_index[coeffs]
        for direction_idx in range(len(directions)):
            if coeffs[direction_idx] + 1 >= args.side:
                continue
            target = list(coeffs)
            target[direction_idx] += 1
            j = coeff_to_index[tuple(target)]
            key = (min(i, j), max(i, j), direction_idx)
            if key in edge_set:
                continue
            edge_set.add(key)
            edges.append([i, j, direction_idx])

    result = {
        "source": str(Path(args.input)),
        "kind": "degree16_direction_additive_patch",
        "field": data["field"]["label"],
        "k": data["parameters"]["k"],
        "side": args.side,
        "num_directions": len(directions),
        "num_points": len(points),
        "num_edges": len(edges),
        "points": points,
        "edges": edges,
        "coefficients": coeffs_for_points,
        "directions": [
            {
                "direction_index": direction["direction_index"],
                "collision_index": direction["collision_index"],
                "u_embedding": direction["u_embedding"],
                "abs_u_minus_1": direction["abs_u_minus_1"],
                "delta": direction["delta"],
            }
            for direction in directions
        ],
        "edge_certification": "Each edge difference is exactly one exported u direction in the number-field basis.",
        "caveat": "This additive patch is not the proof's denominator-lattice/Minkowski-window sample.",
    }
    if args.include_exact_points:
        result["exact_point_basis_vectors"] = exact_points

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2))

    print("directions:", len(directions))
    print("side:", args.side)
    print("points:", len(points))
    print("edges:", len(edges))
    print("output:", output_path)


if __name__ == "__main__":
    main()
