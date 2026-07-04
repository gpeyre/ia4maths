# Experiment 02: split-prime sign vectors

## Purpose

The direct Sage relative-field implementation works through degree 8 but is
too slow at degree 16.  This experiment replaces generic prime factorization
by the explicit structure of multiquadratic fields.

For

`K = Q(i, sqrt(d1), ..., sqrt(dm))`

and a prime `p` that splits completely, a prime ideal above `p` is determined
by a sign vector for fixed square roots of

`-1, d1, ..., dm mod p`.

CM conjugation flips only the sign of `i`.

## Script

```bash
python3 unit-distance/python/multiquadratic_split.py --field openai_multiquadratic_base --p 101 --k 1
```

## Verified outputs

For `p = 101`:

| Field | Degree of `K` | Split labels | CM pairs |
|---|---:|---:|---:|
| `Q(i, sqrt(5))` | 4 | 4 | 2 |
| `Q(i, sqrt(5), sqrt(13))` | 8 | 8 | 4 |
| `Q(i, sqrt(5), sqrt(13), sqrt(17))` | 16 | 16 | 8 |
| `Q(i, sqrt(5), sqrt(13), sqrt(17), sqrt(21), sqrt(33))` | 64 | 64 | 32 |

The full OpenAI multiquadratic base has `2^32 = 4294967296` possible `J(a)`
records for `k = 1` if all 32 CM pairs are used.  The script therefore
materializes records only when the count is below `--max-records`, or when
`--max-pairs` is used.

## Important distinction

This layer constructs the split-prime labels and the OpenAI pigeonhole
combinatorics.  It does **not** itself principalize ideal ratios and does not
produce coordinates.

The next layer takes selected sign-vector ideal ratios and recovers actual
generators `gamma`, producing algebraic directions

`u = gamma / gamma^c`.

That principalization step is now prototyped in
`unit-distance/pari/degree16_openai_principalization_probe.gp` for degree 16
using PARI/GP.  The remaining gap is coordinate export and bounded-window
enumeration.
