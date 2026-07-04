# Experiment 03: degree-16 PARI principalization

## Purpose

The Sage relative-field implementation was too slow for

`K = Q(i, sqrt(5), sqrt(13), sqrt(17))`.

This experiment tests whether PARI/GP can handle the same OpenAI-style
principalization stage in the absolute field.

## Script

```bash
/Users/gpeyre/miniconda3/envs/unit-distance-sage/bin/gp -q unit-distance/pari/degree16_openai_principalization_probe.gp
```

The saved run is:

`unit-distance/output/degree16_openai_principalization_probe.txt`.

A parsed JSON version is produced by:

```bash
python3 unit-distance/python/parse_pari_degree16_log.py
```

and saved as:

`unit-distance/output/degree16_openai_principalization_probe.json`.

## Verified run

Parameters:

- `p = 101`
- `k = 2`
- all `8` CM-conjugate prime pairs over `101`

PARI/GP computed:

- degree `16` absolute defining polynomial;
- `16` Galois automorphisms;
- CM conjugation detected as automorphism index `7`;
- `16` prime ideals over `101`, paired into `8` CM pairs;
- class number `1024`, class group invariants `[8, 8, 8, 2]`;
- `(k+1)^8 = 6561` OpenAI-style ideals `J(a)`;
- nontrivial class collisions and exact principal generators.
- parsed JSON containing collision exponent vectors, `gamma` basis vectors,
  and projected direction embeddings.

The first principalized collisions produce nontrivial generators `gamma`.
For the corresponding directions

`u = gamma / gamma^c`,

the projected numerical checks satisfy `|u| - 1` at about `1e-72` to `1e-110`.

## Important correction

An early draft used PARI's reduced-product flag in `idealmul` when rebuilding
the actual ideals `J(a)`.  That preserves the ideal class but not the literal
ideal product, so it incorrectly collapsed principal generators to `1`.

The current script uses unreduced ideal products for `build_J`, while using
class-vector arithmetic only for the fast collision search.

## Consequence

The degree-16 principalization/generator stage is now viable.  The remaining
work is to export these PARI generators and ideals into the coordinate
pipeline:

1. convert PARI basis vectors for `gamma` into a stable JSON format;
2. compute all embeddings and direction coordinates;
3. build the denominator lattice for the selected `J(a)` family;
4. enumerate a true Minkowski window;
5. verify exact algebraic edges after projection.
