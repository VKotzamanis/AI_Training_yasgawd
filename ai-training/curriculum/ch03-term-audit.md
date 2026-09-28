# Chapter 3 — term audit

Required by `HANDOFF.md` §6.5: every technical term the chapter uses, with the frame where it is
defined. A term with no defining frame is a defect.

Frame numbers are positions in `slides/beamer/03-control.tex`, counting the title frame as 1.
Twenty-three frames.

## Terms this chapter defines

| Term | Defined on | How it is defined |
|---|---|---|
| lever | 2, 4 | a prompt change aimed at a dimension the rating layer scored |
| attachment | 3, 15 | a file, image or pasted page placed in the window alongside the message |
| **reliable knowledge cutoff** | 16 | the date through which a model's knowledge is most extensive and reliable, distinguished from the training-data cutoff |
| few-shot example | 9 | a worked instance of the output shape, supplied instead of a description of it |
| negative example | 10 | an instance of the output you do not want, which still enters the window as an instance |
| role | 11 | a stated persona in the system prompt; documented to focus behaviour and tone |
| effort | 13 | a five-level setting biasing how readily the model thinks, documented for the API and the coding tool |
| per-message steering | 13 | wording in a single turn that biases the same thinking decision |
| working | 14 | the intermediate claims a verdict rests on, each independently checkable |
| verdict | 14, 19 | a judgement with no working attached |
| constraint stacking | 20 | several requirements that cannot all hold, one of which is dropped without report |
| leading question | 18 | a question whose preferred answer is visible in its wording |
| portability | 21 | whether a prompt tuned on one model holds on another |

The term in bold is the one the room is most likely to have met in a wrong form. "Knowledge
cutoff" is used loosely everywhere to mean one date; the vendor publishes two, and only one of
them is the date after which answers stop being reliable. Frame 16 uses the precise term.

## Terms inherited from earlier chapters

Used here, defined there, not redefined.

**From Chapter 1:** token, context window, model, parameters, training, inference, session,
probability, statelessness.

**From Chapter 2:** system prompt, rater, rubric, dimension, instruction following, truthfulness,
harmlessness, formatting, verbosity, tone, reward model, RLHF.

The six dimension names carry the whole structure of this chapter and none of them is redefined
here. Frame 4 names all six in one figure and points back rather than re-teaching them, which is
the check that Chapter 2 actually did its job.

## Colour discipline

**No number colours appear in this chapter.** The four-colour code answers one question — what
kind of number is this — and Chapter 3 contains almost no numbers. Using teal or ochre here for
emphasis would break the code's meaning. Emphasis is `\kw{}`, which is bold and black.

Two colours are used structurally in the figures and they are not number colours: UH red marks
the weak or failing side of a comparison, teal the improved side. That pairing is consistent
across all eight figures.

## Evidence balance

| Footer | Frames | Which |
|---|---|---|
| `\citesource{anthropic-prompting}` | 9 | 5, 6, 7, 8, 9, 10, 11, 12, 21 |
| `\citesource{anthropic-thinking}` | 1 | 13 |
| `\citesource{anthropic-models}` | 1 | 16 |
| `\citesource{wei2022}` | 1 | 22 |
| `\provenance{derived}` | 9 | 2, 3, 4, 14, 15, 17, 18, 19, 20 |
| `\provenance{none}` | 2 | 1, 23 |

**Eleven of the twelve citations are vendor documentation about the vendor's own product.** That
is the correct primary source for how to steer that product and it is still one company's account
of its own behaviour. Frame 22 says so on its face rather than leaving the reader to add up
footers, and frame 23 makes it the chapter's closing open question.

The ten `derived` frames are the chapter's own reasoning from Chapter 2's mechanism. Three of them
— 18, 19, 20 — are the anti-patterns, and each is derived rather than cited because the argument
is that a rated behaviour, requested backwards, is what you get. That follows from Chapter 2 and
needs no external source.

## Checks run

| Check | Result |
|---|---|
| Frame check: every frame has a footer, every key `[V]` | PASS, 23 frames |
| LaTeX errors | 0 |
| Overfull vboxes (content running into the footline) | 0 |
| Figure aspect ratios inside the 3.4–4.7:1 band | 8 of 8 PASS |
| Banned constructions in slide bodies | 0 |
| Full-sentence assertion headlines | 22 of 22 titled frames |
| Every defined term has a defining frame | 13 of 13 |

The headline count is the one worth recording against the old deck, which had **seven** assertions
out of seventeen.

## Known gaps

- **Frame 16's dates are version-fragile.** They were fetched 2026-08-20 and are flagged for
  re-fetch in the delivery week, in `references.md` and in the frame's own speaker notes.
- **Frame 12's verbosity caveat is version-fragile** for the same reason and carries the same flag.
- **No animation slot is reserved in this chapter.** Chapters 1 and 2 each carry one. Nothing here
  obviously needs motion; the strongest candidate would be frame 20, showing a constraint being
  dropped as the answer is produced, and it is not built.
