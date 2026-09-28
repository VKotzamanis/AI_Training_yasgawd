# Chapter-Draft Review Rubric — Implementation Plan

> **For agentic workers:** Execute tasks in order; Task 2 is a gate — do not start
> Task 4 until it passes. Steps use checkbox (`- [ ]`) syntax for tracking. This is a
> documentation/orchestration plan: "tests" are the named verification commands and
> gates, and there are no git commits (the working directory is not a repository).

**Goal:** Build and calibrate a review rubric, then apply it via subagents to all 19
draft chapters in `ai-training/slides/`, producing one evidence-backed report per
chapter plus a cross-chapter repetition report and a ranked summary.

**Architecture:** A single rubric file (five failure classes, hard evidence rules,
fixed finding format) → calibration against the approved Chapter 1 deck → per-chapter
review subagents (two at a time) → adversarial verification of technical findings →
cross-chapter merge → summary. Reviewer output is structured so the merge step is
mechanical.

**Tech stack:** Claude Code Agent tool (Opus 5 reviewers — `model: "opus"`; Sonnet 5
acceptable only for the Task 6 merge), markdown throughout.

## Global Constraints

- **Maximum two subagents running at any moment.** This machine has 16 GB of
  non-upgradable RAM and has crashed under six concurrent subagents. Two is the
  ceiling, not a starting point.
- **Approved exemplar:** `REVIEWD/AI_TRAINING.pdf`, slides 1–13 and 16. Slides 14–15
  are placeholders and slide 17 is empty — reviewers must be told to skip them.
- **Review targets:** `ai-training/slides/01-substrate.md` through
  `19-judgement.md` (19 files). Chapter 1's draft (`01-substrate.md`) is already
  superseded by the approved deck but is still reviewed — its verdict decides whether
  any material is worth salvaging into later chapters.
- **Evidence rule (absolute):** no finding without a verbatim quote and a line
  number. A reviewer that cannot quote the problem has not found a problem.
- **No finding inflation:** a rubric that produces findings on demand is worthless.
  "No findings in this class" is a valid, reportable outcome.
- **Reports directory:** `FOR-REVIEW/rubric-reports/` (already created).

---

### Task 1: Write the rubric file

**Files:**
- Create: `FOR-REVIEW/RUBRIC.md`

**Interfaces:**
- Produces: the rubric text every Task-4 subagent receives verbatim; the finding ID
  format `[chNN-###]` and the report skeleton that Tasks 5–7 parse.

- [ ] **Step 1: Write `FOR-REVIEW/RUBRIC.md` with exactly this content** (edit only
  if Task 2 calibration forces it):

````markdown
# Chapter Draft Review Rubric — v1

## Authority and calibration

The approved exemplar is `REVIEWD/AI_TRAINING.pdf` (slides 1–13, 16; skip 14, 15, 17).
It defines the target: one message per slide, a topic closed once and never reopened,
definitions carrying a technical alias, claims carrying equations or numbers, direct
declarative prose. Your job is to measure a draft chapter against that target and
report what blocks it from reaching it.

## Reviewer procedure (in order, no skipping)

1. **Read the entire chapter before recording anything.** You must be able to state
   the chapter's argument in a form its author would accept. If you cannot, your
   first finding is an F-class finding on the chapter, not a guess.
2. **Build the topic ledger** (the table in the report skeleton): every topic, the
   slide where it opens, the slide where it closes. This table is evidence
   infrastructure for R- and F-class findings — build it before hunting.
3. **Write the one-sentence Message for each slide.** Where you cannot, that slide
   gets an F finding whose quote is the slide's actual text.
4. **List the chapter's own promises** — title, stated agenda, section headers —
   then check each promise for a payoff slide. Unpaid promises are C findings.
5. **Only then** sweep for T and S findings.
6. **Apply the so-what test to every candidate finding**: if fixing it would not
   change what a trainee understands or retains, drop it.

## Failure classes

### R — Repetition / reopened topic
Content that restates an already-delivered point without new information, or reopens
a topic after its closing slide. Detection is mechanical: any topic whose ledger row
shows more than one open interval, or two slides whose Messages are the same
sentence. Severity: blocker when a whole slide is redundant; major for a repeated
block or bullet; minor for a repeated sentence.

### F — Flow / unclear intent
A slide with no statable Message; a slide consuming a concept defined only on a later
slide (forward dependency); a section whose boundary cannot be located; an ordering
that forces the reader to hold more than one open question at a time. Quote the text
that fails; name the slide the dependency actually lives on.

### T — Technical inaccuracy
A wrong statement, wrong equation, wrong number, a term used against its field
definition, or a citation that cannot be located. Every T finding must state what
correct looks like and on what basis. Tag each T finding `CONFIRMED` only when you
can ground the correction in a source you actually opened during this review or in
mathematics you executed; otherwise tag it `PLAUSIBLE` — a later verification pass
adjudicates. Never present memory as grounding.

### C — Coverage or contract gap
A concept the chapter uses but never defines, anywhere; a promise (title, agenda,
section header) with no payoff slide; or a component defined without its contract.
At the slide where a component receives its definition (its definitional home — not
at every later mention), five fields are mandatory: (1) a one-sentence definition in
positive form; (2) the signal contract — input (name, type/shape) → output (name,
type/shape); (3) necessity — the concrete failure when the component is removed;
(4) the observable capability it enables in the deployed product; (5) its location —
pipeline step, stage (training / inference / harness), and architectural scope. A
missing field is a C finding, major by default. Quote the first use of the undefined
concept, or the definitional section lacking the field.

### S — Style violations (four, exhaustively; flag nothing else as style)
- **S1 — explanation by subtraction:** a definition of the form "X is not A. It is
  B." where B is never independently defined. The negation is doing the work and
  delivers none.
- **S2 — empty parallel:** an analogy or contrast that transfers zero technical
  content. Calibration exemplar (from a rejected draft): "MCP is not a contract. It
  is a protocol. API is the contract."
- **S3 — pretense over information:** aphorism, dramatic fragment, or rhetorical
  repetition standing where information should be. Flag only when the sentence
  replaces content; leave decorated content alone.
- **S4 — nonstandard term:** a coined or slang term where a standard term exists, or
  one standard term swapped for a different standard term with a different meaning.
  Name the correct term in the fix line.

## Finding format (exact — the merge step parses this)

### [chNN-###] <class R|F|T|C|S1..S4> <blocker|major|minor> — slide/section <n>
Quote: "<verbatim text, with line number(s) from the .md file>"
Why it fails: <one or two sentences>
Fix direction: <one line; for T: what correct looks like + basis; tag CONFIRMED or PLAUSIBLE>

## Report skeleton (one file per chapter)

# Review: <chapter file> — <date> — reviewer: <model>
## Topic ledger
| topic | opens (slide) | closes (slide) | reopened at |
## Slide messages
<slide n: one sentence each — or the F finding it triggered>
## Findings
<sorted: blockers, then major, then minor; numbered [chNN-001] onward>
## Coverage checklist
<each chapter promise → paid at slide n / unpaid (C finding ref)>
## Topics exported
<what this chapter delivers that later chapters may assume — one line each>
## Checks not run
<explicitly: what you could not verify and why>
## Verdict
<rebuild | salvage-with-edits | usable-with-fixes> — one justification paragraph.
A chapter with any unresolved blocker cannot be "usable-with-fixes".
````

- [ ] **Step 2: Verify the file parses as intended**

Run: `grep -c '^### ' FOR-REVIEW/RUBRIC.md`
Expected: `6` — the five failure-class headings (R, F, T, C, S) plus the
`### [chNN-###]` finding-format heading. Any other count means the rubric text
drifted from this plan; reconcile before proceeding.

---

### Task 2: Calibration gate — run the rubric on the approved deck

**Files:**
- Create: `FOR-REVIEW/rubric-reports/calibration-ch1.md` (subagent output)
- Possibly modify: `FOR-REVIEW/RUBRIC.md` (only if calibration fails)

**Interfaces:**
- Consumes: `FOR-REVIEW/RUBRIC.md` (Task 1), `REVIEWD/AI_TRAINING.pdf`.
- Produces: a pass/fail decision recorded at the top of the calibration report.

- [ ] **Step 1: State the pass criterion before dispatch.** The rubric passes
  calibration when the approved deck (slides 1–13, 16) yields **zero blocker
  findings in classes R, F, S** and the reviewer's topic ledger reproduces the
  deck's six-section structure. T findings against the approved deck are allowed
  and are recorded for the author — the deck is approved for style and flow, not
  certified error-free.
- [ ] **Step 2: Dispatch one Opus 5 subagent** with the Task-4 prompt template
  (below), substituting the PDF path for the chapter file and adding: "This deck is
  the approved exemplar; you are calibrating the rubric, not judging the deck.
  Skip slides 14, 15, 17 (placeholders)."
- [ ] **Step 3: Evaluate.** If R/F/S blockers appear against the approved deck, the
  rubric's thresholds are wrong (the deck defines the standard). Tighten the class
  definition that misfired, append a `v1.1` changelog line to `RUBRIC.md`, rerun
  Step 2 once. Two consecutive failures mean the rubric needs redesign — stop and
  reconsult rather than iterating blind.
- [ ] **Step 4: Record the decision.** First line of `calibration-ch1.md`:
  `CALIBRATION: PASS (rubric v1)` or the failure note.

---

### Task 3: Scope check against the prior 19-chapter peer review

**Files:**
- Create: `FOR-REVIEW/rubric-reports/PRIOR-REVIEW-SCOPE.md`

- [ ] **Step 1:** Read `ai-training/curriculum/peer-review-19-chapters.md`,
  `review-ch02.md`, `review-ch03.md` (main session, no subagent — this is reading,
  not review).
- [ ] **Step 2:** Write `PRIOR-REVIEW-SCOPE.md`: a table — prior review's classes of
  finding vs this rubric's five classes; which chapters it already flagged and for
  what; explicit instruction to Task-4 reviewers per chapter: "the prior review
  already flagged X — do not re-derive it; cite it and move on." One paragraph per
  chapter maximum.
- [ ] **Step 3: Verify:** the file names all 19 chapters.
  Run: `grep -oE '(0[1-9]|1[0-9])-' FOR-REVIEW/rubric-reports/PRIOR-REVIEW-SCOPE.md | sort -u | wc -l`
  Expected: `19`

---

### Task 4: Per-chapter review fan-out

**Files:**
- Create: `FOR-REVIEW/rubric-reports/ch01-review.md` … `ch19-review.md`

**Interfaces:**
- Consumes: `RUBRIC.md` (v-final from Task 2), `PRIOR-REVIEW-SCOPE.md` (Task 3).
- Produces: 19 reports in the Task-1 skeleton; their "Topics exported" and ledger
  sections feed Task 5; their T findings feed Task 6.

- [ ] **Step 1: Dispatch reviewers two at a time** (hard cap; wait for both to
  return before the next pair), chapters in numeric order. Prompt template — fill
  `{NN}` and `{FILE}`:

```
Review one draft training chapter against a fixed rubric. You are a forensic
reviewer; your report will be parsed mechanically, so follow the rubric's report
skeleton exactly.

1. Read /home/vx/Desktop/Claude/AI Training/FOR-REVIEW/RUBRIC.md — it defines the
   procedure, the five failure classes, the finding format, and the report skeleton.
   Follow its "Reviewer procedure" section in order.
2. Read the chapter under review, in full, before recording anything:
   /home/vx/Desktop/Claude/AI Training/ai-training/slides/{FILE}
   (Slidev markdown: slides separated by `---`; count slides from 1 at the first
   content slide. Cite findings by slide number AND file line number.)
3. Read /home/vx/Desktop/Claude/AI Training/FOR-REVIEW/rubric-reports/PRIOR-REVIEW-SCOPE.md
   — where the prior review already flagged something in this chapter, cite it in
   one line instead of re-deriving it.
4. Write your report to
   /home/vx/Desktop/Claude/AI Training/FOR-REVIEW/rubric-reports/ch{NN}-review.md
   using finding IDs [ch{NN}-001] onward.

Hard rules: verbatim quote + line number for every finding; T findings tagged
CONFIRMED only on grounding you opened or computed during this review, else
PLAUSIBLE; "no findings in this class" is a valid outcome; do not pad. Your final
message: the verdict line and the finding count by class — nothing else.
```

- [ ] **Step 2: After each pair returns, verify report structure before dispatching
  the next pair:**

Run: `grep -L '^## Verdict' FOR-REVIEW/rubric-reports/ch*-review.md`
Expected: empty output (every report has a Verdict section). A malformed report is
re-dispatched once with the defect named.

- [ ] **Step 3: Completion check.**
Run: `ls FOR-REVIEW/rubric-reports/ch*-review.md | wc -l`
Expected: `19`

---

### Task 5: Cross-chapter repetition and contradiction pass

**Files:**
- Create: `FOR-REVIEW/rubric-reports/CROSS-CHAPTER.md`

**Interfaces:**
- Consumes: the "Topic ledger" and "Topics exported" sections of all 19 reports.

- [ ] **Step 1:** Concatenate the 19 "Topics exported" and ledger sections
  (main session; mechanical extraction).
- [ ] **Step 2:** One subagent (Opus 5) receives only that concatenation plus:
  "Flag (a) any topic exported by more than one chapter — cross-chapter repetition;
  (b) any topic a chapter consumes that no earlier chapter exports — curriculum-level
  forward dependency; (c) any pair of exported one-liners that contradict. Output:
  three tables, each row citing the chapter numbers involved. No prose."
- [ ] **Step 3: Verify** every row in the output names at least two chapter numbers
  (table a, c) or one chapter number (table b); reject and re-dispatch otherwise.

---

### Task 6: Adversarial verification of T findings

**Files:**
- Modify: each `chNN-review.md` containing T findings (append a `## T verdicts`
  section; never edit the original finding text)

- [ ] **Step 1:** Collect every T finding across the 19 reports
  (`grep -h '\] T ' FOR-REVIEW/rubric-reports/ch*-review.md`).
- [ ] **Step 2:** Batch them per chapter; dispatch verification subagents two at a
  time. Prompt per batch: "For each finding below, attempt to REFUTE it: find the
  reading under which the draft text is correct, check the mathematics yourself, and
  search documentation/literature where the claim is checkable. Verdict per finding:
  UPHELD / REFUTED / UNDECIDABLE, one sentence of grounds, sources named. Default to
  UNDECIDABLE when evidence is thin — an upheld wrong finding costs a chapter
  rewrite."
- [ ] **Step 3:** Append verdicts to each report's `## T verdicts` section.
  REFUTED findings stay visible with their refutation — removed findings hide
  rubric failure modes that v2 needs to know about.
- [ ] **Step 4: Verify:** every T finding ID appears in a verdicts section.

---

### Task 7: Synthesis

**Files:**
- Create: `FOR-REVIEW/rubric-reports/SUMMARY.md`

- [ ] **Step 1:** Write `SUMMARY.md` (main session): table of 19 chapters ×
  {verdict, blockers, majors, minors, finding count per class, upheld-T count},
  sorted worst-first; below it, the Task-5 cross-chapter tables verbatim; below
  that, a five-line "rubric v2 notes" list — every place a reviewer misapplied a
  class or a REFUTED T finding revealed a rubric ambiguity.
- [ ] **Step 2: Verify totals:** the summary's per-class counts equal
  `grep -c` over the reports; run the greps and reconcile any mismatch before
  presenting.

---

## Self-review (performed at plan-writing time)

- **Spec coverage:** the user named four failure targets — repetition, break of
  flow, technical inaccuracy, lack of technical coverage → classes R, F, T, C
  (Task 1). Style failures the user described in prose (subtraction, empty
  parallels, pretense) → class S with the user's own exemplar as calibration.
  "Opus 5/Sonnet 5 subagents" → Task 4/6 model choices. "EVERY other chapter" →
  all 19 files enumerated, completion checks in Tasks 4–5.
- **Placeholder scan:** `{NN}`/`{FILE}` are dispatch-time template variables, not
  omissions; rubric text and all prompts are complete.
- **Consistency:** finding ID format `[chNN-###]` is identical in Task 1's rubric,
  Task 4's prompt, and Task 6's grep.
