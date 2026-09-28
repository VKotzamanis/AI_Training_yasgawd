// Writes a freshness stamp into every exported PDF: sha256 of the deck markdown + slide count.
// The stamp travels inside the file, so an annotated copy can always be checked against
// the source it was exported from. Run after any export.
import { readdirSync, readFileSync } from 'node:fs'
import { createHash } from 'node:crypto'
import { execFileSync } from 'node:child_process'
import { dirname, resolve, join } from 'node:path'
import { fileURLToPath } from 'node:url'
import { parseSync } from '@slidev/parser/core'

const here = dirname(fileURLToPath(import.meta.url))
const slides = resolve(here, '../..')
const decks = readdirSync(slides).filter(f => /^\d\d-.*\.md$/.test(f)).sort()

for (const deck of decks) {
  const path = join(slides, deck)
  const md = readFileSync(path, 'utf-8')
  const n = parseSync(md, path).slides.length
  const sha = createHash('sha256').update(md).digest('hex').slice(0, 16)
  const pdf = join(slides, 'exports', deck.replace(/\.md$/, '.pdf'))
  const stamp = `slidev-review v1 | ${deck} | slides=${n} | sha256=${sha}`
  try {
    execFileSync('mutool', ['run', join(here, 'stamp.js'), pdf, stamp], { stdio: 'pipe' })
    console.log(`stamped  ${deck.padEnd(24)} slides=${String(n).padEnd(3)} ${sha}`)
  } catch (e) {
    console.error(`FAILED   ${deck}: ${e.message.split('\n')[0]}`)
  }
}
