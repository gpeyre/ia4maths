# Next iteration

## Immediate experiment

Run the Sage prototype:

```bash
bash unit-distance/sage/run_q_i_sqrt5.sh --k 1 --coeff-bound 1 --edge-closure
```

Questions to answer from the JSON output:

1. Does Sage factor `101 O_K` into four prime ideals?
2. Does the CM-conjugation pairing recover two pairs?
3. Does `ideal.is_principal()` expose principal generators for the ideal
   ratios?
4. How many distinct directions `u = gamma / gamma^c` are found?
5. Do projected direction lengths equal `1` numerically?
6. Does the edge-closure point cloud produce exact algebraic edges?

## If principalization fails

The current helper tries common Sage ideal methods.  If it returns zero
directions despite principal ideals existing, replace it by one of:

- Sage's class-group/principal-form machinery;
- a direct PARI `bnfisprincipal` call through Sage;
- Magma's `IsPrincipal` with generator output.

This is the most likely first technical adjustment.

## If the field is too trivial

If `K = Q(i, sqrt(5))` has class number one, the experiment is still useful:
it validates embeddings, conjugation, split prime pairing, directions, and
edge verification.  The next field should then be

`K = Q(i, sqrt(5), sqrt(13))`.

After that, move to the OpenAI multiquadratic base

`K = Q(i, sqrt(5), sqrt(13), sqrt(17), sqrt(21), sqrt(33))`.

## If the coefficient box is misleading

The coefficient box is only a computational scaffold.  Replace it by the
Minkowski sup-norm window:

`||x|| = max_v |sigma_v(x)| / scale_v <= R`.

For the OpenAI prototype, the scale is simple because the directions have
absolute value one in every CM embedding.  For the Sawin route, the scale is
`sqrt(|alpha|_v)`.

## Plot policy

Any picture produced before the true bounded-window implementation should be
called "prototype algebraic realization" rather than "empirical Sawin/OpenAI
curve".

## Completed after the first pass

- SageMath 10.9, PARI/GP 2.17.3, and `cypari2` are installed in the
  `unit-distance-sage` Conda environment.
- The `Q(i, sqrt(5))` smoke tests succeeded.
- The prototype now supports an actual Minkowski window via `--window-radius`.
- Because the ideal basis is highly skew, useful small windows need endpoint
  coefficient patches.  Use `--direction-patches` together with
  `--center-direction` and `--window-radius`.
- `unit-distance/python/plot_configuration.py` plots generated JSON files.

## Current status

See `unit-distance/STATUS.md`.

The direct Sage relative-field path works through degree 8 and becomes too
slow at degree 16.  The next implementation should exploit the explicit
multiquadratic sign-vector structure instead of asking Sage to do generic
relative-field ideal factorization.

## New next step

The degree-16 PARI/GP and cypari2 pipeline now principalizes actual
OpenAI-style ideal ratios in `Q(i, sqrt(5), sqrt(13), sqrt(17))`, exports exact
directions, and builds additive coordinate patches.

Next iteration:

1. Rebuild the denominator ideal/lattice corresponding to the selected
   OpenAI-style `J(a)` family in PARI or Sage.
2. Convert PARI HNF ideal bases into exact lattice bases usable by Python/Sage.
3. Enumerate a small true Minkowski window in that denominator lattice.
4. Compare the proof-faithful window graph with the additive-patch smoke tests.
