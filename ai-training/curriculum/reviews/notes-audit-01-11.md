# Presenter notes audit — decks 01, 03–11

Audited 2026-08-20. Scope: the `<!-- Says / From / Chapter / To -->` block appended to every
slide in `01-substrate.md`, `03-control.md`, `04-measurement.md`, `05-intrinsic-failure.md`,
`06-extrinsic-failure.md`, `07-physical-limits.md`, `08-brain-and-model.md`, `09-the-agent.md`,
`10-memory.md`, `11-orchestration.md`. **150 slides, 150 note blocks, all four fields present on
every one.** Ground truth for cross-chapter claims: `curriculum/architecture.md`, cross-checked
against `curriculum/chapter-briefs.md` where a note appeals to a brief.

Method, stated before the work: for each slide, (1) read the body — not the heading — and compare
against `Says:`; (2) compare `From:` against the actual preceding slide and `To:` against the
actual following slide, mechanically, by building an adjacency table of every heading paired with
its neighbours' link fields; (3) for first and last slides of a deck, compare against the chapter
sequence in `architecture.md`; (4) check every `Chapter:` field that names a thread against the
five-thread map. Pass criterion: a defect is only reported where the slide's own text can be
quoted against the note.

## Summary

| Deck | Slides | Result |
|---|---|---|
| `01-substrate.md` | 15 | 3 defects — one confirmed thread mislabel, two suspected |
| `03-control.md` | 18 | Clean |
| `04-measurement.md` | 18 | 2 defects, both suspected — one statistical, one terminological |
| `05-intrinsic-failure.md` | 22 | Clean |
| `06-extrinsic-failure.md` | 13 | Clean |
| `07-physical-limits.md` | 18 | Clean |
| `08-brain-and-model.md` | 13 | Clean |
| `09-the-agent.md` | 10 | 1 defect, suspected |
| `10-memory.md` | 12 | Clean |
| `11-orchestration.md` | 11 | Clean |

**Linkage is clean everywhere.** All 150 `From:`/`To:` fields point at the correct adjacent slide.
Every deck-opening `From:` correctly describes the preceding chapter's handoff and every
deck-closing `To:` correctly describes the following chapter, checked against `architecture.md`.
The Chapter 8 → Chapter 10 seam claim — that Chapter 10 reopens Chapter 8's closing line
*verbatim* — is true: both read "The model has no hippocampus. **So you have to be its
hippocampus.**" No fabricated `TODO`/blocked-status claim was found; every note that describes a
slide as pending correctly reflects a `TODO(...)` marker on that slide.

## Defects

### 1. CONFIRMED — `01-substrate.md`, "The question this chapter opens and will not answer"

Note bullet:

> `- **Chapter:** Opens the substrate-versus-brain thread that Chapter 8 closes, without answering it here.`

There is no such thread. `architecture.md` defines exactly five threads — Truthfulness,
Memory & context, Cost, Trust boundary, Verification — and the brain question is not among them;
it is a chapter-to-chapter forward reference (Ch 8: "The question from Chapter 1, answered").
The deck itself reserves the word for the real ones, with an explicit marker each time:

> `**Thread opened — cost.** The token is the unit of *meaning* here.`

> `**Thread opened — memory and context.** Introduced here as a bounded buffer.`

The brain-question slide carries no such marker. Its full body is:

> `**Is this like a brain?**` / `- Hold it. It is the wrong question to answer first.` /
> `- Chapter 8 returns to it — after we have priced the thing and watched it fail.` /
> `- The answer is more interesting once you know what it actually computes.`

Consequence: "thread" is a defined term in this curriculum with a published map. A presenter who
calls the brain question a sixth thread contradicts the map the course hands out. Suggested fix:
"Opens the brain question that Chapter 8 answers" — drop the word *thread*.

### 2. SUSPECTED — `04-measurement.md`, "Two more traps"

Note bullet:

> `- **Says:** Warns that the noise floor is imprecise and that running three arms without declaring all of them inflates the effective error rate.`

Slide text:

> `- **Three arms means three comparisons.** And the per-arm rate cannot be 5%, because two slides
> ago you proved five cases have no 5% rejection region at all. At the only level actually
> attainable, 0.0625 per arm, three arms give a family-wise rate of about **18%**. **Declare every
> arm**, including the boring ones.`

The 18% is a consequence of multiplicity alone. It is 18% whether or not you declare every arm —
declaring changes nothing about the family-wise rate. Declaration addresses a *different* defect,
named separately in the slide's own footnote:

> `Reporting only the interesting arm is post-hoc selection of the winning condition — and doing
> that in a chapter about method would be self-refuting.`

The note fuses the two into one causal claim that is wrong in the direction that matters: it
implies declaring all three arms controls the inflation. In a chapter teaching statistical method
to experimentalists, this is the note most likely to produce a false statement said aloud.
Marked SUSPECTED only because a charitable reading — "the *as-reported* error rate of a
selectively reported arm is inflated" — is defensible in isolation; it is not what the slide says.

### 3. SUSPECTED — `01-substrate.md`, title slide

Note bullet:

> `- **Says:** Introduces Chapter 1 as the single operation, next-token prediction, that everything else in the course rests on.`

Slide text, in full:

> `# Chapter 1 — Substrate` / `### What the system computes` / `Everything in this course rests on
> one operation. This chapter is that operation, and nothing else.`

The slide deliberately withholds the name of the operation. It is revealed four slides later,
under "The entire objective": `Given a sequence of tokens, predict the next one.` The note supplies
the answer on the title slide. Nothing false is asserted about the course, but the note describes
the slide as containing a name the slide does not contain, and reading it in presenter mode
pre-empts the reveal the deck sequences deliberately.

### 4. SUSPECTED — `09-the-agent.md`, "The permission model is the safety story"

Note bullet:

> `- **Chapter:** States the chapter's core safety claim -- the diff, not the permission setting, is the artefact of responsibility.`

Slide heading and body:

> `## The permission model is the safety story` / `- Read-only by default...` /
> `- Permissions are per action, and can be narrowed or broadened per project.` /
> `**The diff is the artefact of responsibility.** It is the moment the change becomes yours.`

The slide asserts both things and sets neither against the other: the permission model *is* the
safety story, and the diff is where responsibility lands. The note's contrastive construction —
"the diff, **not the permission setting**" — appears nowhere on the slide and runs against its
heading. Right slide, subtly wrong point.

### 5. SUSPECTED — `04-measurement.md`, "Why prompting advice circulates as folklore"

Note bullet:

> `- **Says:** Diagnoses folklore prompting claims as single, unblinded, uncontrolled runs.`

Slide text:

> `- Someone changes a prompt, the output looks better, and they tell you.` /
> `- They ran it once. They looked at the output before deciding what "better" meant. They did not
> run the old prompt again.`

The three defects on the slide are n = 1, a **post-hoc pass criterion**, and no control condition.
The middle one is not a blinding failure. Blinding is a distinct procedure that gets its own slide
four positions later ("Blinding, and what it does not achieve" — strip labels, opaque IDs, shuffle,
grade pass/fail), and the chapter's method keeps it separate from "a pass criterion per case,
**defined before you look at any output**". Substituting one standard term for the other blurs a
distinction the chapter is built on.

### 6. SUSPECTED, minor — `01-substrate.md`, "Why it is called *temperature*"

Note bullet:

> `- **Says:** Derives the softmax temperature formula and its correspondence to the Boltzmann distribution, with a unit-consistency check.`

The formula is stated, not derived — it appears as a bare display equation followed by a symbol
table. What the bullets derive is the *correspondence*:

> `- This is the Boltzmann distribution, $p_i \propto \exp(-E_i/k_\mathrm{B}T_\mathrm{phys})$, with
> the sampling $T$ read as a **multiple of a reference temperature** $T_0$...`

Low severity: the compound object of "derives" makes the sentence ambiguous rather than false.
Flagged for completeness; reasonable to leave as is.

## Bottom line

**Safe to ship into presenter mode and PDF annotations, after fixing item 1 and item 2.**

Defect density is six items across 150 slides, and four of the six are wording precision rather
than false content. The two that warrant a change before delivery are item 1 (uses the course's own
defined term "thread" for something that is not one, contradicting the handed-out thread map) and
item 2 (states a causal relation the slide does not support, in the chapter whose entire subject is
statistical care). Items 3–5 are worth a pass if the notes are being edited anyway; item 6 is
optional.

Structural integrity is the strong result here: 150/150 note blocks present with all four fields,
150/150 linkage claims correct against actual slide adjacency, chapter handoffs correct against
`architecture.md` at every deck boundary, thread attributions correct against the five-thread map
in every case but item 1, and the Chapter 8 → 10 verbatim-seam claim verified by direct string
comparison. No note was found asserting a slide contains a demo, figure, number or citation that
it does not, and no note misreported a pending `TODO(...)` item as complete or a complete item as
pending.

### Out of scope, noticed in passing

`chapter-briefs.md` §Chapter 8 still carries "Human working memory holds roughly four items against
a context window of hundreds of thousands of tokens. The numbers run opposite to the analogy." Deck
08 explicitly retracts that framing ("So retract the whole framing, including 'the numbers run
opposite to the analogy'"). The deck and its notes are consistent with each other; the brief is
stale. Not a notes defect.

### What this audit did not do

- Deck `02-formation.md` and decks 12–19 were not in scope and were not read.
- Notes were checked against slide text and `architecture.md` only. **No note was checked against
  the underlying literature** — whether a slide's own claim about a source is true is a separate
  audit. Where a note faithfully reports a slide, it is marked clean here even if the slide's claim
  is itself unverified.
- Rendering was not tested. Whether these HTML comment blocks reach Slidev presenter mode and the
  PDF annotation layer intact is a build question, not a truth question, and was not run.
- `05-intrinsic-failure.md`, "The distinction people miss" cites only `turpin2023` while also
  reporting a modern-reasoning-model result ("often below 20% of the time"). That is a possible
  slide-level sourcing gap, not a note defect, and was not pursued.
