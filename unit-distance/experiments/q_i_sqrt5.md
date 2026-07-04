# Experiment 01: `K = Q(i, sqrt(5))`

## Purpose

This is the first non-toy coordinate-realization experiment.  It does not
attempt to reproduce the optimized exponent.  It tests whether the actual
OpenAI mechanism can be made computational:

- factor a rational split prime in a CM field;
- build the ideal products from the pigeonhole lemma;
- principalize collided ideal ratios;
- form algebraic directions `u = gamma / conjugate(gamma)`;
- enumerate a finite lattice sample;
- project to the plane and verify exact unit-distance edges.

## Field

Use

`K = Q(theta)`, where `theta = sqrt(5) + i`.

Then

`theta^4 - 8 theta^2 + 36 = 0`.

Inside `K`,

- `sqrt(5) = (14 theta - theta^3)/12`;
- `i = (theta^3 - 2 theta)/12`;
- complex conjugation over `Q(sqrt(5))` sends
  `theta` to `(8 theta - theta^3)/6`.

This gives an absolute degree-4 field with an explicit CM involution.

## Split prime

Use `p = 101`.

Reason:

- `101 = 1^2 + 10^2`, so `101` splits in `Q(i)`;
- `45^2 = 5 mod 101`, so `101` splits in `Q(sqrt(5))`;
- hence `101` splits completely in `Q(i, sqrt(5))`.

Expected factorization:

`101 O_K = P_1 P_1^c P_2 P_2^c`.

## Prototype construction

For small `k`, build

`J(a) = prod_j P_j^{a_j} (P_j^c)^{k-a_j}`.

For this degree-4 field there should be only two conjugate pairs, so for
`k = 1` there are four ideals, for `k = 2` there are nine, and so on.

For each pair of ideals `J(a), J(b)`, test whether

`J(a) J(b)^(-1)`

is principal.  If yes, choose a generator `gamma` and form

`u = gamma / gamma^c`.

Each such `u` has complex absolute value one in every CM embedding, so it is a
candidate unit-distance direction after projection.

## Lattice sample

The proof uses the denominator lattice `Q^(-2)`, where

`Q = prod_j (P_j P_j^c)^k`.

For the first pass, enumerate a coefficient box in a `Z`-basis of `Q^(-2)`.
This is not yet the optimal bounded ball from the proof, but it is enough to
verify exact unit edges:

`x` and `x + u` are both in the enumerated set.

For the very first smoke test, use `--edge-closure`.  This adds `x + u` to
the sampled set whenever `x` is sampled and `u` is a found direction.  It gives
actual coordinates and exact edges as soon as a direction is found, but it is
not yet the proof's bounded-window construction.

Later iterations should replace the coefficient box by the correct sup-norm
window in the Minkowski embedding, and then optimize the translate.

## Success criteria

Minimum success:

- Sage factors `101 O_K` into four degree-one prime ideals.
- The script finds at least one exact algebraic direction `u`.
- The script outputs a finite point set with at least one verified edge.

Good success:

- Multiple directions are found.
- The point cloud has enough edges to visualize.
- Projected edge lengths are numerically `1` to high precision.

Failure modes worth analyzing:

- Principalization helper needs a different Sage/PARI call.
- The coefficient-box lattice sample is too crude and misses edges.
- The field has class number one, giving a valid but too-trivial collision
  test.  This is acceptable for the first pass; the next pass should use a
  larger field with a nontrivial class group.

## Commands

```bash
bash unit-distance/sage/run_q_i_sqrt5.sh --k 1 --coeff-bound 1 --edge-closure
bash unit-distance/sage/run_q_i_sqrt5.sh --k 2 --coeff-bound 2 --edge-closure
```
