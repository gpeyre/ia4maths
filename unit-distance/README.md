# Unit-distance coordinate realization

This folder is a research workspace for turning the new asymptotic
unit-distance constructions into actual finite planar point sets.

The slides currently show the story and theory curves.  This folder is for
the separate computational question:

> Can we generate actual point coordinates for the OpenAI/Sawin/Emmerich
> constructions, compute their exact unit-distance graph, and then animate the
> real empirical curves?

## Current conclusion

The constructions are explicit at the proof/certificate level, but not as
ready-to-plot coordinate data.  A coordinate generator must additionally
construct finite number fields, ideals, embeddings, class-group collisions,
principal generators, lattice windows, and projections.

The first honest target is not the optimized Sawin/Emmerich certificate.  It
is a small algebraic prototype:

`K = Q(i, sqrt(5))`, with split prime `101` and small multiplicity `k`.

This should already test the real OpenAI mechanism: split prime ideals,
principalized ideal ratios, directions of absolute value one, lattice-window
enumeration, planar projection, and exact edge verification.

## Folder layout

- `research-program.md`: global plan and mathematical status.
- `experiments/q_i_sqrt5.md`: first concrete experiment.
- `experiments/sign_vector_layer.md`: fast split-prime combinatorics for
  higher-degree multiquadratic fields.
- `experiments/pari_degree16_principalization.md`: PARI/GP principalization
  probe for the degree-16 OpenAI-style field.
- `experiments/degree16_direction_patches.md`: first degree-16 coordinate
  patches built from exact exported directions.
- `sage/q_i_sqrt5_openai_prototype.sage`: Sage prototype for the first
  experiment.
- `pari/degree16_openai_principalization_probe.gp`: PARI/GP probe that finds
  actual principal generators in `Q(i, sqrt(5), sqrt(13), sqrt(17))`.
- `python/parse_pari_degree16_log.py`: converts the PARI text log into JSON
  for the next coordinate-generation stage.
- `python/pari_degree16_export.py`: direct cypari2 exporter for degree-16
  principalized directions and a star configuration.
- `python/direction_patch_from_export.py`: builds additive point patches from
  exported exact directions.

## Tooling

This needs Sage, PARI/GP, or Magma.  The current local environment has a
dedicated Conda environment with SageMath, PARI/GP, and `cypari2`.

Expected first run once Sage is available:

```bash
bash unit-distance/sage/run_q_i_sqrt5.sh --k 1 --coeff-bound 1 --edge-closure
```

For a larger exploratory point cloud:

```bash
bash unit-distance/sage/run_q_i_sqrt5.sh --k 2 --coeff-bound 2 --edge-closure
```

The script writes JSON output under `unit-distance/output/` by default.

For the first honest bounded-window run:

```bash
bash unit-distance/sage/run_q_i_sqrt5.sh --k 1 --coeff-bound 80 --window-radius 0.02 --output unit-distance/output/q_i_sqrt5_k1_window.json
```

For a centered window containing verified unit edges:

```bash
bash unit-distance/sage/run_q_i_sqrt5.sh --k 1 --coeff-bound 1 --center-direction 0 --window-radius 0.51 --direction-patches --output unit-distance/output/q_i_sqrt5_k1_center0_window.json
```

For the next degree-8 field:

```bash
bash unit-distance/sage/run_q_i_sqrt5.sh --field q_i_sqrt5_sqrt13 --k 1 --coeff-bound 0 --edge-closure --max-directions 16 --output unit-distance/output/q_i_sqrt5_sqrt13_k1_smoke.json
```

For a bounded but pair-limited probe of a higher-degree field:

```bash
bash unit-distance/sage/run_q_i_sqrt5.sh --field q_i_sqrt5_sqrt13_sqrt17 --max-pairs 4 --k 1 --coeff-bound 0 --edge-closure --max-directions 16 --output unit-distance/output/q_i_sqrt5_sqrt13_sqrt17_pair4_smoke.json
```

The fast sign-vector layer avoids Sage's generic high-degree field arithmetic:

```bash
python3 unit-distance/python/multiquadratic_split.py --field openai_multiquadratic_base --p 101 --k 1 --max-pairs 8
```

The degree-16 PARI/GP principalization probe:

```bash
/Users/gpeyre/miniconda3/envs/unit-distance-sage/bin/gp -q unit-distance/pari/degree16_openai_principalization_probe.gp
```

This verifies all 8 CM pairs over `101`, enumerates `6561` OpenAI-style
ideals for `k = 2`, and recovers nontrivial principal generators whose
directions have numerical modulus `1`.

To convert the saved PARI log into structured JSON:

```bash
python3 unit-distance/python/parse_pari_degree16_log.py
```

Preferred direct cypari2 export plus a first direction-star configuration:

```bash
/Users/gpeyre/miniconda3/envs/unit-distance-sage/bin/python unit-distance/python/pari_degree16_export.py
```

Additive patch coordinate smoke tests:

```bash
python3 unit-distance/python/direction_patch_from_export.py --include-exact-points
python3 unit-distance/python/direction_patch_from_export.py --side 3 --output unit-distance/output/degree16_direction_patch_s3.json
```

To plot a generated JSON file:

```bash
python3 unit-distance/python/plot_configuration.py unit-distance/output/q_i_sqrt5_k1_b1.json
```

Local installation used here:

- Conda environment: `unit-distance-sage`
- Sage binary:
  `/Users/gpeyre/miniconda3/envs/unit-distance-sage/bin/sage`
- Sage version verified: `10.9`
- PARI/GP verified: `2.17.3`
- `cypari2` import verified

On this macOS setup, Sage needed two local adjustments:

- `DOT_SAGE` and `IPYTHONDIR` are routed to `unit-distance/.sage` and
  `unit-distance/.ipython`.
- Conda's `libdeflate.0.dylib` needed ad-hoc signing with `codesign`.

## Research policy for plots

Until this pipeline produces actual coordinates for a method, do not label
its numerical curve as empirical.  The grid has real empirical data now; the
OpenAI/Sawin/Emmerich curves should be theoretical or explicitly schematic.
