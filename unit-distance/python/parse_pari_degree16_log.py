#!/usr/bin/env python3
"""Parse the degree-16 PARI/GP principalization log into JSON.

The GP probe is intentionally human-readable.  This parser creates a stable
machine-readable bridge for the next coordinate-generation stage.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


DEFAULT_INPUT = "unit-distance/output/degree16_openai_principalization_probe.txt"
DEFAULT_OUTPUT = "unit-distance/output/degree16_openai_principalization_probe.json"


def parse_int(value: str) -> int:
    return int(value.strip())


def parse_int_vector(text: str) -> list[int]:
    return [int(v) for v in parse_vector(text)]


def parse_vector(text: str) -> list[str]:
    cleaned = text.strip()
    if cleaned.endswith("~"):
        cleaned = cleaned[:-1]
    if not (cleaned.startswith("[") and cleaned.endswith("]")):
        raise ValueError(f"expected vector, got: {text}")
    inner = cleaned[1:-1].strip()
    if not inner:
        return []
    return [item.strip() for item in inner.split(",")]


def parse_complex_embedding(text: str) -> dict[str, str]:
    value = text.strip()
    match = re.match(r"^(.+?)\s+([+-])\s+(.+)\*I$", value)
    if match is None:
        return {"raw": value}
    real, sign, imag_abs = match.groups()
    imag = imag_abs if sign == "+" else f"-{imag_abs}"
    return {"real": real.strip(), "imag": imag.strip(), "raw": value}


def parse_log(text: str, source: str) -> dict:
    result = {
        "source": source,
        "parameters": {},
        "field": {},
        "cm": {},
        "prime_decomposition": {"pairs": []},
        "class_group": {},
        "pair_classes": [],
        "timings_ms": {},
        "collisions": [],
    }
    current_collision = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped:
            continue

        if stripped.startswith("p="):
            for key, value in re.findall(r"(\w+)=([^ ]+)", stripped):
                result["parameters"][key] = parse_int(value)
            continue

        if stripped.startswith("polynomial_degree="):
            result["field"]["degree"] = parse_int(stripped.split("=", 1)[1])
            continue

        if stripped.startswith("field_polynomial="):
            result["field"]["polynomial"] = stripped.split("=", 1)[1]
            continue

        if stripped.startswith("cm_index="):
            result["cm"]["index"] = parse_int(stripped.split("=", 1)[1])
            continue

        if stripped.startswith("cm_detection_error="):
            result["cm"]["detection_error"] = stripped.split("=", 1)[1]
            continue

        if stripped.startswith("automorphisms="):
            result["field"]["automorphisms"] = parse_int(stripped.split("=", 1)[1])
            continue

        if stripped.startswith("split_prime_ideals="):
            result["prime_decomposition"]["split_prime_ideals"] = parse_int(
                stripped.split("=", 1)[1]
            )
            continue

        if stripped.startswith("cm_pairs_total="):
            result["prime_decomposition"]["cm_pairs_total"] = parse_int(
                stripped.split("=", 1)[1]
            )
            continue

        if stripped.startswith("cm_pairs_used="):
            result["prime_decomposition"]["cm_pairs_used"] = parse_int(
                stripped.split("=", 1)[1]
            )
            continue

        pair_match = re.match(r"^pair_(\d+)=(\[.*\])$", stripped)
        if pair_match:
            result["prime_decomposition"]["pairs"].append(
                {
                    "index": int(pair_match.group(1)),
                    "prime_indices": parse_int_vector(pair_match.group(2)),
                }
            )
            continue

        if stripped.startswith("class_number="):
            result["class_group"]["class_number"] = parse_int(stripped.split("=", 1)[1])
            continue

        if stripped.startswith("class_group_cyc="):
            result["class_group"]["cyc"] = parse_int_vector(stripped.split("=", 1)[1])
            continue

        pair_class_match = re.match(
            r"^pair_class_(\d+)_P=(\[.*?\]) Pc=(\[.*\])$", stripped
        )
        if pair_class_match:
            result["pair_classes"].append(
                {
                    "index": int(pair_class_match.group(1)),
                    "P": parse_int_vector(pair_class_match.group(2)),
                    "Pc": parse_int_vector(pair_class_match.group(3)),
                }
            )
            continue

        if stripped.startswith("J_record_count="):
            result["j_record_count"] = parse_int(stripped.split("=", 1)[1])
            continue

        timing_match = re.match(r"^([a-zA-Z0-9_]+_ms)=(-?\d+)$", stripped)
        if timing_match:
            result["timings_ms"][timing_match.group(1)] = int(timing_match.group(2))
            continue

        collision_match = re.match(r"^collision_(\d+)$", stripped)
        if collision_match:
            current_collision = {"index": int(collision_match.group(1))}
            result["collisions"].append(current_collision)
            continue

        if current_collision is not None and stripped.startswith("left_index="):
            match = re.match(r"^left_index=(\d+) right_index=(\d+)$", stripped)
            if match:
                current_collision["left_index"] = int(match.group(1))
                current_collision["right_index"] = int(match.group(2))
            continue

        if stripped.startswith("collisions_reported="):
            result["collisions_reported"] = parse_int(stripped.split("=", 1)[1])
            continue

        if current_collision is not None and "=" in stripped:
            key, value = stripped.split("=", 1)
            if key in {"left_exponents", "right_exponents", "delta", "class"}:
                current_collision[key] = parse_int_vector(value)
            elif key == "principal_class_vector":
                current_collision[key] = parse_int_vector(value)
            elif key == "gamma":
                current_collision["gamma_basis_vector"] = parse_vector(value)
            elif key == "u_embedding":
                current_collision["u_embedding"] = parse_complex_embedding(value)
            elif key == "abs_u_minus_1":
                current_collision["abs_u_minus_1"] = value
            continue

    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    parsed = parse_log(input_path.read_text(), str(input_path))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(parsed, indent=2))

    print("collisions:", len(parsed["collisions"]))
    print("output:", output_path)


if __name__ == "__main__":
    main()
