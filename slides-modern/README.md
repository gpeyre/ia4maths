# IA4Maths Slidev Decks

Modern Slidev versions of the French and English IA4Maths decks.

These decks replace the Beamer source with editable Markdown, a shared visual
system, reusable Vue components, browser-rendered interactive slides, and PDF
exports.

## Open The Slides

| Language | Interactive dev server | Static build | PDF |
| --- | --- | --- | --- |
| English | [localhost:3030](http://localhost:3030/) | [dist/en/index.html](dist/en/index.html) | [dist/ia4maths_en.pdf](dist/ia4maths_en.pdf) |
| French | [localhost:3031](http://localhost:3031/) | [dist/fr/index.html](dist/fr/index.html) | [dist/ia4maths_fr.pdf](dist/ia4maths_fr.pdf) |

The `localhost` links work while the corresponding Slidev dev server is
running. The `dist/` links work after `npm run build` and `npm run export:*`.

## Quick Start

```bash
npm install
npm run dev:en
npm run dev:fr
```

Use the keyboard arrows to navigate the interactive slides.

## Build And Export

```bash
npm run build
npm run export:en
npm run export:fr
```

Outputs:

- Interactive HTML: `dist/en` and `dist/fr`
- PDF decks: `dist/ia4maths_en.pdf` and `dist/ia4maths_fr.pdf`

## Source Layout

| Path | Purpose |
| --- | --- |
| `slides.en.md` | English deck content |
| `slides.fr.md` | French deck content |
| `style.css` | Shared visual design system |
| `components/Roadmap.vue` | Reusable roadmap slide component |
| `global-bottom.vue` | Footer and progress rail |
| `assets/` | Images, PDFs, and generated visual assets |
| `scripts/qa-screenshots.mjs` | Browser screenshot QA helper |

The original LaTeX decks remain in `../slides/en` and `../slides/fr`.
