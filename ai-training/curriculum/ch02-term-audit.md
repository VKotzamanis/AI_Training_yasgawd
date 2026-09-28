# Chapter 2 — term audit

Required by `HANDOFF.md` §6.5: every technical term the chapter uses, with the frame where it is
defined. A term with no defining frame is a defect.

Frame numbers are positions in `slides/beamer/02-formation.tex`, counting the title frame as 1.
Thirty-three frames.

## Terms this chapter defines

| Term | Defined on | How it is defined |
|---|---|---|
| pretraining | 3 (glossed), 4 | one objective run over a very large corpus, with no labels, which then stops |
| corpus | 3 (glossed), 4 | the text pretraining ran over |
| supervised fine-tuning | 5 | training on pairs of request and written response, so the model learns the shape of an answer |
| demonstration | 3 (glossed), 5 | the response a person writes as the one that should have come out |
| **system prompt** | 5 | standing text placed before your message, which this stage trains the model to treat as instruction |
| rater | 3 (glossed), 6 | a paid person working to a written instrument, usually with no contact with whoever wrote it |
| instrument | 6 | the written document a rater works to; glossed in the same sentence as *rater* |
| preference, comparison | 3 (glossed), 8 | a person choosing between two responses to one request |
| rubric | 9 | the set of dimensions a response is scored against |
| dimension | 9 | one scored axis; six of them, and they conflict |
| unassessable | 11 | the band for a claim that would take longer than the time box to check |
| reward model | 19 | a function fitted to a finite set of comparisons, which then scores any response |
| **RLHF** | 20 | generate, score with the reward model, adjust to score higher, repeat |
| **Constitutional AI** | 23 | the named instance: the model critiques and revises its own responses against written principles |
| **RLAIF** | 23 | the general pattern, with the model standing in for the rater |

Terms in bold were only in the speaker notes when the chapter was first drafted. The room hears
all four of them constantly outside this course, so each was moved onto a frame.

## Terms inherited from Chapter 1

Used here, defined there, not redefined: token, model, parameters, weights, network, training,
inference, knowledge cutoff, session, context window, probability, distribution.

Parameter counts on frame 20 use Chapter 1's ochre, because they are parameters. **No second colour
system is introduced.** The four Chapter 1 colours answer one question — what kind of number is
this — and a competing scheme for evidential strength would dilute the one that works. Evidential
strength is carried by the footer instead.

## The term-order check

Run over frame bodies with the speaker notes stripped, because the rule is about what the room
reads. It found five hits, all on frame 3, and all of the same kind: **the pipeline map names its
five stages before any of them is expanded.**

That is deliberate and it is the pattern Chapter 1 uses on its own preview — Wolfram's parenthetical
deferral, which the teaching research recommends taking directly. It was implicit; frame 3 now
states it: *each name on this diagram is defined on the frame that expands it*.

With frame 3 read as the gloss point, every term first appears on or after the frame that defines it.

## Evidence balance

Measured across the thirty-three frames, because this chapter's whole problem is that it rests on
two bases that must not be conflated.

| | Frames | What it means |
|---|---|---|
| `\citesource` | 8 | rests on a published source, tagged `[V]` in `references.md` |
| `\provenance{instrument}` | 15 | a structural observation from the five annotation instruments, with its document count printed on the frame |
| `\provenance{derived}` | 7 | follows from earlier frames, or is the instructor's synthesis |
| `\provenance{observation}` | 1 | established by running it |
| `\provenance{none}` | 2 | title frame and the exercise run sheet |

Eight distinct published sources: `ouyang2022`, `stiennon2020`, `bai2022hh`, `bai2022cai`,
`yang2023`, `ye2024`, `li2023emotion`, `vaugrante2024`. All `[V]`; `check-frames.py` refuses
anything else.

**The `instrument` form is new and was built for this chapter.** `CLAUDE.md` §1a is explicit that
the `[E1]`–`[E4]` scale is not the `[V]`/`[P]`/`[U]`/`[X]` scale, that an `[E1]` finding never earns
a `[V]`, and that the two must never be converted into one another. The form states on its face that
the observation is not citable and never becomes a citation, and its note carries the count — *three
of five documents* — so evidential strength reaches the room as a number rather than as a tag it
would have to be taught.

## Frames without a visual

Thirty-one of thirty-three carry one: nine figures, nineteen TikZ diagrams, two tables, one
animation slot.

- **Frame 1** is the theme's full-bleed title page.
- **Frame 33** is text only, matching Chapter 1's closing frame — a summary beside a set of open
  questions, which is the structure the instructor asked for.

## Animation slot

| Frame | Slot | What goes in it | Who makes it |
|---|---|---|---|
| 2 | F, 1600 × 422 px | a base model given the running question, continuing with more questions instead of answering | instructor, capture |

**This is the chapter's phenomenon-before-explanation frame** and it currently reserves a box with
nothing in it. Chapter 1 learned this the hard way: its greedy-decoding frame argued a mechanism it
never demonstrated, and it was the one frame the instructor marked confusing.

If no base model is reachable, a documented transcript is acceptable and the frame must say which
it is.

## What is deliberately not taught

Five findings are held back and sit in the facilitator notes as answers to questions that will get
asked, each resting on one document: score-and-rationale mismatch, the Goodhart machinery and its
countermeasures, execution as ground truth, minimum citation counts, and role variation by client.

Also excluded, on the same grounds — each rests on one document and would be taught as general if it
appeared on a frame: non-directional rating axes, adjacent-band audit tolerance, and
English-proficiency filtering of raters. Any of them can be taught as *one instrument's solution to a
real problem*, which is honest and nearly as interesting.

## Open

- **`TODO(verify)` on frame 24.** The brief wants test-case hardcoding as a concrete reinforced
  reward hack, attributed by a vendor to reward hacking during training. The system card carrying
  that quote is `[P]` and has not been read. It does not reach a frame until it has been.
- **The rating exercise** is three frames here and its full specification lives in
  `assets/rating-exercise/README.md`, which has not been rewritten for the current chapter. The
  changes implied by two further documents are listed in `ch02-annotation-findings.md` §13 and are
  not yet applied.
