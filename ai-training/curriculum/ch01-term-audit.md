# Chapter 1 — term audit

Required by `HANDOFF.md` §6.5: every technical term the chapter uses, with the slide where it is
defined. A term with no defining slide is a defect.

Frame numbers are positions in `slides/beamer/01-substrate.tex`, counting the title frame as 1.

**Rewritten 2026-08-20** when the chapter moved to Beamer and was restructured against the
instructor's review: the order now follows the pipeline diagram left to right, one running example
(the stirrups sentence) replaces two, and a new frame carries the minimisation-to-distribution
bridge. Twenty-four frames, up from twenty-one.

## Terms defined in this chapter

| Term | Defined on | How it is defined |
|---|---|---|
| prompt | 2 | the text you send |
| artificial intelligence | 3 | umbrella label for a family of methods, with no single technical definition |
| machine learning | 3 | **defined in the figure, not the text** — behaviour fitted from data instead of written down as rules |
| neural network | 3, 5, 9 | a fitted function built from layers of weighted sums; named on 9 as a borrowed word |
| language model | 3 | a model fitted to predict text |
| large language model, LLM | 3 | a neural network fitted to predict text; acronym expanded where it appears |
| the corpus | 4 | the text training ran over, and what it decides about where the model is reliable |
| model | 5 | a stored list of numbers together with the program that reads them |
| parameters | 5 | the numbers in that list |
| weights | 5 | named on the frame as the other word for parameters |
| network | 5 | the layered arithmetic that reads the parameters |
| size (of a model) | 5 | how many parameters it has |
| training | 6, 7 | the phase in which the numbers are changed; then, concretely, a search for values minimising total error |
| inference | 6 | running the finished numbers on your text |
| knowledge cutoff | 6 | the date training stopped |
| session | 6 | one continuous conversation, from opening it to closing it |
| error, minimising error | 7 | the summed discrepancy between the fitted function and the data, shown as residuals |
| surprise | 8 | how low a probability the model gave the token that actually came next |
| distribution | 8 | what training shaped, because surprise cannot be defined without a probability |
| token | 8 (glossed), 12 (defined) | a chunk of characters taken from a fixed list settled before training |
| learning | 9 | the search of frame 7, given as a borrowed word |
| context window | 11 | everything the model is given, up to a fixed maximum |
| standing instructions | 11 | text placed in the window at the start of every session |
| vocabulary | 12 | the fixed list the tokens are taken from |
| token ID | 12 | the integer each token corresponds to; a label, not a quantity |
| logits | 14 | the raw scores the network emits, one per token |
| pass | 14 | one run of the network over the window |
| attention | 15 | a weighted sum in which each earlier position's weight comes from comparing it against the position being scored |
| transformer | 15 | the arrangement of arithmetic built out of that operation |
| softmax | 16 | the function converting scores into probabilities that add to one |
| temperature | 16, 19 | the divisor on the scores inside softmax, annotated on the equation itself |
| greedy selection | 17 | taking the top-scoring token every time |
| drawing, sampling | 18 | taking one token according to the probabilities |
| tool | 22 | a program the system runs alongside the network, whose result is written into the window |

## The checks that were actually run

Three gates, all mechanical, all currently passing.

- **`check-frames.py`** — every frame carries a footer; every cited key resolves and is tagged
  `[V]`. 24 of 24.
- **Overfull vbox count** — an overfull vbox is precisely a frame whose content runs into the
  chevron footline. It found **seventeen** such frames on the first build. Now zero.
- **Term order** — every term first appears on or after the frame that defines it, checked over
  frame bodies with the speaker notes stripped, because the rule is about what the room reads.

Three defects were found by the term-order check and fixed:

- **token** appeared on frame 8, two frames before it is glossed. Frame 8 now glosses it in the
  same sentence, which is the rule.
- **pass** appeared on frame 11, three frames before frame 14 defines it. Frame 11 now says
  "every time the network runs".
- **drawn** carried two meanings — a token *drawn from a list* on frame 12, and a token *drawn from
  a distribution* on frame 18. One word, two senses, in a chapter that is careful about vocabulary.
  Frame 12 now says *taken from*; **drawn** is reserved for sampling.

**Two accepted exceptions, on the title frame.** *Language model* and *model* appear in the
chapter's subtitle before frames 3 and 5 define them. A chapter cannot be titled without naming its
subject.

## Frames without a figure

Twenty-three of twenty-four carry a visual: eleven figures, four TikZ diagrams, two animation
slots, one annotated equation, and the full-bleed title page.

**Frame 24 is text only**, by design — the instructor asked for the closing frame to be a summary
beside a set of open questions rather than a diagram. The Slidev version carried an annotated
pipeline diagram there and this one does not, which is a deliberate trade rather than an oversight.

## Animation slots

| Frame | Slot | What goes in it | Who makes it |
|---|---|---|---|
| 2 | F, 1600 × 422 px | a question typed, the reply appearing left to right at natural speed | instructor, screen recording |
| 17 | F, 1600 × 422 px | temperature zero, run long enough that the output falls into a loop | instructor, screen recording |

Frames 15, 18, 19 and 20 carry a static figure with an `animation A3/A4/A5/A7 replaces this`
marker, so the PDF stays complete whether or not the animation is ever built. Specification in
`ch01-animation-slots.md`.

## Terms deliberately not used in this chapter

| Term | Why it is absent |
|---|---|
| KV cache | The brief has it here so Chapter 7 can price it. Its payoff is six chapters away. Chapter 7 defines it where it is priced. `assets/figures/01-kv-growth.png` is generated for that chapter and used by no deck today. |
| positional encoding | Changes no decision this audience will make. Named once, in the closing speaker note, as excluded. |
| multi-head attention | Same. |
| query, key, value | Vaswani's role names. They appear only in a speaker note giving the paper's exact wording. Putting them on the slide would leave three terms undefined in exchange for nothing. |
| activations | Slide 7 says "what happens inside the network" instead, so the brain-comparison line needs no new term. |
| noise ceiling | Slide 7 spells it out inline — "a ceiling estimated from how noisy the recordings are" — rather than naming it. The appendix names it. |
| chunk (working memory) | Belongs to the units point, which moves to Chapter 10 where the context window is live. |
| embedding | Not needed for any claim this chapter makes. |
| hallucination, sycophancy, fine-tuning, RLHF | All belong to Chapters 2 and 5 and none is used here. |

## Forward references this chapter makes

| On slide | Points to | For |
|---|---|---|
| 7 | appendix (`slides/08-brain-and-model.md`) | the brain-comparison literature in full |
| 10 | Ch 7, Ch 13 | pricing tokens |
| 18 | Ch 10 | the standing instruction file |
| 19 | Ch 12, Ch 14 | tools and retrieval |
| 20 | Ch 10, Ch 18 | memory, and provider retention |
| 21 | Ch 2, 4, 5, 6, 7, 9, 10, 13 | where each of the six facts is spent |

## Citation status

Two slides carry a footer.

- **Slide 7** — `schrimpf2021`, `hadidi2026`, both `[V]`. The line rests three checkable claims on
  them: the work is correlational, the headline is normalised by a ceiling, and an author of the
  original co-wrote the re-analysis.
- **Slide 12** — `vaswani2017`, `[V]`, §3.2 read, wording quoted in the speaker note.

The other nineteen slides carry no footer. They are definitional, or they restate a mechanism the
chapter has already built. `CLAUDE.md` house style requires a footer on every slide and §1b names
one exception, which is not this one. **The rule and this chapter cannot both stand as written.**
See `peer-review-19-chapters.md`, finding A8. The instructor should rule on it.

## Outstanding captures

Three figures are marked SCHEMATIC or ILLUSTRATIVE on their own faces and should be replaced or
supplemented before delivery.

- **Slide 2** — a real screenshot of the interface, replacing the drawn panel.
- **Slides 9 and 10** — a real tokeniser run, on this sentence and on a MATLAB snippet, and on the
  group's own vocabulary for the cost bars.
- **Slides 15 and 17** — one prompt run five times, and the same prompt at temperature zero run
  long enough to show the repetition. Both recorded with the model ID and the date.

Slide 7's figure is illustrative by construction — the parameter values are drawn from a fixed seed
and the movement is the claim, not the numbers. It needs no capture.

The chapter is deliverable without the three captures. It is weaker without them, because slide 17
argues repetition from the mechanism and never shows it happening.

---

## Round 2 — rebuild of 2026-08-24

24 frames. Rebuilt against the instructor's 52 PDF annotations, the blind peer review's 27
findings, and rulings C1/C2/C3.

**Structure.** Tokens now precede the training-objective frame, which deleted the inline gloss that
existed only to work around the old order. The pipeline map opens the mechanism. Context and
session frames are adjacent, with the tools frame merged into the context frame. One frame cut
(C1). Two brain-comparison frames added (C2), back to back.

**Terms newly defined on the slide face**, each previously missing or trapped in a figure:

| Term | Frame | Was |
|---|---|---|
| neural network | 3 | defined only inside a figure, rendering at roughly 4 pt |
| corpus | 4 | used with a definite article, never defined |
| session | 6 | defined only in a speaker note, then used in a headline |
| surprise | 12 | used as a plain-English word; now $-\log p$ for the token that came next |
| logit | 13 | used before definition |
| transformer | 14 | glossed with an em dash, not defined |
| greedy decoding | 16 | called "greedy selection" inside an invalid derivation |

**Evidence balance after the rebuild**

| Footer | Frames |
|---|---|
| `\citesource` | 4 — vaswani2017, anthropic-code-exec, schrimpf2021+hadidi2026, fedorenko2024 |
| `\provenance{definition}` | 7 |
| `\provenance{schematic}` | 4 |
| `\provenance{computed}` | 3 |
| `\provenance{derived}` | 3 |
| `\provenance{observation}` | 2 |
| `\provenance{none}` | 1 |

**Four `TODO` markers are visible on slides**, not hidden: `TODO(verify)` on the reliability claim,
`TODO(cite)` on greedy degeneration, and `TODO(capture)` on the token-count figure and the
tokeniser frames. Each marks a claim that has not reached `[V]`.

## Checks run, round 2

| Check | Result |
|---|---|
| Frame check: every frame has a footer, every key `[V]` | PASS, 24 frames |
| LaTeX errors | 0 |
| Overfull vboxes | 0 |
| **Overfull hboxes** (content off the side of the slide) | **0 — newly gated; the gate was blind to these until 2026-08-22** |
| Headlines at or under 8 words | 24 of 24 |
| Figure aspect ratios in band | all, with the two brain figures exempt |
| One value per quantity in the running example | PASS — p(absent) reconciled |

## Known gaps carried forward

- Frame 4's reliability claim has no `[V]` source. Ruling C3 keeps it at position 4, where it
  cannot be derived from anything earlier.
- The greedy-degeneration frame rests on a recording that has not been made.
- Token counts in the cost figure are schematic; no tokeniser has been run.
- Peer-review item 9, deck-wide in-figure text size, is deferred pending measurement.
- Peer-review item 19, the COI flag on `anthropic-code-exec`, is still unverified.
- Two animation slots remain empty.
