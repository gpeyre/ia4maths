import { chromium } from "playwright-chromium"
import { mkdir } from "node:fs/promises"

const decks = [
  { lang: "en", url: "http://localhost:3030/" },
  { lang: "fr", url: "http://localhost:3031/" },
]

const checkpoints = new Set([1, 2, 6, 9, 10, 16, 21])

await mkdir("qa", { recursive: true })

const browser = await chromium.launch()
try {
  for (const deck of decks) {
    const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 })
    await page.goto(deck.url, { waitUntil: "networkidle" })
    await page.waitForTimeout(1200)

    for (let slide = 1; slide <= 21; slide++) {
      if (checkpoints.has(slide)) {
        await page.screenshot({
          path: `qa/${deck.lang}-${String(slide).padStart(2, "0")}.png`,
          fullPage: false,
        })
      }
      if (slide < 21) {
        await page.keyboard.press("ArrowRight")
        await page.waitForTimeout(1000)
      }
    }
    await page.close()
  }
} finally {
  await browser.close()
}
