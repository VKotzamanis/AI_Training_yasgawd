// Generate the keyed source list from ../references.md.
// Citation keys are never hand-typed in a slide; they resolve against this output.
// Marker syntax, appended to a reference line in references.md:
//   {#key | Author, A. | Year | Venue | identifier | kind | coi}
//   kind: "paper" | "testimony"   coi: "coi" to require a conflict-of-interest note, else "-"
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const here = dirname(fileURLToPath(import.meta.url))
const refs = resolve(here, '../../references.md')
const out  = resolve(here, '../sources.json')

const TAG = /\[(V|P|U|X)\]/
const MARK = /\{#([A-Za-z0-9_-]+)\s*\|([^}]*)\}/

const sources = {}
let n = 0
for (const line of readFileSync(refs, 'utf8').split('\n')) {
  const m = line.match(MARK)
  if (!m) continue
  const [key, author, year, venue, id, kind, coi] = [m[1], ...m[2].split('|').map(s => s.trim())]
  const tag = (line.match(TAG) || [])[1]
  if (!tag) {
    console.error(`gen-sources: FAIL — {#${key}} has no [V]/[P]/[U]/[X] tag on its line`)
    process.exit(1)
  }
  sources[key] = { author, year, venue, id: id === '-' ? '' : id, kind, coi: coi === 'coi', tag }
  n++
}

mkdirSync(dirname(out), { recursive: true })
writeFileSync(out, JSON.stringify(sources, null, 2) + '\n')
console.log(`gen-sources: ${n} keyed source(s) -> sources.json`)
