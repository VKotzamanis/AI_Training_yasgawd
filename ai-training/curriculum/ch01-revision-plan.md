# Chapter 1 — revision plan against the 2026-08-21 annotations

<!-- decision: ch01-revision-round-2 | status: adopted | supersedes: none -->

**Source:** `REVIEWD/01-substrate_REVIEWD_VK.pdf`, 52 annotations across 22 of 24 pages.
Stamp `sha256=afec89ab3633e66f` — annotations are against the current build, not a stale one.

**Status: NOT EXECUTED.** Two items conflict with locked rules and need a ruling first (§3).

---

## 1. Accepted without qualification

These are correct, and three of them are defects I should have caught.

| # | Frame | Change | Why it is right |
|---|---|---|---|
| A1 | 8, 12, 13 | **Move tokens (12, 13) before the training-objective frame (8).** | Frame 8 uses *token* substantively and glosses it inline as *"— a chunk of text from a fixed list, defined on slide 12 —"*. That gloss is an admission the order is wrong. Moving the frames deletes the gloss and fixes the sequence in one move. |
| A2 | 10 | **Make the pipeline flowchart the introductory frame, before tokens. Flowchart only, no body text.** | It is the map. A map shown after the territory is a summary, not a map. |
| A3 | 11, 23 | **Group the context frames: context window, then what the window costs, then the window is discarded.** | Frame 23 currently sits eighteen frames after the concept it closes. |
| A4 | 5 | **Tighten the model definition.** "A long list of numbers together with the program that reads them" does not discriminate — a lottery draw satisfies it. Add what makes it a model: the numbers were *fitted to data to minimise prediction error*, and the program computes a *distribution over the next token*. | The definition has to exclude things that are obviously not models. |
| A5 | 6 | **Remove the internal contradiction.** The frame says training *"set those numbers and then stopped"* and then lists *"Training — the numbers are being changed"*. | Both cannot be true on one frame. |
| A6 | 6 | **Replace the graphic.** The current one shows the knowledge cutoff; the frame is about how the numbers get calibrated. Proposed: unlabelled data → foundation model → applications. | Correct, and it is the standard picture. Constraint: name RLHF, do not teach it — that is Chapter 2's. |
| A7 | 21 | **Cut.** Two runs, same scores, different answers. | Frame 2 already states it and frame 18 already explains it. Third statement of one idea. |
| A8 | 22 | **Merge tools into the context frame.** | Tools write into the window; that is the context frame's subject. |
| A9 | all | **Delete cross-references of the form "defined on slide N".** | A slide should not send the reader to another slide. |
| A10 | 8 | **Replace "surprised" with the technical term.** | It is doing real work as a gloss for the training objective and should be named properly, with the plain-English gloss demoted to the notes. |
| A11 | 16, 3 | **Remove em dashes.** | House style call. |
| A12 | 4 | **Rephrase the reliability frame.** *"It is reliable where a great deal has been written"* → the prediction can be fluent and still wrong, and what governs it is how much and how good the training text was on that topic. | The current phrasing invites the reading that volume alone determines correctness. |
| A13 | 12, 13 | **Add the worked token example: why *shear* may split.** | Domain-relevant, checkable by the room, and it makes the fixed-vocabulary point concrete. |
| A14 | 13 | **Say where the frequency is measured** — in the tokeniser's training corpus, not in general English. | "Written where?" is a fair question the frame does not answer. |
| A15 | 14, 15 | **Define *logit* and *softmax* at first use**, as labelled bullets. | The term audit claims they are defined; they are used before they are. |
| A16 | 20 | Delete *"Four passes here. A paragraph is a few hundred..."*. Keep the figure. | Redundant with the figure. |
| A17 | 16 | Demote *"worked case"* to a subheading. | Formatting. |
| A18 | 9 | **Cut the brain-comparison line entirely.** | The brain has not been introduced at that point, and the material belongs where response formation is taught. |

---

## 2. Accepted with a correction to the mechanism

The teaching goal is right; the stated mechanism is not, and installing it would have to be undone later.

**Frame 7 — the fitting frame.**

The annotation proposes: *"The model does not solve A·X=B, it tries discrete numbers and finds the error and spits back the number with the smallest error."*

The conclusion — the model predicts rather than verifies — is correct and is the point of the frame.
The mechanism is not. **Trying values and minimising error is training. It happens once, before
delivery.** At inference the model does one forward pass and produces a distribution; it does not
search. If the room leaves Chapter 1 believing the model searches at answer time, Chapter 5
(degradation) and Chapter 7 (what a run costs) both have to undo it first.

**Proposed instead:** keep the y = 2x + 1 fitting picture as what *training* does, and add one line
making the split explicit — the search happens during training and stops; at inference the fitted
numbers are used once. The "it does not verify, it predicts" conclusion is then reached without
the wrong mechanism.

Also accepted on this frame: define total squared error before using it, and drop the left-hand
graph.

---

## 3. Needs a ruling — conflicts with a locked rule

### R1. The provenance footers

The annotation says **remove** *"Definition — this term is introduced by the course. No external
source."*

`CLAUDE.md` hard rule **1c** says every slide carries a footer, ruled 2026-08-20 — *"Footer in all
slides"* — and it is enforced mechanically by `check-frames.py`, which fails the build on a frame
without one. Deleting them breaks the build and reverses a ruling.

**Read of the actual complaint:** what is on the slide is a full sentence in the footer, which is
visually loud on a frame the annotations elsewhere ask to simplify. That is a verbosity problem,
not a footer problem.

**Proposal:** keep the footer, compress it to a single quiet word — `definition`, `derived`,
`computed` — in small grey type. Rule satisfied, clutter gone.

**Ruling needed:** compress, or genuinely remove and amend rule 1c?

### R2. Headline length

The annotation says **5–6 words max**, and separately that headings should be **much smaller**.

Measured: **19 of 23 headlines exceed 8 words; five run 15–17.** The complaint is justified.

The conflict is with the assertion-evidence finding in `research-slide-design.md`: sentence
headlines outperformed topic-phrase headlines on recall, 79% against 69%. It is the one slide-design
choice in this project with converging experimental support, and Chapter 3 was rebuilt on it.

**The research is about sentences versus topic phrases, not about length.** A short assertion keeps
the benefit:

| Now | Words | Compressed, still an assertion | Words |
|---|---|---|---|
| A token is a chunk of characters taken from a fixed list settled before training | 15 | Tokens come from a fixed list | 6 |
| Training searches for the numbers that make the total error smallest | 11 | Training minimises total error | 4 |
| Taking the top-scoring token every time makes the text repeat | 10 | Greedy decoding repeats itself | 4 |
| The window is discarded when the session ends | 16 | The session ends; the window is discarded | 7 |

**Proposal:** cap at 8 words, keep subject + finite verb, reduce the frametitle font size.

**Ruling needed:** is 8 words with the assertion preserved acceptable, or do you want topic phrases
at 5–6 words and the recall finding set aside?

---

## 4. Corrections to specific annotations

| Annotation | Status | Reason |
|---|---|---|
| *"Attention is a technical term? I doubt it is."* | **It is.** | Vaswani et al. 2017, `[V]` in `references.md`, body read 2026-08-20. The term stays; the *definition* on frame 15 is genuinely confusing and gets rewritten. |
| *"is 'greedy' the technical term?"* | **Yes.** | Greedy decoding. Stays. |
| *"temperature is a SETTING, not calculated. Right?"* | **Correct.** | It is a sampling parameter set before the run. |
| *"Opus 1M: 1M tokens, i.e. 45B 'the' words"* | **Wrong number.** | "the" is one token, so 1M tokens is about 1M instances of it. Verified vendor figure for a 1M window: **≈555k words, ≈2.5M characters**. Use that. |
| *"illustrations with agy-nano-banana"* | **Blocked by your own rule.** | `production-plan.md` §4a bars generated imagery for technical content — unauditable, no provenance. As decorative topic markers only it is arguably inside the carve-out. Your call; flagged because you set the rule. |
| *"add some examples (RLHF)"* on frame 9 | **Name only.** | RLHF is Chapter 2's central mechanism. Naming it forward is fine; teaching it here means Chapter 2 opens on covered ground. |
| *"Niche terms cost more but ground the prompt"* | **Half supported.** | The cost half is arithmetic. "Ground the prompt" is a claim about output quality with no source. Either derive it or drop the clause. |

---

## 5. Not flagged in the annotations, but outstanding

- **Two animation slots are still empty** (Slot F, 1600 × 422 px). One is on the temperature frame.
- **The tokeniser frames still say SCHEMATIC** — they need the capture.
- **Frame 2 starts the non-determinism thread** that frames 18 and 21 continue. Cutting 21 (A7)
  leaves 2 and 18, which is right, but the duplication begins at 2 and the annotation only caught it
  at 21.
- **A live caveat worth checking before it reaches a slide:** current models may reject the
  `temperature` parameter outright at the API. The chapter teaches temperature as a concept, which
  is legitimate, but if the room tries to set it and gets an error that is a bad first experience.
  **Not verified against a fetched primary source yet — do not put it on a slide until it is.**

---

## 6. Execution order, once R1 and R2 are ruled

1. Ruling on R1 and R2. Nothing starts before this — both touch every frame.
2. Reorder (A1, A2, A3) and cut (A7, A8, A18). Structure before prose; rewriting a frame that is
   about to be cut is wasted.
3. Rebuild the two replaced figures (A6 pipeline, frame 7 fitting split).
4. Frame-level prose and definitions (A4, A5, A9–A17, §2).
5. Re-run the gates: frame check, 0 LaTeX errors, 0 overfull vboxes, aspect band, term audit.
6. Re-stamp, rebuild the PDF, hand back.

## 7. What this plan does not cover

- The independent peer review, which is running separately and may reorder items 2–4.
- The two captures and the animation slots, which are instructor work.
- Any change to Chapter 2 or 3 that a Chapter 1 reorder forces. The thread map is re-read at step 5,
  not before.
