# Chapter 1 — final build plan

<!-- decision: ch01-final-build | status: adopted | supersedes: ch01-revision-round-2 -->

**Goal:** one Chapter 1 PDF carrying every accepted change from three sources — the instructor's
52 PDF annotations, the blind peer review's 27 findings, and rulings C1/C2/C3 — plus two new
brain-comparison frames.

**Inputs:** `ch01-revision-plan.md` (annotations), `ch01-peer-review.md` (blind review),
rulings in-session 2026-08-24.

---

## 1. What "all the changes" resolves to

30 edits, 1 cut, 1 merge, 2 new frames. Net frame count unchanged at 24.

| Source | Accepted | Superseded / dropped |
|---|---|---|
| Instructor annotations (52) | A1–A17 | A18 (cut brain line) — superseded by C2, which brings the brain back as two frames |
| Peer review blocking (8) | all 8 | #1 already done (the `\fitwidth` fix) |
| Peer review strong (12) | 10 | #17 moot (frame cut by C1); #20 declined — reviewer named its own cost and it fights C3 |
| Peer review optional (7) | 3 | #21 moot, #22 superseded by A1, #24 superseded by A8 |
| Rulings | C1, C2, C3 | — |

**Item 9 (deck-wide figure text too small) is deferred, not dropped.** It is computed from
`figsize`/`fontsize` ratios rather than measured, and it sits against the instructor's "the figure
is excellent". It gets measured after this build, not guessed at during it.

---

## 2. The new frame order

The reorder is the load-bearing change and everything else waits on it. Moving a frame breaks any
sentence that says "next" or "previous", so structure lands before prose.

| New | Old | Frame | What changes |
|---|---|---|---|
| 1 | 1 | Title | — |
| 2 | 2 | The answer arrives a piece at a time | Fix the pronoun (rev 26). Replace the cut line with what a prompt may contain — UTF-8 characters, spaces, typos all count |
| 3 | 3 | Language models are one branch of AI | **Neural-network definition moves into the body** (PR 8); it currently exists only inside a figure at ~4 pt |
| 4 | 4 | Reliability follows how much was written | Rephrase in place (C3). Define **corpus** on the slide. `TODO(verify)` — see §5 |
| 5 | 5 | A model is numbers plus a program | Tighten so it excludes a lottery draw and a JPEG: the numbers were **arrived at by fitting** (A4, PR 25) |
| 6 | 6 | Training set those numbers and then stopped | Remove the internal contradiction (A5). New graphic (A6). Define **session** in the body (PR 10) |
| 7 | 7 | Training searches for the smallest total error | Make the training/inference split explicit (§2 of the revision plan). "does the same search" → **"runs the same kind of search"** (PR 12). Define total squared error. Drop the left graph |
| 8 | 9 | Training changed the numbers, nothing else | Brain line removed here; it returns as frames 22–23 |
| 9 | 10 | Text becomes numbers, then scores, then text | **Flowchart only** (A2). Fix the false promise "every box gets its own slide" (PR 13) |
| 10 | 12 | Tokens come from a fixed list | Add the *shear* split example (A13). Say whose vocabulary. Distinguish integers from token IDs |
| 11 | 13 | Token count follows frequency, not length | Say **where** the frequency is measured (A14). Soften the absolute claim (PR 5). Keep `TODO(capture)` |
| 12 | 8 | Training minimises surprise at the next token | **Now sits after tokens** (A1), so the inline gloss is deleted. Technical term for *surprise*, defined as −log p (A10, PR 11). Hedge that this is pretraining's objective (PR 11) |
| 13 | 14 | The network returns one score per token | "four shown" → **"eight shown"** (PR 2). Figure split so this frame shows **logits only** (PR 3). Define **logit** (A15) |
| 14 | 15 | Attention decides which earlier tokens matter | Rewrite the weighted-sum definition; define **transformer** |
| 15 | 16 | Softmax turns scores into probabilities | **Fix the arithmetic** (PR 4). Add the T → 0 limit note (PR 14). Fix or delete the stale figure note (PR 15). Define **softmax** (A15). "Worked case" becomes a subheading (A17) |
| 16 | 17 | Always taking the top token repeats | Retag `observation`, add `TODO(cite)` — the derivation is invalid and the claim is empirical (PR 6) |
| 17 | 18 | The token is drawn, not taken | Kept (C1). Absorbs anything worth keeping from the cut frame |
| 18 | 19 | Temperature sets how sharply the top score wins | Reuse the softmax equation with **T** highlighted; show low-T and high-T |
| 19 | 20 | Each token is appended and everything reruns | Delete "Four passes here…" (A16). Fix the note's "every pass costs the same arithmetic" (PR 18) |
| 20 | 11 + 22 | Everything given sits in the context window | **Tools merged in** (A8). Context frames now adjacent (A3) |
| 21 | 23 | The session ends and the window goes | **Rewrite the false claim** — the network keeps nothing; the transcript persists and is re-sent (PR 16) |
| 22 | — | **NEW — the brain, annotated** | C2 |
| 23 | — | **NEW — the same map, for the model** | C2, closing on Fedorenko |
| 24 | 24 | What we covered | Update to the new content |

**Cut:** old frame 21, *Two runs give different answers* (C1). Its payoff was a callback to frame 2's
puzzle, and that puzzle line is itself being cut, so nothing is left to pay off.

**Deleted throughout:** em dashes (A11), and every "defined on slide N" cross-reference (A9) — the
reorder removes the need for the main one.

---

## 3. The two new frames

Design ruled by the instructor: image only, one-word labels, everything else spoken.

**Frame 22 — the brain.** One generated illustration, **no text in the image**. Nine regions
colour-coded, each with a one-word label for what it controls in people.

**Frame 23 — the model.** The same illustration, the same nine colours, the words swapped for the
model's counterpart. The identical silhouette is deliberate: it is what makes the closing line land.

| Colour | Region | Human | Model |
|---|---|---|---|
| 1 | Brainstem | vital | prediction |
| 2 | Basal ganglia | reward | reward |
| 3 | Hypothalamus | drives | drives |
| 4 | Amygdala | threat | refusal |
| 5 | Hippocampus | memory | context |
| 6 | Neocortex | knowledge | weights |
| 7 | Fronto-parietal | reasoning | thinking |
| 8 | Language network | language | language |
| 9 | Sensory cortex | senses | tokens |

Closing line on 23, bold, with `\citesource{fedorenko2024}`:

> **Language and thought are separable systems in people — a double dissociation — and one set of
> weights in the model.**

All reasoning goes in `\note{}`. The instructor delivers it orally.

**The labels are overlaid in LaTeX, not generated.** Generated text is unreliable and the label
*positions* carry the anatomical claim. The generated asset is illustration only; the technical
content stays auditable. This is also what keeps the frames inside `production-plan.md` §4a, which
bars generated imagery for technical content.

---

## 4. Figures

| Figure | Action |
|---|---|
| `01-logits.png` | **New.** Panel 1 of `fig_scores` alone, for frame 13. Resolves PR 3 — the logits frame currently displays the softmax panel |
| `01-scores.png` | Keep both panels, now used only on frame 15 |
| `01-training-pipeline.png` | **New.** Unlabelled data → foundation model → applications, replacing frame 6's cutoff graphic (A6) |
| `01-softmax-T.png` | Restore to frame 15 or delete the note that points at it (PR 15). Its numbers must be recomputed under PR 4 |
| `01-brain.png` | **New, generated via agy/Nano Banana.** Mid-sagittal cutaway, no text |
| `01-fitting.png` | Drop the left panel (§2) |

---

## 5. Rule-1 exposure, stated plainly

Three claims will not have a `[V]` source when this build finishes.

| Frame | Claim | Handling |
|---|---|---|
| 4 | Reliability tracks how much was written on a topic | `TODO(verify)`. C3 keeps it at position 4, where it cannot be derived. Chapter 5's degradation sources are the likely home |
| 11 | Token counts, as drawn | `TODO(capture)` — the generator's own docstring says no tokeniser was run |
| 16 | Greedy decoding falls into loops | `TODO(cite)`, retagged `observation`. Search terms recorded |

None of these reaches a slide as an unmarked assertion. All three are visible in the deck.

---

## 6. Execution order

Each step names its check. A step is not done until its check passes.

1. **Structure** — reorder, cut old 21, merge old 22 into old 11.
   *Check:* 24 frames; `check-frames.py` passes; no frame says "next"/"previous" about a frame that moved.
2. **Figures** — split `fig_scores`, build the pipeline graphic, trim the fitting figure.
   *Check:* aspect audit in band for every new PNG; `01-logits.png` shows one panel.
3. **Brain frames** — generate, retrieve, verify, overlay labels, write both frames.
   *Check:* artifact present in `agy-artifacts/`; no text in the image; nine labels on each frame.
4. **Prose and definitions** — all remaining A-items and peer-review items.
   *Check:* term-order pass on slide faces with notes stripped — every term defined before substantive use.
5. **Arithmetic** — the softmax worked case recomputed against the committed figure data.
   *Check:* one value for p(absent) across the deck; recompute both by hand and by script.
6. **Gates** — build, term audit, stamp.
   *Check:* 0 LaTeX errors, 0 overfull boxes of either kind, frame check passes, aspect band clean.

---

## 7. What holds this up

**The image.** Steps 1, 2, 4, 5 are independent of it and start now. Step 3 waits on the skill
install and on the instructor's review of the generated brain — he asked to see it before it lands
on a slide.

If the image is rejected, frames 22–23 ship as a TikZ schematic instead and the rest of the chapter
is unaffected.

---

## 8. Risks

| Risk | Mitigation |
|---|---|
| The reorder breaks a forward reference the check cannot see | Term-order pass is step 4's check, run on slide faces with notes stripped |
| The softmax fix propagates into figures that reuse `CAND_PROBS` | Recompute from the committed table, not from the slide; grep every frame for a probability literal afterwards |
| Merging tools into the context frame overfills it | `\fitwidth` handles width; height is caught by the vbox gate |
| Generated anatomy is wrong | Labels are mine, not generated, and region positions get checked against a source before placement |
| Two new frames push Chapter 1 long | Not a criterion |

## 9. What this plan does not cover

- **Peer-review item 9**, deck-wide figure legibility. Deferred to measurement after this build.
- **Peer-review item 19**, the COI flag on `anthropic-code-exec` — still unverified.
- The two empty animation slots and the tokeniser capture, both instructor work.
- Chapters 2 and 3, whose headlines remain over the 8-word cap.
