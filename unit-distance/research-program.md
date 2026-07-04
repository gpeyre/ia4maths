# Coordinate realization program for the new unit-distance constructions

## Status

The OpenAI, Sawin, and Emmerich constructions are constructive at the
asymptotic certificate level, but they do not currently provide finite planar
coordinate files.  A coordinate generator must add several missing pieces:

- a concrete finite tower layer `F`;
- the CM extension `K/F`, usually `K = F(i)`;
- integral bases and all complex embeddings;
- split prime ideals and conjugate prime pairs;
- class-group or relative-class-group collisions;
- principal generators for collided ideal ratios;
- a bounded lattice window and a good translate;
- the final projection to one complex embedding.

Plain Python is not enough for this.  The backend should be Sage, PARI/GP, or
Magma.

Current computational status:

- Sage produces actual verified coordinate subsets through
  `Q(i, sqrt(5), sqrt(13))`.
- Sage's generic relative-field ideal arithmetic stalls at
  `Q(i, sqrt(5), sqrt(13), sqrt(17))`.
- PARI/GP now principalizes actual OpenAI-style degree-16 ideal ratios in the
  absolute field for `p = 101`, `k = 2`, recovering nontrivial generators
  `gamma` and unit-modulus directions `gamma / gamma^c`.
- Direct cypari2 export now produces exact direction data, and additive
  degree-16 coordinate patches have been generated up to 2187 points and 10206
  certified unit edges.
- The next missing layer is not principalization or basic coordinates, but the
  proof-faithful denominator lattice: true Minkowski-window enumeration,
  projection, and exact edge verification from the original OpenAI geometry.

## What the papers/repository give

OpenAI/human writeup:

- Uses a CM field `K = L(i)`, where `L` is a finite layer in an infinite
  Golod-Shafarevich 2-class tower.
- Uses split prime ideals `P_j, conjugate(P_j)` and a pigeonhole argument in
  the class group of `K`.
- Produces many elements `u = alpha / conjugate(alpha)` with absolute value
  one in every complex embedding.
- Then uses a bounded window in the lattice `D^{-1} O_K` and projects one
  complex coordinate.

Sawin:

- Refines the OpenAI mechanism by working with ideals in a CM extension
  `K/F`.
- Produces an ideal `I` and an element `alpha in N_{K/F}(I)`.
- Needs many `beta in I` satisfying `beta conjugate(beta) = alpha`.
- Projects `B(R,w) cap I` to one complex embedding, normalized by
  `sqrt(|alpha|_v)`.

Emmerich:

- Optimizes the finite certificate `(T, S_Q, k, R)` and verifies larger
  exponents.
- Explicitly does not construct finite fields, ideals, embeddings, a bounded
  window, or planar coordinates.

## Core algorithm, OpenAI-style first target

This is the easier route for a first true coordinate realization, even if it
does not initially reach the optimized exponent.

Input:

- a concrete CM field `K = L(i)`;
- one or more rational primes `p` split completely in `K`;
- a small integer `k`;
- a window radius `R`.

Algorithm:

1. Compute `O_K`, complex embeddings, discriminant, and class group.
2. Factor each `p O_K`.
3. Pair each prime ideal `P` with `conjugate(P)`.
4. Build ideals
   `J(a) = prod_j P_j^{a_j} conjugate(P_j)^{k-a_j}`,
   with `0 <= a_j <= k`.
5. Hash the class of each `J(a)` in `Cl(K)`.
6. Pick a large class-group fiber.
7. For pairs `J(a), J(b)` in that fiber, principalize
   `J(a) J(b)^(-1) = (gamma)`.
8. Form unit-distance directions
   `u = gamma / conjugate(gamma)`.
9. Define the lattice `Lambda = Q^(-2)` or the corresponding denominator
   lattice used by the proof.
10. Enumerate candidate points in `(tau + Lambda) cap B_R`, for sampled
    translates `tau`.
11. Project to one complex embedding and normalize.
12. Verify unit distances algebraically.

Expected first result:

- actual coordinates;
- actual unit-distance edges;
- no asymptotic exponent claim yet.

## Sawin/Emmerich route

This is the route needed for the optimized exponents.

Input:

- a verified certificate `(T, S_Q, k, R)`;
- a concrete finite field `F` satisfying the tower/splitting conditions;
- `K = F(i)`;
- prime ideals of `F` above all primes in `S_Q`.

Algorithmic replacement of the OpenAI pigeonhole:

1. Work in the modified relative class group `G_K` used by Sawin.
2. Enumerate ideals with relative norm
   `prod_{p in S_Q} mathfrak p^{k(p)}`.
3. Hash pairs `(J, generator of N_{K/F}(J))` modulo the equivalence in
   `G_K`.
4. From a large fiber, recover an ideal `I`, an element `alpha`, and many
   `beta in I` with `beta conjugate(beta) = alpha`.
5. Use Sawin's lattice norm
   `||x|| = sup_v |x_v| / sqrt(|alpha|_v)`.
6. Enumerate `B(R,w) cap I`, project, and verify edges.

This is harder than the OpenAI-style route because the relative class group
and norm generators must be represented explicitly.

## Why arbitrary `n` is not immediate

The proofs give arbitrarily large examples, not a simple exact-size generator.
For a target `n`, a practical generator should:

1. choose a tower layer and radius producing at least `n` points;
2. compute all edges in the generated configuration;
3. choose an induced subset, random subset, or optimized subset of size `n`;
4. report the actual surviving number of unit distances.

This would give actual empirical curves, but exact optimal behavior for every
`n` is a separate combinatorial optimization problem.

## Scale warning

The proof constants are enormous.  For the Emmerich v23 certificates, the
base `A = 2 R prod_p p^{k(p)/(2e(p))} + 1` has

- Sawin published example: `log10(A) ~= 119.46`;
- optimized candidate: `log10(A) ~= 124.07`;
- integer ES certificate: `log10(A) ~= 125.83`;
- discrete recombination certificate: `log10(A) ~= 128.71`.

Since the proof bounds `#U` by roughly `A^(2d)`, even `d = 1` corresponds to
astronomical upper-bound scales.  Therefore the first computable realizations
should target the mechanism, not the certified asymptotic constants.

## Milestones

M0. Install or use Sage/Magma/PARI.

M1. Reproduce the classical Gaussian-integer grid inside the same code path.

M2. Run the OpenAI-style class-group collision on a small explicit CM field
where all arithmetic is easy.

M3. Use the multiquadratic base field from the OpenAI example and a small
`k`, producing actual coordinates without claiming the asymptotic exponent.

M4. Compute one finite 2-class-tower layer satisfying the required splitting
conditions and repeat M3.

M5. Implement Sawin's relative-class-group version and feed it the
Sawin/Emmerich certificates.

## Best first experiment

Do not start with the full Sawin or Emmerich certificate.  Start with the
small CM field

`K = Q(i, sqrt(5))`, with totally real subfield `F = Q(sqrt(5))`.

Reason:

- the rational prime `101` splits in `Q(i)` and in `Q(sqrt(5))`;
- hence `101` splits completely in `K`;
- the field has degree only `4`, so class groups, prime ideals, embeddings,
  and principal generators should be computable;
- this is a real algebraic instance of the OpenAI mechanism, although it is
  not an asymptotic tower-layer realization.

Concrete target for this experiment:

1. Factor `101 O_K`.
2. Pair the four prime ideals into two conjugate pairs over `F`.
3. Take `k = 1, 2, 3`.
4. Principalize the ideals
   `P_1^{a_1} conjugate(P_1)^{k-a_1}
    P_2^{a_2} conjugate(P_2)^{k-a_2}`.
5. Form directions `u = gamma / conjugate(gamma)`.
6. Enumerate a small bounded lattice window.
7. Output actual projected coordinates and verify exact unit-distance edges.

If this succeeds, move to

`K = Q(i, sqrt(5), sqrt(13))`

and then to the OpenAI multiquadratic base

`K = Q(i, sqrt(5), sqrt(13), sqrt(17), sqrt(21), sqrt(33))`.

The last field is still not a nontrivial tower layer, but it is the explicit
multiquadratic quotient appearing in the OpenAI example and is the natural
gateway before computing Hilbert 2-class-field layers.

## Slide implication

Until M2-M5 exist, any B/C/D "empirical" curves in the animation should be
removed or explicitly labeled as schematic.  The only honest numerical curve
available now is the grid curve, plus theoretical/asymptotic curves from the
certificates.

## References

- Sawin, "An explicit lower bound for the unit distance problem",
  https://arxiv.org/abs/2605.20579
- OpenAI/human writeup, "A note on the unit distance problem",
  https://arxiv.org/abs/2605.20695
- Emmerich certificate optimizer,
  https://github.com/emmerichmtm/UnitDistanceProblemOptimizationOfSawinsLowerBound
