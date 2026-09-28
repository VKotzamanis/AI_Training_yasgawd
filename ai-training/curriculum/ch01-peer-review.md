# Chapter 1 — independent peer review, 2026-08-21

Run by an Opus 5 subagent, **blind to `REVIEWD/`**, so convergence with the instructor's
annotations is independent signal rather than anchoring.

27 findings: 8 blocking, 12 strong, 7 optional. 3 of 24 frames carry no defect.

## Claims I verified before relaying

| Claim | Verdict | Evidence |
|---|---|---|
| Frame 10 diagram overflows the slide; `build.sh` never catches it | **CONFIRMED, and systemic** | `01-substrate.log`: `Overfull \hbox (53.4261pt too wide)` at line 243. `build.sh:20` greps `Overfull \\vbox` only. Ch 2 carries three, worst **87.6 pt**. |
| Frame 14 says "the four shown" over an eight-bar figure | **CONFIRMED** | `01-substrate.tex:334` vs `gen-figures.py`: `labels = CANDIDATES + FILLERS` |
| The softmax worked case conflicts with the figures | **CONFIRMED** | Frame 16 uses z = 2.0/1.0 → p = 0.731. Figures use log(`CAND_PROBS`) and label p(absent) = 0.41. Frame 16's own method on the figure's data gives 0.603. Three values for one quantity. |
| Frame 16's note points at a figure that is not on the frame | **CONFIRMED** | `grep -c softmax-T 01-substrate.tex` = 0; the note describes three marked points. |
| `anthropic-code-exec` lacks a COI flag | **UNVERIFIED** | The `uh-sources.tex` field layout does not match the reviewer's description. Needs a look at `references.md` directly. |

## The gate defect

`build.sh` gates on `Overfull \vbox` and never on `Overfull \hbox`. Vertical overflow runs into
the footline; **horizontal overflow runs off the side of the slide and is invisible to the gate**.

| Deck | Overfull hboxes | Worst |
|---|---|---|
| 01-substrate | 2 | 53.4 pt (≈ 19 mm off-slide) |
| 02-formation | 3 | **87.6 pt (≈ 31 mm off-slide)** |
| 03-control | 0 | — |

Chapters 1 and 2 were both reported as clean builds. They were not. The fix is one line:

```sh
over=$(grep -cE 'Overfull \\(v|h)box' /tmp/uh-$deck.log)
```

This is the same failure class as hard rule 7 — a check that runs, passes, and asserts the wrong
string.

## Convergence with the instructor's annotations, reached independently

| Frame | Instructor | Reviewer |
|---|---|---|
| 5 | "So is LOTTO an LLM?" — definition does not discriminate | "A JPEG plus a decoder, an FE mesh plus a solver satisfy it" |
| 13 | "Written where?" | The claim is false as an absolute; the figure's own data gives r = +0.297 |
| 14 | "What is softmax? what is logit? define them" | The logits frame displays the softmax panel; the sum-to-one sentence is a probability claim under a logits headline |
| 10 | Make it the opening map, flowchart only | The map's ordering promise is false, and the diagram is clipped |
| 11/12/13 | Tokens before probability | Reorder to token → cost → window |
| 22 | Combine with the context frame | Both frames draw the same diagram |
| 18 | "Not even warranted" | Cut it; byte-identical figure to frame 14 |
| headlines | 5–6 words | 19 of 23 exceed 8; full compression table supplied, assertions preserved |

## Found by the reviewer, missed in the annotations

- **Frame 23** — annotated "Great slide". The column reads *"Discarded — the window, the
  conversation, anything you pasted."* Every attendee can reopen yesterday's conversation and read
  it back. What is discarded is the network's state; the transcript persists and is re-sent.
- **Frame 17** — the stated derivation is invalid. "Same input, same scores, same top token" is
  false pass-to-pass, because frame 20 establishes the input grows every pass. The frame is also
  tagged `derived` for what is an empirical finding with no source.
- **Frame 7** — "a language model does the same search" over least squares, which has a closed-form
  solution. Half this room fits lines for a living.
- **Frame 20 note** — "Every pass costs the same arithmetic" is false and contradicts Chapter 7.
- **`session`** is defined only in a speaker note, then used on the slide face of 11 and in 23's
  headline.
- **Frame 16** — T sits in the denominator and frame 17 demonstrates T = 0.

## Conflicts requiring a ruling

| # | Instructor | Reviewer | Notes |
|---|---|---|---|
| C1 | Cut frame 21 ("milked") | Keep 21, cut 18, fold 18's mechanism into it | Both agree one goes. Disagreement is which. |
| C2 | Frame 9 brain line — "remove completely" | Keep frame 9 as a two-column brain-comparison frame with its citation | |
| C3 | Frame 4 — rephrase in place, add examples | Move to after frame 8, where it becomes derivable instead of asserted | |

## Where I think the reviewer overreaches

- **Item 9** (all figure text renders at 3.7–5.5 pt) is computed from `figsize`/`fontsize` ratios,
  not measured. The reviewer says so. It also sits against the instructor's "the figure is
  excellent" on frame 20. Measure before acting.
- **Item 20** (move attention before scores) is contradicted by the reviewer's own stated cost, and
  cuts across the instructor's ordering. Optional at most.
- **Item 27** (the summary frame's headline is a topic phrase) is technically right and trivial.
