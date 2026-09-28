CALIBRATION: PASS (rubric v1)

# Review: REVIEWD/AI_TRAINING.pdf (slides 1–13, 16) — 2026-08-27 — reviewer: claude-opus-5[1m]

Purpose: calibrate `FOR-REVIEW/RUBRIC.md` v1 against the approved exemplar. The deck is
the reference target, not the object under judgment. Findings below are recorded for the
author; the rubric's behaviour on them is the actual output, and it is in
**Rubric calibration notes** at the end.

Slides 14, 15 and 17 were not opened (instructed skip: 14–15 are placeholders replaced by
`CH1_NETWORK_SLIDES.md`, 17 is empty).

**Text source.** The main deck's `.pptx` was not available; only the PDF export was. All
quotes are taken from `pdftotext -layout` output of `AI_TRAINING.pdf` and carry that
extraction's line numbers (`pdftotext L<n>`) alongside the slide number, since the rubric's
quote format assumes an `.md` source. Runs of spaces produced by two-column layout are
collapsed to one; no other character is altered.

---

## Topic ledger

| topic | opens (slide) | closes (slide) | reopened at |
|---|---|---|---|
| AI / ML / NN / LLM as nested method families | 2 | 2 | — |
| AI as non-analytical (vs closed-form) method | 2 | 2 | — |
| contextual text prediction ≠ ground truth | 3 | 3 | — |
| corpus (definition) | 4 | 4 | named again 5–8 as an input; never redefined |
| reliability (definition) | 4 | 4 | — |
| corpus-coverage vs answer-failure regimes | 4 | 4 | — |
| training / ERM (name + alias) | 5 | 7 | — (mechanism deferred to 16, out of range) |
| knowledge cutoff | 5 | 5 | — |
| prompt / conditioning sequence | 5 | 5 | — |
| context window, $O(k_{max}^2)$ compute | 5 | 5 | — (cost closed at 17, out of range) |
| inference / autoregressive decoding | 5 | 5 | — (loop completed at 20, out of range) |
| model = parameters + program | 6 | 6 | — |
| parameters / weights / model size | 6 | 7 | — |
| token (definition) | 6 | 9 | verbatim callback at 8 — see calibration note R-1 |
| network = layered architecture | 6 | 6 | — (equations at 14–15, out of range) |
| two-stage parameter setting | 7 | 7 | refined at 10 ("multi-stage"), mapped at 11 |
| static weights / training stops before the prompt | 7 | 7 | — |
| tokenizer behaviour: rare strings and typos shatter | 8 | 9 | — |
| token ID vs token count; cost model | 9 | 9 | — |
| how frontier capabilities are acquired | 10 | 10 | — (answered at 11 and Supp §S13) |
| API, MCP (definitions) | 10 | 10 | reappear as boxes at 12–13 in a different role |
| training-time component map (brain ↔ stack) | 11 | 11 | — |
| session-start component inventory | 12 | 12 | — |
| prompt-processing flow | 13 | 13 | — |
| training as an optimization problem (loss, softmax) | 16 | 16 | — |

Twenty-five topics, twenty-five single open intervals. No topic in the reviewed range has
two open intervals once calibration note R-1 is applied.

---

## Slide messages

- **1** — Chapter 1 of an AI literacy course, on LLM architecture: what an LLM is and how
  to understand one.
- **2** — AI, ML, NN and LLM are nested families of non-analytical methods, each defined by
  the mechanism it uses, each with an everyday example.
- **3** — Two agents answer the same physics question differently; the failing one
  reproduced memorized textbook phrasing instead of computing the forces, and it sounded
  just as confident as the correct one.
- **4** — Whether a model is confidently correct, confidently wrong, or admits ignorance
  depends on how well the topic is covered in the training corpus and on the model's
  reliability.
- **5** — Five operating terms — Training, Knowledge Cutoff, Prompt, Context Window,
  Inference — each with its formal technical alias and, where one exists, its equation.
- **6** — A model is a package: a long array of parameters set in training, plus a program
  that runs them against token vectors to emit a probability distribution.
- **7** — Parameters are set in two training stages, unsupervised next-token training then
  human alignment, and training stops before your prompt is ever seen.
- **8** — A token is the unit of text the model actually receives, and how a string splits
  depends on how often it occurred in the corpus, which is why typos cost more.
- **9** — Token count, not token ID, is what costs money and time, and word length does not
  predict token count.
- **10** — Frontier capabilities come from multi-stage training with specialized networks
  whose learned behaviours consolidate into the deployed parameter set, plus external tools
  reached over APIs and MCP.
- **11** — The components that set the model up map one-to-one onto brain functions:
  tokenizer/input, pretraining/prediction, encoders/media, SFT/response structure,
  RLHF/reward, reward model/value, refusal direction/harm avoidance.
- **12** — Before you type, a session already contains the model plus the software around
  it — tokenizer, guardrails, system prompt, sampler, tool interfaces, token budget — again
  mapped onto brain functions.
- **13** — When your prompt arrives, that machinery runs in order: retrieve session
  context, think in a scratchpad, delegate to tools, sample, generate the response.
- **16** — Training is an optimization problem you can set up in four moves: assume a
  program with random weights, turn its scores into probabilities, define the loss, and
  evaluate it over corpus pairs.

Fourteen slides, fourteen statable Messages. No slide triggered the "no statable Message"
branch of class F.

---

## Findings

Sorted blockers → major → minor. **No blocker-severity findings in any class.**

### [cal-001] F major — slide 3
Quote: "First Agent's answer: … Second Agent's answer:" / "'Net hydrostatic force is zero.'
… 'Net hydrostatic force is downward.'" / "The model stumbled because it relied on
memorized text patterns rather than calculating the physical forces from first principles."
(`pdftotext` L45, L47, L50–53)
Why it fails: the slide sets two contradictory answers side by side, then diagnoses "the
model" in the singular without ever saying which of the two stumbled or what the correct
answer is. The reader must hold "which one is right?" open through the Root Cause and
Inherent LLM Risk bullets, and a reader who guesses wrong takes away an inverted lesson.
Fix direction: state the correct answer on the slide — with a perfect watertight seal there
is no water beneath the base, so the water contacts only the top and side faces, the side
pressures cancel horizontally, and the top face carries $\rho g h A$ downward; the net
vertical hydrostatic force is **downward**, and the first agent's "zero" is the failure,
produced by the memorized "no water underneath → no buoyant force" pattern. One line
naming the failing answer closes it.

### [cal-002] T major — slide 4
Quote: "Model Reliability" … "Confidently Correct … Confidently Wrong … Blissfully
Ignorant" … "Corpus Size" (`pdftotext` L68–70, L75–78); definition on the same slide:
"Reliability: A dimension of AI trustworthiness representing the property of an AI system
to consistently maintain intended behavior and satisfy performance criteria under expected
operational distributions." (L81–82)
Why it fails: the two horizontal arrows share one visual convention — label at the tail,
arrowhead marking the direction of increase. The dark-red arrow puts its head at the left,
so corpus coverage increases toward Common Knowledge, which is correct. The green arrow
puts its head at the right, which asserts that reliability is *highest* at "Blissfully
Ignorant" and *lowest* at "Confidently Correct". Under the slide's own definition the
ordering is the opposite at both ends.
Fix direction: no single monotone arrow can carry this quantity — under the printed
definition reliability runs Confidently Correct (high) → Confidently Wrong (lowest, it both
fails the performance criterion and breaks intended behaviour) → Blissfully Ignorant
(middle, it fails the criterion but keeps intended behaviour). Replace the arrow with three
point markers at the three regimes, or reverse the arrowhead to match the corpus axis and
annotate the middle regime as the minimum. **CONFIRMED** — basis: the Reliability
definition printed on slide 4, read during this review; the contradiction is internal and
needs no external source.

### [cal-003] S4 major — slide 16
Quote: "You define a loss function (residual calculation)." (`pdftotext` slide-16 extract
L16)
Why it fails: the formula printed directly beneath it is the mean negative log-likelihood,
$\mathcal{L}(\theta) = -\frac{1}{n}\sum \log P(\mathbf{x}^{(i)}_{k+1}|\mathbf{x}^{(i)}_{1:k};\theta)$.
"Residual" is a standard term for $y-\hat{y}$ in least squares — the exact object this
audience fits weekly — and it does not appear in that formula. The gloss sends the reader
looking for a difference that is not there. Worse, Chapter 1's own supplement puts
"residual" on a different object: §S12 derives $\nabla_\mathbf{z}\mathcal{L} = P -
\mathbf{e}_y$ and calls *that* "the same object as the residual $\hat{y}-y$ in least
squares, promoted from scalar to distribution". As written, slide 16 and §S12 attach the
same standard term to two different quantities.
Fix direction: gloss the loss as "negative log-likelihood / cross-entropy — the mean
surprise of the token that actually came next", and reserve "residual" for the gradient,
where §S12 already puts it. Correct term: negative log-likelihood (equivalently
cross-entropy loss).

### [cal-004] C major — chapter-level, definitional slides 2, 4, 5, 6, 10
Quote (representative): "Corpus: The general and unstructured collection of training
material used to develop an LLM's baseline knowledge (i.e., training data)." (slide 4,
L80); "Model Context Protocol (MCP): An open protocol standardizing how external tools
(e.g., Gmail) and data sources (e.g., GitHub) are made available to an LLM's operating
environment." (slide 10, L208–209)
Why it fails: the C class makes five fields mandatory at each definitional home. The
reviewed range holds **17 definitional homes** (slide 2: AI, ML, NN, LLM; slide 4: Corpus,
Reliability; slide 5: Training, Knowledge Cutoff, Prompt, Context Window, Inference;
slide 6: Model, Parameters, Token, Network; slide 10: API, MCP). Field 1 (one-sentence
positive definition) is present in 17 of 17. Field 2 (signal contract with type/shape) is
fully present in 2 (Prompt, Inference) and partial in 2 (Model, Network). Field 3
(necessity — the failure when the component is removed) is present in 0. Field 4 (observable
capability in the deployed product) is present in 0; the Knowledge Cutoff hint is the
nearest thing to it. Field 5 (location: pipeline step, stage, scope) is partial in 4 and
complete in 0. Applied literally, the rule yields **66 major C findings against the approved
exemplar**.
Fix direction: this is a rubric defect, not a deck defect — see calibration note C-1. The
deck should not be edited against it. The five-field strip is the *supplement's* own
contract, stated in `CH1_SUPPLEMENT.md` lines 15–18, and it is honoured there in every §S
section; the deck's job is one-sentence definitions with a technical alias.

### [cal-005] C major — chapter-level, agenda footer (every slide 2–13, 16)
Quote: "AI-101 & TERMS … TOKENS & CONTEXT … LIVE DEMONSTRATION … THE MODEL IN LLM …
NETWORK & OUTPUT … SUMMARY & TIPS" (`pdftotext` L37–38 and on every subsequent slide)
Why it fails: the footer promises six sections and marks the active one with the dinosaur
glyph. Five are paid — AI-101 & TERMS (2–5), THE MODEL IN LLM (6–7), TOKENS & CONTEXT
(8–9), NETWORK & OUTPUT (10–13, completed by the 14–20 spec), LIVE DEMONSTRATION (16).
**SUMMARY & TIPS has no payoff slide** anywhere in the reviewed range, in the seven-slide
replacement spec, or in the supplement, and PDF page 17 is empty.
Fix direction: author the closing section, or drop it from the footer. Note the scope
limit: I was given slides 1–13 and 16 plus the 14–20 spec, so a summary slide living beyond
spec slide 20 would not be visible to me.

### [cal-006] T minor — slide 8
Quote: "'Reinforcement' → ␣reinforcement → 117657" / "'Reinforcment' → ␣rein | for | c |
ment→ 17855, 1938, 66, 508" (`pdftotext` L166–168)
Why it fails: both ID sequences are correct for the lowercase strings shown after the first
arrow, but not for the capitalized headwords in quotes. BPE does not case-fold, so the
displayed chain implies a normalization step the tokenizer does not perform. Measured on
o200k_base: `' reinforcement'` → `[117657]` (1 token, matches); `' Reinforcement'` →
`[79152, 22298]` (2 tokens, `' Rein' + 'forcement'`). `' reinforcment'` → `[17855, 1938,
66, 508]` (matches all four IDs exactly); `' Reinforcment'` → `[79152, 1938, 66, 508]`.
Fix direction: lowercase the two headwords, or keep the capitals and print the capitalized
IDs — the pedagogical point (one token becomes four when the word is misspelled) survives
either way, and holds for the capitalized pair too (2 → 4). **CONFIRMED** — basis:
`tiktoken` 0.14.0, encoding `o200k_base` (merge table SHA-256
446a9538…cfb1a2d), executed locally 2026-08-27 23:20; source logged in `REFERENCES.md`.

### [cal-007] T minor — slide 4
Quote: "Corpus Size" (axis label, `pdftotext` L68–70), against the slide's own opening
line: "It depends on the topic's availability on the Corpus and the model's Reliability."
(L67)
Why it fails: corpus size is a single scalar property of a model ("trained on N trillion
tokens") and cannot vary along an axis whose three stops are Common Knowledge, Niche
Topics and Obscure/Unknown. What varies is how much of that fixed corpus concerns the
topic — which is exactly what the slide's opening sentence says, and what its own Corpus
definition ("the general and unstructured collection of training material") implies. As
labelled, the axis invites the model-selection heuristic "bigger corpus → more reliable",
which is not the slide's claim.
Fix direction: relabel the axis "Coverage of the topic in the Corpus" or "Topic frequency
in the Corpus". **CONFIRMED** — basis: the opening sentence and the Corpus definition on
slide 4 itself, read during this review.

### [cal-008] F minor — slide 5 (dependency lives on slide 6)
Quote: "Prompt(Conditioning Sequence): The initial input token sequence, 𝐱{1:𝑘}, passed to
the model to condition its autoregressive predictive distribution … determining the
probability distribution over all possible subsequent tokens." (`pdftotext` L97–98); also
"Context Window(Sequence Length): The maximum number of tokens, 𝐱{1:𝑘max}, the model can
process in a single pass." (L101) and "Training … parameters are iteratively updated" (L91)
Why it fails: three of slide 5's five definitions are built on "token" and one on
"parameters". Both receive their definitions on slide 6 — "Token: The fundamental unit of
text (word or piece of word) processed by the model." and "Parameters: Also called weights."
(L124–125) — one slide later, with token expanded again on 8–9. Slide 5 therefore consumes
two concepts defined only downstream.
Fix direction: minor by deliberate design — the deck's section order puts AI-101 & TERMS
before THE MODEL IN LLM, both words carry enough colloquial meaning to survive one slide,
and the gap is exactly one slide. Either add a forward pointer ("token: defined next
slide") or accept it. Recorded because the rule fires mechanically, not because the deck
should be resequenced. See calibration note F-1.

---

## Coverage checklist

| promise | source | status |
|---|---|---|
| "What a Large Language Model (LLM) is and how we can understand them better." | slide 1 subtitle | paid across 2–13, 16 |
| AI-101 & TERMS | footer agenda | paid 2–5 |
| THE MODEL IN LLM | footer agenda | paid 6–7 |
| TOKENS & CONTEXT | footer agenda | paid 8–9 |
| NETWORK & OUTPUT | footer agenda | opened 10–13; closed by spec slides 14–20 (out of range) |
| LIVE DEMONSTRATION | footer agenda | paid 16 (Case Study 1) + `llm_lab.m` |
| SUMMARY & TIPS | footer agenda | **unpaid — [cal-005]** |
| "Large (Corpus) ✓ Language (Text) ✓ Model ?" | slide 6 headline | paid on slide 6 |
| "Input & Output: What is a Token? (1/2)" | slide 8 headline | paid by 9 "(2/2)" |
| "Frontier LLMs have many capabilities. How do they acquire them?" | slide 10 | paid Supp §S12 + §S13 (out of range) |
| "How are they able to understand text, images, and sound at the same time?" | slide 10 | paid Supp §S14 (out of range) |
| "What gives a model its 'personality' and 'morality'?" | slide 10 | paid Supp §S13 (out of range, explicitly) |
| "How does a model decide how to structure its response?" | slide 10 | paid Supp §S13 (SFT ↔ Response Structuring) |
| which agent stumbled, and why | slide 3 | **unpaid — [cal-001]** |
| what a T-Decoder is | slides 12–13 boxes | paid spec slide 17 + Supp §S4a |
| what a tokenizer is | slide 8 footnote, 11–12 boxes | paid Supp §S1 |
| backpropagation, SGD | slide 5 Training definition | paid Supp §S12 |
| SFT, RM, RLHF, RLVR, refusal direction | slide 11 boxes | paid Supp §S13 |
| multimodal encoders | slide 11 box | paid Supp §S14 |
| guardrails, agent harness, effort level, scratchpad, token balance, session context | slides 12–13 boxes | paid Supp §S16 ledger |

Twelve terms that the reviewed slide range leaves undefined are paid by
`CH1_NETWORK_SLIDES.md` and `CH1_SUPPLEMENT.md`. Filing them as C findings would have been
wrong — see calibration note C-2.

---

## Topics exported

The full ch01 export — deck 1–13 and 16, spec slides 14–20, supplement §S1–§S17 — is
written to `FOR-REVIEW/rubric-reports/TOPICS-LEDGER.md` under
`## ch01-approved`, 51 lines. Sequential reviewers read that file, not this section.

From the reviewed slide range specifically, later chapters may assume without re-explaining:
the AI/ML/NN/LLM nesting; prediction-vs-ground-truth and the confidence failure mode; corpus
and reliability; the slide-5 terminology set with its aliases; model = parameters + program;
the two training stages and static weights; token, token ID vs token count, and the cost
model; API and MCP; the three brain-map component inventories; and the Case Study 1
formulation of training as loss minimization.

---

## Checks not run

1. **Slides 14, 15, 17 were not opened.** Instructed skip.
2. **The main deck's `.pptx` was never available** — only `CH1_SLIDES_14-20.pptx` is in
   `REVIEWD/`. Everything here comes from the flattened PDF export, so animation build
   order and element z-order are invisible to me.
3. **Slides 3 and 9 render with overlapping text in the PDF.** On slide 3 the prompt
   quotation, the two agent answers and the analysis bullets occupy the same region; on
   slide 9 the cost chart shows axes, a duplicated "Tokens" axis title and stray "word /
   letters" legend text with no visible series. I treated both as export artifacts of an
   animated build and filed **no finding**. If the built slides really do show all elements
   at once, slide 3 is illegible and slide 9's chart is broken — check in PowerPoint. The
   rubric has no class for this, which is itself a calibration result (note X-1).
4. **Colour semantics on slide 3.** Red/green colouring may already mark the wrong and
   right answers; the overlap made this unresolvable from the render, so [cal-001] may be
   partly paid already. It is filed on the text, which does not name the failing answer.
5. **Slide-11/12/13 connector pairings were not re-derived.** §S16 itself states its
   pairings "were read off the slide's colour-matched connectors in the PDF render; confirm
   them against the source PPTX before shipping." I did not perform that confirmation.
6. **Slide 5's "Limited by VRAM in runtime" was not checked** against any vendor
   context-window specification. I judged it incomplete rather than wrong — the trained
   architectural ceiling on context length goes unmentioned — and filed nothing. A
   verification pass may reasonably disagree and open a T finding here.
7. **Slide 7's "<1%" alignment-data share was not verified** against any published
   training-data breakdown. Plausible; not filed.
8. **Slide 3's physics is my own derivation**, not a citation. I worked it by hand (sealed
   base ⇒ water contacts top and sides only ⇒ side pressures cancel ⇒ top face carries
   $\rho g h A$ downward). No fluid-mechanics text was opened, so [cal-001]'s statement of
   the correct answer is unsourced.
9. **The brain-region ↔ function pairings on slides 11–13 were read for plausibility
   only** (VTA↔reward signalling, amygdala↔harm avoidance, thalamus↔input relay,
   pre-SMA↔response structuring, prefrontal cortex↔value-based decision). No neuroscience
   source was opened. No finding was filed, and no clearance should be read into that
   silence.
10. **The supplement's verification-pending citations** (Kingma & Ba 2015, Srivastava et al.
    2014, Dosovitskiy et al. 2021, Shazeer et al. 2017, the RLVR term's origin) were not
    checked. They sit outside the reviewed slide range.
11. **No draft chapter was reviewed.** One approved exemplar can show that the classes do
    not fire destructively on good input. It cannot show that they fire correctly on bad
    input — the false-negative rate of rubric v1 is entirely unmeasured by this exercise.

---

## Verdict

**usable-with-fixes.** No unresolved blocker. The deck carries fourteen statable Messages
across fourteen slides, twenty-five topics each with a single open interval, mechanically
locatable section boundaries, and a numeric layer that survives recomputation — every token
split and token ID on slides 8–9 reproduces against o200k_base, `permeability` and
`geotechnical` are both twelve letters and split 1 versus 3 tokens as claimed, `' stirrups'`
really does split `' stir' + 'r' + 'ups'` with `r` at ID 81, and slide 16's loss, softmax
and dataset expressions are all correct as written. The eight findings are eight one-line
edits: name the failing answer on slide 3, fix one arrowhead and one axis label on slide 4,
lowercase two headwords on slide 8, add a forward pointer on slide 5, change one
parenthetical on slide 16, and author the promised closing section. Two of the eight
([cal-004], [cal-005]) are chapter-level rather than slide-level, and [cal-004] should be
resolved by amending the rubric, not the deck.

---

## Rubric calibration notes

The point of the exercise. Each note names what the rubric did and what should change.

### Gate

R: 0 findings. F: 2 (major, minor). S: 1 (S4 major). **Zero blockers in R, F and S → PASS.**
T: 3 (1 major, 2 minor), all CONFIRMED. C: 2 major, neither gate-affecting. No class
definition misfired badly enough to fail the exemplar, and the two that misfired at all
(C-contract, R's mechanical test) are diagnosed below.

### R-1 — the mechanical R test produces false positives that only step 6 kills

Three candidates fired and all three were dropped by the so-what test:

- **Slide 8's epigraph** repeats slide 6's token definition verbatim: "The fundamental unit
  of text (word or piece of word) processed by the model." (L157 vs L125). By the letter of
  R ("any topic whose ledger row shows more than one open interval") this is a reopening.
  It is in fact a section-opening callback, marked as a quotation, re-anchoring the
  definition at the top of the section that expands it. Deleting it would make the deck
  worse.
- **APIs/MCPs** appear at 10 (defined), 12 (present at session start) and 13 (invoked
  during processing) — three appearances, three distinct roles.
- **Slides 12 and 13 share seven boxes** (T-Decoder, Model, APIs/MCPs, System Prompt,
  Sandbox Scratchpad, Behavioral Conditioning, Peripheral Control) but their Messages are
  not the same sentence: 12 is the static inventory, 13 is the dynamic flow.

Recommendation: R needs an explicit carve-out, or the mechanical test needs a qualifier.
Suggested wording: *a verbatim restatement that opens the section which expands it is not a
reopening; a component recurring across a before/during/after sequence is not a reopening
unless its role is unchanged.* Without step 6, rubric v1 would have produced three false R
findings against the approved deck — and the exemplar is the definition of "correct", so
these are false positives by construction.

### F-1 — the forward-dependency rule fires on the exemplar and needs a severity floor

[cal-008] is a true positive by the letter of the rule and a non-problem in practice: the
gap is one slide and the words are colloquially available. As written, F offers no severity
ladder, so a reviewer with a different temperament could file the same observation as a
blocker and fail a chapter over it. Recommendation: state that a forward dependency spanning
one slide, on a term with an adequate everyday meaning, is minor; reserve major and blocker
for dependencies that span sections or that carry a technical meaning the everyday word
contradicts.

### C-1 — the five-field contract is unsatisfiable by the deck and must be scoped

This is the largest calibration result. Applied literally, the C contract produces **66
major findings against the approved exemplar** (17 definitional homes × 5 fields, minus 19
fields actually present — see [cal-004] for the field-by-field count). A rule that flags the
reference target 66 times is not measuring the target.

The diagnosis is available in the chapter's own materials. `CH1_SUPPLEMENT.md` lines 15–18
state: "Every component section opens with the same five-row strip, before any equation:
what the component **is**, the **signal** it converts, what fails without it, what it
**enables** in the deployed product, and where it **sits**." That is the C contract,
verbatim, and the supplement honours it in all seventeen §S sections. The rule was authored
for a prose companion documenting *components on a signal path*, and it was then applied to
deck slides that introduce *terms*.

Recommendation: split the class. **C-coverage** (a concept used but never defined anywhere;
a promise with no payoff) applies everywhere and is what caught [cal-005]. **C-contract**
(the five fields) applies only where a component with an input→output signal path receives
its definitional home, and only in prose companions — never to a slide whose job is a
one-sentence definition plus a technical alias. Under that scoping the exemplar's deck
yields zero C-contract findings and the supplement yields zero, which is the correct
outcome for an approved chapter.

### C-2 — "anywhere" needs a scope statement

C says "a concept the chapter uses but never defines, anywhere". Adjudicating "anywhere"
against the reviewed slide range alone would have produced roughly twelve false C findings
— tokenizer, T-Decoder, backpropagation, SGD, SFT, reward model, RLHF, RLVR, refusal
direction, multimodal encoders, guardrails, agent harness — every one of which is paid by
the coverage table in `CH1_NETWORK_SLIDES.md` (lines 393–413) or a §S section of
`CH1_SUPPLEMENT.md`. Recommendation: the rubric should say that *chapter* means every
artifact shipped as that chapter — deck, spec, supplement, lab handout — and that reviewers
must open the coverage tables before filing any C-coverage finding.

### T-1 — adjudicating T against the supplement killed a candidate

Slide 10's "The deployed model consolidates these learned behaviors into a unified parameter
space" reads, on the deck alone, like an overreach: reward models are discarded at
deployment and multimodal encoders remain separate networks. Both objections dissolve on
reading the supplement. §S13 says the RM "exists only during training and is discarded at
deployment" and then explicitly ratifies the slide: "Slide 10's 'unified parameter space' is
the result — SFT and the preference objectives write into the same θ". The slide says
*behaviours*, not *networks*, and it is right. I nearly filed this and did not.
Recommendation: fold this into the reviewer procedure — *before filing a T finding on a
slide, check whether a companion document adjudicates the same claim.*

### S-1 — S4 and T overlap on terminology errors; set a precedence rule

[cal-003] satisfies both S4 ("one standard term swapped for a different standard term with
a different meaning") and T ("a term used against its field definition"). The choice is not
cosmetic: S is a gate class and T is not, so the same observation can either count toward
the gate or not depending on which box the reviewer ticks. Recommendation: state a
precedence — suggested, *if the sentence would still be wrong after the term is corrected,
it is T; if correcting the term repairs the sentence, it is S4.* Under that rule [cal-003]
is S4, which is how it is filed.

### S-2 — S2 and S3 correctly did not fire, and that is the more useful result

The S2 calibration exemplar is an MCP sentence from a rejected draft. This deck's MCP
definition — "An open protocol standardizing how external tools (e.g., Gmail) and data
sources (e.g., GitHub) are made available to an LLM's operating environment" — transfers
real content and was not flagged. Slide 16's "Your only feedback comes from a game of hot
and cold" is an analogy that carries genuine technical structure (a scalar better/worse
signal, no closed form, no derivative of the target available) and was not flagged as S2
either. Nothing in the reviewed range triggered S1 or S3. S1–S3 discriminate correctly on
good input; whether they catch bad input is untested here.

### X-1 — no class covers production defects, and one had to be forced into T

[cal-002] is an arrowhead pointing the wrong way. It is a claim, so T accepts it, but the
fit is uncomfortable and a reviewer could reasonably have dropped it as "a figure issue,
not in the class list". The overlapping text on slide 3 and the broken chart on slide 9 have
no home at all and were left in *Checks not run*. Recommendation: either add a sixth class
for production and figure defects, or state in T that a figure's asserted claim — axis
direction, arrow semantics, connector pairing — is inside T, and add one line to the
procedure telling reviewers to note render defects without classing them.

### X-2 — the rubric has no positive test for what the exemplar does well

Two structural features carried this deck and neither is measurable under v1. The footer
agenda marks the active section with a glyph on every slide, which makes F's "a section
whose boundary cannot be located" mechanically checkable in one pass — a draft without such
a marker is strictly harder to review and the rubric cannot say so. And slide 5's
superscript-alias convention ("Prompt^(Conditioning Sequence)", "Inference^(Autoregressive
Decoding)") is precisely the "definitions carrying a technical alias" the Authority section
names as the target, yet no class rewards or requires it. Recommendation: add a short
"target features" checklist to the report skeleton — section markers present, aliases on
defined terms, one Message per slide — scored rather than flagged, so reviewers report what
a draft is missing rather than only what it does wrong.

### Severity vocabulary

R defines blocker/major/minor explicitly. F, T, C and S do not — C says "major by default"
and the rest say nothing. Since the calibration gate is *blocker-severity findings in R, F
and S*, and "blocker" is undefined for F and S, the gate currently rests on reviewer
temperament for two of its three classes. Recommendation: define the ladder once, for all
five classes, before the nineteen sequential reviews start.
