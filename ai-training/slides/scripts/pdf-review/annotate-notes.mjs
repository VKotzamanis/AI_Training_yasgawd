// Writes each slide's presenter note into its PDF page as a sticky note authored "deck-map".
// The author tag is what lets the extraction step tell my notes from the reviewer's comments.
import { readdirSync, readFileSync, writeFileSync, unlinkSync } from 'node:fs'
import { execFileSync } from 'node:child_process'
import { dirname, resolve, join } from 'node:path'
import { fileURLToPath } from 'node:url'
import { parseSync } from '@slidev/parser/core'

const here = dirname(fileURLToPath(import.meta.url))
const slides = resolve(here, '../..')
const decks = readdirSync(slides).filter(f => /^\d\d-.*\.md$/.test(f)).sort()
const NOTE = /<!--\s*([\s\S]*?)-->\s*$/

let total = 0
for (const deck of decks) {
  const path = join(slides, deck)
  const parsed = parseSync(readFileSync(path, 'utf-8'), path)
  const pdf = join(slides, 'exports', deck.replace(/\.md$/, '.pdf'))

  const items = []
  parsed.slides.forEach((s, i) => {
    const m = (s.raw || s.content || '').match(NOTE)
    if (m) items.push({ page: i, text: m[1].trim() })
  })
  if (!items.length) { console.log(`skip     ${deck} — no notes found`); continue }

  const js = join(here, `.tmp-annot-${deck}.js`)
  writeFileSync(js, `
var doc = Document.openDocument(${JSON.stringify(pdf)})
var items = ${JSON.stringify(items)}
for (var i = 0; i < items.length; i++) {
  var page = doc.loadPage(items[i].page)
  var a = page.createAnnotation("Text")
  a.setRect([700, 380, 726, 406])   // top-right; page is 735 x 414
  a.setContents(items[i].text)
  a.setAuthor("deck-map")
  a.update()
}
doc.save(${JSON.stringify(pdf)}, "incremental")
`)
  try {
    execFileSync('mutool', ['run', js], { stdio: 'pipe' })
    console.log(`annotated ${deck.padEnd(24)} ${String(items.length).padStart(2)} notes`)
    total += items.length
  } catch (e) {
    console.error(`FAILED   ${deck}: ${e.message.split('\n')[0]}`)
  } finally { unlinkSync(js) }
}
console.log(`\ntotal annotations written: ${total}`)
