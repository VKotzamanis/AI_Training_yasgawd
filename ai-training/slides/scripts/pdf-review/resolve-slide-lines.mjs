// Slide index -> markdown line range, using Slidev's own parser.
// Counting '---' by hand is wrong: deck front-matter uses two separators, and any
// slide carrying its own front-matter block uses two more for a single slide.
import { parseSync } from '@slidev/parser/core'
import { readFileSync } from 'fs'

const file = process.argv[2]
const md = readFileSync(file, 'utf-8')
const result = parseSync(md, file)
console.log(JSON.stringify(result.slides.map(s => ({
  slide: s.index + 1,                     // == PDF page number
  content_start_line: s.contentStart + 1, // 1-indexed
  end_line: s.end,
})), null, 0))
