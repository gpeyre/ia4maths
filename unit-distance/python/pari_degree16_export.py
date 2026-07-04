#!/usr/bin/env python3
"""Direct PARI/cypari2 exporter for degree-16 OpenAI-style directions.

This replaces the text-log parser as the main machine-readable bridge from
PARI principalization to coordinate generation.  It still targets only

    K = Q(i, sqrt(5), sqrt(13), sqrt(17)).

The script exports:

- exact basis vectors for principal generators gamma;
- exact basis vectors for u = gamma / gamma^c;
- projected numerical coordinates of the directions;
- a small "direction star" point configuration {0, u_1, ..., u_m}.

The star is a coordinate smoke test, not the full bounded-window construction.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from cypari2 import Pari


DEFAULT_OUTPUT = "unit-distance/output/degree16_openai_principalization_direct.json"
DEFAULT_CONFIG_OUTPUT = "unit-distance/output/degree16_direction_star.json"


def gen_int_vector(v) -> list[int]:
    return [int(x) for x in v]


def gen_str_vector(v) -> list[str]:
    return [str(x) for x in v]


def canonical_mod_vector(v: list[int], cyc: list[int]) -> list[int]:
    return [x % m for x, m in zip(v, cyc)]


def class_add_scaled(acc: list[int], v: list[int], scale: int, cyc: list[int]) -> list[int]:
    return [(a + scale * b) % m for a, b, m in zip(acc, v, cyc)]


def decode_exponents(record_id: int, base: int, pair_count: int) -> list[int]:
    exps = []
    q = record_id
    for _ in range(pair_count):
        exps.append(q % base)
        q //= base
    return exps


def class_of_exponents(
    exps: list[int],
    eP: list[list[int]],
    ePc: list[list[int]],
    k: int,
    cyc: list[int],
) -> list[int]:
    cls = [0] * len(cyc)
    for a, cls_p, cls_pc in zip(exps, eP, ePc):
        cls = class_add_scaled(cls, cls_p, a, cyc)
        cls = class_add_scaled(cls, cls_pc, k - a, cyc)
    return cls


def complex_parts(pari: Pari, z) -> dict:
    real = pari.real(z)
    imag = pari.imag(z)
    return {
        "real": str(real),
        "imag": str(imag),
        "real_float": float(real),
        "imag_float": float(imag),
        "raw": str(z),
    }


def detect_cm_conjugation(pari: Pari, nf, pol, auts) -> tuple[int, str, object]:
    z = pari.nfeltembed(nf, pari(f"Mod(x,{pol})"))[0]
    target = pari.conj(z)
    best_index = 0
    best_error = None
    for idx, aut in enumerate(auts):
        error = pari.abs(pari.nfeltembed(nf, aut)[0] - target)
        if best_error is None or error < best_error:
            best_index = idx
            best_error = error
    return best_index + 1, str(best_error), auts[best_index]


def pair_prime_ideals(pari: Pari, nf, dec, cm) -> list[tuple[int, int]]:
    hnfs = [pari.idealhnf(nf, dec[i]) for i in range(len(dec))]
    used = [False] * len(dec)
    pairs = []
    for i in range(len(dec)):
        if used[i]:
            continue
        target = pari.idealhnf(nf, pari.nfgaloisapply(nf, cm, dec[i]))
        match = None
        for j, hnf in enumerate(hnfs):
            if not used[j] and hnf == target:
                match = j
                break
        if match is None:
            raise RuntimeError(f"could not pair prime ideal {i + 1}")
        used[i] = True
        used[match] = True
        pairs.append((i + 1, match + 1))
    return pairs


def build_J(pari: Pari, nf, prime_hnfs, pairs, exps: list[int], k: int):
    J = pari.idealhnf(nf, 1)
    for a, (p_idx, pc_idx) in zip(exps, pairs):
        P = prime_hnfs[p_idx - 1]
        Pc = prime_hnfs[pc_idx - 1]
        if a > 0:
            J = pari.idealmul(nf, J, pari.idealpow(nf, P, a))
        if k - a > 0:
            J = pari.idealmul(nf, J, pari.idealpow(nf, Pc, k - a))
    return J


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", type=int, default=101)
    parser.add_argument("--k", type=int, default=2)
    parser.add_argument("--pair-limit", type=int, default=8)
    parser.add_argument("--max-report", type=int, default=12)
    parser.add_argument("--precision", type=int, default=100)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--configuration-output", default=DEFAULT_CONFIG_OUTPUT)
    args = parser.parse_args()

    timings = {}
    pari = Pari()
    pari(f"default(realprecision,{args.precision})")

    start = time.perf_counter()
    pari("x='x")
    pol = pari(
        "pol=polcompositum(x^2+1,x^2-5)[1];"
        "pol=polcompositum(pol,x^2-13)[1];"
        "pol=polcompositum(pol,x^2-17)[1];"
        "pol"
    )
    timings["field_polynomial_s"] = time.perf_counter() - start

    start = time.perf_counter()
    nf = pari.nfinit(pol)
    auts = pari.nfgaloisconj(nf)
    cm_index, cm_error, cm = detect_cm_conjugation(pari, nf, pol, auts)
    timings["nf_and_automorphisms_s"] = time.perf_counter() - start

    start = time.perf_counter()
    dec = pari.idealprimedec(nf, args.p)
    pairs_all = pair_prime_ideals(pari, nf, dec, cm)
    pairs = pairs_all[: args.pair_limit]
    prime_hnfs = [pari.idealhnf(nf, dec[i]) for i in range(len(dec))]
    timings["prime_pairing_s"] = time.perf_counter() - start

    start = time.perf_counter()
    bnf = pari.bnfinit(pol, 1)
    pari("bnf_tmp=bnfinit(pol,1)")
    class_number = int(pari("bnf_tmp.no"))
    cyc = gen_int_vector(pari("bnf_tmp.cyc"))
    timings["bnf_s"] = time.perf_counter() - start

    start = time.perf_counter()
    eP = []
    ePc = []
    pair_classes = []
    for pair_index, (p_idx, pc_idx) in enumerate(pairs, start=1):
        cls_p = canonical_mod_vector(
            gen_int_vector(pari.bnfisprincipal(bnf, prime_hnfs[p_idx - 1], 0)),
            cyc,
        )
        cls_pc = canonical_mod_vector(
            gen_int_vector(pari.bnfisprincipal(bnf, prime_hnfs[pc_idx - 1], 0)),
            cyc,
        )
        eP.append(cls_p)
        ePc.append(cls_pc)
        pair_classes.append({"index": pair_index, "P": cls_p, "Pc": cls_pc})
    timings["prime_class_vectors_s"] = time.perf_counter() - start

    start = time.perf_counter()
    base = args.k + 1
    record_count = base ** len(pairs)
    seen: dict[tuple[int, ...], tuple[int, list[int]]] = {}
    collisions = []
    for record_id in range(record_count):
        exps = decode_exponents(record_id, base, len(pairs))
        cls = class_of_exponents(exps, eP, ePc, args.k, cyc)
        key = tuple(cls)
        if key in seen:
            left_id, left_exps = seen[key]
            right_exps = exps
            JL = build_J(pari, nf, prime_hnfs, pairs, left_exps, args.k)
            JR = build_J(pari, nf, prime_hnfs, pairs, right_exps, args.k)
            ratio = pari.idealdiv(nf, JL, JR)
            principal = pari.bnfisprincipal(bnf, ratio, 3)
            principal_class = gen_int_vector(principal[0])
            gam = principal[1]
            gam_c = pari.nfgaloisapply(nf, cm, gam)
            u = pari.nfeltdiv(nf, gam, gam_c)
            u_emb = pari.nfeltembed(nf, u)[0]
            abs_u_minus_1 = pari.abs(pari.abs(u_emb) - 1)
            collisions.append(
                {
                    "index": len(collisions) + 1,
                    "left_index": left_id + 1,
                    "right_index": record_id + 1,
                    "left_exponents": left_exps,
                    "right_exponents": right_exps,
                    "delta": [a - b for a, b in zip(left_exps, right_exps)],
                    "class": cls,
                    "principal_class_vector": principal_class,
                    "gamma_basis_vector": gen_str_vector(gam),
                    "gamma_conjugate_basis_vector": gen_str_vector(gam_c),
                    "u_basis_vector": gen_str_vector(u),
                    "u_embedding": complex_parts(pari, u_emb),
                    "abs_u_minus_1": str(abs_u_minus_1),
                }
            )
            if len(collisions) >= args.max_report:
                break
        else:
            seen[key] = (record_id, exps)
    timings["collision_search_and_principalization_s"] = time.perf_counter() - start

    result = {
        "source": "cypari2 direct export",
        "field": {
            "label": "Q(i, sqrt(5), sqrt(13), sqrt(17))",
            "degree": int(pari.poldegree(pol)),
            "polynomial": str(pol),
            "automorphisms": len(auts),
        },
        "parameters": {
            "p": args.p,
            "k": args.k,
            "pair_limit": args.pair_limit,
            "max_report": args.max_report,
            "precision": args.precision,
        },
        "cm": {
            "index": cm_index,
            "automorphism": str(cm),
            "detection_error": cm_error,
        },
        "prime_decomposition": {
            "split_prime_ideals": len(dec),
            "cm_pairs_total": len(pairs_all),
            "cm_pairs_used": len(pairs),
            "pairs": [
                {"index": idx, "prime_indices": list(pair)}
                for idx, pair in enumerate(pairs, start=1)
            ],
        },
        "class_group": {
            "class_number": class_number,
            "cyc": cyc,
        },
        "pair_classes": pair_classes,
        "j_record_count": record_count,
        "collisions_reported": len(collisions),
        "collisions": collisions,
        "timings_s": timings,
    }

    unique_directions = []
    seen_directions = {}
    for collision in collisions:
        key = tuple(collision["u_basis_vector"])
        if key in seen_directions:
            collision["duplicate_of_direction_index"] = seen_directions[key]
            continue
        direction_index = len(unique_directions) + 1
        seen_directions[key] = direction_index
        collision["duplicate_of_direction_index"] = None
        unique_directions.append(
            {
                "direction_index": direction_index,
                "collision_index": collision["index"],
                "u_basis_vector": collision["u_basis_vector"],
                "u_embedding": collision["u_embedding"],
                "abs_u_minus_1": collision["abs_u_minus_1"],
                "delta": collision["delta"],
            }
        )
    result["unique_direction_count"] = len(unique_directions)
    result["unique_directions"] = unique_directions

    points = [[0.0, 0.0]]
    edges = []
    for idx, direction in enumerate(unique_directions, start=1):
        emb = direction["u_embedding"]
        points.append([emb["real_float"], emb["imag_float"]])
        edges.append([0, idx, idx - 1])

    config = {
        "source": str(Path(args.output)),
        "kind": "degree16_direction_star",
        "field": result["field"]["label"],
        "k": args.k,
        "num_points": len(points),
        "num_edges": len(edges),
        "points": points,
        "edges": edges,
        "edge_certification": "Each edge is {0, u}, with u = gamma / gamma^c from an exact principalized ideal ratio.",
        "directions": unique_directions,
        "collision_count_before_deduplication": len(collisions),
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2))

    config_path = Path(args.configuration_output)
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(json.dumps(config, indent=2))

    print("field degree:", result["field"]["degree"])
    print("CM pairs used:", len(pairs))
    print("J records:", record_count)
    print("collisions:", len(collisions))
    print("unique directions:", len(unique_directions))
    print("output:", output_path)
    print("configuration:", config_path)


if __name__ == "__main__":
    main()
