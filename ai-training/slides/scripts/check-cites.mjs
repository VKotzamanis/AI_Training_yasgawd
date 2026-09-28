// Build check. Fails if a slide cites an unknown key, or a key tagged [U].
// CLAUDE.md: "The build check fails if a key tagged [U] appears in a slide — do not disable it."
import { readFileSync, readdirSync, existsSync } from 'node:fs'
import { parseSync } from '@slidev/parser/core'
import { dirname, resolve, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const here = dirname(fileURLToPath(import.meta.url))
const slidesDir = process.argv[2] ? resolve(process.cwd(), process.argv[2]) : resolve(here, '..')
const expectFail = process.argv.includes('--expect-fail')
// sources.json is always project-root, independent of which directory is being scanned
const sources = JSON.parse(readFileSync(resolve(here, '../sources.json'), 'utf8'))

const decks = readdirSync(slidesDir).filter(f => /^\d\d-.*\.md$/.test(f))
const KEY = /<Cite\s+[^>]*k="([^"]+)"/g

let unknown = 0, unverified = 0, cited = 0
const uncited = []
for (const deck of decks) {
  const text = readFileSync(join(slidesDir, deck), 'utf8')
  if (!KEY.test(text)) uncited.push(deck)
  KEY.lastIndex = 0
  for (const m of text.matchAll(KEY)) {
    // a Cite may carry several comma-separated keys; every one is checked
    for (const key of m[1].split(',').map(x => x.trim()).filter(Boolean)) {
      cited++
      const src = sources[key]
      if (!src) { console.error(`  ${deck}: unknown citation key "${key}"`); unknown++; continue }
      // CLAUDE.md hard rule 1: "Only [V] may appear in slide content."
      // [P] is partially verified and is NOT permitted either.
      if (src.tag !== 'V') {
        console.error(`  ${deck}: key "${key}" is tagged [${src.tag}] — only [V] may appear on a slide`)
        unverified++
      }
    }
  }
}

console.log(`check:cites — ${decks.length} deck(s), ${cited} citation(s)`)
if (uncited.length) {
  // A deck with no <Cite> passes every other check trivially. Both peer reviews found
  // unverified claims sitting exactly there, so absence of citations is now reported.
  console.warn(`check:cites — ${uncited.length} deck(s) cite nothing; claims in them are unchecked:`)
  for (const d of uncited) console.warn(`    ${d}`)
}
// Footer coverage. Ruled 2026-08-20: every slide carries a footer, no exceptions.
// Opt-in per deck via slides/.footer-check, one filename per line, so a deck joins the
// rule when it is rebuilt rather than eighteen drafts failing the build today.
let missingFooters = 0
const optInPath = resolve(slidesDir, '.footer-check')
if (existsSync(optInPath)) {
  const optIn = readFileSync(optInPath, 'utf8').split('\n').map(s => s.trim()).filter(Boolean)
  for (const deck of optIn) {
    const file = join(slidesDir, deck)
    if (!existsSync(file)) { console.error(`  .footer-check lists "${deck}", which does not exist`); missingFooters++; continue }
    const text = readFileSync(file, 'utf8')
    // Slidev's own parser, not a --- count: head matter and per-slide front matter both
    // use separators, so counting them gives the wrong slide boundaries.
    const lines = text.split('\n')
    const slides = parseSync(text, file).slides
    for (const s of slides) {
      const body = lines.slice(s.contentStart, s.end).join('\n')
      if (!/<Cite\s/.test(body)) {
        console.error(`  ${deck}: slide ${s.index + 1} carries no footer`)
        missingFooters++
      }
    }
    console.log(`check:cites — ${deck}: ${slides.length} slide(s) checked for a footer`)
  }
}

const failed = unknown || unverified || missingFooters
if (expectFail) {
  // Self-test: a build check nobody tests is a build check that silently stops working.
  if (!failed) { console.error('selftest FAILED — fixture did not trip the check'); process.exit(1) }
  console.log(`selftest PASSED — fixture tripped the check (${unknown} unknown, ${unverified} unverified)`)
  process.exit(0)
}
if (failed) {
  console.error(`check:cites FAILED — ${unknown} unknown, ${unverified} unverified, ${missingFooters} slide(s) without a footer`)
  process.exit(1)
}
console.log('check:cites PASSED')
