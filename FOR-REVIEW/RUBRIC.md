# Chapter Draft Review Rubric — v1.1

Changelog v1.1 (2026-08-27, post-calibration): C-class contract check scoped to a
component's fullest treatment in the chapter. Calibration evidence: applied per-slide,
the contract fired 66 major findings against the approved exemplar, because deck
slides introduce at definition depth and defer — the contract is the supplement
convention. R/F/S/T unchanged; calibration PASS unaffected (narrowing only).

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

**Scope of the contract check (v1.1):** the contract binds at the component's
*fullest treatment in the chapter*. A slide that introduces a term at deck depth and
points to a fuller treatment (a supplement section, a named later slide) is not a
definitional home — the pointer's target is; check the fields there. Where a chapter
has no fullest treatment of a component it relies on, that is an ordinary coverage
gap (concept used, never defined), not a per-field contract finding.

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
