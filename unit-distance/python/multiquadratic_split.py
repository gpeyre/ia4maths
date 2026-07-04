#!/usr/bin/env python3
"""Fast split-prime combinatorics for multiquadratic CM fields.

This script avoids generic number-field ideal arithmetic.  For

    K = Q(i, sqrt(d1), ..., sqrt(dm))

and a rational prime p that splits completely, a prime over p is determined by
choosing signs for fixed square roots of -1, d1, ..., dm modulo p.  CM
conjugation flips only the sign of i.

The output is not a coordinate realization.  It is the fast front-end needed
before principalization: split-prime labels, CM pairs, J(a) records, and formal
ideal-ratio directions.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path


FIELDS = {
    "q_i_sqrt5": {
        "label": "Q(i, sqrt(5))",
        "radicands": [-1, 5],
    },
    "q_i_sqrt5_sqrt13": {
        "label": "Q(i, sqrt(5), sqrt(13))",
        "radicands": [-1, 5, 13],
    },
    "q_i_sqrt5_sqrt13_sqrt17": {
        "label": "Q(i, sqrt(5), sqrt(13), sqrt(17))",
        "radicands": [-1, 5, 13, 17],
    },
    "openai_multiquadratic_base": {
        "label": "Q(i, sqrt(5), sqrt(13), sqrt(17), sqrt(21), sqrt(33))",
        "radicands": [-1, 5, 13, 17, 21, 33],
    },
}


def legendre_symbol(a: int, p: int) -> int:
    value = pow(a % p, (p - 1) // 2, p)
    if value == p - 1:
        return -1
    return value


def modular_sqrt(a: int, p: int) -> int:
    """Return one square root of a modulo odd prime p."""
    a %= p
    if a == 0:
        return 0
    if p == 2:
        return a
    if legendre_symbol(a, p) != 1:
        raise ValueError(f"{a} is not a square modulo {p}")
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    q = p - 1
    s = 0
    while q % 2 == 0:
        s += 1
        q //= 2

    z = 2
    while legendre_symbol(z, p) != -1:
        z += 1

    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q + 1) // 2, p)

    while t != 1:
        i = 1
        t2i = pow(t, 2, p)
        while t2i != 1:
            t2i = pow(t2i, 2, p)
            i += 1
            if i == m:
                raise RuntimeError("Tonelli-Shanks failed")
        b = pow(c, 1 << (m - i - 1), p)
        m = i
        c = pow(b, 2, p)
        t = (t * c) % p
        r = (r * b) % p
    return min(r, p - r)


def sign_vectors(length: int):
    return list(itertools.product([-1, 1], repeat=length))


def split_prime_labels(radicands: list[int], p: int):
    roots = [modular_sqrt(d, p) for d in radicands]
    labels = []
    for signs in sign_vectors(len(radicands)):
        residues = [int((s * r) % p) for s, r in zip(signs, roots)]
        labels.append({"signs": list(signs), "residues": residues})
    return roots, labels


def cm_pair_labels(labels):
    by_signs = {tuple(label["signs"]): label for label in labels}
    pairs = []
    for signs, label in sorted(by_signs.items()):
        if signs[0] != 1:
            continue
        conjugate = (-signs[0],) + signs[1:]
        pairs.append({"prime": label, "conjugate": by_signs[conjugate]})
    return pairs


def build_j_records(pair_count: int, k: int, max_records: int):
    total = (k + 1) ** pair_count
    if total > max_records:
        return total, None
    return total, [list(v) for v in itertools.product(range(k + 1), repeat=pair_count)]


def canonical_delta(delta):
    neg = tuple(-x for x in delta)
    return min(tuple(delta), neg)


def formal_directions(records):
    if records is None:
        return None
    directions = {}
    for i, left in enumerate(records):
        for right in records[i + 1 :]:
            delta = tuple(a - b for a, b in zip(left, right))
            directions[canonical_delta(delta)] = {
                "delta": list(canonical_delta(delta)),
            }
    return list(directions.values())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--field", choices=sorted(FIELDS), default="openai_multiquadratic_base")
    parser.add_argument("--p", type=int, default=101)
    parser.add_argument("--k", type=int, default=1)
    parser.add_argument("--max-pairs", type=int, default=None)
    parser.add_argument("--max-records", type=int, default=200000)
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    field = FIELDS[args.field]
    radicands = field["radicands"]
    roots, labels = split_prime_labels(radicands, args.p)
    pairs = cm_pair_labels(labels)
    total_pairs = len(pairs)
    if args.max_pairs is not None:
        pairs = pairs[: args.max_pairs]

    total_records, records = build_j_records(len(pairs), args.k, args.max_records)
    directions = formal_directions(records)

    result = {
        "field_key": args.field,
        "field": field["label"],
        "p": args.p,
        "k": args.k,
        "radicands": radicands,
        "degree": 2 ** len(radicands),
        "roots_mod_p": roots,
        "legendre_symbols": [legendre_symbol(d, args.p) for d in radicands],
        "num_split_prime_labels": len(labels),
        "num_total_cm_pairs": total_pairs,
        "num_used_cm_pairs": len(pairs),
        "cm_pairs": pairs,
        "num_j_records": total_records,
        "records_materialized": records is not None,
        "j_records": records,
        "num_formal_directions": None if directions is None else len(directions),
        "formal_directions": directions,
    }

    output = args.output
    if output is None:
        suffix = args.field
        if args.max_pairs is not None:
            suffix += f"_pair{args.max_pairs}"
        output = f"unit-distance/output/{suffix}_split_p{args.p}_k{args.k}.json"

    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2))

    print("field:", result["field"])
    print("degree:", result["degree"])
    print("p:", args.p)
    print("roots:", roots)
    print("split prime labels:", len(labels))
    print("CM pairs:", total_pairs, "used:", len(pairs))
    print("J records:", total_records, "materialized:", records is not None)
    print("formal directions:", result["num_formal_directions"])
    print("output:", path)


if __name__ == "__main__":
    main()
