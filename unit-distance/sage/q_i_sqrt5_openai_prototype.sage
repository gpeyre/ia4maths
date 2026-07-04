#!/usr/bin/env sage
"""
First coordinate-realization prototype for the OpenAI unit-distance mechanism.

Target field:
    K = Q(i, sqrt(5)) = Q(theta), theta = sqrt(5) + i.

This script needs Sage.  It is intentionally conservative: it brute-forces
small ideal-ratio principalization tests and enumerates a coefficient box in
the denominator lattice.  Later iterations should replace the coefficient box
by the exact Minkowski sup-norm window and translate optimization.
"""

import argparse
import json
import os
from itertools import combinations, product

from sage.all import *


def build_q_i_sqrt5():
    R.<x> = PolynomialRing(QQ)
    K.<theta> = NumberField(x^4 - 8*x^2 + 36)
    sqrt5 = (14 * theta - theta^3) / 12
    ii = (theta^3 - 2 * theta) / 12

    # CM conjugation over Q(sqrt(5)): sqrt(5) is fixed and i changes sign.
    theta_conj = (8 * theta - theta^3) / 6
    cm_conj = K.hom([theta_conj], K)
    return {
        "field": K,
        "label": "Q(i, sqrt(5))",
        "equation": "Q(theta), theta^4 - 8 theta^2 + 36 = 0",
        "sqrt5": sqrt5,
        "ii": ii,
        "cm_conj": cm_conj,
    }


def build_q_i_sqrt5_sqrt13():
    R.<x> = PolynomialRing(QQ)
    K.<ii, a, b> = NumberField([x^2 + 1, x^2 - 5, x^2 - 13])
    cm_conj = K.hom([-ii], K)
    return {
        "field": K,
        "label": "Q(i, sqrt(5), sqrt(13))",
        "equation": "Q(i, sqrt(5), sqrt(13)) as a relative multiquadratic tower",
        "sqrt5": a,
        "ii": ii,
        "cm_conj": cm_conj,
    }


def build_q_i_sqrt5_sqrt13_sqrt17():
    R.<x> = PolynomialRing(QQ)
    K.<ii, a, b, c> = NumberField([x^2 + 1, x^2 - 5, x^2 - 13, x^2 - 17])
    cm_conj = K.hom([-ii], K)
    return {
        "field": K,
        "label": "Q(i, sqrt(5), sqrt(13), sqrt(17))",
        "equation": "Q(i, sqrt(5), sqrt(13), sqrt(17)) as a relative multiquadratic tower",
        "sqrt5": a,
        "ii": ii,
        "cm_conj": cm_conj,
    }


def build_openai_multiquadratic_base():
    R.<x> = PolynomialRing(QQ)
    K.<ii, a, b, c, d, e> = NumberField(
        [x^2 + 1, x^2 - 5, x^2 - 13, x^2 - 17, x^2 - 21, x^2 - 33]
    )
    cm_conj = K.hom([-ii], K)
    return {
        "field": K,
        "label": "Q(i, sqrt(5), sqrt(13), sqrt(17), sqrt(21), sqrt(33))",
        "equation": "OpenAI multiquadratic base K = L_T(i), not a tower layer",
        "sqrt5": a,
        "ii": ii,
        "cm_conj": cm_conj,
    }


def build_field(name):
    if name == "q_i_sqrt5":
        return build_q_i_sqrt5()
    if name == "q_i_sqrt5_sqrt13":
        return build_q_i_sqrt5_sqrt13()
    if name == "q_i_sqrt5_sqrt13_sqrt17":
        return build_q_i_sqrt5_sqrt13_sqrt17()
    if name == "openai_multiquadratic_base":
        return build_openai_multiquadratic_base()
    raise ValueError("unknown field: %s" % name)


def image_ideal(phi, ideal):
    K = phi.codomain()
    return K.ideal([phi(g) for g in ideal.gens()])


def pair_conjugate_primes(prime_ideals, cm_conj):
    unused = list(range(len(prime_ideals)))
    pairs = []
    while unused:
        i = unused.pop(0)
        target = image_ideal(cm_conj, prime_ideals[i])
        match_pos = None
        for pos, j in enumerate(unused):
            if prime_ideals[j] == target:
                match_pos = pos
                break
        if match_pos is None:
            raise RuntimeError("Could not pair a prime ideal with its CM conjugate")
        j = unused.pop(match_pos)
        pairs.append((prime_ideals[i], prime_ideals[j]))
    return pairs


def ideal_generator_if_principal(ideal):
    """Return a generator if Sage exposes one, otherwise return None."""
    principal = ideal.is_principal()
    if isinstance(principal, tuple):
        if not principal[0]:
            return None
        if len(principal) > 1 and principal[1] != 0:
            return principal[1]
    elif not principal:
        return None

    if hasattr(ideal, "number_field"):
        K = ideal.number_field()
    else:
        K = ideal.ring().number_field()
    candidate_lists = []
    for method_name in ("gens_reduced", "gens_two", "gens"):
        if hasattr(ideal, method_name):
            try:
                candidate_lists.append(list(getattr(ideal, method_name)()))
            except (TypeError, NotImplementedError, RuntimeError):
                pass

    for candidates in candidate_lists:
        for g in candidates:
            if g != 0 and K.ideal(g) == ideal:
                return g

    return None


def build_openai_ideals(K, pairs, k):
    records = []
    for exponents in product(range(k + 1), repeat=len(pairs)):
        J = K.ideal(1)
        for a, (P, Pc) in zip(exponents, pairs):
            J *= (P ** a) * (Pc ** (k - a))
        records.append({"exponents": tuple(exponents), "ideal": J})
    return records


def direction_records(K, records, cm_conj, max_directions):
    seen = set()
    directions = []

    for left, right in combinations(records, 2):
        ratio_ideal = left["ideal"] * (right["ideal"] ** (-1))
        gamma = ideal_generator_if_principal(ratio_ideal)
        if gamma is None:
            continue
        u = gamma / cm_conj(gamma)
        key = str(u)
        inv_key = str(1 / u)
        if key in seen or inv_key in seen:
            continue
        seen.add(key)
        directions.append(
            {
                "u": u,
                "gamma": gamma,
                "from": left["exponents"],
                "to": right["exponents"],
            }
        )
        if len(directions) >= max_directions:
            break

    return directions


def denominator_lattice(K, pairs, k):
    Q = K.ideal(1)
    for P, Pc in pairs:
        Q *= (P * Pc) ** k
    return Q ** (-2)


def number_field_of_ideal(ideal):
    if hasattr(ideal, "number_field"):
        return ideal.number_field()
    return ideal.ring().number_field()


def element_vector(K, z):
    try:
        V, _from_v, to_v = K.vector_space()
    except NotImplementedError:
        V, _from_v, to_v = K.absolute_vector_space()
    return to_v(z)


def element_coefficients_in_basis(K, basis, z):
    columns = [element_vector(K, b) for b in basis]
    matrix = Matrix(QQ, len(columns[0]), len(columns), columns).transpose()
    # The constructor above uses rows in some Sage versions. Rebuild with
    # explicit columns to avoid ambiguity.
    matrix = Matrix(QQ, len(columns[0]), len(columns))
    for j, col in enumerate(columns):
        for i, value in enumerate(col):
            matrix[i, j] = value
    return list(matrix.solve_right(element_vector(K, z)))


def enumerate_lattice_box(lattice, coeff_bound, coeff_center=None):
    basis = list(lattice.basis())
    K = number_field_of_ideal(lattice)
    zero = K(0)
    if coeff_center is None:
        coeff_center = [0] * len(basis)
    integer_centers = [int(round(float(c))) for c in coeff_center]
    ranges = [
        range(c - coeff_bound, c + coeff_bound + 1)
        for c in integer_centers
    ]
    points = []
    for coeffs in product(*ranges):
        z = zero
        for c, b in zip(coeffs, basis):
            z += c * b
        points.append(z)
    return points


def unique_points(point_lists):
    points = {}
    for point_list in point_lists:
        for z in point_list:
            points[z] = z
    return list(points.values())


def all_complex_embeddings(K):
    return K.embeddings(ComplexField(100))


def minkowski_sup_norm(z, embeddings):
    if not embeddings:
        return 0.0
    return max(float(abs(emb(z))) for emb in embeddings)


def filter_minkowski_window(points, embeddings, radius, center=None):
    radius = float(radius)
    if not points:
        return points
    if center is None:
        center = points[0].parent()(0)
    return [
        z for z in points
        if minkowski_sup_norm(z - center, embeddings) <= radius
    ]


def add_edge_closure(points, directions):
    """Add z + u for sampled z and each direction u.

    This gives an early smoke-test configuration with guaranteed exact edges.
    It is not the final bounded-window construction.
    """
    closed = dict((z, z) for z in points)
    for z in list(points):
        for record in directions:
            y = z + record["u"]
            if y not in closed:
                closed[y] = y
    return list(closed.values())


def choose_embedding(K, sqrt5, ii):
    CC = ComplexField(100)
    target_sqrt5 = CC(5).sqrt()
    best = None
    for emb in K.embeddings(CC):
        score = abs(emb(sqrt5) - target_sqrt5) + abs(emb(ii) - CC.gen())
        if best is None or score < best[0]:
            best = (score, emb)
    return best[1]


def verify_edges(points, directions):
    point_index = {z: idx for idx, z in enumerate(points)}
    edges = []
    for i, z in enumerate(points):
        for d_idx, record in enumerate(directions):
            u = record["u"]
            j = point_index.get(z + u)
            if j is not None:
                edges.append((i, j, d_idx))
    return edges


def complex_pair(z):
    return [float(real(z)), float(imag(z))]


def int_list(values):
    return [int(v) for v in values]


def absolute_discriminant(K):
    if hasattr(K, "absolute_discriminant"):
        return K.absolute_discriminant()
    return K.discriminant()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--field",
        choices=[
            "q_i_sqrt5",
            "q_i_sqrt5_sqrt13",
            "q_i_sqrt5_sqrt13_sqrt17",
            "openai_multiquadratic_base",
        ],
        default="q_i_sqrt5",
    )
    parser.add_argument("--p", type=int, default=101)
    parser.add_argument("--k", type=int, default=1)
    parser.add_argument("--coeff-bound", type=int, default=1)
    parser.add_argument(
        "--window-radius",
        type=float,
        default=None,
        help="Filter candidates by max_v |sigma_v(x)| <= radius.",
    )
    parser.add_argument(
        "--center-direction",
        type=int,
        default=None,
        help="Center the window at u/2 for the selected direction index.",
    )
    parser.add_argument(
        "--direction-patches",
        action="store_true",
        help="Also enumerate coefficient patches around all found directions.",
    )
    parser.add_argument("--max-directions", type=int, default=64)
    parser.add_argument(
        "--max-pairs",
        type=int,
        default=None,
        help="Use only the first max-pairs CM prime pairs.",
    )
    parser.add_argument(
        "--include-ok-basis",
        action="store_true",
        help="Include the full ring-of-integers basis in JSON output.",
    )
    parser.add_argument(
        "--edge-closure",
        action="store_true",
        help="Also include z+u for sampled points z and directions u.",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="JSON output path. Defaults to unit-distance/output/q_i_sqrt5_k*.json",
    )
    args = parser.parse_args()

    field_data = build_field(args.field)
    K = field_data["field"]
    sqrt5 = field_data["sqrt5"]
    ii = field_data["ii"]
    cm_conj = field_data["cm_conj"]
    factorization = list(K.ideal(args.p).factor())
    prime_ideals = [P for P, exponent in factorization for _ in range(exponent)]

    pairs = pair_conjugate_primes(prime_ideals, cm_conj)
    total_pairs = len(pairs)
    if args.max_pairs is not None:
        pairs = pairs[: args.max_pairs]
    records = build_openai_ideals(K, pairs, args.k)
    directions = direction_records(K, records, cm_conj, args.max_directions)
    lattice = denominator_lattice(K, pairs, args.k)
    minkowski_embeddings = all_complex_embeddings(K)
    lattice_basis = list(lattice.basis())
    window_center = K(0)
    coeff_center = None
    if args.center_direction is not None:
        if args.center_direction < 0 or args.center_direction >= len(directions):
            raise ValueError("center direction index out of range")
        window_center = directions[args.center_direction]["u"] / 2
        coeff_center = element_coefficients_in_basis(K, lattice_basis, window_center)
    point_lists = [enumerate_lattice_box(lattice, args.coeff_bound, coeff_center)]
    if args.direction_patches:
        zero_coeffs = [0] * len(lattice_basis)
        point_lists.append(enumerate_lattice_box(lattice, args.coeff_bound, zero_coeffs))
        for record in directions:
            direction_coeffs = element_coefficients_in_basis(
                K,
                lattice_basis,
                record["u"],
            )
            point_lists.append(
                enumerate_lattice_box(lattice, args.coeff_bound, direction_coeffs)
            )
    points = unique_points(point_lists)
    candidate_count = len(points)
    if args.window_radius is not None:
        points = filter_minkowski_window(
            points,
            minkowski_embeddings,
            args.window_radius,
            window_center,
        )
    if args.edge_closure:
        points = add_edge_closure(points, directions)
    edges = verify_edges(points, directions)
    embedding = choose_embedding(K, sqrt5, ii)

    coords = [complex_pair(embedding(z)) for z in points]
    direction_coords = [complex_pair(embedding(record["u"])) for record in directions]

    result = {
        "field": field_data["label"],
        "field_model": field_data["equation"],
        "degree": int(K.absolute_degree()),
        "discriminant": str(absolute_discriminant(K)),
        "p": int(args.p),
        "k": int(args.k),
        "coeff_bound": int(args.coeff_bound),
        "candidate_count": int(candidate_count),
        "window_radius": None if args.window_radius is None else float(args.window_radius),
        "center_direction": None if args.center_direction is None else int(args.center_direction),
        "direction_patches": bool(args.direction_patches),
        "edge_closure": bool(args.edge_closure),
        "ring_of_integers_basis": (
            [str(b) for b in K.ring_of_integers().basis()]
            if args.include_ok_basis
            else None
        ),
        "factorization": [
            {"ideal": str(P), "exponent": int(exponent)}
            for P, exponent in factorization
        ],
        "num_prime_ideals": len(prime_ideals),
        "num_total_conjugate_pairs": int(total_pairs),
        "num_conjugate_pairs": len(pairs),
        "max_pairs": None if args.max_pairs is None else int(args.max_pairs),
        "num_J_ideals": len(records),
        "num_directions": len(directions),
        "directions": [
            {
                "u": str(record["u"]),
                "gamma": str(record["gamma"]),
                "from": int_list(record["from"]),
                "to": int_list(record["to"]),
                "projected": direction_coords[idx],
                "lattice_coefficients": [
                    str(c)
                    for c in element_coefficients_in_basis(K, lattice_basis, record["u"])
                ],
            }
            for idx, record in enumerate(directions)
        ],
        "window_center": str(window_center),
        "window_center_projected": complex_pair(embedding(window_center)),
        "window_center_lattice_coefficients": (
            None if coeff_center is None else [str(c) for c in coeff_center]
        ),
        "num_points": len(points),
        "num_edges": len(edges),
        "points": coords,
        "minkowski_sup_norms": [
            minkowski_sup_norm(z, minkowski_embeddings) for z in points
        ],
        "edges": [list(edge) for edge in edges],
    }

    output = args.output
    if output is None:
        output = "unit-distance/output/q_i_sqrt5_k%s_b%s.json" % (
            args.k,
            args.coeff_bound,
        )
    output_dir = os.path.dirname(output)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(output, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print("field degree:", K.absolute_degree())
    print("factorization length:", len(factorization))
    print("conjugate pairs:", len(pairs))
    print("J ideals:", len(records))
    print("directions:", len(directions))
    print("candidates:", candidate_count)
    if args.window_radius is not None:
        print("window radius:", args.window_radius)
    print("points:", len(points))
    print("edges:", len(edges))
    print("output:", output)


if __name__ == "__main__":
    main()
