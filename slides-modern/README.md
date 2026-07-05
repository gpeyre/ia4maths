# IA4Maths Slidev Decks

Modern Slidev versions of the French and English IA4Maths decks.

These decks replace the Beamer source with editable Markdown, a shared visual
system, reusable Vue components, browser-rendered interactive slides, and PDF
exports.

## Open The Slides

| Language | Public interactive deck | Public PDF | Interactive dev server | Static preview |
| --- | --- | --- | --- | --- |
| English | [gpeyre.github.io/ia4maths/en](https://gpeyre.github.io/ia4maths/en/) | [ia4maths_en.pdf](https://gpeyre.github.io/ia4maths/ia4maths_en.pdf) | [localhost:3030](http://localhost:3030/) | [localhost:4173](http://localhost:4173/) |
| French | [gpeyre.github.io/ia4maths/fr](https://gpeyre.github.io/ia4maths/fr/) | [ia4maths_fr.pdf](https://gpeyre.github.io/ia4maths/ia4maths_fr.pdf) | [localhost:3031](http://localhost:3031/) | [localhost:4174](http://localhost:4174/) |

The public links work after GitHub Pages is enabled on `main /docs`. The
`localhost` links work while the corresponding Slidev dev or preview server is
running.

The static HTML builds in `dist/en` and `dist/fr` are browser apps. Serve them
over HTTP with the preview commands below; opening `dist/*/index.html` directly
as a `file://` URL can show a blank page in Chromium-based browsers because ES
module assets are blocked from local files.

GitHub also displays repository HTML files as source code rather than rendering
them. The reliable public workflow is to publish the generated `docs/` folder
with GitHub Pages.

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
npm run preview:en
npm run preview:fr
npm run export:en
npm run export:fr
npm run publish:pages
```

Outputs:

- Interactive HTML: `dist/en` and `dist/fr`
- GitHub Pages folder: `../docs`
- Local static preview: http://localhost:4173/ and http://localhost:4174/
- PDF decks: `dist/ia4maths_en.pdf` and `dist/ia4maths_fr.pdf`

For a full public rebuild:

```bash
npm run build:pages
```

Then push the repository and set GitHub Pages to
`Settings -> Pages -> Deploy from a branch -> main /docs`.

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
