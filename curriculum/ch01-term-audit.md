# Chapter 1 — term audit

Required by `HANDOFF.md` §6.5: every technical term the chapter uses, with the slide where it is
defined. A term with no defining slide is a defect.

Slide numbers are positions in `slides/01-substrate.md`, counting the title slide as 1.
**Renumbered 2026-08-20** when the brain slide was inserted at position 7; everything from the old
slide 7 onward shifted by one.

## Terms defined in this chapter

| Term | Defined on | How it is defined |
|---|---|---|
| prompt | 2 | the text you send |
| artificial intelligence | 3 | umbrella label for a family of methods, with no single technical definition |
| machine learning | 3 | behaviour fitted from data instead of written down as rules |
| neural network | 3, 4, 7 | a fitted function built from layers of weighted sums; named on 7 as a borrowed word |
| language model | 3 | a model fitted to predict text |
| large language model, LLM | 3 | a neural network fitted to predict text; acronym expanded where it appears |
| model | 4 | a stored list of numbers together with the program that does arithmetic with them |
| parameters | 4 | the numbers in that list |
| weights | 4 | named on the slide as the other word for parameters |
| network | 4 | the layered arithmetic that reads the parameters |
| size (of a model) | 4 | how many parameters it has |
| training | 5, 6 | the phase in which the numbers are changed; then, concretely, a search for parameter values minimising total error |
| inference | 5 | running the finished numbers on your text |
| knowledge cutoff | 5 | the date training stopped |
| session | 5 | one continuous conversation, from opening it to closing it |
| error, minimising error | 6 | the summed discrepancy between the fitted function and the data, shown as residuals |
| learning | 7 | a search for values that lower the error; given as a borrowed word |
| token | 8 (glossed), 9 (defined) | a chunk of characters drawn from a fixed list settled before training |
| token ID | 8, 9 | the integer each token corresponds to |
| vocabulary | 9 | the fixed list the tokens are drawn from |
| logits | 11 | the raw scores the network emits, one per token |
| pass | 11 | one run of the network over the tokens in the window |
| attention | 12 | a weighted sum in which each earlier position's weight comes from comparing it against the position being scored |
| transformer | 12 | the arrangement of arithmetic built out of that operation |
| softmax | 13 | the function converting scores into probabilities that add to one |
| temperature | 13, 14 | the divisor on the scores inside softmax, annotated on the equation itself |
| sampling, sampler | 15 | drawing one token according to the probabilities |
| greedy selection | 17 | taking the top-scoring token every time |
| context window | 18 | the tokens supplied to one pass, up to a fixed maximum |
| standing instructions | 18 | text placed in the window at the start of every session |
| tool | 19 | a program the system can run alongside the network, whose result is written into the window |

## The check that was actually run

A term appearing in the table above is not enough; it has to appear for the first time on or after
the slide that defines it. That is checked mechanically over the slide bodies with the presenter
notes stripped, and it passes for every term.

Two defects were found by that check and fixed:

- **softmax** appeared inside the slide-11 figure, two slides before slide 13 defines it. The
  figure's panel title now reads "the same scores turned into probabilities".
- **tool** was used on slides 5 and 20 in the everyday sense of "the thing you are using", which
  collides with the narrow definition on slide 19 — a program the system runs alongside the
  network. Both were reworded.

**Two accepted exceptions, on the title slide.** *Language model* and *model* appear in the
chapter's subtitle before slide 3 and slide 4 define them. A chapter cannot be titled without
naming its subject, and the title slide says on its face that nothing is assumed.

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
