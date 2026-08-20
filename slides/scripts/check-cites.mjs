// Build check. Fails if a slide cites an unknown key, or a key tagged [U].
// CLAUDE.md: "The build check fails if a key tagged [U] appears in a slide — do not disable it."
import { readFileSync, readdirSync } from 'node:fs'
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
for (const deck of decks) {
  const text = readFileSync(join(slidesDir, deck), 'utf8')
  for (const m of text.matchAll(KEY)) {
    const key = m[1]
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

console.log(`check:cites — ${decks.length} deck(s), ${cited} citation(s)`)
const failed = unknown || unverified
if (expectFail) {
  // Self-test: a build check nobody tests is a build check that silently stops working.
  if (!failed) { console.error('selftest FAILED — fixture did not trip the check'); process.exit(1) }
  console.log(`selftest PASSED — fixture tripped the check (${unknown} unknown, ${unverified} unverified)`)
  process.exit(0)
}
if (failed) {
  console.error(`check:cites FAILED — ${unknown} unknown, ${unverified} unverified`)
  process.exit(1)
}
console.log('check:cites PASSED')
