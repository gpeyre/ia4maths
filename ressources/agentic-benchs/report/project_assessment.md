# Comparative Assessment of `antigravity-olivier/`, `antigravity-antoine/`, `codex-gabriel/`, `claude-gabriel/`, `codex-clement/`, `codex-kimia/`, `openclaw-jeremie/`, `hermes-jeremie/`, and `emmanuel/`

## Scope

This report evaluates the nine agent-produced projects against the shared request
in `todo.md`. The requested work was not simply to make plots: it asked for a
pedagogical PyTorch notebook for the three-Dirac stochastic interpolant, a polished
LaTeX article with literature and integrated figures, a Gaussian-to-Gaussian
closed-form analysis including a theorem comparing the endpoint flow map with
Gaussian optimal transport, a second notebook exporting Gaussian covariance ellipse
figures, and a professional repository structure.

I assessed:

- `todo.md`
- `antigravity-olivier/README.md`
- `antigravity-olivier/python/*.py`
- `antigravity-olivier/python/*.ipynb`
- `antigravity-olivier/paper/main.tex`
- `antigravity-antoine/README.md`
- `antigravity-antoine/python/build_notebooks.py`
- `antigravity-antoine/python/*.ipynb`
- `antigravity-antoine/paper/main.tex`
- `antigravity-antoine/paper/main.pdf`
- `antigravity-antoine/paper/*.pdf`
- `codex-gabriel/README.md`
- `codex-gabriel/Makefile`
- `codex-gabriel/requirements.txt`
- `codex-gabriel/python/*.py`
- `codex-gabriel/python/*.ipynb`
- `codex-gabriel/paper/main.tex`
- `claude-gabriel/README.md`
- `claude-gabriel/python/requirements.txt`
- `claude-gabriel/python/*.ipynb`
- `claude-gabriel/paper/main.tex`
- `claude-gabriel/paper/main.pdf`
- `codex-clement/flow_matching_utils.py`
- `codex-clement/create_notebooks.py`
- `codex-clement/generate_figures.py`
- `codex-clement/*.ipynb`
- `codex-clement/main.pdf`
- `codex-kimia/README.md`
- `codex-kimia/Makefile`
- `codex-kimia/requirements.txt`
- `codex-kimia/scripts/export_figures.py`
- `codex-kimia/scripts/write_project.py`
- `codex-kimia/python/*.ipynb`
- `codex-kimia/paper/article.tex`
- `codex-kimia/paper/article.pdf`
- `codex-kimia/paper/figures/*.pdf`
- `openclaw-jeremie/README.md`
- `openclaw-jeremie/ORCHESTRATION.md`
- `openclaw-jeremie/pyproject.toml`
- `openclaw-jeremie/requirements.txt`
- `openclaw-jeremie/uv.lock`
- `openclaw-jeremie/python/flow_matching_diracs.py`
- `openclaw-jeremie/scripts/make_notebooks_and_figures.py`
- `openclaw-jeremie/tests/*.py`
- `openclaw-jeremie/notebooks/*.ipynb`
- `openclaw-jeremie/paper/main.tex`
- `openclaw-jeremie/paper/main.pdf`
- `openclaw-jeremie/paper/references.bib`
- `openclaw-jeremie/paper/figures/*.pdf`
- `hermes-jeremie/README.md`
- `hermes-jeremie/pyproject.toml`
- `hermes-jeremie/requirements.txt`
- `hermes-jeremie/uv.lock`
- `hermes-jeremie/.github/workflows/ci.yml`
- `hermes-jeremie/python/flow_matching_dirac/*.py`
- `hermes-jeremie/python/scripts/*.py`
- `hermes-jeremie/python/notebooks/*.ipynb`
- `hermes-jeremie/tests/test_core.py`
- `hermes-jeremie/paper/main.tex`
- `hermes-jeremie/paper/main.pdf`
- `hermes-jeremie/paper/references.bib`
- `hermes-jeremie/paper/figures/*.pdf`
- `emmanuel/README.md`
- `emmanuel/MISSION.md`
- `emmanuel/python/README.md`
- `emmanuel/python/requirements.txt`
- `emmanuel/python/fmg/*.py`
- `emmanuel/python/tests/test_fmg.py`
- `emmanuel/python/*.ipynb`
- `emmanuel/paper/paper.tex`
- `emmanuel/paper/theorem.md`
- `emmanuel/paper/references.bib`
- `emmanuel/paper/figures/*.pdf`
- `emmanuel/lean/README.md`
- `emmanuel/lean/FMG.lean`
- `emmanuel/lean/FMG/Basic.lean`
- `emmanuel/lean/FMG/Gaussian.lean`
- `emmanuel/lean/unproved.md`
- `emmanuel/docs/audits/*.md`
- `emmanuel/report/report.md`

I also ran and inspected the following checks:

- `python3 codex-gabriel/python/check_math.py`: passed all mathematical invariant
  checks.
- `python3 antigravity-olivier/python/generate_plots.py`: failed under the bare
  `python3` environment because `matplotlib` was unavailable.
- `python3 antigravity-olivier/python/generate_gaussian_plots.py`: failed for the same
  dependency reason.
- Notebook execution metadata for `antigravity-antoine/`: both notebooks are
  executed (`6/6` and `2/2` nonempty code cells executed), with figure outputs
  stored in the notebooks.
- `pdftotext` and `pdftoppm` on the available/generated PDFs from
  `antigravity-olivier/`, `antigravity-antoine/`, `codex-gabriel/`,
  `claude-gabriel/`, `codex-clement/`, `codex-kimia/`, `openclaw-jeremie/`, `hermes-jeremie/`, and
  `emmanuel/`: all nine are readable and render, but the
  visual polish, source availability, and mathematical completeness differ
  substantially.
- Notebook execution metadata for `claude-gabriel/`: both notebooks are fully executed
  (`16/16` and `15/15` code cells executed).
- `claude-gabriel/paper/main.log`: no unresolved-reference or citation warnings found.
- Notebook execution metadata for `codex-clement/`: both notebooks are unexecuted
  (`0/6` and `0/5` code cells executed).
- `python3` import probes for `codex-clement/`: importing
  `flow_matching_utils.py` fails in the bare environment because `torch` is not
  installed, and the project supplies no dependency file.
- `codex-clement/main.pdf`: 8 pages, rendered cleanly; no corresponding LaTeX
  source was provided.
- Notebook execution metadata for `codex-kimia/`: both notebooks have all
  nonempty code cells executed; each also contains one empty trailing code cell
  with no execution count.
- `python3 -c 'import torch, matplotlib, nbformat'` and
  `make -C codex-kimia figures`: failed in this host environment because Torch
  triggered a duplicate OpenMP runtime error (`libomp.dylib already
  initialized`).
- `env KMP_DUPLICATE_LIB_OK=TRUE python3 codex-kimia/scripts/export_figures.py`:
  completed and regenerated the PDF figures. This confirms the project code can
  run here with the unsafe OpenMP workaround, but the documented bare
  `make figures` command is not clean in this environment.
- `make -C codex-kimia paper`: succeeded and rebuilt `paper/article.pdf`.
- `pdftoppm` on `codex-kimia/paper/article.pdf`: representative pages render
  cleanly; the 6-page PDF is readable.
- Direct exact Gaussian endpoint check for `codex-kimia/`'s noncommuting
  matrices: \(\|\Sigma_0\Sigma_1-\Sigma_1\Sigma_0\|_F=0.6753\),
  \(\|T_1-T_{\rm OT}\|_F=0.1778\),
  \(\|T_1-T_1^\top\|_F=0.3479\), and
  \(\|T_1\Sigma_0T_1^\top-\Sigma_1\|_F=2.35\times10^{-15}\).
- Notebook execution metadata for `openclaw-jeremie/`: both notebooks are fully
  executed (`8/8` and `7/7` code cells executed), with substantial markdown
  derivations.
- `pdftoppm` on `openclaw-jeremie/paper/main.pdf`: all 5 pages render cleanly, with
  legible trajectory, OT-comparison, Gaussian ellipse, and theorem pages.
- `pdflatex`, `bibtex`, and further sequential `pdflatex` runs in
  `openclaw-jeremie/paper/`: rebuilt `main.pdf` with references resolved and no final
  warnings in `main.log`.
- `python3 -m pytest -q openclaw-jeremie`: could not run in the bare host environment
  because `pytest` is not installed.
- `UV_CACHE_DIR=/private/tmp/uv-cache uv run --locked pytest -q` in
  `openclaw-jeremie/`: created a local virtual environment but could not complete the
  dependency installation because package downloads from PyPI failed. I
  therefore treat the test suite as present and well designed, but not locally
  verified in this audit pass.
- Notebook execution metadata for `hermes-jeremie/`: both notebooks are unexecuted
  (`0/5` and `0/3` nonempty code cells executed). The notebooks are generated
  from committed scripts and the paper figures are pre-generated, but the
  submitted notebook artifacts do not contain outputs.
- `KMP_DUPLICATE_LIB_OK=TRUE MPLCONFIGDIR=/private/tmp/mpl-hermes-jeremie
  UV_CACHE_DIR=/private/tmp/uv-hermes-jeremie uv run pytest` in `hermes-jeremie/`: passed all
  5 tests after the locked environment was installed. I removed the generated
  `hermes-jeremie/.venv` afterward.
- `pdftoppm` on `hermes-jeremie/paper/main.pdf`: all 7 pages render cleanly and the
  theorem/figure pages are legible. The main visual weakness is float placement:
  several figures appear after the sections that introduce them, including
  final Gaussian figures after the references.
- `python3 emmanuel/python/tests/test_fmg.py`: passed all 8 tests.
- Notebook execution metadata for `emmanuel/`: both notebooks are fully executed
  (`6/6` and `7/7` code cells executed).
- `pdflatex`, `biber`, and two further `pdflatex` runs in `emmanuel/paper/`:
  produced `emmanuel/paper/paper.pdf`, 13 pages, with references resolved.
- `pdftoppm` on the generated `emmanuel/paper/paper.pdf`: representative pages
  render cleanly, with legible theorem pages and embedded figures.
- `rg` over `emmanuel/lean/FMG.lean`, `emmanuel/lean/FMG/Basic.lean`, and
  `emmanuel/lean/FMG/Gaussian.lean`: no `sorry` or project-local `axiom`
  in the imported Lean anchor files. A deliberate adversarial axiom file exists
  under `FMG/Adversarial/`, but it is not imported by the main Lean library.
- `lake build` in `emmanuel/lean/`: started successfully, fetched and began
  compiling Mathlib, but I interrupted it after it was rebuilding thousands of
  upstream modules from source. I therefore did not use a completed local Lean
  build as evidence for the full audit.
- `pdfinfo`, `pdftotext`, and `pdftoppm` on
  `antigravity-antoine/paper/main.pdf`: the 4-page PDF renders cleanly and the
  trajectory/ellipse figures are visible. The paper is short, has no
  bibliography despite the literature requirement, and uses red hyperlink
  boxes/default LaTeX styling.

The `antigravity-olivier/` plotting-script failure is mainly a reproducibility issue, not
in itself evidence that the pre-generated figures are wrong. It matters because
the request explicitly asked for a professional code base.

## Executive Summary

`emmanuel/` is now the most complete and ambitious submission. It has the best
overall repository structure, pinned dependencies, executed notebooks,
notebook-generated paper figures, a substantial 13-page paper that builds from
source, a Python test suite that passes, a semi-discrete OT implementation for
unequal Dirac weights, internal code/citation audits, and a Lean development
that formally anchors the commuting Gaussian case. Its Gaussian theorem is also
the strongest: the paper gives the endpoint map as the principal square root
\((\Sigma_1\Sigma_0^{-1})^{1/2}\), equivalent to the congruence formula used by
`codex-gabriel/`, and then uses symmetry to characterize exactly when it agrees with
Bures OT. The main caveats are that the main numerical library is NumPy/SciPy
rather than PyTorch-native, with PyTorch used mainly for an autodiff cross-check;
the full noncommuting theorem is not formalized in Lean; one wiki page is stale
about endpoint schedule-independence; and the submitted tree did not include a
prebuilt paper PDF until I generated one from the LaTeX source.

`codex-gabriel/` remains an excellent compact answer and is still the cleanest
minimal reproducible solution. It has a coherent reusable
PyTorch implementation, executed notebooks with mathematical text cells and
figure export, a reproducible `Makefile`, a requirements file, and a
mathematically sound Gaussian theorem with numerical checks. The project is not
perfect: one figure float interrupts the theorem/proof flow, and the VP schedule
choice should be named more explicitly as a square-root variance-preserving
schedule rather than a beta-schedule diffusion convention. These are polish
issues, not core failures.

`openclaw-jeremie/` is now the strongest submission below the top two. It is a polished
and unusually professional repository: README, orchestration log, `pyproject`,
`requirements.txt`, `uv.lock`, reusable PyTorch code, tests, executed notebooks,
source LaTeX, prebuilt PDF, and generated PDF/PNG figures are all present. Its
three-Dirac implementation is correct and pedagogical, and its OT comparison is
carefully described as an exact balanced finite-sample assignment rather than an
overclaimed continuous Laguerre solve. The main reason it does not challenge
`codex-gabriel/` and `emmanuel/` is the Gaussian theory: it correctly writes the
noncommuting flow as a time-ordered exponential and gives a true SPD criterion
for equality with the Brenier map, but it does not derive the requested explicit
closed-form congruence formula for \(T_t\), nor the structural commutation
criterion in terms of \(\Sigma_0,\Sigma_1\). I also could not run its tests here
because dependency downloads failed, although the tests themselves are present.

`hermes-jeremie/` is a strong upper-mid submission, closest in spirit to `openclaw-jeremie/`.
It has a professional wrapper, `pyproject.toml`, `uv.lock`, CI, reusable
PyTorch code, figure-generation scripts, source LaTeX, prebuilt PDF, generated
PDF/PNG figures, and a test suite that passes locally after installing the
locked environment. Its three-Dirac density and velocity formulas are correct,
and its Gaussian section is mathematically cautious: it proves the commuting
case and explicitly says the noncommuting flow is time ordered and generally
differs from OT. The main drawbacks are that the submitted notebooks are
unexecuted, the OT comparison is a greedy balanced "OT-like" visualization
rather than a certified semi-discrete solver, the Gaussian theorem lacks both
the explicit general closed-form \(T_t\) and the covariance-level iff
criterion, and the paper's float placement is less polished than the best
submissions.

`claude-gabriel/` is a strong mid-tier answer. It is much closer
to the requested shape than `antigravity-olivier/`: it has a professional repository
wrapper, a license, requirements, two executed notebooks, many notebook-exported
PDF figures, and a substantive 11-page paper. Its Dirac-mixture notebook is
genuinely PyTorch-based and pedagogical. Its main weakness is the Gaussian
theorem: the paper states a global "if and only if" result, but the proof only
establishes sufficiency plus an infinitesimal necessity result near commuting
covariances, and explicitly leaves the non-perturbative necessity as future
work. It also does not derive the general closed-form \(T_t\) requested in
`todo.md`; it numerically integrates the flow map with Euler steps. A second
pass also shows that its small schedule-to-schedule differences in \(T_1\) are
numerical integration artifacts: the exact independent-Gaussian endpoint map is
schedule-independent.

`codex-kimia/` is a compact and mostly honest submission that lands between
`claude-gabriel/` and `codex-clement/`. It has a README, requirements file, Makefile,
paper source, prebuilt paper PDF, figure PDFs, and PyTorch notebooks/scripts.
Its three-Dirac conditional velocity is correct and genuinely tensor-based, and
its paper is readable and source-rebuildable. It is stronger than
`codex-clement/` as a repository because it includes source and a build path.
Its limiting factor is the Gaussian theory: it proves only the commuting case,
does not derive the general noncommuting closed-form \(T_t\) or the exact
if-and-only-if equality criterion, and relies on numerical integration for the
noncommuting comparison. The documented `make figures` command also failed in
this host Python because of a Torch/OpenMP runtime conflict, although the figure
script ran with `KMP_DUPLICATE_LIB_OK=TRUE`.

`codex-clement/` is no longer merely a code sketch now that `main.pdf` is
present. The PDF is a real 8-page numerical note with an abstract, introduction,
general stochastic-interpolant setup, three-Dirac derivation, Gaussian section,
figures, conclusion, and references. Its PyTorch utility module is cleaner than
`antigravity-olivier/`'s NumPy scripts for the three-Dirac part, and its Gaussian
discussion is more cautious than 's: it correctly emphasizes
time-ordering in the noncommuting case instead of relying on a false symmetry
argument. However, it still has no README, no requirements file, no LaTeX
source, no executed notebooks, no stored figure PDFs, and no general
noncommuting closed-form \(T_t\). The PDF therefore raises the submission
substantially, but it remains incomplete relative to `todo.md`.

`antigravity-antoine/` is a small but nontrivial submission. It is stronger
than `antigravity-olivier/` on literal notebook compliance: it has two executed
notebooks, PyTorch code for the three-Dirac velocity, source LaTeX, a prebuilt
paper PDF, and notebook-exported PDF figures. However, it is much less
professional than the mid-tier projects: the README references a missing
`requirements.txt`, there is no package, no tests, no Makefile/CI, and the
paper is only a short 4-page note with no bibliography. Its three-Dirac
conditional velocity is correct, but the OT comparison uses nearest-Dirac
assignment in a non-equilateral, non-centered three-atom configuration, so it
is not a certified semi-discrete OT map. The Gaussian section gives the correct
linear velocity matrix but does not compute the requested closed-form \(T_t\);
it numerically integrates \(M_t\) and states the commuting iff result without
a full proof.

`antigravity-olivier/` is a plausible partial solution. It contains many of the requested
files, derives the correct conditional velocity for the independent three-Dirac
case, produces trajectory and Gaussian ellipse figures, and has a readable LaTeX
paper. However, it misses several important requirements: its notebooks/scripts
are NumPy/SciPy rather than PyTorch, the paper figures are generated mainly by
scripts rather than by the notebooks, the Gaussian flow-map theorem is
incomplete and its proof is not mathematically reliable in the noncommuting
case, the VP schedule used there violates the endpoint conditions, and the repo
lacks the usual reproducibility machinery.

Approximate scores:

| Project | Math correctness | Code realization | Paper/visual polish | Goal reached | Overall |
|---|---:|---:|---:|---:|---:|
| `antigravity-olivier/` | 5.5 / 10 | 5 / 10 | 5.5 / 10 | 5.5 / 10 | 5.4 / 10 |
| `antigravity-antoine/` | 5.8 / 10 | 6 / 10 | 5.5 / 10 | 5.8 / 10 | 5.8 / 10 |
| `codex-clement/` | 7 / 10 | 5.5 / 10 | 6.5 / 10 | 6 / 10 | 6.2 / 10 |
| `codex-kimia/` | 7 / 10 | 7 / 10 | 7 / 10 | 7 / 10 | 7.0 / 10 |
| `claude-gabriel/` | 6.5 / 10 | 7.5 / 10 | 7 / 10 | 7.2 / 10 | 7.1 / 10 |
| `hermes-jeremie/` | 7.8 / 10 | 8 / 10 | 7.5 / 10 | 7.6 / 10 | 7.7 / 10 |
| `openclaw-jeremie/` | 8.2 / 10 | 8.6 / 10 | 8 / 10 | 8.2 / 10 | 8.2 / 10 |
| `codex-gabriel/` | 9 / 10 | 9 / 10 | 8 / 10 | 9 / 10 | 8.8 / 10 |
| `emmanuel/` | 9.3 / 10 | 8.8 / 10 | 9 / 10 | 9.2 / 10 | 9.1 / 10 |

## Request Decomposition

The request can be decomposed into the following deliverables:

1. A pedagogical notebook in `python/` for \(X_0 \sim N(0,I)\) and \(X_1\) a
   mixture of three Diracs.
2. Use the closed-form density of \(X_t\) and compute the advection velocity
   \(u_t(x)=\mathbb E[\dot X_t \mid X_t=x]\) in PyTorch.
3. Show sample trajectories with the three Dirac targets in three colors, with
   each trajectory colored by the closest terminal Dirac.
4. Compare three schedules: linear, variance-preserving, and cosine.
5. Contrast the stochastic-interpolant trajectories with optimal-transport
   trajectories.
6. Make the notebook pedagogical, with mathematical derivations in text cells
   between plots.
7. Write a detailed LaTeX article in `paper/` with abstract, introduction and
   literature, general setup, three-Dirac experiments with figures, and Gaussian
   theory.
8. In the Gaussian case \(X_0 \sim N(0,\Sigma_0)\),
   \(X_1 \sim N(0,\Sigma_1)\), compute \(\Sigma_t\) and the flow map \(T_t\)
   as functions of \(a(t)\) and \(b(t)\).
9. Compare \(T_1\) with the Gaussian OT map, characterize equality, and present
   a polished theorem with proof.
10. Add a second notebook generating covariance ellipse figures as PDFs.
11. Structure the repository professionally with a detailed README and expected
   reproducibility support.

## Mathematical Correctness

### Three-Dirac Conditional Velocity

All nine projects identify the correct density for the independent coupling:

\[
p_t(x)=\sum_{k=1}^3 \pi_k\,\varphi_{a(t)^2 I}(x-b(t)y_k).
\]

All nine also use the correct posterior responsibilities:

\[
\gamma_k(x,t)=
\frac{\pi_k \exp(-\|x-b(t)y_k\|^2/(2a(t)^2))}
{\sum_j \pi_j \exp(-\|x-b(t)y_j\|^2/(2a(t)^2))}.
\]

For \(a(t)>0\), the conditional-expectation velocity is

\[
u_t(x)=\frac{\dot a(t)}{a(t)}x+
\left(\dot b(t)-\frac{\dot a(t)b(t)}{a(t)}\right)
\sum_k \gamma_k(x,t)y_k.
\]

`antigravity-olivier/` gives this formula in both the notebook and the paper, and its
NumPy implementation follows it up to small endpoint stabilizations. That part
is essentially correct.

`antigravity-antoine/` also derives the correct conditional-expectation formula
and implements it in PyTorch in the executed Dirac notebook. The implementation
uses softmax responsibilities over squared distances, computes the posterior
atom mean, and integrates trajectories with `scipy.integrate.solve_ivp` while
calling the PyTorch velocity inside the ODE callback. This satisfies the core
Dirac velocity requirement better than `antigravity-olivier/`, although it is
not a clean PyTorch-native simulation end-to-end because the ODE solver is
SciPy and the code lives only inside a notebook/script rather than a reusable
tested module.

`codex-gabriel/` gives the same formula, implements it in PyTorch in
`python/stochastic_interpolants.py`, and tests it indirectly through
continuity-equation residuals in `python/check_math.py`. The check produced
residuals around \(10^{-14}\), which is strong evidence that the velocity and
density are mutually consistent.

`claude-gabriel/` also gives the correct three-Dirac formula and implements it in
PyTorch in `flow_matching_diracs.ipynb`. The notebook computes posterior weights
with a softmax over log-likelihoods, evaluates the conditional velocity
\[
v_t(x)=\sum_k\pi_k(x,t)
\left[\frac{\dot a(t)}{a(t)}(x-b(t)\mu_k)+\dot b(t)\mu_k\right],
\]
uses a midpoint ODE integrator, and exports trajectory, density, velocity-field,
posterior, and OT-comparison figures. It is less modular than `codex-gabriel/` because
the implementation lives inside the notebook rather than in a reusable tested
module, but it satisfies the PyTorch notebook part of the Dirac request much
better than `antigravity-olivier/`.

`codex-clement/` also implements the correct formula in PyTorch in
`flow_matching_utils.py`: it computes posterior atom weights with a softmax,
forms the posterior atom mean, and returns
\[
\frac{\dot a(t)}{a(t)}x+
\left(\dot b(t)-\frac{b(t)\dot a(t)}{a(t)}\right)\bar y(t,x).
\]
The utility code is modular and uses RK4 for trajectory integration, which is a
strength. The weakness is not the formula but the submitted artifact: the
notebooks are unexecuted, the bare environment lacks `torch`, and no dependency
file is provided to make the PyTorch code reproducible.

`codex-kimia/` implements the same formula directly in PyTorch in both the
notebook-generated code and `scripts/export_figures.py`. It uses tensor
softmax responsibilities, clamps \(a(t)\) near the endpoint for numerical
stability, and integrates trajectories with a second-order predictor-corrector
scheme. The code is less modular and less tested than `codex-gabriel/`, but it
does satisfy the PyTorch velocity requirement for the three-Dirac part much
more literally than `antigravity-olivier/` or `emmanuel/`.

`openclaw-jeremie/` gives the same formula in `paper/main.tex` and implements it in
`python/flow_matching_diracs.py` with PyTorch tensors throughout. The code
computes posterior responsibilities by a softmax over squared distances, forms
the posterior atom mean, and returns
\[
\dot a(t)\frac{x-b(t)\bar y(t,x)}{a(t)}+\dot b(t)\bar y(t,x).
\]
The Dirac notebook is executed and pedagogical: it exposes the schedule table,
responsibilities, density values, the split between base and atom velocity
terms, a vector-field plot, validation diagnostics, and the generated figures.
The submitted tests include continuity residual, endpoint proportion, and
assignment-cost checks. I could not run those tests locally because the locked
environment could not finish downloading dependencies, but the code structure
and notebook outputs are stronger than the mid-tier submissions.

`hermes-jeremie/` also implements the formula correctly in PyTorch, in a reusable
package under `python/flow_matching_dirac/`. The density code uses log-sum-exp
for the mixture density, the responsibilities are computed by a stable softmax
over atom likelihoods, and the velocity module returns
\[
\frac{\dot a(t)}{a(t)}x+
\left(\dot b(t)-\frac{\dot a(t)}{a(t)}b(t)\right)\bar y(t,x).
\]
The implementation is cleanly separated into `density.py`, `velocity.py`,
`sampling.py`, `schedules.py`, and plotting utilities, and the local
`uv run pytest` check passed all 5 tests after installing the locked
environment. The limitation is artifact-level: the notebooks in
`python/notebooks/` are generated but not executed, so the submitted notebooks
do not themselves show the pedagogical outputs requested by `todo.md`.

`emmanuel/` gives the same conditional-expectation formula and packages it
cleanly in `python/fmg/mixture.py`. Its implementation uses log-space posterior
weights, supplies an independent PyTorch autodiff cross-check through
`velocity_autodiff`, and includes a test that the closed-form velocity agrees
with the autodiff score identity. The stronger mathematical point is that the
project supports unequal Dirac weights and then solves the semi-discrete OT
comparison with a Laguerre-cell method rather than relying only on the symmetric
nearest-centroid shortcut. The caveat is literal compliance with the PyTorch
wording in `todo.md`: the main notebook and production velocity code are
NumPy/SciPy-based, with PyTorch used for verification, so it is not as
PyTorch-native as `codex-gabriel/` or `claude-gabriel/`.

Verdict:

- `antigravity-olivier/`: correct formula, but no automated check.
- `antigravity-antoine/`: correct formula in an executed PyTorch notebook, but
  no reusable module or invariant tests.
- `claude-gabriel/`: correct formula, PyTorch notebook implementation, no separate
  invariant test suite.
- `codex-clement/`: correct modular PyTorch formula, but notebooks are unexecuted
  and no dependency setup is supplied.
- `codex-kimia/`: correct PyTorch implementation, with no independent invariant
  test suite.
- `openclaw-jeremie/`: correct modular PyTorch implementation, executed notebooks, and
  a good test suite present, though not locally run in this audit.
- `hermes-jeremie/`: correct modular PyTorch implementation and locally passing tests,
  but the generated notebooks are unexecuted.
- `codex-gabriel/`: correct formula, implemented and tested.
- `emmanuel/`: correct formula, tested and generalized to unequal weights, but
  NumPy/SciPy is the main numerical substrate rather than PyTorch.

### Schedules

`antigravity-olivier/` implements:

- linear: \(a=1-t\), \(b=t\)
- cosine: \(a=\cos(\pi t/2)\), \(b=\sin(\pi t/2)\)
- VP SDE-style schedule:
  \(a(t)=\exp(-\frac12\int_0^t \beta(s)\,ds)\),
  \(b(t)=\sqrt{1-a(t)^2+\epsilon}\)

The linear and cosine schedules satisfy the exact endpoint conditions. The VP
schedule is a common diffusion-style choice, but for finite \(\beta_{\max}\) it
does not give \(a(1)=0\) exactly. More concretely, the implementation adds
`eps` inside the square root:

\[
b(t)=\sqrt{1-a(t)^2+\varepsilon}.
\]

With the project's default \(\beta_{\min}=0.1\), \(\beta_{\max}=20\), and
\(\varepsilon=10^{-6}\), this gives

| Time | `antigravity-olivier/` VP \(a(t)\) | `antigravity-olivier/` VP \(b(t)\) |
|---:|---:|---:|
| \(t=0\) | \(1.0\) | \(0.001\) |
| \(t=1\) | \(0.0065715865\) | \(0.9999789069\) |

Thus the schedule violates both exact boundary conditions \(b(0)=0\) and
\(a(1)=0\). The numerical effect is visually small, but the request is about a
mathematical stochastic interpolant with precise endpoints, so this is a real
correctness issue.

`antigravity-antoine/` implements:

- linear: \(a=1-t\), \(b=t\)
- trigonometric variance preserving: \(a=\cos(\pi t/2)\), \(b=\sin(\pi t/2)\)
- square-root schedule: \(a=\sqrt{1-t}\), \(b=\sqrt t\), labeled
  "cosine/sub-VP"

All three satisfy the endpoint constraints. The square-root schedule has
singular derivatives at both endpoints; the code avoids exact endpoint
evaluation with small epsilons and integrates only to \(t=0.99\). This is
acceptable for plots, but the naming is confusing: the third schedule is not a
cosine schedule, while the second one is the usual cosine/trigonometric
variance-preserving interpolation.

`codex-gabriel/` implements:

- linear: \(a=1-t\), \(b=t\)
- variance preserving: \(a=\sqrt{1-t}\), \(b=\sqrt t\)
- cosine: \(a=\cos(\pi t/2)\), \(b=\sin(\pi t/2)\)

This VP choice satisfies \(a^2+b^2=1\) and the endpoint conditions exactly,
though its endpoint derivatives are singular. `codex-gabriel/` handles this numerically
by integrating on \([10^{-4},1-10^{-4}]\). This is a reasonable and explicit
choice. The project could still be clearer that this is not the same convention
as `antigravity-olivier/`'s beta-schedule VP, but it is internally consistent.

`claude-gabriel/` implements the same linear and cosine schedules as the others, and a
VP schedule
\[
a(t)=\sqrt{1-t^2},\qquad b(t)=t.
\]
This also satisfies \(a(t)^2+b(t)^2=1\) and the exact endpoint constraints.
The derivative \(\dot a(t)=-t/\sqrt{1-t^2}\) is singular at \(t=1\), and the
notebooks handle this numerically by avoiding exact endpoint evaluation in the
ODE integration and adding small stabilizers in derivative evaluations. This is
reasonable for plotting, but it should be stated more explicitly in the paper.

`codex-clement/` uses the same linear, cosine, and
\(a(t)=\sqrt{1-t^2}, b(t)=t\) VP schedules as `claude-gabriel/`. The endpoint
definitions are mathematically consistent, and the implementation clamps the
singular VP derivative. Its trajectory integrator stops at \(t=0.995\), and the
Gaussian endpoint comparison stops at \(t=0.999\), so the numerical figures
avoid the singular endpoint rather than showing exact terminal convergence.

`codex-kimia/` uses linear, VP
\((a,b)=(\cos(\pi t/2),\sin(\pi t/2))\), and cosine easing
\((a,b)=(\cos^2(\pi t/2),\sin^2(\pi t/2))\). These satisfy the endpoint
constraints exactly and avoid `antigravity-olivier/`'s beta-schedule endpoint problem.
The implementation still clamps \(a\) near zero in the Dirac velocity and
integrates only to \(1-10^{-4}\), so exact terminal convergence is handled
numerically rather than analytically.

`openclaw-jeremie/` implements linear, \(a(t)=\sqrt{1-t^2},b(t)=t\) variance-preserving,
and cosine schedules. These satisfy the endpoint constraints, and the test file
contains explicit endpoint assertions for all schedules. The numerical ODE
integrates to \(t=0.9995\) for the singular Dirac target, which is the right
practical choice and is described honestly as a pre-terminal classifier rather
than exact arrival at atoms.

`hermes-jeremie/` uses the same endpoint-consistent schedule family as `openclaw-jeremie/` and
`claude-gabriel/`: linear, \(a(t)=\sqrt{1-t^2},b(t)=t\) variance-preserving, and cosine.
The schedule tests assert the correct endpoint behavior near \(t=1\), and the
ODE integrations stop short of the singular endpoint. This is mathematically
sound. The only presentation drawback is that the schedule comparison figure is
paper/script-generated, while the submitted schedule notebook cells are not
executed.

`emmanuel/` implements linear, variance-preserving, cosine, and cubic schedules
with explicit boundary checks. Its documentation is more careful than most of
the other submissions about the fact that linear, cosine, and cubic can trace
the same covariance locus after reparametrization, while the VP schedule traces
a genuinely different locus. The tests exercise boundary conditions. One
remaining inconsistency is in `docs/wiki/schedules.md`: that page still says
the Gaussian endpoint map is schedule-independent only in the commuting case,
whereas the paper and tests correctly assert unconditional endpoint
schedule-independence for the Gaussian affine-plane problem.

Verdict:

- `antigravity-olivier/`: schedule comparison is present, but VP endpoint consistency is
  imperfect.
- `antigravity-antoine/`: endpoint-consistent schedules, but confusing
  "cosine/sqrt" naming and endpoint singularities handled numerically.
- `claude-gabriel/`: schedule comparison is present and endpoint-consistent; singular
  VP endpoint is handled numerically rather than analyzed deeply.
- `codex-clement/`: endpoint-consistent schedules, but numerical integrations
  stop short of \(t=1\) and the notebooks are unexecuted.
- `codex-kimia/`: endpoint-consistent schedules, with endpoint singularities
  handled by clamping/stopping short.
- `openclaw-jeremie/`: endpoint-consistent schedules, good endpoint tests, and honest
  pre-terminal handling of singular Dirac targets.
- `hermes-jeremie/`: endpoint-consistent schedules and passing endpoint tests, but
  unexecuted notebooks weaken the delivered pedagogical artifact.
- `codex-gabriel/`: schedule comparison is mathematically cleaner and better documented.
- `emmanuel/`: best tested schedule handling, with one stale wiki-page statement
  about Gaussian endpoint schedule-independence.

### Optimal-Transport Comparison in the Three-Dirac Case

For a centered, isotropic Gaussian source and three equal-weight Dirac masses
placed as an equilateral triangle centered at the origin, the semi-discrete OT
Laguerre cells reduce by symmetry to nearest-target cones. Therefore mapping
each \(X_0\) to the nearest Dirac point is correct up to zero-measure cell
boundaries.

`antigravity-olivier/` uses this nearest-centroid rule and plots linear OT trajectories.
The main mathematical limitation is that the paper writes the OT velocity using
\(T_{\rm OT}(X_0)\) without fully expressing the Eulerian velocity as a function
of \(x\) and \(t\). The code does reconstruct the cell label from \(x\) for the
linear case, so the plotted linear OT trajectories are credible.

`antigravity-antoine/` also uses nearest-atom assignment and straight-line
paths as its OT comparison, but here the geometry is less defensible. Its atoms
\((2,2),(-2,2),(0,-2)\) are not an equilateral centered configuration, and the
target mean is not zero. Therefore nearest Euclidean Voronoi cells do not
automatically have equal Gaussian mass and should not be presented as the exact
semi-discrete OT map. The notebook comments even say this "approximates" OT,
but then also states that for \(N(0,I)\) and equal weights it is exactly closest
Dirac assignment. That exactness claim is not justified for this atom layout.
The figure is useful as a straight-line visual contrast, not as a certified OT
comparison.

`codex-gabriel/` explains why the nearest-target cells are correct, implements the OT
rays directly, and also plots path-length comparisons. This is more precise and
more pedagogical.

`claude-gabriel/` uses an angular-sector assignment for the symmetric equal-weight
three-Dirac OT map. This is equivalent to the nearest-target cones in this
geometry, and it is documented in the notebook code. The paper says "closest
Dirac (in a measure-preserving way)", which is acceptable for this symmetric
case but would be too informal in a general semi-discrete OT setting.

`codex-clement/` uses the nearest-atom rule through `ot_dirac_paths`, which is
also correct for this symmetric equal-mass setup. Its notebook text explains
the symmetry argument. The limitation is again artifact-level rather than
formula-level: the OT comparison is integrated into `main.pdf`, but the
corresponding submitted notebook is unexecuted.

`codex-kimia/` goes slightly beyond the nearest-centroid shortcut by optimizing
semi-discrete dual potentials with a stochastic softmax approximation. In the
submitted example the three target weights are equal, so the problem is still
the symmetric easy case, but the implementation is at least structurally closer
to a Laguerre-cell OT solver than the pure nearest-atom sketches. There is no
separate mass-balance test, so I treat it as a good visualization rather than a
verified semi-discrete solver.

`openclaw-jeremie/` is careful in a different direction. It does not claim to solve the
continuous semi-discrete Laguerre dual. Instead, it solves the exact balanced
finite assignment problem on the displayed Gaussian sample by dynamic
programming, with prescribed equal empirical capacities. This is not as
mathematically general as Emmanuel's Laguerre-cell solver, but it is a clean and
honest comparison: the source sample is partitioned into equal-size batches that
minimize squared cost, then straight paths are plotted to the atoms. The tests
include a brute-force check on a small balanced instance.

`hermes-jeremie/` is honest but weaker on this component. The paper correctly defines
the semi-discrete Laguerre-cell OT problem, but the code uses
`balanced_radial_assignment`, a deterministic greedy finite-sample heuristic
that matches empirical atom counts by assigning samples according to a cost
margin. The README and paper explicitly label the resulting paths as "OT-like"
or a visual contrast rather than a certified semi-discrete solver. This makes
the presentation scientifically safe, but it is less complete than Emmanuel's
Laguerre-cell solver and less exact than `openclaw-jeremie/`'s finite balanced assignment
on the displayed sample.

`emmanuel/` is strongest here. The submitted three-Dirac experiment uses
unequal target weights \((0.45,0.30,0.25)\), so nearest-centroid cells would no
longer be mathematically justified. The project instead implements a
semi-discrete OT solver in `fmg/ot_semidiscrete.py`, using POT's exact LP dual
when available and a damped Newton fallback, then assigns Laguerre cells. Its
test suite checks the fit residual, and the paper includes the resulting
cell/trajectory contrast. This is a genuine improvement over the symmetric-only
OT comparisons in the other projects.

Verdict:

- `antigravity-olivier/`: mostly correct, but somewhat informal.
- `antigravity-antoine/`: visual straight-line contrast present, but the
  nearest-atom exact-OT claim is not justified for its chosen atom geometry.
- `claude-gabriel/`: correct for the symmetric case and well visualized, still informal
  as a general OT statement.
- `codex-clement/`: correct for the symmetric case and integrated into the PDF,
  but the notebook version is unexecuted.
- `codex-kimia/`: good PyTorch OT baseline for the symmetric case, with
  approximate dual optimization but no mass-balance test.
- `openclaw-jeremie/`: strong finite-sample OT analogue, exactly optimized for the
  displayed balanced sample, but not a continuous Laguerre dual solve.
- `hermes-jeremie/`: honest OT-like greedy balanced visualization, useful but not a
  certified semi-discrete or exact finite assignment solve.
- `codex-gabriel/`: correct and well explained.
- `emmanuel/`: best OT comparison; it handles unequal weights with actual
  Laguerre cells.

### Gaussian Theory

For independent centered Gaussian endpoints, the covariance path is

\[
\Sigma_t = a(t)^2\Sigma_0 + b(t)^2\Sigma_1.
\]

The conditional velocity is linear:

\[
u_t(x)=B_t x,\qquad
B_t=(a\dot a\,\Sigma_0+b\dot b\,\Sigma_1)\Sigma_t^{-1}.
\]

The exact flow map solving \(\dot T_t=B_tT_t\), \(T_0=I\), is

\[
T_t=\Sigma_0^{1/2}
\left(a(t)^2I+b(t)^2\Sigma_0^{-1/2}\Sigma_1\Sigma_0^{-1/2}\right)^{1/2}
\Sigma_0^{-1/2}.
\]

At \(t=1\), this becomes

\[
T_1=\Sigma_0^{1/2}
\left(\Sigma_0^{-1/2}\Sigma_1\Sigma_0^{-1/2}\right)^{1/2}
\Sigma_0^{-1/2}.
\]

The Gaussian OT map is

\[
T_{\rm OT}=
\Sigma_0^{-1/2}
\left(\Sigma_0^{1/2}\Sigma_1\Sigma_0^{1/2}\right)^{1/2}
\Sigma_0^{-1/2}.
\]

The two endpoint maps agree if and only if
\(\Sigma_0\Sigma_1=\Sigma_1\Sigma_0\).

`codex-gabriel/` states and proves this theorem essentially correctly. Its proof uses
the congruence
\(\Sigma_t=\Sigma_0^{1/2}M_t\Sigma_0^{1/2}\), with
\(M_t=a^2I+b^2A\), where
\(A=\Sigma_0^{-1/2}\Sigma_1\Sigma_0^{-1/2}\). Since \(M_t\) and
\(\dot M_t\) commute, differentiating \(M_t^{1/2}\) is valid. This gives the
linear generator \(B_t\). The symmetry/equality argument for \(T_1=T_{\rm OT}\)
is also correct.

`emmanuel/` reaches the same correct endpoint theorem, but presents it in the
left-multiplicative principal-square-root form
\[
T_1=(\Sigma_1\Sigma_0^{-1})^{1/2}.
\]
This is equivalent to the congruence formula above: its square is
\(\Sigma_1\Sigma_0^{-1}\), it has positive spectrum, and it also equals
\[
\Sigma_0^{1/2}
\left(\Sigma_0^{-1/2}\Sigma_1\Sigma_0^{-1/2}\right)^{1/2}
\Sigma_0^{-1/2}.
\]
The paper then gives a clean endpoint proof of the equality criterion: if
\(T_1\) is symmetric, then \(T_1^2=\Sigma_1\Sigma_0^{-1}\) is symmetric, so
\(\Sigma_1\Sigma_0^{-1}=\Sigma_0^{-1}\Sigma_1\), equivalently
\([\Sigma_0,\Sigma_1]=0\). This avoids the two traps that damaged the weaker
submissions: treating a time-ordered exponential as an ordinary exponential
without commutation, and inferring endpoint symmetry from instantaneous
properties of the generator.

Emmanuel also proves unconditional endpoint schedule-independence through a
flatness/cancellation argument on the affine plane \(u\Sigma_0+v\Sigma_1\), and
its tests numerically check that noncommuting endpoints have zero schedule
spread but nonzero symmetry and OT residuals. The limitation is scope of
formalization: `lean/FMG/Gaussian.lean` formalizes the commuting case
\(T=\Sigma_1^{1/2}\Sigma_0^{-1/2}=T_{\rm OT}\), with no `sorry` or local axiom
in the imported files, but `lean/unproved.md` explicitly leaves the
matrix-ODE identification, flatness theorem, and noncommuting converse outside
Lean. The paper proof is convincing for this audit, but it is not fully
machine-checked.

`antigravity-olivier/` gets the covariance and velocity matrix formula right. However,
it does not give the general closed-form \(T_t\) above. Instead, it gives the
matrix ODE and only writes a closed form in the commuting case. The theorem's
conclusion, "equality iff the covariances commute", is correct, but the proof
is not clean: it claims that symmetry of the time-dependent flow follows from
symmetry of the instantaneous generator \(A_t\), which is not generally valid
for noncommuting time-varying matrices. It also does not rigorously derive the
noncommuting endpoint map that must be compared to OT.

More precisely, `antigravity-olivier/` defines

\[
A_t=\frac12\dot\Sigma_t\Sigma_t^{-1},
\qquad
\dot T_t=A_tT_t,\qquad T_0=I.
\]

It then argues, in effect, that \(T_t\) is symmetric if and only if \(A_t\) is
symmetric. This is the unreliable step. For a matrix ODE, symmetry of the
instantaneous generator does not by itself imply symmetry of the flow unless
there is an additional commutation property. Indeed,

\[
\frac{d}{dt}T_t^\top=(A_tT_t)^\top=T_t^\top A_t^\top.
\]

If \(A_t=A_t^\top\), this gives \(\dot T_t^\top=T_t^\top A_t\), not
\(\dot T_t^\top=A_tT_t^\top\). Thus \(T_t^\top\) does not generally solve the
same left-multiplication ODE as \(T_t\). It would solve the same ODE only if
\(T_t^\top A_t=A_tT_t^\top\), i.e. if the evolving flow and generator commute.
That commutation is exactly the kind of property that fails in the
noncommuting covariance case.

A concrete way to see the issue is to take two symmetric matrices \(S_1,S_2\)
that do not commute and define a piecewise-constant generator:

\[
A_t=S_1\quad\text{for the first half of time},\qquad
A_t=S_2\quad\text{for the second half}.
\]

The flow is then

\[
T=e^{\Delta S_2}e^{\Delta S_1}.
\]

Both factors are symmetric positive definite, but their product is generally
not symmetric unless the factors commute. This is the same algebraic obstruction
that appears in the Gaussian stochastic-interpolant ODE. In noncommuting
matrix problems, the solution is a time-ordered exponential, not the ordinary
exponential of an integral, and products of symmetric noncommuting factors need
not be symmetric.

There is a second related gap: even if one shows that \(A_t\) is nonsymmetric at
some intermediate times, that alone does not prove that the endpoint \(T_1\) is
nonsymmetric. Endpoint symmetry is a global property of the integrated flow,
and nonsymmetric infinitesimal generators can in principle have cancellations.
To prove \(T_1\neq T_{\rm OT}\), one needs an endpoint formula or another
endpoint invariant.

The reliable proof is the one used by `codex-gabriel/`: compute the actual flow map

\[
T_t=\Sigma_0^{1/2}
\left(a(t)^2I+b(t)^2\Sigma_0^{-1/2}\Sigma_1\Sigma_0^{-1/2}\right)^{1/2}
\Sigma_0^{-1/2}.
\]

Then at \(t=1\), \(T_1\) can be compared directly with the Brenier map
\[
T_{\rm OT}=
\Sigma_0^{-1/2}
\left(\Sigma_0^{1/2}\Sigma_1\Sigma_0^{1/2}\right)^{1/2}
\Sigma_0^{-1/2}.
\]
The endpoint map \(T_1\) pushes \(\Sigma_0\) to \(\Sigma_1\), but it is
symmetric exactly when \(\Sigma_0\) and \(\Sigma_1\) commute. This direct
endpoint comparison is what `antigravity-olivier/`'s proof is missing.

`antigravity-antoine/` gives the correct Gaussian covariance and velocity
matrix in an equivalent conditional-expectation form:
\[
A_t=\frac{\dot a}{a}I+
\left(\dot b-\frac{\dot a b}{a}\right)b\Sigma_1
(a^2\Sigma_0+b^2\Sigma_1)^{-1},
\]
which simplifies to
\[
(a\dot a\,\Sigma_0+b\dot b\,\Sigma_1)\Sigma_t^{-1}.
\]
However, despite the paper title "Exact Map" and the README claim that it
derives closed-form expressions for the Gaussian case, it does not compute the
requested closed-form \(T_t\). It only states the ODE
\(\dot M_t=A_tM_t\), numerically integrates it in the notebook, and says that
for the linear schedule the endpoint agrees with OT iff the covariances
commute. No proof of the iff statement is supplied, and no exact endpoint
formula is used for the noncommuting example. This is mathematically safer than
a false noncommuting proof, but it falls well short of the assignment's
Gaussian theorem requirement.

`codex-clement/` derives the same covariance path and velocity matrix as the
other projects:
\[
K_t=(a\dot a\,\Sigma_0+b\dot b\,\Sigma_1)\Sigma_t^{-1}.
\]
It also correctly notes that the noncommuting flow is a time-ordered matrix
exponential and gives the commuting-case simplification
\[
T_t=\Sigma_t^{1/2}\Sigma_0^{-1/2}.
\]
This is more cautious than `antigravity-olivier/`'s proof, because it does not assert that
instantaneous symmetry automatically implies endpoint symmetry. But it still
misses the requested general noncommuting closed form for \(T_t\), and it uses
RK4 integration up to \(t=0.999\) for the endpoint comparison. Thus it avoids a
major false proof, but it does not solve the central Gaussian task.

`codex-kimia/` is very close to `codex-clement/` mathematically, but with
better source availability. It derives
\[
\Sigma_t=a(t)^2\Sigma_0+b(t)^2\Sigma_1,\qquad
A_t=(a\dot a\,\Sigma_0+b\dot b\,\Sigma_1)\Sigma_t^{-1},
\]
and correctly writes the noncommuting flow as a time-ordered exponential. Its
theorem is explicitly limited to commuting covariances, where simultaneous
diagonalization gives
\[
T_t=Q\,\mathrm{diag}\!\left(
\sqrt{\frac{a(t)^2\lambda_{0,i}+b(t)^2\lambda_{1,i}}{\lambda_{0,i}}}
\right)Q^\top
\]
and \(T_1=\Sigma_1^{1/2}\Sigma_0^{-1/2}=T_{\rm OT}\). This proof is correct,
and it avoids the false `antigravity-olivier/`-style symmetry shortcut.

The missing piece is the same central one: `codex-kimia/` does not derive the
general noncommuting closed form for \(T_t\), does not prove the exact
if-and-only-if equality criterion, and does not note that the Gaussian endpoint
map is schedule-independent in the noncommuting case. For its own noncommuting
example, the exact endpoint formula gives
\[
\|T_1-T_{\rm OT}\|_F=0.1778,\qquad
\|T_1-T_1^\top\|_F=0.3479,\qquad
\|T_1\Sigma_0T_1^\top-\Sigma_1\|_F=2.35\times10^{-15}.
\]
Those numbers support the paper's qualitative claim that the noncommuting flow
differs from OT, but they also show that an exact endpoint analysis was
available and would have made the Gaussian section much stronger.

`openclaw-jeremie/` is stronger than `codex-kimia/` and `codex-clement/` in how it
frames the noncommuting issue, but it is still not as complete as
`codex-gabriel/` or `emmanuel/`. It correctly derives
\[
\Sigma_t=a(t)^2\Sigma_0+b(t)^2\Sigma_1,\qquad
M_t=(a\dot a\,\Sigma_0+b\dot b\,\Sigma_1)\Sigma_t^{-1},
\]
and writes the linear flow as the time-ordered exponential
\[
T_t=\mathcal T\exp\!\left(\int_0^t M_s\,ds\right).
\]
This is mathematically safe: it does not pretend that the noncommuting flow can
be simplified by ordinary exponentiation, and it proves the covariance
pushforward identity \(T_t\Sigma_0T_t^\top=\Sigma_t\).

The paper's theorem also gives a true equality criterion:
\[
T_1=T_{\rm OT}\quad\Longleftrightarrow\quad T_1
\text{ is symmetric positive definite}.
\]
This follows from uniqueness of the Brenier map among SPD linear pushforwards.
However, as a response to `todo.md`, it is weaker than the top submissions in
two ways. First, the theorem does not derive the requested explicit general
closed form
\[
T_t=\Sigma_0^{1/2}
\left(a(t)^2I+b(t)^2\Sigma_0^{-1/2}\Sigma_1\Sigma_0^{-1/2}\right)^{1/2}
\Sigma_0^{-1/2}.
\]
Second, the "iff" criterion is expressed in terms of the unknown endpoint flow
being SPD rather than in structural covariance terms, so it stops short of the
more useful commuting/noncommuting characterization. The notebook demonstrates
a noncommuting example numerically, and a commuting diagonal example agrees
with OT, but the exact noncommuting endpoint formula and structural proof are
not present.

`hermes-jeremie/` follows a similar cautious route, but with a slightly weaker theorem.
It derives the correct covariance path
\[
\Sigma_t=a(t)^2\Sigma_0+b(t)^2\Sigma_1
\]
and the correct linear Eulerian velocity
\[
M_t=(a\dot a\,\Sigma_0+b\dot b\,\Sigma_1)\Sigma_t^{-1}.
\]
Its theorem is explicitly restricted to commuting covariances, where
simultaneous diagonalization gives
\[
T_t=\Sigma_t^{1/2}\Sigma_0^{-1/2}
\]
in the common eigenbasis and \(T_1=T_{\rm OT}\). For noncommuting
covariances, the paper says the flow is a time-ordered exponential and
generally does not match the Gaussian OT map, and the code visualizes this by
numerically integrating the matrix ODE.

This is mathematically safe: `hermes-jeremie/` does not make
`antigravity-olivier/`'s invalid jump
from instantaneous symmetry to endpoint symmetry, and it does not overclaim a
global iff theorem like `claude-gabriel/`. But it still misses the central requested
closed form
\[
T_t=\Sigma_0^{1/2}
\left(a(t)^2I+b(t)^2\Sigma_0^{-1/2}\Sigma_1\Sigma_0^{-1/2}\right)^{1/2}
\Sigma_0^{-1/2},
\]
and it does not prove the structural equality criterion
\(\Sigma_0\Sigma_1=\Sigma_1\Sigma_0\). Its Gaussian section is therefore
reliable but incomplete.

`claude-gabriel/` sits between `antigravity-olivier/` and `codex-gabriel/`. It correctly derives the
Gaussian covariance path and the linear velocity matrix
\[
A_t=(\dot a(t)a(t)\Sigma_0+\dot b(t)b(t)\Sigma_1)\Sigma_t^{-1}.
\]
It also correctly proves the covariance transport identity
\[
M_t\Sigma_0M_t^\top=\Sigma_t
\]
for the numerically integrated flow map \(M_t\). However, it explicitly says in
the Gaussian notebook that \(M_t\) has "no simple closed form" in the
noncommuting case and integrates the matrix ODE numerically with first-order
Euler:

```text
M = M + dt * (A_t @ M)
```

This falls short of the `todo.md` request to compute \(T_t\) in closed form as a
function of \(a(t)\) and \(b(t)\). The exact congruence formula used by `codex`
is missing.

`claude-gabriel/`'s paper also has a theorem/proof mismatch. The theorem states the global
claim
\[
T_1=T_{\rm OT}\quad\Longleftrightarrow\quad
\Sigma_0\Sigma_1=\Sigma_1\Sigma_0,
\]
but the proof of the \((\Rightarrow)\) direction is only infinitesimal: it sets
\(\Sigma_1(\varepsilon)=\Sigma_0+\varepsilon\Delta\) and proves the condition
to first order in \(\varepsilon\). The paper then says no counterexample was
found numerically and that a non-perturbative proof is left as an open question.
That is honest in the body of the proof, but it contradicts the theorem
statement, abstract, and conclusion, which present the result as fully proved.

There is also a local algebraic typo/sign error in the commuting proof:
`claude-gabriel/`'s displayed diagonal generator uses
\[
\frac{-2a(t)\dot a(t)\lambda_i^0+2b(t)\dot b(t)\lambda_i^1}
{a(t)^2\lambda_i^0+b(t)^2\lambda_i^1},
\]
whereas the velocity matrix formula implies
\[
\frac{a(t)\dot a(t)\lambda_i^0+b(t)\dot b(t)\lambda_i^1}
{a(t)^2\lambda_i^0+b(t)^2\lambda_i^1}
=\frac12\frac{\mathrm d}{\mathrm dt}
\log(a(t)^2\lambda_i^0+b(t)^2\lambda_i^1).
\]
The final commuting endpoint formula is the right one, but the displayed
intermediate generator is not.

For `claude-gabriel/`'s own noncommuting Gaussian example
\[
\Sigma_0=\begin{pmatrix}2&0\\0&0.5\end{pmatrix},
\qquad
\Sigma_1=\begin{pmatrix}0.9&0.6\\0.6&0.9\end{pmatrix},
\]
the exact closed-form independent-interpolant endpoint map from the `codex`
formula gives:

| Quantity | Value |
|---|---:|
| \(\|\Sigma_0\Sigma_1-\Sigma_1\Sigma_0\|_F\) | \(1.2727922061\) |
| \(\|T_1-T_{\rm OT}\|_F\) | \(0.3789071466\) |
| \(\|T_1-T_1^\top\|_F\) | \(0.6716005759\) |
| \(\|T_1\Sigma_0T_1^\top-\Sigma_1\|_F\) | \(3.51\times10^{-16}\) |

These numbers agree with the notebook's qualitative conclusion that the
noncommuting endpoint map differs from OT, but they also show that the exact
closed-form endpoint map was available and would have made the proof stronger.

A further consequence of the exact formula is that \(T_1\) is independent of
the schedule for independent Gaussian endpoints. The schedule changes the
intermediate path \(T_t\), but at \(t=1\)
\[
T_1=\Sigma_0^{1/2}
\left(\Sigma_0^{-1/2}\Sigma_1\Sigma_0^{-1/2}\right)^{1/2}
\Sigma_0^{-1/2}
\]
contains no \(a,b\). `claude-gabriel/`'s Gaussian notebook prints slightly different
endpoint maps for the linear, VP, and cosine schedules; these differences are
numerical artifacts from first-order Euler integration, not real mathematical
scheme-dependence. For the printed 2000-step endpoint maps in the notebook,
the errors relative to the exact \(T_1\) are:

| `claude-gabriel/` numerical scheme | \(\|M_1^{\rm Euler}-T_1^{\rm exact}\|_F\) |
|---|---:|
| Linear | \(1.06\times10^{-3}\) |
| VP | \(4.47\times10^{-4}\) |
| Cosine | \(1.04\times10^{-4}\) |

This also makes `claude-gabriel/`'s remark that "scheme-dependence in \(M_1\) is a
genuinely second-order phenomenon" misleading for the exact Gaussian flow: the
endpoint map has no schedule-dependence at any order. Only the intermediate
trajectory and the numerical integration error depend on the schedule.

The same issue affects `claude-gabriel/`'s validation of the infinitesimal law. The paper
says the universal first-order coefficient is confirmed "to machine precision"
for all three schemes. The executed Gaussian notebook instead prints

| Infinitesimal-law check | Reported max error |
|---|---:|
| Linear | \(3.21\times10^{-4}\) |
| VP | \(3.78\times10^{-8}\) |
| Cosine | \(6.09\times10^{-9}\) |

The linear discrepancy is consistent with first-order Euler discretization error
at step size \(1/4000=2.5\times10^{-4}\), not with machine-precision
confirmation. This does not refute the infinitesimal expansion itself, but it
weakens the numerical evidence presented by `claude-gabriel/`'s paper and notebook.

For 's own numerical Gaussian matrices,

\[
\Sigma_0=
\begin{pmatrix}2&0.5\\0.5&1\end{pmatrix},\qquad
\Sigma_1=
\begin{pmatrix}1&-0.8\\-0.8&2\end{pmatrix},
\]

a direct check using the correct closed-form independent-interpolant endpoint
map gives:

| Quantity | Value |
|---|---:|
| \(\|\Sigma_0\Sigma_1-\Sigma_1\Sigma_0\|_F\) | \(0.4242640687\) |
| \(\|T_1-T_{\rm OT}\|_F\) | \(0.0543035180\) |
| \(\|T_1-T_1^\top\|_F\) | \(0.1075913907\) |
| \(\|T_1\Sigma_0T_1^\top-\Sigma_1\|_F\) | \(1.15\times10^{-15}\) |

This confirms the subtle point the article should have emphasized: the
independent-interpolant endpoint map does push the source covariance to the
target covariance, but it is a different, nonsymmetric linear map from the
Brenier OT map when the covariances do not commute.

Verdict:

- `antigravity-olivier/`: right direction and correct headline theorem, but incomplete
  and partially flawed proof.
- `antigravity-antoine/`: correct Gaussian velocity matrix, but no closed-form
  \(T_t\), no proof of the iff theorem, and only a numerical linear-schedule
  covariance plot.
- `claude-gabriel/`: correct Dirac experiment and useful Gaussian numerics, but missing
  the closed-form noncommuting flow map; its global theorem is true but not
  proved by the submitted argument, and its Euler artifacts are overinterpreted.
- `codex-clement/`: correct covariance/velocity setup and cautious
  noncommuting discussion, with a commuting-case theorem but no general
  noncommuting closed-form \(T_t\).
- `codex-kimia/`: correct and honest commuting-case theorem; no general
  noncommuting closed-form \(T_t\) or iff proof.
- `openclaw-jeremie/`: correct time-ordered formulation and true SPD equality
  criterion, but still missing the explicit general closed-form \(T_t\) and
  structural commuting characterization.
- `hermes-jeremie/`: correct commuting theorem and safe time-ordered noncommuting
  discussion, but no explicit general closed-form \(T_t\) or structural iff
  proof.
- `codex-gabriel/`: correct and complete enough for the requested article.
- `emmanuel/`: strongest Gaussian write-up; correct principal-square-root
  endpoint theorem and schedule-independence, with only the commuting case
  formally anchored in Lean.

## Code Realization

### `antigravity-olivier/`

Strengths:

- Provides both requested project areas: `python/` and `paper/`.
- Contains executed notebooks for the three-Dirac and Gaussian cases.
- Produces pre-generated PNG/PDF plots.
- The three-Dirac trajectory script is clear and easy to read.
- The paper compiles to an existing `paper/main.pdf`.

Weaknesses:

- The requested numerical notebook was supposed to be in PyTorch. `antigravity-olivier/`'s
  notebooks and scripts use NumPy/SciPy, not PyTorch.
- The Dirac notebook does not export the paper figures; the separate
  `generate_plots.py` script does. This weakens the requested notebook-to-paper
  workflow.
- The Gaussian notebook is very thin compared with the requested depth. It only
  displays a linear schedule comparison in the notebook, while the standalone
  script generates all three schedule figures.
- There is no `requirements.txt`, `environment.yml`, `pyproject.toml`, or
  top-level reproducibility command.
- The only Makefile is in `paper/` and compiles the paper, but does not rebuild
  notebooks or regenerate figures.
- There are no tests or mathematical invariant checks.
- Relative paths are fragile. For example, notebook generation writes to
  `python/...` relative to the current working directory.
- The repository contains `.DS_Store` files, which is unprofessional noise.
- The paper hardcodes a fake-looking author/affiliation. That is not a
  mathematical bug, but it does reduce polish.

Overall, `antigravity-olivier/` looks like a manually assembled demonstration rather
than a professional reproducible research repository.

### `antigravity-antoine/`

Strengths:

- Provides the requested high-level areas: README, `python/` notebooks/scripts,
  `paper/main.tex`, `paper/main.pdf`, and generated figure PDFs.
- Both submitted notebooks are executed. The Dirac notebook has all substantive
  code cells run, and the Gaussian notebook contains executed numerical output.
- The three-Dirac velocity is implemented with PyTorch tensors, softmax
  posterior responsibilities, and an explicit conditional atom mean.
- The schedules are endpoint-consistent in the usual interpolation sense:
  linear, trigonometric variance-preserving, and square-root interpolation.
- The Gaussian covariance and velocity matrix are implemented in a mathematically
  correct equivalent form.
- The paper PDF is present, source-backed, and renders cleanly.

Weaknesses:

- The README asks the user to run `pip install -r requirements.txt`, but no
  `requirements.txt` is included.
- There is no package, no reusable module, no tests, no Makefile, no CI, and no
  top-level rebuild command.
- The ODE trajectories use `scipy.integrate.solve_ivp` while calling a PyTorch
  velocity inside the callback, so the implementation is only partially
  PyTorch-native.
- The OT comparison is overinterpreted. The selected target atoms are not the
  centered equilateral configuration used in several other submissions, and the
  nearest-atom assignment is not justified as the exact semi-discrete OT map for
  equal Gaussian source masses.
- The Gaussian notebook numerically integrates the flow matrix and stops short
  of the endpoint; it does not implement or verify the requested closed-form
  \(T_t\).
- The paper is very short and has no bibliography despite the requested
  introduction and literature context.

Overall, `antigravity-antoine/` is stronger than `antigravity-olivier/` on literal
PyTorch compliance and source-backed paper delivery, but it remains a thin
notebook demonstration rather than a professional reproducible research project.

### `claude-gabriel/`

Strengths:

- Provides a cleaner repository wrapper than `antigravity-olivier/`: `README.md`,
  `LICENSE`, `.gitignore`, `python/requirements.txt`, two notebooks, a paper,
  and a dedicated `paper/figures/` directory.
- Both notebooks are fully executed.
- The Dirac notebook is genuinely PyTorch-based and pedagogical. It implements
  schedules, posterior weights, velocity evaluation, midpoint ODE integration,
  density plots, velocity fields, posterior evolution, and OT comparisons.
- The notebooks export all paper figures into `paper/figures/`, matching the
  requested notebook-to-paper workflow.
- The paper is longer and more complete than the `antigravity-olivier/` paper, with a
  table of contents, related work, theorem environments, inline bibliography,
  and many integrated figures.
- The LaTeX log does not show unresolved references or citation warnings.

Weaknesses:

- There is no top-level `Makefile` or single `make all`/`check` command. The
  README gives reproduction commands, but they are manual.
- There is no mathematical test script comparable to `codex-gabriel/python/check_math.py`.
- The Gaussian notebook relies on first-order Euler integration for the flow map
  and reports nonzero covariance push-forward errors, e.g. about \(2.07\times
  10^{-3}\) for the linear scheme with 2000 steps. This is fine for a numerical
  demo but not ideal for a "closed-form" assignment.
- The slight scheme-to-scheme differences in the printed Gaussian endpoint maps
  are numerical artifacts. The exact Gaussian endpoint map is schedule
  independent, a fact the notebook misses because it does not derive the
  congruence-square-root formula.
- The Gaussian notebook's universal infinitesimal-law check is not as accurate
  as the paper claims: for the linear scheme it reports a \(3.21\times10^{-4}\)
  max error, which is comparable to the Euler step size and not machine
  precision.
- The Gaussian implementation is mostly NumPy, not PyTorch. This is less
  concerning than in the Dirac case because the PyTorch requirement in `todo.md`
  specifically targeted the three-Dirac simulation.
- The project has no reusable Python module; most code is embedded in notebooks.

Overall, `claude-gabriel/` is a solid reproducible-notebook project, especially for the
Dirac experiment, but its Gaussian part is more exploratory/numerical than the
brief requested.

### `codex-clement/`

Strengths:

- Provides a compact reusable PyTorch utility module in
  `flow_matching_utils.py`.
- Implements the closed-form Dirac density, posterior weights, conditional
  velocity, RK4 trajectory integration, symmetric three-Dirac OT rays, Gaussian
  covariance path, Gaussian velocity matrix, Gaussian OT map, and ellipse
  generation.
- Uses double precision by default, which is appropriate for the Gaussian
  matrix computations.
- Separates notebook creation (`create_notebooks.py`) from figure generation
  (`generate_figures.py`), which is a reasonable project pattern in principle.
- The notebook markdown is concise and pedagogical, especially in the
  three-Dirac derivation.
- Provides `main.pdf`, an 8-page compiled numerical note integrating the main
  derivations and figures.

Weaknesses:

- There is no README, no license, no requirements file, no environment file, no
  Makefile, and no test/check script.
- The LaTeX source for `main.pdf` is absent, so the paper cannot be rebuilt,
  edited, or checked from source.
- Both notebooks are unexecuted: `flow_matching_three_diracs.ipynb` has `0/6`
  code cells executed and `gaussian_covariance_flows.ipynb` has `0/5`.
- Importing the utility module fails under the bare `python3` environment
  because `torch` is missing, and the project does not tell the user how to
  install it.
- The path assumptions are fragile. `create_notebooks.py` sets
  `ROOT = Path(__file__).resolve().parents[1]`, so running it from
  `codex-clement/` would write notebooks to the workspace-level `python/`
  directory rather than inside `codex-clement/`. `generate_figures.py` similarly
  writes figures to a workspace-level `figures/` directory.
- The stored notebooks try to add `ROOT / "python"` to `sys.path`, while the
  submitted utility module lives directly in `codex-clement/`. Depending on the
  Jupyter working directory, this can make imports fail or accidentally resolve
  to unrelated workspace files.
- No standalone generated figure files are included in `codex-clement/`; the
  figures are visible only inside `main.pdf` unless the scripts are rerun.
- The Gaussian endpoint map is integrated numerically with RK4 and stops before
  \(t=1\); there is no exact closed-form implementation or invariant check.

Overall, `codex-clement/` is a meaningful numerical note plus a promising code
skeleton. The new PDF fixes the earlier "missing article" problem, but the
project is still not packaged as a reproducible research repository.

### `codex-kimia/`

Strengths:

- Provides a conventional, compact repository wrapper: `README.md`,
  `requirements.txt`, `Makefile`, two notebooks, paper source, paper PDF, and
  standalone PDF figures.
- Uses PyTorch for the three-Dirac velocity, trajectory integration, and
  semi-discrete OT visualization.
- The notebooks are mostly executed: all nonempty code cells have execution
  counts and outputs where expected. Each notebook also has one empty trailing
  code cell without an execution count.
- `make -C codex-kimia paper` rebuilt the 6-page paper successfully.
- `scripts/export_figures.py` regenerated the figure PDFs when run with
  `KMP_DUPLICATE_LIB_OK=TRUE`.
- The paper source and figures are included, unlike `codex-clement/`.

Weaknesses:

- The documented `make figures` command failed in this host environment because
  `import torch` triggered a duplicate OpenMP runtime error. The workaround
  `KMP_DUPLICATE_LIB_OK=TRUE` is explicitly described by OpenMP as unsafe, so I
  count this as a real reproducibility issue even though the project code then
  runs.
- There is no mathematical test/check script. The project has generated figures
  and executed notebooks, but no invariant checks like
  `codex-gabriel/python/check_math.py` or Emmanuel's `test_fmg.py`.
- The Gaussian flow map is integrated numerically in the notebook, and the
  paper only proves the commuting case.
- `requirements.txt` is unpinned (`torch`, `numpy`, `matplotlib`, `jupyter`,
  `nbformat`), so exact reproduction is not stable across environments.
- The repository includes `.ipynb_checkpoints/` and `__pycache__/`, which are
  minor cleanliness issues.
- `scripts/write_project.py` rewrites notebooks and fallback figures; this is
  useful scaffolding, but it also means direct edits to notebooks can be
  overwritten unless the workflow is understood.

Overall, `codex-kimia/` is a clean mid-tier artifact: much more reproducible
than `codex-clement/`, less overclaiming than `claude-gabriel/`, but not mathematically
complete enough to challenge `codex-gabriel/` or `emmanuel/`.

### `openclaw-jeremie/`

Strengths:

- Provides one of the most professional repository wrappers in the benchmark:
  `README.md`, `ORCHESTRATION.md`, `.gitignore`, `pyproject.toml`,
  `requirements.txt`, `uv.lock`, reusable Python code, tests, executed
  notebooks, paper source, paper PDF, bibliography, and generated PDF/PNG
  figures.
- The main implementation in `python/flow_matching_diracs.py` is PyTorch-native
  for the requested Dirac velocity, density, posterior responsibilities,
  schedules, ODE integration, Gaussian helpers, and finite balanced assignment.
- Both notebooks are executed. The Dirac notebook has 8 executed code cells and
  8 markdown cells; the Gaussian notebook has 7 executed code cells and 6
  markdown cells. They are pedagogical rather than just figure dumps.
- `scripts/make_notebooks_and_figures.py` is a coherent rebuild script: it
  validates formulas, regenerates figures, writes the notebooks, and executes
  them.
- The tests are unusually relevant for this task: continuity residual, terminal
  proportions, brute-force finite assignment, schedule endpoints, Gaussian
  pushforward checks, and OT pushforward checks are all represented in the test
  files.
- The finite balanced assignment code is honest about its scope. It solves the
  exact displayed finite-sample balanced problem rather than claiming to be a
  continuous semi-discrete OT dual solver.
- `openclaw-jeremie/paper/main.tex` rebuilds cleanly after the standard
  `pdflatex`/`bibtex`/`pdflatex` sequence, and the rendered 5-page PDF is
  readable with well placed figures.

Weaknesses:

- The notebooks live under `notebooks/` rather than `python/`, while `todo.md`
  specifically asked for the numerical notebook in `python/`. This is a mild
  structure mismatch because the reusable package itself is under `python/`.
- I could not run the test suite locally. The bare `python3` environment lacks
  `pytest` and `torch`; `uv run --locked pytest -q` began creating `.venv` from
  the lockfile but dependency downloads failed. This is an audit-environment
  limitation, but it means I cannot count the tests as locally passed.
- The Gaussian code integrates the noncommuting matrix ODE numerically. It
  checks pushforward and symmetry diagnostics, but it does not implement the
  exact closed-form congruence formula for \(T_t\).
- The Gaussian theorem's SPD criterion is true but somewhat implicit: it says
  equality with OT holds iff the final flow map is SPD, rather than deriving the
  structural commuting criterion directly from a closed-form endpoint formula.
- The paper is concise. Its literature review and Gaussian proof are cleaner
  than the weak submissions, but less complete than `codex-gabriel/` and much
  less developed than `emmanuel/`.

Overall, `openclaw-jeremie/` is a strong upper-tier artifact. It is more reproducible
and mathematically disciplined than `claude-gabriel/`, and its PyTorch code is more
literal than `emmanuel/` for the Dirac task. Its main gap is exactly the central
Gaussian closed-form \(T_t\) requested in `todo.md`, which keeps it below
`codex-gabriel/` and `emmanuel/`.

### `hermes-jeremie/`

Strengths:

- Provides a professional compact repository: `README.md`, `.gitignore`,
  `pyproject.toml`, `requirements.txt`, `uv.lock`, CI, reusable Python package,
  scripts, tests, notebooks, source paper, prebuilt PDF, bibliography, and
  generated PDF/PNG figures.
- The implementation is PyTorch-native for the requested three-Dirac density,
  responsibilities, exact velocity, sampling, RK4 integration, Gaussian
  covariance helpers, and Gaussian OT matrix.
- The package is well factored into small modules:
  `density.py`, `velocity.py`, `schedules.py`, `sampling.py`, `ot.py`,
  `gaussian.py`, `plotting.py`, and `targets.py`.
- `uv run pytest` passed all 5 tests after installing the locked environment.
  The tests cover schedule endpoints, responsibility normalization/hardening,
  density normalization by quadrature, finite velocity values, and the Gaussian
  covariance ODE identity.
- The notebooks and figures are generated from committed scripts, which makes
  the project easy to regenerate once dependencies are available.
- The paper source and figures are included, and the rendered PDF is cleanly
  inspectable.

Weaknesses:

- The submitted notebooks are not executed: `01_dirac_flow_matching.ipynb` has
  `0/5` nonempty code cells executed and `02_gaussian_covariances.ipynb` has
  `0/3`. This materially weakens the requested pedagogical notebook artifact.
- The OT comparison is a greedy balanced finite-sample heuristic, not a
  certified semi-discrete Laguerre solve and not an exact finite assignment
  optimization. The project labels it honestly as OT-like, but that honesty
  also confirms the limitation.
- The Gaussian code integrates the noncommuting flow matrix numerically for the
  contrast figure; it does not implement the exact general congruence formula
  for \(T_t\).
- The tests are useful but narrower than `openclaw-jeremie/`'s and `codex-gabriel/`'s:
  no continuity-equation residual, no Gaussian endpoint closed-form check, no
  exact OT assignment check, and no notebook execution check.
- Running `uv` under the sandbox initially failed because its default cache is
  outside the workspace and then required network access to install the locked
  environment. This is normal for `uv`, but it means the project is not
  zero-dependency reproducible from the submitted tree alone.

Overall, `hermes-jeremie/` is a strong and clean submission. It is below `openclaw-jeremie/`
mainly because its notebooks are unexecuted, its OT comparison is only a
heuristic visualization, and its Gaussian theorem is the commuting/time-ordered
version rather than the explicit noncommuting closed form requested in
`todo.md`.

### `emmanuel/`

Strengths:

- Provides the broadest professional wrapper: `README.md`, `MISSION.md`,
  `python/README.md`, pinned `requirements.txt`, a reusable `fmg/` package,
  tests, executed notebooks, paper source, paper figures, Lean files, internal
  audits, and a delivery/report layer.
- `python/tests/test_fmg.py` passed all 8 tests in my local run. The tests cover
  schedule boundaries, symmetric square roots, closed-form velocity versus
  autodiff, finite posteriors near the endpoint, trajectory landing, unequal
  semi-discrete OT fitting, commuting Gaussian equality, and noncommuting
  schedule-independence with non-OT behavior.
- Both notebooks are executed and export PDF figures into `paper/figures/`.
- The semi-discrete OT code handles unequal weights, with a POT exact-LP path
  and a library-free damped-Newton fallback.
- The Gaussian code keeps the non-symmetric drift unsymmetrized, checks
  pushforward residuals, and exposes Bures OT, Bures geodesic, commutator norm,
  symmetry defect, and schedule-spread diagnostics.
- The paper builds from source after the standard `pdflatex`, `biber`,
  `pdflatex`, `pdflatex` sequence.
- The Lean anchor is honestly scoped: the imported theorem file has no `sorry`
  or project-local `axiom`, and the unformalized items are listed separately
  rather than smuggled into the proof assistant.

Weaknesses:

- The main notebook/library implementation is NumPy/SciPy-first, despite the
  request's PyTorch wording. PyTorch is present and used for an autodiff
  cross-check, but `emmanuel/` is not a PyTorch-native numerical artifact.
- The full noncommuting Gaussian theorem is not Lean-formalized. Only the
  commuting case is formalized; flatness, ODE identification, and the
  noncommuting converse remain informal paper mathematics.
- The submitted tree did not include `paper/paper.pdf`; I generated it during
  the audit. This is much less serious than `codex-clement/` lacking source, but
  it does mean the delivered artifact was source-first rather than ready-to-read.
- `docs/wiki/schedules.md` is stale about Gaussian endpoint
  schedule-independence, saying it holds only in the commuting case. The paper,
  tests, and theorem note supersede it, but stale documentation is a
  reproducibility hazard.
- The internal code audit reports that default `ruff check .` sees notebook
  lint issues, even though the library and tests are clean. This is polish and
  claim alignment, not a scientific error.
- The project includes substantial meta-report/cosmon infrastructure. It is
  impressive, but it also makes the artifact heavier and noisier than `codex-gabriel/`
  for a reader who only wants the requested notebooks and paper.

Overall, `emmanuel/` is the most complete research artifact. It is slightly less
literal than `codex-gabriel/` on the PyTorch implementation detail, but stronger on
semi-discrete OT, paper polish, theorem exposition, and formal-proof hygiene.

### `codex-gabriel/`

Strengths:

- Uses a reusable PyTorch module, `python/stochastic_interpolants.py`, for
  schedules, densities, posterior weights, velocities, ODE integration,
  Gaussian maps, OT maps, and ellipse generation.
- Provides generated but fully executed pedagogical notebooks.
- The Dirac notebook includes density contours, velocity fields, sample
  trajectories, schedule comparisons, OT rays, and a path-length comparison.
- The Gaussian notebook exports PDF figures to `paper/figures/` and directly
  compares the stochastic-interpolant endpoint map with the Gaussian OT map.
- The article uses `\graphicspath{{figures/}}`, a bibliography file, and
  integrates generated figures cleanly.
- The top-level `Makefile` has `check`, `notebooks`, `paper`, and `all` targets.
- `requirements.txt` lists the core dependencies.
- `python/check_math.py` validates schedules, posterior normalization,
  continuity-equation residuals, Gaussian covariance push-forwards, generator
  identities, noncommuting endpoint-map separation, and the commuting equality
  case.

Weaknesses:

- The VP schedule is a square-root interpolation rather than a beta-schedule
  diffusion VP. This is acceptable and documented, but readers expecting the
  beta-schedule convention may want a sentence explaining the choice.
- The notebooks are generated from `build_notebooks.py`, which is good for
  reproducibility but can make direct notebook editing less natural.
- The repository is still small; it does not include a lockfile or CI
  configuration. This is minor relative to the request.

Overall, `codex-gabriel/` behaves like a compact reproducible research artifact.

## Paper Quality

I rendered all nine PDFs with `pdftoppm` and inspected the pages around the
largest figures and theorem sections. All nine PDFs render and are readable,
but the mathematical completeness and source reproducibility differ
substantially.

### `antigravity-olivier/paper/main.tex`

The paper has the requested high-level sections: abstract, introduction,
general setup, three-Dirac experiment, Gaussian case, theorem, proof, numerical
comparison, and conclusion. The writing is readable. It integrates figures from
`../python/plots/`.

Main issues:

- The Gaussian theorem proof is not rigorous enough in the noncommuting case.
- The general closed-form \(T_t\) requested in `todo.md` is missing.
- The VP schedule is presented as satisfying the endpoint interpolation, but the
  implemented beta schedule does not exactly make \(a(1)=0\).
- The OT velocity expression in the Dirac section is not fully Eulerian.
- The article is less polished mathematically than it appears at first glance:
  it states correct conclusions but skips key noncommuting matrix details.
- The rendered PDF places the large four-panel Dirac trajectory figure between
  the beginning and continuation of the Gaussian theorem proof. This makes the
  most delicate part of the paper harder to follow.
- The figures have script-style titles inside each panel, large legends, and
  heavy gridlines. They are useful diagnostics, but they look more like notebook
  screenshots than publication figures.
- The author block uses "Antigravity / Google DeepMind Team /
  antigravity@google.com", which reads like placeholder branding rather than a
  serious article metadata choice.

### `antigravity-antoine/paper/main.tex`

The Antoine paper is a short 4-page LaTeX note with source, prebuilt PDF, and
notebook-exported figures. It has a title, abstract, three-Dirac formula,
trajectory figures, Gaussian covariance and velocity formulas, and a brief
linear-schedule Gaussian comparison. The PDF renders cleanly and the included
figures are readable.

Main strengths:

- The Dirac conditional velocity formula is correct and matches the executed
  PyTorch notebook.
- The Gaussian covariance path and velocity matrix are written in a correct
  equivalent form.
- Unlike `codex-clement/`, the LaTeX source is present, so the article can in
  principle be rebuilt and edited.

Main issues:

- The title and README advertise an "exact" Gaussian flow map, but the paper
  never derives the requested closed-form \(T_t\). It only writes the matrix ODE
  and relies on numerical integration.
- The statement that the linear-schedule endpoint equals Gaussian OT iff the
  covariances commute is asserted rather than proved.
- The OT comparison for the Dirac example is presented as nearest-atom
  straight-line assignment without proving that this is the semi-discrete OT
  solution for the chosen, non-symmetric atoms.
- There is no bibliography or real literature discussion.
- The theorem/proof layer is underdeveloped. The paper gives formulas and
  figures, but not the polished theorem requested in `todo.md`.
- The PDF uses default LaTeX styling and red hyperlink boxes, and the author
  metadata is generic.

Overall, `antigravity-antoine/` is a better delivered artifact than
`antigravity-olivier/` in the narrow sense that it includes source LaTeX, a PDF,
and executed PyTorch notebooks. It is still clearly below `codex-clement/` and
the mid-tier projects because the Gaussian theorem and reproducibility layer
remain too thin.

### `claude-gabriel/paper/main.tex`

The `claude-gabriel/` paper is one of the more expansive compiled papers at 11 pages. It
has a table of contents, related work, general theory, schedule
definitions, a detailed Dirac-mixture case, density and velocity field evolution
figures, Gaussian covariance figures, a theorem section, and an inline
bibliography. It renders without unresolved-reference warnings.

Main issues:

- The abstract and theorem statement claim a global "if and only if" Gaussian
  result, but the proof only establishes sufficiency and infinitesimal
  necessity. The paper itself later admits the non-perturbative necessity proof
  is future work. This is the largest paper-level flaw.
- The conclusion says "closed-form solutions for Gaussian transport, including
  covariance evolution and flow maps", but the noncommuting flow map is
  numerically integrated, not derived in closed form.
- The remark that scheme-dependence in \(M_1\) is a second-order effect is
  misleading. For the exact independent-Gaussian flow, \(T_1\) is
  schedule-independent; the observed differences across schedules come from
  numerical integration error.
- The claim that the universal infinitesimal coefficient is confirmed "to
  machine precision" is not supported by the executed notebook output for the
  linear scheme, which reports a \(3.21\times10^{-4}\) max error.
- The commuting-case proof contains a displayed diagonal-generator formula with
  an incorrect sign/factor, even though the final endpoint formula is correct.
- The rendered PDF uses default red boxes around internal links and citations.
  They are not unresolved references, but they make the table of contents and
  theorem pages look less polished.
- Figures are numerous and useful, but some multi-panel figures are small after
  scaling and have notebook-style titles/gridlines.

Overall, this is a more complete and polished article than `antigravity-olivier/`, but
it is less mathematically reliable than `codex-gabriel/` because its central Gaussian
claim is overstated relative to its proof.

### `codex-clement/`

The newly added `codex-clement/main.pdf` is an 8-page LaTeX-generated numerical
note. It has a clean title page, abstract, introduction, general setup,
three-Dirac derivation, Gaussian proposition/theorem, five integrated figures,
a numerical reproducibility section, conclusion, and references. The rendered
layout is generally clean: pages are readable, figures are not clipped, and the
trajectory and covariance plots are scientifically useful.

Main issues:

- No LaTeX source is provided. The PDF is therefore inspectable but not
  reproducible or editable from the submitted project.
- The paper still does not give the requested general noncommuting closed-form
  \(T_t\). It explicitly treats the noncommuting flow as a time-ordered
  exponential, gives the commuting-case closed form, and compares a numerical
  noncommuting endpoint with OT.
- The theorem is more honest than `claude-gabriel/`'s global overclaim, but it is also
  weaker than the assignment asks for and weaker than the `codex-gabriel/` theorem.
- The reproducibility section says the figures come from
  `python/flow_matching_three_diracs.ipynb`,
  `python/gaussian_covariance_flows.ipynb`,
  `python/flow_matching_utils.py`, and `python/generate_figures.py`. The
  submitted `codex-clement/` directory instead contains these files at the
  project root, not under `python/`, and the notebooks are unexecuted.
- There are no standalone generated figure PDFs in `codex-clement/`, only the
  embedded figures in `main.pdf`.

Overall, this paper is a substantial improvement over the earlier
`codex-clement/` audit. It is more mathematically cautious than `antigravity-olivier/`
and better visually polished, but it remains below `claude-gabriel/` and `codex-gabriel/` as a
complete reproducible project.

### `codex-kimia/paper/article.tex`

The Kimia paper is a compact 6-page LaTeX article with source and a prebuilt
PDF. It has an abstract, introduction, general setup, three-Dirac derivation,
semi-discrete OT comparison, Gaussian covariance/velocity section, a commuting
Gaussian theorem, discussion, reproducibility note, and references. I rebuilt
it with `make -C codex-kimia paper` and rendered representative pages; the PDF
is readable, and the figures are not clipped.

Main strengths:

- The paper is honest about the Gaussian theorem: it proves the commuting case
  rather than overstating the global iff result.
- It correctly warns that noncommuting Gaussian flows require time ordering.
- The paper includes source and all figure PDFs, unlike `codex-clement/`.
- The writing is concise and the theorem proof is algebraically correct for
  simultaneous diagonalization.

Main issues:

- The Gaussian result is much weaker than the requested one: no general
  noncommuting closed-form \(T_t\), no exact endpoint formula, no
  schedule-independence theorem, and no iff equality proof.
- The noncommuting discussion is qualitative; it does not use the exact
  endpoint formula even for its own numerical matrices.
- The paper is short and less pedagogical than `claude-gabriel/`, `codex-gabriel/`, or
  `emmanuel/`; the literature review is minimal.
- The figures are serviceable but small, with notebook-style gridlines and
  titles.

Overall, this is a solid mid-tier paper: cleaner and more reproducible than
`codex-clement/`, but mathematically less complete than `codex-gabriel/` and
less ambitious than `claude-gabriel/`.

### `openclaw-jeremie/paper/main.tex`

The `openclaw-jeremie/` paper is a clean 5-page LaTeX note with source, bibliography,
prebuilt PDF, and generated PDF figures. It has an abstract, introduction,
general setup, three-Dirac derivation, trajectory and finite-assignment figures,
Gaussian covariance/velocity derivation, theorem, proof, Gaussian ellipse
figure, discussion, and references. I rebuilt it with
`pdflatex`, `bibtex`, and further sequential `pdflatex` passes; the final log
had no unresolved-reference or citation warnings, and all pages render cleanly.

Main strengths:

- The paper is honest about the noncommuting Gaussian case. It uses a
  time-ordered exponential rather than an invalid ordinary exponential or
  symmetry shortcut.
- The Dirac derivation is correct and concise, and the figures are legible.
- The OT comparison is carefully worded as an exact balanced finite assignment
  on the displayed sample, not as a full continuous semi-discrete OT solve.
- The theorem's SPD criterion for equality with the Brenier map is true and
  cleanly proved from uniqueness of the SPD pushforward map.
- The source/PDF/figures/bibliography are all included, so the article is
  actually rebuildable.

Main issues:

- The paper still misses the requested explicit general closed-form \(T_t\) in
  the noncommuting Gaussian case. The time-ordered exponential is correct, but
  it is not the closed congruence formula requested in `todo.md`.
- The equality criterion is expressed as "the final flow map is SPD" rather
  than deriving the more informative covariance-level commuting criterion.
- The article is shorter and less detailed than the best papers. Its literature
  section is appropriate but compact, and the Gaussian section does not explore
  schedule-independence as fully as `codex-gabriel/` or `emmanuel/`.
- The Gaussian figure is useful but visually modest; it works as a note figure,
  not as a highly polished publication figure.

Overall, this is the best paper below `codex-gabriel/` and `emmanuel/`: more
mathematically reliable than `claude-gabriel/`, more reproducible than `codex-clement/`,
and much more professional than `antigravity-olivier/`, but still missing the central
closed-form Gaussian map.

### `hermes-jeremie/paper/main.tex`

The `hermes-jeremie/` paper is a 7-page LaTeX article with source, bibliography, prebuilt
PDF, and generated PDF/PNG figures. It has a clean abstract, introduction,
general stochastic-interpolant setup, three-Dirac density/velocity derivation,
schedule and trajectory figures, an OT-contrast subsection, a Gaussian
covariance-flow theorem, covariance ellipse figures, discussion, and
references. I rendered all pages with `pdftoppm`; the PDF is readable and the
mathematical notation is legible.

Main strengths:

- The three-Dirac derivation is correct and concise.
- The paper is careful about the singular endpoint and endpoint stiffness.
- The OT comparison is worded honestly as a balanced sample-level visual
  contrast rather than a certified semi-discrete solver.
- The Gaussian theorem is safe: it proves the commuting case and explicitly
  states that the noncommuting flow is time ordered and generally differs from
  Gaussian OT.
- The figures are scientifically useful and are available as standalone
  PDF/PNG files.

Main issues:

- The Gaussian theorem is weaker than the requested result. It does not derive
  the explicit general noncommuting closed-form \(T_t\), nor the covariance-level
  iff criterion for equality with OT.
- The noncommuting Gaussian comparison is numerical, based on integrating the
  flow matrix, even though the exact endpoint congruence formula would make the
  comparison sharper.
- The paper's float placement is not fully polished. The first schedule figure
  appears before the OT subsection, while several key Dirac figures and the
  Gaussian figures appear after the theorem/discussion/references rather than
  close to their first discussion.
- The displayed figure style is clean but notebook-like, with default axes and
  compact panel labels.
- The submitted notebooks that generate the pedagogical material are
  unexecuted, so the paper is more complete than the notebook artifacts.

Overall, `hermes-jeremie/` has a reliable and readable paper, stronger than the weaker
mid-tier papers on mathematical honesty. It remains below `openclaw-jeremie/` because
`openclaw-jeremie/`'s theorem is slightly more informative and its notebooks are executed,
and below `codex-gabriel/`/`emmanuel/` because it lacks the exact Gaussian
closed-form map.

### `emmanuel/paper/paper.tex`

The Emmanuel paper is a polished 13-page article after build. It has a clean
abstract, literature-framed introduction, general stochastic-interpolant setup,
three-Dirac section with density, velocity cross-check, trajectory, and
semi-discrete OT figures, a substantial Gaussian theorem section, a
noncommuting witness, a falsification sweep, discussion, and bibliography. I
built it from source with `pdflatex`, `biber`, and two additional `pdflatex`
runs; the final log had references resolved, and the rendered representative
pages were legible.

Main strengths:

- The theorem statement is the most complete: it includes unconditional
  endpoint schedule-independence, equivalence between commutation, symmetry,
  equality with OT, and the commuting-map formula.
- The noncommuting proof route is much stronger than in `antigravity-olivier/` and
  `claude-gabriel/`: it explicitly warns against the Magnus/time-ordering trap, then
  uses the closed form \(T_1=(\Sigma_1\Sigma_0^{-1})^{1/2}\) to close the
  converse.
- The figures are integrated and scientifically useful. The covariance-ellipse
  pages make the commuting/noncommuting contrast visible, and the sweep figure
  includes a schedule-spread diagnostic that supports endpoint
  schedule-independence.
- The limits/formalization paragraph is honest: Lean formalizes the commuting
  case, not the full global theorem.

Main issues:

- The paper was not submitted as a prebuilt PDF; it was source-only until I
  generated `paper.pdf`.
- The Lean-backed part is narrower than the theorem headline. This is disclosed
  honestly, but readers should not confuse "has a Lean development" with "the
  full noncommuting theorem is machine-checked."
- The paper is dense. The proof section carries local transversality material
  before the closed-form argument that actually closes the theorem; that
  geometric material is useful but not load-bearing, and a shorter final paper
  could make this hierarchy clearer.
- Some surrounding docs are stale relative to the final theorem, especially the
  schedules wiki page.

Overall, this is the strongest paper among the submitted projects. It is not
just visually polished; it also fixes the key mathematical gap that remained in
`claude-gabriel/` and `codex-clement/`.

### `codex-gabriel/paper/main.tex`

The paper is substantially stronger. It explains the stochastic interpolant
setup, derives the Dirac density and conditional velocity, discusses the
semi-discrete OT geometry, and presents a clean Gaussian theorem with the
correct closed-form flow map. It includes numerical figures generated by the
notebooks and a conventional bibliography.

Main issues:

- It could add a little more historical detail in the literature review, but
  the cited works are appropriate.
- It could make the square-root VP convention more explicit relative to
  diffusion beta schedules.
- One rendered float lands between the theorem statement and the proof. The
  theorem itself remains readable, but the layout could be improved by moving
  the OT/path-length figure before the Gaussian theorem or forcing it earlier.
- Some figure labels are compact and a little small after scaling. This is a
  polish issue; the figures remain legible and scientifically useful.

These are minor improvements, not blockers.

## Requirement-by-Requirement Coverage

| Requirement | `antigravity-olivier/` | `antigravity-antoine/` | `codex-clement/` | `codex-kimia/` | `claude-gabriel/` | `hermes-jeremie/` | `openclaw-jeremie/` | `codex-gabriel/` | `emmanuel/` |
|---|---|---|---|---|---|---|---|---|---|
| Three-Dirac notebook | Present, executed, but NumPy/SciPy and not fully figure-exporting | Present and executed; PyTorch velocity, SciPy ODE | Present but unexecuted; PyTorch utility code | Present, mostly executed, PyTorch-based | Present, executed, PyTorch-based, rich figures | Present but unexecuted; PyTorch package/scripts | Present, executed, PyTorch-based, pedagogical | Present, executed, PyTorch-based, pedagogical | Present, executed, rich figures, NumPy/SciPy-first |
| Closed-form density | Derived, not strongly used in plotting | Derived and implemented with responsibilities | Derived and implemented | Derived and implemented | Derived, implemented and plotted | Derived, implemented with log-sum-exp | Derived, implemented, validated in notebooks/tests | Derived, implemented as `log_density`, plotted | Derived, implemented, tested near endpoint |
| Velocity in PyTorch | Not satisfied | Mostly: PyTorch velocity, SciPy integration | Satisfied in utility code, but not executed | Satisfied | Satisfied for Dirac case | Satisfied in reusable module and tests | Satisfied in reusable module and notebooks | Satisfied | Partially: PyTorch autodiff cross-check, but main code is NumPy/SciPy |
| Three colored Diracs and colored trajectories | Satisfied | Satisfied in notebook figures | Scripted but not executed or stored | Satisfied | Satisfied | Satisfied in generated figures | Satisfied, with pre-terminal labeling clearly stated | Satisfied | Satisfied, with unequal target weights |
| Three schedules | Satisfied for independent trajectories, but VP endpoint imperfect | Satisfied with endpoint-consistent schedules | Satisfied, with integrations stopped before \(t=1\) | Satisfied, with endpoint clamping/stopping short | Satisfied with exact endpoint schedules | Satisfied and endpoint-tested; integrates pre-terminally | Satisfied and endpoint-tested; integrates singular target pre-terminally | Satisfied with exact endpoint schedules | Satisfied and tested; adds cubic/reparametrization discussion |
| Contrast with OT trajectories | Present for linear OT | Present, but nearest-atom OT claim unjustified | Present in utility/notebook, unexecuted | Present with approximate Laguerre dual optimization | Present with symmetric angular-cell assignment | Greedy balanced OT-like visualization | Exact balanced finite-sample assignment, honestly scoped | Present with derivation, rays, and path-length plot | Strongest: semi-discrete Laguerre OT for unequal weights |
| Pedagogical markdown | Partial | Partial: executed but thin | Concise but unexecuted | Good | Strong | Good text in generated notebooks, but unexecuted | Strong, with exposed tensors and diagnostics | Strong | Strong, plus internal audit docs |
| LaTeX article | Present | Present with source/PDF, but very short | PDF present, no LaTeX source | Present with source and PDF | Present, but theorem overstated | Present with source and PDF; cautious theorem | Present with source and clean PDF | Present and strong mathematically | Present, builds to strongest/polished PDF |
| Literature intro | Present but lightweight | Essentially missing; no bibliography | Present and concise | Present but minimal | Present and broad | Present and appropriate but compact | Present and appropriate but compact | Present and appropriate | Present and well supported by citation audit |
| Gaussian \(\Sigma_t\) | Correct | Correct | Correct | Correct | Correct | Correct | Correct | Correct | Correct |
| Gaussian \(T_t\) closed form | Missing except commuting case | Missing; matrix ODE numerics only | Missing except commuting case; RK4 integration | Missing except commuting case; numerical integration | Missing in noncommuting case; numerical Euler integration | Missing except commuting case; numerical integration | Time-ordered exponential only; no explicit congruence closed form | Correct general formula | Correct endpoint formula and schedule-independence; full \(T_t(a,b)\) less explicitly packaged |
| Compare \(T_1\) with OT | Headline correct, proof flawed/incomplete | Asserted for linear schedule, not proved | Numerical comparison only, not exact endpoint | Numerical comparison plus commuting theorem | Good numerical comparison, theorem proof only infinitesimal for necessity | Numerical contrast plus commuting theorem; no structural iff | True SPD criterion plus numerical noncommuting check, but no structural iff | Correct | Correct and best explained |
| Polished theorem and proof | Partial | Weak: formulas and assertion, no proof | Partial: cautious commuting theorem, no general \(T_t\) | Correct commuting theorem only | Mixed: serious but overclaimed | Correct commuting theorem; incomplete general case | Good but incomplete: true SPD theorem, missing explicit \(T_t\) | Strong | Strongest informal proof; commuting case Lean-anchored |
| Gaussian covariance ellipse notebook | Present but thin, not the primary export path | Present, executed, but ODE-only | Present but unexecuted; figure embedded in PDF | Present, mostly executed, exports PDFs | Present, exports PDFs | Present but unexecuted; exports via script | Present, executed, exports PDFs | Present, exports PDFs | Present, executed, exports PDFs |
| Professional repo | Partial | Weak: no deps, package, tests, Makefile, or CI | Weak: no README, deps, LaTeX source, or standalone figures | Good compact repo, but unpinned deps | Good, but no top-level build/check | Strong: pyproject, lockfile, CI, tests, source paper | Very strong: pyproject, lockfile, tests, source paper, executed notebooks | Strong | Strongest, though somewhat heavy |
| Reproducibility/tests | Weak | Weak: README references missing requirements file; no tests | Weak: no deps, no tests, unexecuted notebooks | Medium: source/build present, no tests, OpenMP issue | Medium: requirements and executed notebooks, no tests | Good: locked env and 5 tests passed; notebooks unexecuted | Strong test/build design, but dependency install failed in this audit | Strong for this scope | Strong: pinned deps, tests, source paper, executed notebooks; full Lean build not locally completed |

## Severity-Ranked Findings

### High severity

1. `antigravity-olivier/` does not satisfy the PyTorch requirement. The central
   three-Dirac notebook and scripts are written with NumPy/SciPy, even though
   `todo.md` explicitly requests a PyTorch notebook and PyTorch velocity
   computation.
2. `antigravity-olivier/` does not provide the requested general Gaussian flow-map
   formula. It gives the matrix ODE and a commuting-case expression, but misses
   the correct noncommuting closed form
   \[
   T_t=\Sigma_0^{1/2}
   (a(t)^2I+b(t)^2\Sigma_0^{-1/2}\Sigma_1\Sigma_0^{-1/2})^{1/2}
   \Sigma_0^{-1/2}.
   \]
3. `antigravity-olivier/` has a flawed proof strategy for the Gaussian theorem. The
   conclusion is right, but the proof relies on a symmetry argument for a
   time-varying matrix ODE that is not valid as written.
4. `antigravity-olivier/` uses a VP schedule that violates exact endpoint constraints
   because of both the finite beta integral and the added square-root epsilon.
5. `antigravity-antoine/` does not provide the requested general closed-form
   Gaussian \(T_t\). It gives a correct covariance path and velocity matrix, but
   the central flow map is left as a numerically integrated matrix ODE.
6. `codex-clement/` notebooks are unexecuted and the project has no dependency
   file. In the bare environment, importing `flow_matching_utils.py` fails
   because `torch` is unavailable.
7. `codex-clement/` does not provide the requested general closed-form Gaussian
   \(T_t\). It gives the commuting case and numerically integrates the
   noncommuting ODE with RK4.
8. `codex-kimia/` does not provide the requested general closed-form Gaussian
   \(T_t\) or the exact iff characterization. It proves the commuting case
   correctly and discusses noncommuting time ordering, but the central
   noncommuting theorem remains missing.
9. `openclaw-jeremie/` does not provide the requested explicit general closed-form
   Gaussian \(T_t\). Its time-ordered exponential and SPD equality criterion
   are correct, but the congruence-square-root formula and covariance-level
   commuting characterization remain missing.
10. `hermes-jeremie/` does not provide the requested explicit general closed-form
   Gaussian \(T_t\) or the structural iff criterion. Its commuting theorem and
   time-ordered noncommuting discussion are safe, but incomplete.
11. `claude-gabriel/` states a global Gaussian "if and only if" theorem but only proves
   the necessity direction infinitesimally near \(\Sigma_1=\Sigma_0\). The paper
   later admits the global non-perturbative necessity proof is open, so the
   theorem/abstract/conclusion overclaim the result.
12. `claude-gabriel/` does not provide the requested general closed-form \(T_t\) in the
   Gaussian case. It numerically integrates the matrix ODE with Euler steps
   instead.
13. `claude-gabriel/` misses exact schedule-independence of the Gaussian endpoint map.
   Its printed differences between linear, VP, and cosine \(T_1\) maps are
   numerical artifacts, not mathematical effects.

### Medium severity

1. `antigravity-olivier/` lacks reproducibility infrastructure: no dependency file, no
   top-level Makefile, no test/check script, and no automated rebuild path from
   notebooks to paper.
2. `antigravity-olivier/` uses pre-generated figures from scripts rather than making
   the requested pedagogical notebooks the authoritative source of the figures.
3. `antigravity-antoine/` has weak reproducibility infrastructure: the README
   references a missing `requirements.txt`, and there is no package, Makefile,
   CI, or test/check script.
4. `antigravity-antoine/` overstates the three-Dirac OT contrast. Its
   nearest-atom assignment is a useful visual baseline, but the project does
   not justify it as the exact semi-discrete OT solution for the chosen atoms.
5. `codex-gabriel/` should clarify that its VP schedule is the square-root
   variance-preserving interpolation, not a beta-schedule diffusion VP.
6. `codex-gabriel/` has minor float-placement issues in the rendered paper, including a
   figure between the Gaussian theorem statement and proof.
7. `codex-clement/` provides only `main.pdf`, not the LaTeX source. This makes
   the article inspectable but not rebuildable or directly editable.
8. `codex-clement/` has fragile path assumptions: notebook generation and figure
   generation write outside `codex-clement/` into workspace-level directories.
9. `codex-clement/` includes no standalone generated figure PDFs; the visual
   outputs are embedded in `main.pdf` but not present as separate files.
10. `codex-kimia/`'s documented `make figures` command failed in this host
   environment because `torch` triggered a duplicate OpenMP runtime error. The
   script ran only with `KMP_DUPLICATE_LIB_OK=TRUE`, which is an unsafe
   workaround rather than a clean reproducibility path.
11. `codex-kimia/` has no mathematical test/check script and unpinned
   dependencies, so its figures and formulas are not guarded against numerical
   or environment drift.
12. `openclaw-jeremie/`'s tests could not be executed in this audit environment. The
    project has a lockfile and a good test suite, but `uv run --locked pytest -q`
    could not finish dependency downloads, so I cannot count the tests as
    locally passed.
13. `hermes-jeremie/` submits generated but unexecuted notebooks. The code, tests, and
    generated figures are present, but the requested pedagogical notebook
    artifacts do not contain outputs.
14. `hermes-jeremie/` uses a greedy balanced OT-like assignment rather than a certified
    continuous semi-discrete solver or exact finite assignment optimization.
    It labels this honestly, but the comparison is weaker than the best
    submissions.
15. `claude-gabriel/` overstates its numerical validation of the infinitesimal law: the
   executed notebook reports a \(3.21\times10^{-4}\) linear-schedule error, not
   machine precision.
16. `claude-gabriel/` has a sign/factor error in the displayed commuting-case diagonal
   generator, although the final commuting endpoint formula is correct.
17. `claude-gabriel/` lacks a top-level `Makefile` or test/check script.
18. `emmanuel/` is not PyTorch-native in the main implementation. The request
    explicitly asked for PyTorch velocity computation; Emmanuel's main
    notebook/library path is NumPy/SciPy, with PyTorch used for an autodiff
    validation rather than as the primary implementation substrate.
19. `emmanuel/` has a narrower Lean result than a casual reader might infer
    from "has Lean". The imported Lean theorem formalizes the commuting case
    only; the global schedule-independence and noncommuting converse remain in
    the paper proof.
20. `emmanuel/docs/wiki/schedules.md` is stale relative to the final theorem:
    it says Gaussian endpoint schedule-independence holds only in the commuting
    case, while the paper and tests correctly treat it as unconditional.

### Low severity

1. `antigravity-olivier/` includes `.DS_Store` files and placeholder-looking author
   metadata.
2. `antigravity-antoine/` uses default red hyperlink boxes, generic author
   metadata, and a bibliography-free paper, which makes the article look more
   like a quick note than a polished deliverable.
3. `claude-gabriel/` uses default red hyperlink boxes in the PDF, which makes the table
   of contents and reference-heavy theorem pages look less polished.
4. `codex-gabriel/` could add a lockfile or CI target, but its existing `Makefile`,
   requirements file, and mathematical checks are already adequate for the
   requested scope.
5. `codex-kimia/` includes `.ipynb_checkpoints/` and `__pycache__/`, which are
   minor repository-cleanliness issues.
6. `codex-kimia/` notebooks each contain an empty trailing code cell with no
   execution count. The substantive cells are executed, so this is only a
   polish issue.
7. `openclaw-jeremie/` puts the requested notebooks under `notebooks/` rather than
   `python/`. Since the reusable code is under `python/`, this is a structure
   mismatch rather than a functional failure.
8. `hermes-jeremie/`'s PDF uses green hyperlink boxes and has several large floats
   delayed until after the relevant section or references. This affects polish,
   not correctness.
9. `emmanuel/` did not include a prebuilt `paper.pdf`; I generated it from
   source during the audit. Since the source builds cleanly, this is a delivery
   polish issue rather than a reproducibility failure.
10. `emmanuel/`'s internal audit notes notebook Ruff issues under default
   `ruff check .`. The library and tests are clean, so this is mainly a
   claim/configuration alignment issue.
11. `emmanuel/` contains substantial meta-reporting infrastructure. It is useful
   for provenance, but noisier than necessary for the requested deliverable.

## Final Verdict

`antigravity-olivier/` partially addresses the assignment and would be useful as a first
draft, but it should not be accepted as a complete answer to `todo.md`. Its best
component is the independent three-Dirac derivation and the basic trajectory
plotting. Its main failures are that it does not satisfy the PyTorch notebook
requirement, uses an endpoint-inconsistent VP schedule, and does not compute or
prove the general noncommuting Gaussian flow map cleanly. The project reaches
the visual shape of the requested deliverable but falls short on mathematical
rigor and professional reproducibility.

`antigravity-antoine/` ranks above `antigravity-olivier/` because it has executed
PyTorch notebooks, source LaTeX, a prebuilt PDF, and a correct Dirac velocity
formula. Its Gaussian velocity matrix is also correct. It remains below
`codex-clement/`, however, because it has no dependency file or tests, mixes
PyTorch velocity evaluation with SciPy ODE integration, treats a nearest-atom
visualization as an OT comparison without proof, and never derives the requested
closed-form Gaussian \(T_t\). It is a plausible short demonstration, not a
complete solution to `todo.md`.

`codex-clement/` now ranks above `antigravity-olivier/`. Its 8-page `main.pdf` is a real
numerical note with integrated figures and references, and its PyTorch skeleton
is cleaner than Olivier's NumPy code. Its Gaussian discussion is also more
careful: it recognizes the time-ordered nature of the noncommuting flow instead
of relying on an invalid symmetry argument. The remaining blockers are
reproducibility and completeness: no LaTeX source, no README, no dependency
setup, no executed notebooks, no standalone figure exports, no tests, and no
general closed-form \(T_t\).

`codex-kimia/` ranks above `codex-clement/` because it supplies the missing
source/rebuild layer: README, requirements, Makefile, notebooks, paper source,
paper PDF, and figure PDFs. Its three-Dirac PyTorch implementation is credible,
and its Gaussian paper is honest rather than overclaimed. Its main weakness is
that it stops at the commuting Gaussian theorem and numerical noncommuting
evidence, so it still misses the requested general \(T_t\) and iff comparison.
The Torch/OpenMP failure of the documented `make figures` path also prevents me
from calling it fully clean reproducibility-wise.

`claude-gabriel/` remains a strong mid-tier answer. It does fulfill the PyTorch Dirac
notebook requirement, exports many useful figures, and has a much more complete
paper/repository shell than both `antigravity-olivier/` and `codex-clement/`. Its
weakness is concentrated in the Gaussian theory: it treats the general flow map
numerically and overstates an infinitesimal theorem as a global theorem. A
closer look also shows that it misses the exact schedule-independence of the
Gaussian endpoint map and overstates the precision of its Euler-based numerical
checks.

`openclaw-jeremie/` ranks above `claude-gabriel/` because it combines a professional repository
with a more reliable mathematical stance. Its Dirac implementation is
PyTorch-native and modular, its notebooks are executed and pedagogical, its
figures and paper rebuild cleanly, and its tests are well targeted even though I
could not run them here because dependency downloads failed. The Gaussian
section is careful about time ordering and proves a true SPD equality criterion,
so it avoids `claude-gabriel/`'s overclaim. Its remaining blocker is that it still does not
give the requested explicit closed-form noncommuting \(T_t\) or the structural
commuting characterization, which keeps it below `codex-gabriel/`.

`hermes-jeremie/` ranks just below `openclaw-jeremie/` and above `claude-gabriel/`. It has a clean
professional wrapper, PyTorch-native reusable code, locked dependencies, CI,
source LaTeX, prebuilt PDF, generated figures, and a test suite that passed
locally. Mathematically it is also safer than `claude-gabriel/`: it restricts its theorem
to the commuting case and treats the noncommuting flow as time ordered rather
than pretending to have a full proof. Its weaknesses are concrete: notebooks are
generated but unexecuted, the OT comparison is a greedy balanced visualization
rather than a certified solver, and the Gaussian section still lacks the
explicit general \(T_t\) and the structural iff criterion. Those issues keep it
comfortably below `openclaw-jeremie/` and the top two, but it is a strong submission.

`codex-gabriel/` essentially fulfills the assignment and remains the best
compact baseline. It correctly implements the conditional velocity, gives the
requested numerical and visual comparisons, exports figures from notebooks into
the paper workflow, proves the correct Gaussian theorem using the general
closed-form \(T_t\), and includes a lightweight mathematical test suite. The
remaining improvements are mostly polish: clarify the VP convention, improve
float placement, add more environment pinning, and possibly expand the
literature review.

`emmanuel/` now edges out `codex-gabriel/` as the strongest full submission. It has the
best paper, the broadest reproducibility wrapper, passing tests, executed
notebooks, stronger semi-discrete OT, and the clearest Gaussian endpoint theorem
among all projects. Its caveats are real but not fatal: the main numerical code
is NumPy/SciPy rather than PyTorch-native, the full theorem is not Lean-proved,
and a stale wiki page contradicts the final schedule-independence result. Those
issues lower its code-realization score slightly, but not enough to outweigh
its mathematical and presentation strengths.

Final ranking:

1. `emmanuel/` — best complete research artifact, strongest theorem exposition.
2. `codex-gabriel/` — best compact reproducible implementation and cleanest
   PyTorch-centered baseline.
3. `openclaw-jeremie/` — strongest upper-mid submission, excellent repo and honest
   time-ordered Gaussian treatment, but missing explicit general \(T_t\).
4. `hermes-jeremie/` — strong PyTorch repo with passing tests and cautious Gaussian
   theorem, but unexecuted notebooks and missing explicit general \(T_t\).
5. `claude-gabriel/` — strong notebooks and paper shell, but Gaussian theorem overclaim.
6. `codex-kimia/` — compact source-backed submission, but only commuting
   Gaussian theorem.
7. `codex-clement/` — useful PDF/code sketch, but weak packaging and missing
   general \(T_t\).
8. `antigravity-antoine/` — executed PyTorch notebooks and source PDF, but thin
   reproducibility and no closed-form Gaussian \(T_t\).
9. `antigravity-olivier/` — partial visual/mathematical draft with major compliance and
   proof issues.

The best remediation path is to use `emmanuel/` or `codex-gabriel/` as the final base:
choose `emmanuel/` if the priority is the strongest paper/theorem and polished
research artifact, or `codex-gabriel/` if the priority is a leaner PyTorch-first
implementation. Borrow selected Dirac visualization, CI/test structure, and
finite-assignment ideas from `openclaw-jeremie/`, `hermes-jeremie/`, and `claude-gabriel/`, reuse
`codex-kimia/` or `codex-clement/` material only after importing the exact
Gaussian endpoint theorem, and avoid importing `antigravity-antoine/` or
`antigravity-olivier/` material unless each formula and OT claim is rechecked.
