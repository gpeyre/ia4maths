# Agent Guide For This Slide Deck

This repository contains a Beamer presentation about AI for mathematical theory.
The decks live in `slides/fr/` and `slides/en/`; reference material lives in
`ressources/`; numerical experiments and notebooks live in `python/`. The goal
is not only to add facts, but to preserve a clear, high-quality visual and
narrative style.

## Core Principles

- Work from the Beamer source, not from a generated PowerPoint file.
- Do not generate a `.pptx` unless the user explicitly asks for one. The current
  workflow is PDF-oriented.
- Keep the deck dense enough for a research audience, but not text-heavy.
- Every slide should have one job: context, evidence, example, implication, or
  action.
- Favor precise, compact, audience-facing copy over explanatory prose.
- Prefer high-signal examples, tables, code snippets, and real paper/page
  snapshots over decorative visuals.
- Always verify by compiling and visually inspecting rendered slides.

## Project Layout

- French source: `slides/fr/ia4maths_fr.tex`
- English source: `slides/en/ia4maths_en.tex`
- Main outputs: `slides/fr/ia4maths_fr.pdf` and
  `slides/en/ia4maths_en.pdf`
- Assets: `slides/<lang>/assets/` and `slides/<lang>/assets/generated/`
- Numerics: `python/`, especially `python/unit_distance_constructions.py`
- Supporting documents and benchmark material: `ressources/`
- Temporary renders can go in `/private/tmp` or `tmp/`, but do not make them
  part of the deck unless they are intentional assets.

## Visual Language

The deck uses a soft, consistent color grammar:

- Blue: `Problème` boxes and problem/framing labels.
- Teal: `Résultats` boxes and validated evidence.
- Amber: `Takeaway` boxes, caveats and governance.
- Gray variants: every other box-like container, including examples, prompts,
  actions, implementation scale, screenshots and metadata.

Use violet/green/etc. only as light text or accent colors when useful; do not
give non-`Problème`/`Résultats`/`Takeaway` boxes their own colored background.
If a slide has several neutral boxes, distinguish them with soft gray variants
(`softGrayA`--`softGrayE` or the role-specific environments), not with new
semantic colors.

Use the existing Beamer macros rather than inventing local styling:

- `problembox` + `\problemlabel` for problem/framing.
- `resultbox` + `\resultlabel` for results/evidence.
- `takeawaybox` + `\takeawaylabel` for conclusions/risks.
- `examplebox`, `actionbox`, `claimbox`, `proofbox` and `riskbox` for
  non-axis material; these should render as neutral light-gray variants.
- `neutralbox` and `neutralboxalt` for scale, metadata, or evaluation protocol.

Do not reintroduce heavy drop shadows. The current style is flat, rounded,
subtle, and calmer than dashboard-like UI.

Inside gray/neutral boxes, keep section titles in bold black, not colored.
The box tint already carries the neutral grouping; reserve colored title text
for the canonical `Problème`, `Résultats`, and `Takeaway` labels or for small
inline semantic accents.

For research/evidence slides, default to three explicit axes when space allows:

- `Problème`: what is being tested, formalized, evaluated, or at stake.
- `Résultats`: observed progress, benchmark numbers, artifacts, or evidence.
- `Takeaway`: interpretation, caveat, cost, governance issue, or next implication.

Prefer three substantial regions over many small boxes. If a slide cannot fit
all three axes, keep the axis labels visible in the most important regions and
avoid mixing takeaway content into the results box.

## Writing Style

Use compact slide copy. Bullets should usually follow:

```tex
\item \textbf{Key message} : short explanation.
```

For French slides, the visible key message is in French, but the structure
should stay the same. Avoid full prose sentences inside bullets when a nominal
phrase works better.

Good:

```tex
\item \textbf{Budget} : performance \(\simeq\) tokens.
\item \textbf{Expertise} : guidage maths indispensable ; hors domaine impossible.
```

Less good:

```tex
\item The model performs better when it is given a larger token budget.
```

Keep titles short and stable. Internal box labels should use the shared grammar
whenever possible: problem, results, takeaway.

After rendering, actively hunt for orphan line breaks: a second line with only
one or two trailing words, especially after a colon or at the end of a bullet.
Fix these in this order:

- Shorten the sentence while preserving the message.
- Move secondary detail to another bullet or remove it if it is not needed.
- If the wording must stay, add an explicit balanced line break and align the
  continuation so both lines read intentionally.
- For `\textbf{label}: message` bullets, use the deck macros `\keyitem`,
  `\keyline`, and `\labelline`. They create hanging indents so wrapped lines
  align after the bold label rather than falling back under the bullet.

Check this separately in French and English; translations often wrap
differently. Do not leave a box title, takeaway, or compact bullet ending with a
single isolated word unless it is a deliberate label or mathematical symbol.

## Slide Composition

- Use two-column layouts for most evidence slides.
- Use a full-width top box for the problem/framing when the slide needs it.
- Put results and takeaways side by side when both are central.
- Keep code snippets short and visually recognizable, not exhaustive.
- Crop screenshots aggressively so the audience sees the relevant object.
- If a figure is small, show a readable subset instead of a full unreadable page.
- Do not add visible instructional text such as "how to use this slide".
- Avoid nested cards or many floating elements; use 2 to 4 coherent regions.
- Center the whole visual group vertically when the slide has spare height,
  especially on box-based slides. Avoid `\begin{frame}[t]` unless the slide is
  genuinely dense or a deliberate top-aligned screenshot layout.

## Evidence And Sources

- Cite sources at the bottom with `\source{...}` or a small source line.
- Prefer primary sources: arXiv, official project pages, GitHub repos, reports,
  local documents in `ressources/`.
- If using a web claim that may have changed, verify it before editing.
- Keep citations compact. A slide should not become a bibliography.
- For claims involving dates, scores, model names, or recent benchmarks, be
  concrete and use exact dates when available.

## Assets And Figures

- Reuse existing assets in `slides/<lang>/assets/generated/` when they already
  fit.
- When adding an asset, make sure it is readable at slide scale.
- Prefer PDF/PNG assets that compile cleanly with `pdflatex`.
- For scientific figures, favor real simulations, paper figures, code snippets,
  or notebook outputs over generic illustrations.
- If generating a figure programmatically, save the final asset under
- For numerical figures, prefer reproducible scripts under `python/`, then save
  final deck assets under `slides/<lang>/assets/generated/`.

## Build And QA Workflow

From the repository root:

```bash
cd slides/fr
pdflatex -interaction=nonstopmode -halt-on-error ia4maths_fr.tex
```

Use `ia4maths_en.tex` from `slides/en/` for the English deck. The two decks are
parallel Beamer sources, not generated from a single translation pipeline.

Then inspect warnings:

```bash
rg -n "Overfull|Underfull|Warning|Rerun" slides/fr/ia4maths_fr.log
```

The known harmless warning is the `hyperref` PDF string warning around the
title. Do not ignore `Overfull` or `Underfull` warnings that affect layout.

Render slides for visual QA:

```bash
pdftoppm -png -r 120 slides/fr/ia4maths_fr.pdf /private/tmp/ia4maths-check
magick montage /private/tmp/ia4maths-check-*.png -tile 5x3 -geometry 300x169+6+8 /private/tmp/ia4maths-contact.png
```

Inspect the contact sheet and zoom into dense slides. Check for:

- Text overflow or clipping.
- Figure unreadability.
- Misaligned columns.
- Inconsistent box colors.
- Too much text in one area.
- Source lines colliding with footers.
- Reintroduced shadows or inconsistent local styling.

Also verify that no PowerPoint was generated unintentionally:

```bash
find slides -maxdepth 3 -name '*.pptx' -print
```

## Editing Rules

- Keep edits scoped to the requested slides and shared style macros.
- Use existing colors and box environments instead of ad hoc formatting.
- Do not rename assets without updating all references.
- Do not delete auxiliary sources unless explicitly asked.
- Do not change the deck title, date, author, footer, or global theme unless the
  user asks.
- If a change makes a slide too dense, shorten the text before reducing fonts.

## Current Design Details To Preserve

The preamble defines the active palette and box macros. Preserve the role of:

- `aiBlue` / `softBlue`: `Problème`.
- `aiTeal` / `softTeal`: `Résultats`.
- `aiAmber` / `softAmber`: `Takeaway`.
- `softGrayA`--`softGrayE`: neutral box variants; use more than one when a
  slide contains several non-axis boxes.
- `aiViolet`, `aiGreen`, `aiRed`: optional accents, not generic box fills.

The deck uses `Madrid` + `dolphin`, 16:9 aspect ratio, and a light blue frame
title bar. Frame titles should be bold. Keep that visual identity unless the
user requests a redesign.

## Common Pitfalls

- Adding paragraph-like bullets. Use compact key-message bullets.
- Using too many colors on one slide. The color should encode content type.
- Making every slide a grid of boxes. Use boxes only when they clarify.
- Showing full pages when a crop or subset is needed.
- Leaving image centering unscoped inside Beamer boxes. Put `\par` after the
  box title, then use local centering such as `{\centering ...\par}` so the
  image does not get composed in the same paragraph as the heading.
- Forgetting to compile after a text change.
- Trusting LaTeX success without checking visual output.
- Creating a PPTX despite the user preference against it.
- Letting source lines or navigation symbols overlap content.

## High-Quality Finish Checklist

Before handing back:

- PDF compiles successfully.
- No relevant overfull/underfull layout warnings remain.
- Full contact sheet looks visually coherent.
- Dense slides have been inspected individually.
- New claims have sources.
- Bullet style is compact and consistent.
- Color grammar is still meaningful.
- No `.pptx` file was generated.
