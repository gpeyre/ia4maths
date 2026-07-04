# Experiment 04: degree-16 direction patches

## Purpose

This experiment turns the degree-16 PARI principalization output into actual
planar point coordinates.

It uses exact exported directions

`u = gamma / gamma^c`

from `Q(i, sqrt(5), sqrt(13), sqrt(17))` and forms additive patches

`c_1 u_1 + ... + c_m u_m`.

This gives genuine finite unit-distance graphs, because every recorded edge
has exact difference equal to one exported algebraic unit direction.

## Scripts

Direct PARI/cypari2 export:

```bash
/Users/gpeyre/miniconda3/envs/unit-distance-sage/bin/python unit-distance/python/pari_degree16_export.py
```

Additive patch generation:

```bash
python3 unit-distance/python/direction_patch_from_export.py --include-exact-points
python3 unit-distance/python/direction_patch_from_export.py --side 3 --output unit-distance/output/degree16_direction_patch_s3.json
```

Plotting:

```bash
MPLCONFIGDIR=unit-distance/.matplotlib python3 unit-distance/python/plot_configuration.py unit-distance/output/degree16_direction_patch_s2.json --output unit-distance/output/degree16_direction_patch_s2.png --point-size 7 --max-edges 600
MPLCONFIGDIR=unit-distance/.matplotlib python3 unit-distance/python/plot_configuration.py unit-distance/output/degree16_direction_patch_s3.json --output unit-distance/output/degree16_direction_patch_s3.png --point-size 2.5 --max-edges 5000
```

## Outputs

- `unit-distance/output/degree16_openai_principalization_direct.json`
- `unit-distance/output/degree16_direction_star.json`
- `unit-distance/output/degree16_direction_star.png`
- `unit-distance/output/degree16_direction_patch_s2.json`
- `unit-distance/output/degree16_direction_patch_s2.png`
- `unit-distance/output/degree16_direction_patch_s3.json`
- `unit-distance/output/degree16_direction_patch_s3.png`

## Verified counts

The direct exporter found:

- `12` principalized collisions;
- `7` distinct exact algebraic directions after deduplication.

The additive patches have:

| Patch | Points | Certified edges |
|---|---:|---:|
| star | 8 | 7 |
| side 2 | 128 | 448 |
| side 3 | 2187 | 10206 |

For side length `s` and `m = 7` directions, the expected edge count is

`m (s - 1) s^(m - 1)`,

which gives `448` for `s = 2` and `10206` for `s = 3`.

## Caveat

These are actual algebraic unit-distance configurations, but they are not yet
the OpenAI proof's denominator-lattice/Minkowski-window construction.  They
should be treated as coordinate smoke tests for the degree-16 direction layer,
not as empirical asymptotic samples for the theorem.
