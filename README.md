# AI for Theory: Pedagogical Slide Repository

This repository contains teaching and outreach material for a presentation on
AI for mathematics, with a focus on LLMs, research-level mathematical
reasoning, formalization, agentic workflows and community impact.

The repository is meant to be reusable: it should be easy to rebuild the slides,
inspect the sources behind the claims, regenerate numerical figures and extend
the deck for future talks.

Public GitHub repository: [gpeyre/ia4maths](https://github.com/gpeyre/ia4maths).

## Slides

Recommended public version, once GitHub Pages is enabled for this repository:

- [Slide landing page](https://gpeyre.github.io/ia4maths/)
- [Interactive English deck](https://gpeyre.github.io/ia4maths/en/)
- [Interactive French deck](https://gpeyre.github.io/ia4maths/fr/)
- [English PDF](https://gpeyre.github.io/ia4maths/ia4maths_en.pdf)
- [French PDF](https://gpeyre.github.io/ia4maths/ia4maths_fr.pdf)

GitHub does not render HTML files from the repository file browser. To make the
interactive decks clickable for visitors, enable GitHub Pages with:
`Settings -> Pages -> Deploy from a branch -> main /docs`.

Modern Slidev sources and public-build scripts live in
[`slides-modern/`](slides-modern/).

Legacy ready-to-read PDFs:

- [French slides](slides/fr/ia4maths_fr.pdf): *IA pour la théorie*.
- [English slides](slides/en/ia4maths_en.pdf): *AI for Theory*.

Editable Beamer sources:

- [French source](slides/fr/ia4maths_fr.tex)
- [English source](slides/en/ia4maths_en.tex)
- [Resource index](slides/ressources.md)

Quick local snippet:

```bash
# read the current decks
open slides/fr/ia4maths_fr.pdf
open slides/en/ia4maths_en.pdf

# rebuild one version
cd slides/fr
pdflatex -interaction=nonstopmode -halt-on-error ia4maths_fr.tex
```

## Repository Layout

```text
slides/
  fr/                    French Beamer deck
  en/                    English Beamer deck
python/
  unit_distance_constructions.py
  unit_distance_constructions.ipynb
ressources/
  first-proof-summary.md
  agentic-benchs/        CSD benchmark prompt, submissions and audit material
  *.pdf, *.pptx          external source documents kept for provenance
agent.md                detailed style and editing guide for future agents
tmp/                    scratch renders and temporary QA artifacts
```

The slide decks are intentionally self-contained: each language folder has its
own `assets/` and `assets/generated/` directories. Shared numerical logic lives
in `python/`, while source documents and benchmark material live in
`ressources/`.

## Communication Goal

The presentation is designed for a mathematically mature audience. By the end,
the audience should understand that AI is no longer only a tool for exposition
or coding: it is becoming part of the research workflow for mathematical
reasoning, proof search, formalization, evaluation and community organization.

The current narrative arc is:

1. LLMs and mathematics: why math became a strategic benchmark for reasoning.
2. AI for mathematical research: olympiads, research-level proofs, formal Lean
   projects and scientific discovery.
3. Experience reports: personal and group experiments with agentic workflows.
4. Community impact: reviewing, teaching, training, sovereignty and collective
   actions.

## Building The Slides

The decks are Beamer sources. Build from the corresponding language directory:

```bash
cd slides/fr
pdflatex -interaction=nonstopmode -halt-on-error ia4maths_fr.tex
pdflatex -interaction=nonstopmode -halt-on-error ia4maths_fr.tex
```

```bash
cd slides/en
pdflatex -interaction=nonstopmode -halt-on-error ia4maths_en.tex
pdflatex -interaction=nonstopmode -halt-on-error ia4maths_en.tex
```

The expected outputs are:

- `slides/fr/ia4maths_fr.pdf`
- `slides/en/ia4maths_en.pdf`

PowerPoint export is not part of the normal workflow. Do not generate `.pptx`
files unless explicitly requested.

## Regenerating Numerical Figures

The unit-distance slide uses a reproducible numerical illustration generated
from:

```bash
python3 python/unit_distance_constructions.py
```

The script requires `numpy` and `matplotlib`. In this local workspace, the
figure was regenerated with the `py314` conda environment; any Python
environment with those dependencies should work.

By default, the script writes:

- `slides/fr/assets/generated/unit_distance_series.{png,pdf}` with French
  labels.
- `slides/en/assets/generated/unit_distance_series.{png,pdf}` with English
  labels.

The companion notebook `python/unit_distance_constructions.ipynb` is kept for
interactive exploration, but the script is the clean reproducible entry point.

## Source Material

Most external and local references are kept in `ressources/`. In particular:

- `ressources/first-proof-summary.md` summarizes the First Proof material and
  references.
- `ressources/agentic-benchs/` contains the CSD group benchmark prompt,
  report, submissions and the `codex-gabriel/` scientific artifact.
- PDFs and HTML snapshots under `slides/<lang>/assets/` are slide-facing assets
  or direct visual sources.

When adding claims about recent systems, benchmark results or model behavior,
prefer primary sources and record compact citations directly in the Beamer
source.

## Visual And Writing Style

The deck uses a consistent color grammar:

- Blue: `Problème` boxes and problem/framing labels.
- Teal: `Résultats` boxes and validated evidence.
- Amber: `Takeaway` boxes, caveats and governance.
- Gray variants: all other box-like containers, including examples, prompts,
  actions, screenshots, metadata and implementation scale.

Other palette colors can remain as small text accents, but non
`Problème`/`Résultats`/`Takeaway` boxes should keep a neutral light-gray
background. When a slide contains several neutral boxes, use distinct soft gray
variants (`softGrayA`--`softGrayE`, or the role-specific environments) so the
regions are visually separable without becoming colorful.

Slides should stay compact and research-facing. Prefer the pattern:

```tex
\item \textbf{Key message}: short explanation.
```

Use the existing Beamer environments (`problembox`, `resultbox`,
`takeawaybox`, `examplebox`, `actionbox`, `neutralbox`) rather than local ad hoc
styling.

## Quality Checks

After editing a deck, inspect LaTeX warnings:

```bash
rg -n "Overfull|Underfull|Warning|Rerun" slides/fr/ia4maths_fr.log
rg -n "Overfull|Underfull|Warning|Rerun" slides/en/ia4maths_en.log
```

Render a contact sheet for visual QA:

```bash
pdftoppm -png -r 120 slides/fr/ia4maths_fr.pdf /private/tmp/ia4maths-fr
magick montage /private/tmp/ia4maths-fr-*.png -tile 5x4 -geometry 300x169+6+8 /private/tmp/ia4maths-fr-contact.png
```

Repeat for `slides/en/`. Check for overflow, unreadable screenshots, source
lines colliding with footers, inconsistent colors and box overlap.

Also verify that no PowerPoint file was generated accidentally:

```bash
find slides -maxdepth 3 -name '*.pptx' -print
```

## Extending The Repository

Use `agent.md` as the detailed contribution guide. When adding a new slide:

- place slide-specific visual assets under `slides/<lang>/assets/generated/`;
- place reusable numerics under `python/`;
- place source documents, benchmarks and raw external material under
  `ressources/`;
- compile both decks when the change affects shared structure or translated
  content;
- keep the French and English versions parallel unless the talk context
  requires a deliberate difference.
