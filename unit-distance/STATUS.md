# Status

## Completed

### Tooling

- Created Conda environment `unit-distance-sage`.
- Verified SageMath 10.9.
- Verified PARI/GP 2.17.3.
- Verified `cypari2` import.
- Routed Sage/IPython caches to the project-local `unit-distance/` folder.
- Fixed the macOS Conda dynamic-library issue by ad-hoc signing
  `libdeflate.0.dylib`.

### Degree-4 actual algebraic prototype

Field:

`K = Q(i, sqrt(5))`.

Main outputs:

- `unit-distance/output/q_i_sqrt5_k1_b1.json`
- `unit-distance/output/q_i_sqrt5_k2_b2.json`
- `unit-distance/output/q_i_sqrt5_k1_center0_window.json`
- `unit-distance/output/q_i_sqrt5_k1_center0_R075_patch2.json`

Verified facts:

- `101 O_K` factors into 4 prime ideals.
- These form 2 CM-conjugate pairs.
- For `k=1`, the construction finds 4 directions.
- For `k=2`, the construction finds 12 directions.
- Projected direction lengths are numerically `1.0`.

### Degree-16 PARI/GP principalization probe

Field:

`K = Q(i, sqrt(5), sqrt(13), sqrt(17))`.

Main files:

- `unit-distance/pari/degree16_openai_principalization_probe.gp`
- `unit-distance/output/degree16_openai_principalization_probe.txt`
- `unit-distance/output/degree16_openai_principalization_probe.json`
- `unit-distance/output/degree16_openai_principalization_direct.json`
- `unit-distance/output/degree16_direction_star.json`
- `unit-distance/output/degree16_direction_patch_s2.json`
- `unit-distance/output/degree16_direction_patch_s3.json`
- `unit-distance/experiments/pari_degree16_principalization.md`
- `unit-distance/experiments/degree16_direction_patches.md`
- `unit-distance/python/parse_pari_degree16_log.py`
- `unit-distance/python/pari_degree16_export.py`
- `unit-distance/python/direction_patch_from_export.py`

Verified facts for `p = 101`, `k = 2`:

- PARI/GP builds a degree-16 absolute field quickly.
- `101 O_K` factors into 16 prime ideals.
- The 16 primes are paired into 8 CM-conjugate pairs.
- The class group has order `1024` and invariants `[8, 8, 8, 2]`.
- The script enumerates `(k+1)^8 = 6561` OpenAI-style ideals by class vector.
- It finds nontrivial class collisions and principalizes exact ideal ratios.
- The recovered generators `gamma` give directions
  `u = gamma / gamma^c` with numerical `|u| = 1` up to roughly `1e-72` or
  better.
- The PARI text log is parsed into JSON with collision exponent vectors,
  gamma basis vectors, and projected direction embeddings.
- The direct cypari2 exporter reports 12 principalized collisions and 7 unique
  exact algebraic directions.
- The first degree-16 coordinate smoke tests are generated from those
  directions:
  - star: 8 points and 7 certified edges;
  - side-2 additive patch: 128 points and 448 certified edges;
  - side-3 additive patch: 2187 points and 10206 certified edges.
- The centered-window subset
  `q_i_sqrt5_k1_center0_window.json` has 243 points and 81 exact edges.
- The larger centered-window subset
  `q_i_sqrt5_k1_center0_R075_patch2.json` has 2500 points and 1250 exact
  edges.

This is no longer a toy point cloud: points are algebraic lattice points and
edges are verified by exact algebraic addition `x + u`.

### Degree-8 multiquadratic prototype

Field:

`K = Q(i, sqrt(5), sqrt(13))`.

Main outputs:

- `unit-distance/output/q_i_sqrt5_sqrt13_k1_smoke.json`
- `unit-distance/output/q_i_sqrt5_sqrt13_k1_center0_window.json`
- `unit-distance/output/q_i_sqrt5_sqrt13_k1_center0_R075_patch1.json`

Verified facts:

- `101 O_K` factors into 8 prime ideals.
- These form 4 CM-conjugate pairs.
- For `k=1`, the construction finds 16 directions.
- The smoke test has 17 points and 16 exact edges.
- The centered-window subset
  `q_i_sqrt5_sqrt13_k1_center0_R075_patch1.json` has 19683 points and 6561
  exact edges.
- Projected direction lengths are numerically `1.0`.

## Important caveat

The current centered-window computations are verified subsets of a true
Minkowski window.  They are not yet complete enumerations of all lattice
points in the window.  The reason is that the fractional-ideal basis is very
skew: points close in the Minkowski norm can be far apart in raw coefficient
coordinates.  The current code therefore enumerates small coefficient patches
around selected endpoints and then filters by the true Minkowski norm.

This is honest for producing actual coordinates and verified edges, but it is
not yet enough to claim empirical asymptotic curves.

## Current blocker

The direct Sage relative-field implementation becomes too slow at

`K = Q(i, sqrt(5), sqrt(13), sqrt(17))`

even with `--max-pairs 4`, before producing the first factorization summary.
The process spent several minutes at full CPU and was stopped.

This is no longer a principalization blocker: the PARI/GP absolute-field probe
now principalizes degree-16 OpenAI-style ideal ratios quickly.

The remaining blocker is the proof-faithful lattice layer.  We can now produce
actual degree-16 point coordinates from exported directions, but the ideals and
denominator lattice still must be rebuilt in a coordinate pipeline so that we
can enumerate true Minkowski windows, project points, and verify edges in the
OpenAI proof's original geometry.

## Next algorithmic route

To continue toward the OpenAI base

`Q(i, sqrt(5), sqrt(13), sqrt(17), sqrt(21), sqrt(33))`,

do not rely on generic Sage relative-field factorization.  Instead:

1. Use the explicit multiquadratic structure.
2. Represent split primes by sign vectors of square roots modulo `p`.
3. Build only the needed prime ideals from congruence conditions.
4. Use PARI/GP for principalization after class-vector collisions are
   selected.
5. Export PARI basis vectors and ideals to JSON for coordinate enumeration.
6. Keep `--max-pairs` as a diagnostic throttle.

For a full Sawin/Emmerich realization, the remaining hard step is still the
finite class-field-tower layer plus the relative-class-group construction.

## New fast layer

`unit-distance/python/multiquadratic_split.py` implements the split-prime
front-end without constructing a high-degree Sage number field.  It represents
prime ideals above a split rational prime by sign vectors of square roots
modulo `p`, pairs them under CM conjugation, and enumerates the combinatorics
of the OpenAI pigeonhole ideals `J(a)`.

This layer is not a coordinate generator by itself, but it completes the fast
split-prime bookkeeping needed before the principalization stage.

Verified outputs for `p=101`:

- `q_i_sqrt5_split_p101_k1.json`: degree 4, 4 split-prime labels, 2 CM pairs.
- `q_i_sqrt5_sqrt13_split_p101_k1.json`: degree 8, 8 labels, 4 CM pairs.
- `q_i_sqrt5_sqrt13_sqrt17_split_p101_k1_pair4.json`: degree 16, 16 labels,
  8 total CM pairs, 4 materialized pairs.
- `openai_multiquadratic_base_split_p101_k1_pair8.json`: degree 64, 64 labels,
  32 total CM pairs, 8 materialized pairs.
- `openai_multiquadratic_base_split_p101_k1_allpairs.json`: degree 64, all 32
  CM pairs, `2^32 = 4294967296` formal `J(a)` records for `k=1`; records are
  counted but not materialized.

This bypasses the degree-16 Sage factorization bottleneck for the split-prime
bookkeeping stage.  The new PARI probe also bypasses the degree-16
principalization bottleneck.  The next bottleneck is converting those exact
PARI outputs into point coordinates and exact edge verification.
