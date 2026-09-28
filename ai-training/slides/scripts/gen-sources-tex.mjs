// Emit a LaTeX source table from ../../references.md, alongside the JSON one Slidev uses.
// Citation keys are never hand-typed in a deck; they resolve against this output, and the
// frame check refuses any key that is not tagged [V]. Same discipline as the Slidev path,
// moved to LaTeX because the deck moved.
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs'
import { dirname, resolve } from 'node:path'
import { fileURLToPath } from 'node:url'

const here = dirname(fileURLToPath(import.meta.url))
const refs = resolve(here, '../../references.md')
const out = resolve(here, '../beamer/uh-sources.tex')

const TAG = /\[(V|P|U|X)\]/
const MARK = /\{#([A-Za-z0-9_-]+)\s*\|([^}]*)\}/

// LaTeX specials that appear in real author lists and venue strings.
const tex = s => (s || '')
  .replace(/\\/g, '\\textbackslash{}')
  .replace(/([&%$#_{}])/g, '\\$1')
  .replace(/~/g, '\\textasciitilde{}')
  .replace(/\^/g, '\\textasciicircum{}')
  .replace(/—/g, '---').replace(/–/g, '--')
  .replace(/[“”]/g, "''").replace(/[‘’]/g, "'")
  .replace(/…/g, '\\ldots{}')

const lines = ['% Generated from references.md by gen-sources-tex.mjs. Do not edit by hand.']
let n = 0
for (const line of readFileSync(refs, 'utf8').split('\n')) {
  const m = line.match(MARK)
  if (!m) continue
  const [key, author, year, venue, id, kind, coi] = [m[1], ...m[2].split('|').map(s => s.trim())]
  const tag = (line.match(TAG) || [])[1]
  if (!tag) {
    console.error(`gen-sources-tex: FAIL — {#${key}} has no [V]/[P]/[U]/[X] tag on its line`)
    process.exit(1)
  }
  const idPart = (id && id !== '-') ? `, ${tex(id)}` : ''
  const body = `${tex(author)}, ${tex(year)}. \\emph{${tex(venue)}}${idPart}.`
  const flags = [kind === 'testimony' ? 'testimony' : '', coi === 'coi' ? 'coi' : ''].filter(Boolean).join(',')
  lines.push(`\\uhdefsource{${key}}{${tag}}{${body}}{${flags}}`)
  n++
}
mkdirSync(dirname(out), { recursive: true })
writeFileSync(out, lines.join('\n') + '\n')
console.log(`gen-sources-tex: ${n} keyed source(s) -> beamer/uh-sources.tex`)
