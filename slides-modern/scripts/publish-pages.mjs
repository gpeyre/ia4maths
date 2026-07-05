import { cpSync, mkdirSync, rmSync, writeFileSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const here = dirname(fileURLToPath(import.meta.url))
const slideRoot = resolve(here, '..')
const repoRoot = resolve(slideRoot, '..')
const dist = resolve(slideRoot, 'dist')
const docs = resolve(repoRoot, 'docs')

function copyFresh(from, to) {
  rmSync(to, { recursive: true, force: true })
  mkdirSync(dirname(to), { recursive: true })
  cpSync(from, to, { recursive: true })
}

mkdirSync(docs, { recursive: true })
writeFileSync(resolve(docs, '.nojekyll'), '')

copyFresh(resolve(dist, 'en'), resolve(docs, 'en'))
copyFresh(resolve(dist, 'fr'), resolve(docs, 'fr'))
cpSync(resolve(dist, 'ia4maths_en.pdf'), resolve(docs, 'ia4maths_en.pdf'))
cpSync(resolve(dist, 'ia4maths_fr.pdf'), resolve(docs, 'ia4maths_fr.pdf'))

writeFileSync(resolve(docs, 'index.html'), `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>IA4Maths Slides</title>
  <style>
    :root {
      color: #101828;
      background: #f5f9fb;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }

    body {
      min-height: 100vh;
      margin: 0;
      display: grid;
      place-items: center;
      background: linear-gradient(135deg, #fbfcfe 0%, #f1f7f8 100%);
    }

    main {
      width: min(880px, calc(100vw - 48px));
      display: grid;
      gap: 28px;
    }

    h1 {
      margin: 0;
      font-size: clamp(2.4rem, 6vw, 5rem);
      line-height: 0.95;
      letter-spacing: 0;
    }

    p {
      max-width: 620px;
      margin: 0;
      color: #667085;
      font-size: 1.05rem;
      line-height: 1.55;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 16px;
    }

    a {
      color: inherit;
      text-decoration: none;
    }

    .card {
      display: grid;
      gap: 14px;
      min-height: 150px;
      padding: 24px;
      border: 1px solid #d8dee8;
      border-left: 5px solid #255f92;
      border-radius: 8px;
      background: #fff;
    }

    .card.fr {
      border-left-color: #1f8a83;
    }

    .card strong {
      font-size: 1.25rem;
    }

    .links {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }

    .links a {
      padding: 9px 12px;
      border-radius: 999px;
      background: #eef4f8;
      color: #255f92;
      font-size: 0.9rem;
      font-weight: 700;
    }

    @media (max-width: 720px) {
      .grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <main>
    <header>
      <h1>IA4Maths Slides</h1>
      <p>Modern interactive Slidev decks and PDF exports for the AI for mathematics presentation.</p>
    </header>
    <section class="grid" aria-label="Slide decks">
      <article class="card">
        <strong>AI for Theory</strong>
        <span>English deck</span>
        <nav class="links">
          <a href="./en/">Interactive</a>
          <a href="./ia4maths_en.pdf">PDF</a>
        </nav>
      </article>
      <article class="card fr">
        <strong>IA pour la theorie</strong>
        <span>Version francaise</span>
        <nav class="links">
          <a href="./fr/">Interactif</a>
          <a href="./ia4maths_fr.pdf">PDF</a>
        </nav>
      </article>
    </section>
  </main>
</body>
</html>
`)

console.log(`Published GitHub Pages assets to ${docs}`)
