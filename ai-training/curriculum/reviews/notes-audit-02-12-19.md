# Presenter-notes truthfulness audit — decks 02, 12–19

Audited 2026-08-20. Scope: the `**Says:** / **From:** / **Chapter:** / **To:**` comment block on
every slide of the nine named decks — 108 slides, every note read against its own slide body
rather than its heading. Ground truth for chapter order and threads: `curriculum/architecture.md`.
Cross-checks against `DECISIONS.md` items 2, 4 and 7 where a note names them.

Three failure modes checked separately: fabrication (note asserts what the slide does not
contain), misdescription (right slide, wrong point), broken linkage (`From:`/`To:` naming a
non-adjacent slide, or a thread claim the slide does not carry).

## Summary

| Deck | Slides | Verdict |
|---|---|---|
| `02-formation.md` | 26 | 3 defects — 1 confirmed, 2 suspected |
| `12-extension.md` | 9 | Clean |
| `13-access.md` | 11 | Clean |
| `14-literature.md` | 8 | Clean |
| `15-production.md` | 8 | Clean |
| `16-code-and-numerics.md` | 9 | Clean |
| `17-critique.md` | 8 | Clean |
| `18-governance.md` | 9 | 1 defect — confirmed, minor |
| `19-judgement.md` | 7 | Clean |

Four defects across 108 slides, none of them fabrications and none of them an evidential
misrepresentation of the Part 2b annotation findings.

## Defects

### 1. CONFIRMED — `02-formation.md`, "What a rating task actually contains": cost thread attributed to the wrong chapter

Note bullet:

> - **Chapter:** It introduces the truthfulness, trust-boundary (harmlessness) and cost (verbosity) threads at the point the architecture's thread map names, alongside instruction following and tone.

`curriculum/architecture.md`, thread map:

> | **Cost** | Ch 1 — token as unit of meaning | Ch 7 unit of price → Ch 10 resident context → Ch 11 orchestration premium | Ch 13 — pricing and plan economics |

The map names Chapter 1 as the cost thread's introduction and does not list Chapter 2 anywhere in
that row. Truthfulness and trust boundary are correctly placed at Chapter 2; cost is not. The
slide's own verbosity row forward-references cost —

> | **Verbosity** | a cost in Chapter 7 and a bill in Chapter 13 |

— which is a forward reference, not a thread introduction. A presenter reading this note aloud
would tell the room that the cost thread starts here, contradicting Chapter 1's own closing
claim on the same thread. Fix: describe cost as picked up, not introduced.

Related but **not** a defect, recorded so it is not re-flagged: the note on "Not every parameter
runs" says it "carries the cost thread forward with an explicit forward reference to Chapter 7",
which the slide does say on its face ("Cost depends on it"). That note makes no claim about the
thread map, so it stands.

### 2. SUSPECTED — `02-formation.md`, "A cautionary case: the discovered prompt": misdescribes what the preceding slide's contradicted claim was, and what this slide is evidence for

Note bullet:

> - **From:** Follows the behaviour-to-mechanism slide by supplying the first case study behind its claim that the folk explanation for confident, structured prompting advice is contradicted.

The preceding slide, "Behaviour, traced to mechanism", makes no claim about prompting advice. Its
contradicted folk answer is about output *length*, and it names its own evidence:

> **The verbosity row is the interesting one, because the obvious answer is wrong.** The folk
> story says raters liked long answers, so models got long. Two of the reviewed instruments say
> otherwise: one broke ties deliberately toward **brevity**, the other **deleted length as a
> grading category** partway through the project

The evidence behind that row is the two reviewed vendor instruments, not this slide. The OPRO
case concerns the transferability of a searched instruction phrasing:

> - It was **found by search**, not by testing a hypothesis about encouragement. The narrative arrived afterwards.

It says nothing about why models produce long answers, and the preceding slide records that
mechanism as **"Not known"**. The note therefore asserts a supporting relationship the deck
deliberately does not make — in the chapter whose entire discipline is keeping a finding
attached to its actual evidence. Marked SUSPECTED because the two case studies are genuinely a
sequence about prompting folklore; the defect is the claimed evidential link, not the ordering.
Fix: "Follows the behaviour-to-mechanism slide with the first of two case studies on prompting
claims that did not survive scrutiny."

### 3. CONFIRMED — `18-governance.md`, "Data governance": wrong slide distance to the thread closure

Note bullet:

> - **Chapter:** Carries the trust-boundary thread's outbound half forward with its own citation footer, ahead of the explicit thread closure two slides later.

The deck order after "Data governance" is "Reproducibility", then "Lab-level standardisation",
then the closure slide:

> ## Two threads close here

That is three slides later, not two. Trivial in consequence, but it is a checkable factual
statement in a note and it is wrong. Everything else on this slide's note is accurate, including
the pinned-version caveat and the citation footer.

### 4. SUSPECTED — `02-formation.md`, two `From:` bullets naming non-adjacent slides

Both notes reach past the genuinely preceding slide to a conceptual antecedent. Neither is false
about the deck's argument; both break the convention every other note in these nine decks
follows, and a presenter using `From:` to know what they just said would be misled.

"Reinforcement learning from human feedback":

> - **From:** Follows the reward-model slide by showing what the reward model is actually used for once trained.

The reward-model slide ("Learning a preference") is three positions back. The slide immediately
before is "What disagreement does downstream", which hands over directly and explicitly:

> - Unresolved disagreement does not vanish. It enters the preference data as inconsistency, and the reward model fits it.

"Supervised fine-tuning":

> - **From:** Picks up the title slide's "this is what was added" framing, now naming the first concrete addition after the pretraining and scaling material.

The preceding slide is "Not every parameter runs". The note does acknowledge the intervening
material in the same sentence, which is why this is the weaker of the two instances.

## Checks that passed, stated because they were the stated risks

- **2a/2b split point.** No note in `02-formation.md` describes the chapter as split or the
  decision as made. The split-point slide's note says "with the split itself still undecided per
  DECISIONS.md", and the note two slides earlier calls it "an as-yet-undecided cut". `DECISIONS.md`
  still carries it under "Open — blocking". Clean.
- **`[E1]`–`[E4]` document counts.** Every Part 2b note's counts match its slide exactly: three of
  five for house style, two of five for repaired-text collection, two of five for engineered-out
  equivalence, two of five for judge blindness, three of five for attempt-before-judging, one
  document for the reviewer-layer band rule, one document each for the mid-collection rebuild and
  the hallucination-band theory. No note inflates a single-document finding into a corroborated
  one, no note implies a citable published source, and no note assigns a `[V]` or a citation to
  any annotation observation. The "eighth in evidential order" ranking is reported as the slide
  states it.
- **`16-code-and-numerics.md` observation-versus-cause separation.** The note on "A weakness worth
  showing you" keeps them apart explicitly — "separately flags the training-corpus explanation as
  an unestablished, TODO(cite) hypothesis rather than a demonstrated cause" — matching the slide's
  own "Keep the observation and the explanation apart." Clean.
- **`18-governance.md` blocked disclosure and both thread closures.** Note correctly reports
  BLOCKED status, the journal-list dependency, ASCE as expected-not-confirmed, and `[U]` tagging.
  Both thread closures are named and both match the architecture map. Clean.
- **`12-extension.md` blocked hands-on.** Note correctly identifies the block and `DECISIONS.md`
  item 2, and marks the exercise unresolved rather than describing it as runnable. Clean.
- **Slide-heading traps not inherited by the notes.** `18-governance.md` "The three questions every
  policy answers" carries four bullets; its note lists four and never says three. `19-judgement.md`
  opens on "four places you should put it down" while the next slide gives five tests; the notes
  reproduce each slide as written and the five-test note counts five. Both slide-side
  inconsistencies are real and worth fixing, but the notes are faithful.
- **Thread markers.** Every other thread claim checks out against the map: truthfulness closed in
  Ch 14 for citations only, verification developed Ch 14 → Ch 17 and closed Ch 18, trust boundary
  Ch 2 → 6 → 12 → 18, cost closed Ch 13 tracing Ch 1, 7, 10, 11. Chapter 17's note calls detection
  "the detection thread the deck names" — accurate hedging, since detection is a deck-level thread
  and not one of the architecture's five.
- **`DECISIONS.md` references.** Items 2, 4 and 7 exist and say what the notes claim they say.
- **First and last slides.** Every deck's opening `From:` describes the previous chapter's actual
  handoff, every closing `To:` names the correct next chapter, and `19-judgement.md`'s final note
  correctly states there is no next chapter.

## Bottom line

Safe to ship into presenter mode and PDF annotations after the four fixes above, none of which
requires touching slide content. There are no fabricated notes in these nine decks: no note
asserts a claim its slide does not contain, and the two categories most likely to cause real harm
— inflating an annotation finding's evidential standing, and stating the MATLAB training-corpus
hypothesis as established — are both handled correctly. Defect 1 is the only one that would put a
false statement about the course's own structure in front of the room; defects 2 and 4 degrade the
notes' usefulness as a navigation aid; defect 3 is cosmetic.

## Not done

- Slide content itself was not audited. Where a slide's own body is internally inconsistent
  (three-versus-four policy questions, four-versus-five judgement tests) it is recorded above as
  context, not as a note defect, and no slide has been corrected.
- The Part 2b document counts were verified note-against-slide only. They were **not** checked back
  against `curriculum/ch02-annotation-findings.md`, so a count wrong on the slide and faithfully
  copied into the note would pass this audit.
- No slide's cited claims were checked against `references.md` or `sources.json`; citation-key
  validity and `[V]`/`[P]`/`[U]` tags are out of scope here.
- The ten decks outside this brief (01, 03–11) were not opened.
- Nothing was edited except this file.
