# PDF-Annotation Review Workflow — Implementation Plan

**Goal.** Let the course author mark up exported slide PDFs with sticky notes and highlights in any PDF viewer, and let an AI assistant apply those comments to the correct lines of the correct Slidev markdown source, without ever guessing a location or fabricating a citation.

## Architecture

The round trip has four stages, each independently verifiable. **Export+stamp**: `slides/scripts/pdf-review/stamp-all.mjs` runs after every `slidev export` and writes a version stamp (sha256 of the deck's markdown + slide count) into each PDF's `/Info/Keywords` field, so the freshness check travels with the file instead of living in a sidecar that can go missing. **Extract**: `slides/scripts/pdf-review/map_comments.py` reads the annotated PDF back with `mutool show`/`mutool draw`, resolves each annotation's page object reference to a page number, recovers highlighted text by intersecting `/QuadPoints` with `mutool draw -F stext` character boxes, and checks the stamp against the current source hash. **Map**: the same script resolves page number to markdown line range using Slidev's own installed parser (`@slidev/parser`) rather than counting `---` lines by hand, then locates the specific line inside that range by word-overlap against the comment's nearby or highlighted text. **Apply**: the assistant edits the markdown using the Edit tool's own anchor-uniqueness guarantee, re-runs `npm run check:cites`, re-exports, and re-stamps — never touching a line it could not confidently locate.

All four stages were built and verified empirically against `slides/02-formation.md` / `slides/exports/02-formation.pdf` during planning (details in each task). Nothing below is theoretical.

## Global constraints

- No installs. Toolset is `mutool` 1.28.2, `pdftotext`, `pdfinfo`, Python 3.14 stdlib, Node 20+ with the repo's own `slides/node_modules/@slidev/parser`. `pdfannots`, `qpdf`, `pdftk`, `pypdf`, `fitz` are not available and the plan does not depend on them.
- `mutool run` opens documents with `Document.openDocument(path)`, not `new Document(path)` — the latter throws `Document is not callable` in this build. Every script below uses the working form.
- All 19 exported PDFs share `/MediaBox [0 0 735.12 414]` with no `/Rotate` entry (checked directly on every deck's first page object). The coordinate transform in Task 3 depends on this and must be re-verified if a deck is ever exported at a different size.
- Slide N of a deck corresponds to PDF page N (one page per slide, no `--with-clicks`) — confirmed by running the real Slidev parser against all 19 decks and diffing the slide count against `pdfinfo` page counts; every deck matched exactly.
- Hard rule 7 (assert-before-edit, grep-back-after) governs Task 6. Hard rules 1/1a/1b/2 (only `[V]` sources, `TODO(cite)` for anything else, no fabricated citations) govern how "add a source" comments are handled. `npm run check:cites` must pass after every batch of edits.
- CLAUDE.md was updated mid-session (rules 1a and 1b added, clarifying that the `[E1]–[E4]` evidence scale is separate from `[V]/[P]/[U]/[X]`, and that a slide may discuss a non-`[V]` source without citing it if it rests no claim on it). This plan already reflects both.

## Task 1 — Resolve slide index to markdown line range

**File:** `slides/scripts/pdf-review/resolve-slide-lines.mjs`

The `---` separator count is not the slide count: a deck's own head-matter uses two separators, and any slide with its own front-matter block (`---\nlayout: center\n---`) uses two more for one slide. `slides/02-formation.md` has 25 separator lines but only 23 slides. Rather than re-deriving Slidev's parsing rules by regex, this script calls the installed parser directly (`slides/node_modules/@slidev/parser`), which is what Slidev itself uses to cut the deck into slides.

```js
import { parseSync } from '@slidev/parser/core'
import { readFileSync } from 'fs'

const file = process.argv[2]
const md = readFileSync(file, 'utf-8')
const result = parseSync(md, file)
console.log(JSON.stringify(result.slides.map(s => ({
  slide: s.index + 1,            // == PDF page number
  content_start_line: s.contentStart + 1,   // 1-indexed
  end_line: s.end,
}))))
```

Must be invoked with cwd inside `slides/` (or placed under `slides/scripts/`) so Node's module resolution finds `@slidev/parser` in `slides/node_modules`.

**Verification (already run for all 19 decks):**
```
cd slides && for f in [0-9][0-9]-*.md; do
  n=$(node scripts/pdf-review/resolve-slide-lines.mjs "$f" | python3 -c "import json,sys;print(len(json.load(sys.stdin)))")
  p=$(pdfinfo "exports/${f%.md}.pdf" | awk '/^Pages:/{print $2}')
  [ "$n" = "$p" ] && echo "$f OK" || echo "$f MISMATCH $n vs $p"
done
```
Expected: 19 lines of `OK`. Confirmed during planning — all 19 matched (e.g. `02-formation OK`, parser=23, pdf=23).

## Task 2 — Version-stamp exported PDFs

**Files:** `slides/scripts/pdf-review/stamp.js`, `slides/scripts/pdf-review/stamp-all.mjs`

```js
// stamp.js — mutool run stamp.js FILE.pdf "STAMP_STRING"
var doc = Document.openDocument(scriptArgs[0])
doc.setMetaData("info:Keywords", scriptArgs[1])
doc.save(scriptArgs[0], "incremental")
print("stamped " + scriptArgs[0])
```

```js
// stamp-all.mjs — run after every export
import { execFileSync } from 'child_process'
import { createHash } from 'crypto'
import { readFileSync, readdirSync } from 'fs'

for (const f of readdirSync('.').filter(f => /^\d\d-.*\.md$/.test(f))) {
  const deck = f.replace(/\.md$/, '')
  const pdf = `exports/${deck}.pdf`
  const slides = JSON.parse(execFileSync('node', ['scripts/pdf-review/resolve-slide-lines.mjs', f]))
  const hash = createHash('sha256').update(readFileSync(f)).digest('hex')
  const stamp = `pdfreview:v1:sha256=${hash}:slides=${slides.length}`
  execFileSync('mutool', ['run', 'scripts/pdf-review/stamp.js', pdf, stamp])
  const readback = execFileSync('pdfinfo', [pdf]).toString()
  if (!readback.includes(stamp)) throw new Error(`stamp did not persist for ${pdf}`)
  console.log(`${deck}: stamped, grep-back OK`)
}
```

Wire into `slides/package.json`: change `"export": "npm run sources && slidev export"` to `"export": "npm run sources && slidev export && node scripts/pdf-review/stamp-all.mjs"`.

**Verification:** `doc.setMetaData("info:Keywords", ...)` then reopening and `pdfinfo | grep Keywords` was tested directly — the value round-trips byte for byte through an incremental save. Run `cd slides && node scripts/pdf-review/stamp-all.mjs` once now to backfill all 19 existing PDFs (they currently carry no stamp), then re-run `pdfinfo exports/02-formation.pdf | grep Keywords` and confirm the printed hash equals `sha256sum slides/02-formation.md`.

## Task 3 — Extract annotations, resolve pages, recover highlight text

**File:** `slides/scripts/pdf-review/map_comments.py`

Three sub-problems, each confirmed empirically on a live test PDF built from `02-formation.pdf`:

1. **Page resolution.** `mutool show FILE.pdf pages` prints `page N = OBJ 0 R` for every page. An annotation's `/P OBJ 0 R` is looked up in this table. Tested: an annotation created on page-index 1 produced `/P 10 0 R`; the page table showed `page 2 = 10 0 R`.
2. **Highlight text recovery.** `/QuadPoints` are in PDF-native space (origin bottom-left, y increasing upward); `mutool draw -F stext` line and char boxes are in display space (origin top-left, y increasing downward). The transform, confirmed by creating a highlight over a known searched phrase and diffing the raw saved `/QuadPoints` against the phrase's stext bbox: **`y_display = page_height − y_pdf`**, x unchanged, `page_height` read from the `<page height="...">` attribute of the same stext output (not hardcoded). Tested on a single-line highlight ("Pretraining" → recovered exactly), a partial-line highlight ("predict the next token" inside a longer sentence → recovered exactly, not the whole line), and a highlight spanning a wrapped line (recovered both segments, joined).
3. **Comment vs. highlight-without-note.** A `Highlight` annotation's own `/Contents` (if the reviewer typed a note on it) is preferred verbatim; only when absent does the script fall back to the recovered underlying text as the anchor.

```python
#!/usr/bin/env python3
import subprocess, re, sys, json, hashlib, xml.etree.ElementTree as ET
from pathlib import Path

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0: raise RuntimeError(f"{cmd}\n{r.stderr}")
    return r.stdout

def page_object_map(pdf):
    m = {}
    for line in run(["mutool", "show", pdf, "pages"]).splitlines():
        mo = re.match(r"page (\d+) = (\d+) 0 R", line.strip())
        if mo: m[int(mo.group(2))] = int(mo.group(1))
    return m

def annotation_lines(pdf):
    out = run(["mutool", "show", pdf, "grep"])
    return [l for l in out.splitlines() if "/Type/Annot" in l and "/Subtype/Popup" not in l]

def parse_annot(line):
    d = {"obj": int(re.match(r"(\d+) 0 obj", line).group(1))}
    mp = re.search(r"/P (\d+) 0 R", line); d["p_obj"] = int(mp.group(1)) if mp else None
    ms = re.search(r"/Subtype/(\w+)", line); d["subtype"] = ms.group(1) if ms else None
    mc = re.search(r"/Contents\(((?:[^()\\]|\\.)*)\)", line); d["contents"] = mc.group(1) if mc else None
    mq = re.search(r"/QuadPoints\[([^\]]+)\]", line)
    nums = [float(x) for x in mq.group(1).split()] if mq else []
    d["quadpoints"] = [nums[i:i+8] for i in range(0, len(nums), 8)] if mq else None
    mr = re.search(r"/Rect\[([^\]]+)\]", line)
    d["rect"] = [float(x) for x in mr.group(1).split()] if mr else None
    return d

_stext_cache = {}
def get_stext(pdf, page_num):
    if (pdf, page_num) in _stext_cache: return _stext_cache[(pdf, page_num)]
    out = run(["mutool", "draw", "-F", "stext", pdf, str(page_num)])
    root = ET.fromstring(out[out.index("<?xml"):])
    page_el = root.find("page"); height = float(page_el.get("height"))
    lines = []
    for line_el in page_el.iter("line"):
        x0, y0, x1, y1 = [float(v) for v in line_el.get("bbox").split()]
        chars = []
        for c in line_el.iter("char"):
            q = [float(v) for v in c.get("quad").split()]
            chars.append((min(q[0], q[2], q[4], q[6]), max(q[0], q[2], q[4], q[6]), c.get("c")))
        lines.append({"bbox": (x0, y0, x1, y1), "text": line_el.get("text"), "chars": chars})
    r = {"height": height, "lines": lines}; _stext_cache[(pdf, page_num)] = r; return r

def recover_highlight_text(pdf, page_num, quadpoints):
    stext = get_stext(pdf, page_num); H = stext["height"]; recovered = []
    for quad in quadpoints:
        xs, ys = quad[0::2], quad[1::2]
        minx, maxx = min(xs), max(xs)
        min_y_td, max_y_td = H - max(ys), H - min(ys)
        for line in stext["lines"]:
            lx0, ly0, lx1, ly1 = line["bbox"]
            v = max(0.0, min(ly1, max_y_td) - max(ly0, min_y_td))
            if (ly1 - ly0) <= 0 or v / (ly1 - ly0) < 0.4: continue
            if lx1 < minx or lx0 > maxx: continue
            chosen = [c for (cx0, cx1, c) in line["chars"] if minx - 1 <= (cx0 + cx1) / 2 <= maxx + 1]
            recovered.append("".join(chosen) if chosen else line["text"])
    return " / ".join(recovered)

def nearest_line(pdf, page_num, rect):
    stext = get_stext(pdf, page_num); H = stext["height"]
    y_td = H - (rect[1] + rect[3]) / 2
    best, best_d = None, 1e9
    for line in stext["lines"]:
        d = abs((line["bbox"][1] + line["bbox"][3]) / 2 - y_td)
        if d < best_d: best, best_d = line, d
    return best["text"] if best else None
```

**Verification:** run against the fixture built during planning — `page.search("predict the next token")` inside a sentence, highlighted, then read back: `recovered_text` was exactly `"predict the next token"`, not the full sentence. A highlight spanning a wrapped bullet ("models were" / "undertrained relative to their size") recovered both segments.

## Task 4 — Staleness check and anchor matching (rest of `map_comments.py`)

```python
WORD_RE = re.compile(r"[A-Za-z0-9']+")
def strip_md(s): return re.sub(r"[*_`#>-]", "", re.sub(r"<[^>]+>", "", s))

def best_matching_md_line(md_lines, start, end, target_text):
    if not target_text: return None, 0.0
    target = set(w.lower() for w in WORD_RE.findall(target_text))
    if not target: return None, 0.0
    best_ln, best_score = None, 0.0
    for ln in range(start, min(end, len(md_lines)) + 1):
        cand = set(w.lower() for w in WORD_RE.findall(strip_md(md_lines[ln - 1])))
        if not cand: continue
        score = len(target & cand) / len(target)
        if score > best_score: best_ln, best_score = ln, score
    return best_ln, best_score

def main():
    md_path, pdf_path = Path(sys.argv[1]), sys.argv[2]
    slide_lines = {s["slide"]: s for s in json.loads(run(
        ["node", "slides/scripts/pdf-review/resolve-slide-lines.mjs", str(md_path)]))}
    current_hash = hashlib.sha256(md_path.read_bytes()).hexdigest()
    kw = next((l for l in run(["pdfinfo", pdf_path]).splitlines() if l.startswith("Keywords:")), None)
    stamp = kw.split(":", 1)[1].strip() if kw else None
    m = re.search(r"sha256=([0-9a-f]{64})", stamp) if stamp else None
    stale = not (m and m.group(1) == current_hash)

    pmap = page_object_map(pdf_path)
    md_lines = md_path.read_text().splitlines()
    report = {"deck": md_path.stem, "stale": stale, "current_sha256": current_hash,
              "pdf_stamp": stamp, "comments": []}
    for line in annotation_lines(pdf_path):
        a = parse_annot(line)
        if a["subtype"] not in ("Text", "FreeText", "Highlight"): continue
        page = pmap.get(a["p_obj"]); s = slide_lines.get(page)
        e = {"obj": a["obj"], "subtype": a["subtype"], "page": page,
             "slide_line_range": [s["content_start_line"], s["end_line"]] if s else None,
             "comment_text": a["contents"]}
        if a["subtype"] == "Highlight":
            e["anchor_text"] = recover_highlight_text(pdf_path, page, a["quadpoints"]) if a["quadpoints"] else None
        else:
            e["anchor_text"] = nearest_line(pdf_path, page, a["rect"]) if a["rect"] else None
        if s and e["anchor_text"]:
            ln, sc = best_matching_md_line(md_lines, s["content_start_line"], s["end_line"], e["anchor_text"])
            e["matched_md_line"], e["match_score"] = ln, round(sc, 2)
            e["status"] = "RESOLVED" if sc >= 0.4 else "AMBIGUOUS"
        else:
            e["status"] = "AMBIGUOUS"
        report["comments"].append(e)
    print(json.dumps(report, indent=2))

if __name__ == "__main__": main()
```

**Verification, run during planning on a fixture built from `02-formation.md`/`.pdf`:** a sticky note ("tighten this — too long for one bullet") placed near a bullet on page 5 resolved to `matched_md_line: 90`, `match_score: 1.0` — line 90 is exactly `- Humans write demonstrations: here is a request, here is a good response to it.`, the intended target. A highlight on "undertrained relative to their size" (page 3, inside bold markdown `**...**`) resolved to line 46, score 1.0, despite the `**` markers — `strip_md` removes them before comparison. Then the source file was appended with one extra line (simulating a post-export edit) and the script re-run: `stale` flipped to `true`, confirming the hash check fires on drift and does not require a slide count to actually have changed to catch staleness — any source edit invalidates the mapping.

**On `stale: true`:** the assistant stops before mapping any comment to a line and tells the user: "This PDF's stamp (`sha256=<8 chars>…`) does not match the current source (`sha256=<8 chars>…`). Comments may point at the wrong slide. Re-export and re-annotate, or confirm you want me to proceed anyway knowing page numbers may be wrong." It proceeds only on explicit confirmation, and if so, downgrades every comment's status to `AMBIGUOUS` regardless of match score.

## Task 5 — Handoff convention and unresolved-comment reporting

- Annotated PDFs are dropped in `slides/exports/review/NN-name.pdf` (new directory; add `exports/review/` to `slides/.gitignore` — it holds transient review input, not a deliverable).
- Run: `python3 slides/scripts/pdf-review/map_comments.py slides/NN-name.md slides/exports/review/NN-name.pdf`
- Every comment with `status: AMBIGUOUS` (no rect/quad match, match score below 0.4, or the deck was stale and confirmed anyway) is listed to the human **before any edit is attempted**, in this form: page, subtype, the comment or recovered text, the best candidate line and its score if one exists, and why it wasn't good enough. The assistant asks what was meant rather than picking the best-scoring candidate. `RESOLVED` comments are listed too, as a plan, with the exact line to be changed, before editing — this is the same review-before-edit habit rule 7 already requires.

## Task 6 — Apply edits

For each `RESOLVED` comment, in slide order:
1. `Read` the target line's current content at `matched_md_line`.
2. Apply the requested change via `Edit`, using that exact line text as `old_string` — the tool's own uniqueness check is the "assert anchor exists" step.
3. If the comment says "cut this slide": delete the full `[content_start_line, end_line]` block (from `resolve-slide-lines.mjs`), including its leading `---`, and show the removed content in the diff before it's finalized — irreversible-feeling edits get an explicit look, even though git makes them recoverable.
4. If the comment asks for a source that isn't in `sources.json`/`references.md` as `[V]`: do not invent one. Insert `TODO(cite): <search terms>` as plain text near the claim (not a `<Cite k=.../>`, which would fail the build check with an unknown key).
5. `grep -n` the changed region to confirm the new text is present and the old text is gone.

After all edits for a deck: `cd slides && npm run check:cites` (must exit 0), then `npm run export` (regenerates and re-stamps all PDFs per Task 2), then commit the `.md` and the regenerated `.pdf` together, per the repo's existing "export and commit whenever a chapter is finished" rule.

## For the human author

- **Prefer sticky notes (Text annotations) for anything that isn't itself the exact text to change.** They always carry `/Contents` directly — no recovery step, no ambiguity about where the comment text is. Use a highlight only when the comment *is* "this exact phrase" (e.g., marking the words that need a citation); add a typed note to the highlight if you also want to say something about it — a highlight without a note only works if the phrase is unique enough on the slide to search-match confidently.
- **Easy to action:** "tighten this bullet", "add a unit to the PTO damping coefficient here" (with the phrase highlighted), "cut this slide", "this needs a `[V]` source — search terms: X". Each names a location and a concrete action.
- **Hard to action:** a highlight with no note on a very short or repeated phrase (e.g. highlighting "the" — not unique enough to locate); "make this better" with no location; a note placed in blank margin far from any text (the nearest-line heuristic will guess wrong). If in doubt, add a short note even to a highlight.
- **Avoid:** stacking multiple unrelated instructions in one note (the assistant treats the whole `/Contents` as one instruction); annotating a PDF you're not sure is current — check the deck hasn't changed since you exported it, or just re-export before marking up.

## Limitations

- Word-overlap anchor matching (Task 4) is a bag-of-words heuristic, not a parser. It will mismatch on slides where two bullets share most of their vocabulary, or where the highlighted phrase also appears verbatim elsewhere in the same slide (e.g., a repeated technical term). The 0.4 threshold and the RESOLVED/AMBIGUOUS split contain this, but do not eliminate it — spot-check a sample of RESOLVED items too, not only the AMBIGUOUS ones.
- The coordinate transform (Task 3) is derived empirically from this project's export pipeline (Chromium-via-Slidev, uniform `MediaBox`, no rotation). It is not a general PDF-annotation library; a different export toolchain would need the same empirical check repeated before trusting it.
- Visual order does not always equal source order. For a slide using columns, grids, or side-by-side images, the Nth rendered text block is not reliably the Nth markdown content line. This plan does not attempt to detect that layout and will silently misorder in the worst case — for such slides, treat every comment as AMBIGUOUS until confirmed by eye, or annotate them via the plain-text alternative below instead.
- A PDF viewer that flattens or fully rewrites the file on save (rather than an incremental update) could drop the `/Info/Keywords` stamp entirely. The mismatch handling in Task 4 treats a missing stamp the same as a mismatched one — safe, but it means a legitimately fresh PDF from such a viewer would still trigger the staleness prompt every time.
- **A plain markdown comment file (`review/NN-name-comments.md`, lines like `slide 5: tighten the SFT bullet`) is simpler and more reliable for anything that isn't tied to an exact phrase or exact visual location** — no coordinate transform, no staleness stamp, no annotation-type quirks, and it's trivially diffable and greppable. Prefer it for whole-slide or whole-deck feedback ("cut slide 12", "reorder 8 and 9", "this chapter needs a stronger opener"). The PDF route earns its complexity specifically for phrase-level feedback ("this claim needs a source", "this word is wrong") where pointing at the actual rendered text is worth more than a line number the author has to count out by hand. Use both: PDF markup for phrase-level notes, a plain comment file for structural ones. Do not force structural feedback through the PDF pipeline.

## What was not done

- No script was added to `slides/package.json` yet or committed — Tasks 1–4's scripts exist only as verified content in this plan and in the scratch directory used during planning; they still need to be written into `slides/scripts/pdf-review/` and committed.
- The 19 existing exported PDFs have not been stamped yet (Task 2's backfill run is specified but not executed).
- No real reviewer annotation exists yet to test the human-facing loop end to end; all verification used synthetic annotations created via `mutool run`, not annotations made in Preview/Acrobat/Foxit/etc. Those tools are believed to write standard-compliant incremental updates (per ISO 32000, `/QuadPoints` are always in default page user space regardless of producer), but this was not directly tested against a non-MuPDF-authored annotation.
- StrikeOut, Underline, Squiggly, and Ink annotation subtypes are not handled — only `Text`, `FreeText`, and `Highlight`. A reviewer using another tool's default annotation type (some PDF apps default comments to something other than a sticky note) will produce an annotation this pipeline silently ignores rather than flags; this is a gap, not a designed exclusion, and should be closed before relying on the workflow for a reviewer using an unfamiliar app.
