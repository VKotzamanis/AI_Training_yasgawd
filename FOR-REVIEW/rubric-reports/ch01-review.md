# Review: ai-training/slides/01-substrate.md — 2026-08-27 — reviewer: claude-opus-5[1m]

Reviewed under `FOR-REVIEW/RUBRIC.md` v1.1. Chapter-specific framing: this file is the
**superseded** Slidev draft of Chapter 1 (`CLAUDE.md` directory map: "`slides/*.md` — the
superseded Slidev decks, kept until each chapter is rebuilt"). The delivered Chapter 1 is the
`ch01-approved` entry of `TOPICS-LEDGER.md`. The verdict therefore answers a salvage question,
and overlap with the ledger is recorded as cross-chapter R so the non-overlapping remainder
becomes visible.

Slides counted from 1 at the first content slide (the title slide, line 18). The file contains
**21** slides; the frontmatter says 20 (line 9). Not audience-facing, recorded not flagged.

**The chapter's argument, stated in a form its author would accept:** a language model is a
stored list of numbers plus the program that does arithmetic with them; training set those
numbers by minimising an error over text and then stopped; one run of that program turns the
tokens in the context window into one score for every token in the vocabulary, and the answer
you see is produced by turning those scores into probabilities, drawing one token, appending it,
and running the whole thing again — so anything the product appears to do beyond that is the
sampler, a tool writing into the window, or something outside the network putting text back in.

---

## Topic ledger

| topic | opens (slide) | closes (slide) | reopened at |
|---|---|---|---|
| the generation loop (text → scores → text) | 1 | 16 | 8, 21 |
| progressive output | 2 | 2 | 16 |
| prompt | 2 | 2 | 18 |
| AI / ML / NN / LLM nesting | 3 | 3 | — |
| model = parameters + program | 4 | 4 | 7, 20 |
| parameters / weights / size | 4 | 4 | 5, 7, 20, 21 |
| network (the layered arithmetic) | 4 | 4 | 7, 11, 12 |
| training | 5 | 7 | — |
| inference | 5 | 5 | 16 |
| knowledge cutoff | 5 | 5 | — |
| session | 5 | 5 | 20 |
| error minimisation | 6 | 6 | — |
| borrowed biological names | 7 | 7 | 12 |
| brain comparison | 7 | 7 | — |
| pipeline map | 8 | 8 | 21 |
| token | 9 | 9 | 10, 21 |
| vocabulary | 9 | 9 | 11 |
| token cost | 10 | 10 | 16, 21 |
| logits / scores | 11 | 11 | 13, 15, 21 |
| pass | 11 | 11 | 16, 18 |
| attention / transformer | 12 | 12 | — |
| softmax | 13 | 13 | 14 |
| temperature | **13** | **14** | 15, 17 |
| sampler / sampling | 14 (speaker note) | 15 | 17, 21 |
| determinism of the network | 15 | 15 | 17 |
| decoding loop unrolled | 16 | 16 | 21 |
| greedy selection | 17 | 17 | — |
| context window | **11 (used)** | **18 (defined)** | 19, 20, 21 |
| standing instructions | 18 | 18 | — |
| tool | 19 | 19 | — |
| persistence / window discarded | 20 | 20 | 21 |

Two rows carry the mechanical signature the rubric names: **temperature** opens on 13 and is
delivered again as the whole of 14 ([ch01-009]); **context window** is used on 11 and defined on
18 ([ch01-012]).

## Slide messages

1. The chapter answers what a language model is and what one run of it computes, and previews the text → numbers → scores → text loop.
2. The reply arrives progressively because it is produced one piece at a time, and that observation is what the chapter explains.
3. Language models are one branch of a nested family — AI ⊃ machine learning ⊃ neural networks ⊃ LLMs.
4. A model is a stored list of numbers (parameters, also called weights) together with the program that does arithmetic with them.
5. Training changed those numbers and then stopped; inference only reads them, and the date training stopped is the knowledge cutoff.
6. Training is curve fitting — choose the parameter values that make the total error over the data smallest.
7. "Neural network" and "learning" are borrowed names for a search over numbers, and the brain comparison behind them is correlational.
8. The whole data path is text → tokens → network → one score per token → choose one → text, and it repeats.
9. A token is a chunk of characters drawn from a fixed list settled before training, and the network is handed integers rather than letters.
10. Technical vocabulary splits into more tokens than everyday English, and tokens are the unit of billing, of the context limit and of speed.
11. The network's only output is one score (logit) for every entry in the token list.
12. Attention is a weighted sum that decides which earlier tokens the next score leans on, and the Transformer is the arrangement built from it.
13. Softmax converts the scores into probabilities that add up to one.
14. Temperature sets how sharply the highest score wins.
15. The scores are deterministic; the run-to-run variation lives in the sampler, not in the network.
16. Each chosen token is appended and the whole program runs again on the longer text.
17. Taking the highest-scoring token every time makes the text repeat.
18. The network conditions on the tokens in the context window and on nothing outside it.
19. Tools write their results into the window as tokens, and the scoring step that follows is unchanged.
20. The window is discarded at the end of a session and the parameters are left as they were.
21. Six facts, and the chapter where each one is spent.

All 21 slides carry a statable one-sentence Message and every headline is an assertion rather
than a topic label. No F finding is triggered by this step.

---

## Findings

### [ch01-001] T blocker — slide 17
Quote: "Taking the top-scoring token every time is called **greedy** selection. Same numbers, same input, same output — so once a phrase recurs, the context that produced it recurs with it, and the top-scoring token is the same one again." (line 582); footer `<Cite own="derived" note="From determinism on slide 15. The live demonstration is still to be captured." />` (line 586); headline "## Taking the highest-scoring token every time makes the text fall into a loop" (line 567).
Why it fails: the derivation is invalid and is labelled `derived`. The network conditions on the whole prefix, which grows by exactly one token every pass, so the context never recurs — a phrase recurring is not the context recurring. Determinism over a strictly increasing input cannot produce a cycle, so nothing on slide 15 entails the conclusion. The slide is the chapter's one worked derivation, and it does not hold.
Fix direction: restate as an observation, not a derivation — greedy decoding empirically produces repetitive text; cite `holtzman2020`, already `[V]` in `ai-training/references.md` line 46 ("using likelihood as a decoding objective leads to text that is bland and strangely repetitive"), and respect the scope note recorded there (the paper measures maximisation-based decoding on 2019 models, not any current one); change the provenance from `derived` to a citation footer and keep the `TODO(capture)` recording. **CONFIRMED** — grounded in `references.md` line 46, opened this review, and in the argument executed above; `curriculum/ch01-term-audit.md` line 175 independently records this frame as "called 'greedy selection' inside an invalid derivation", and line 190 records a `TODO(cite)` opened against it.

### [ch01-002] R blocker — slides 3, 4, 5
Quote: "## Artificial intelligence names a family of methods, and language models are one branch of it" (line 83); "## A model is a long list of numbers together with the program that does arithmetic with them" (line 106); "## Training set those numbers and then stopped" (line 144).
Why it fails: all three slides are delivered in full by `ch01-approved`, at equal or greater depth — the four-band nesting with a consumer example per band (ledger: "AI / ML / NN / LLM hierarchy … Deck slide 2. **Do not re-derive the nesting**"); model = parameters + program with a literal numeric array shown and the count formula $|\theta|=\sum_\ell d_\ell(d_{\ell-1}+1)$ (ledger: deck slide 6, spec slide 15); training / inference / knowledge cutoff / static weights, the last as the diagram's explicit "Training Stops Here" boundary (ledger: deck slides 5 and 7). Re-delivering them spends session time on material the room already holds.
Fix direction: drop. Two lines do not duplicate and are worth keeping — the note that language models predate neural networks ("not every language model is a neural network — word-frequency models predate them", line 101) and the definition of **session** (line 171), which the ledger uses throughout but never records as defined.

### [ch01-003] R blocker — slides 8, 9, 10, 11
Quote: "## The whole path runs from text to numbers to scores to one piece of text, and then repeats" (line 267); "## A token is a chunk of characters drawn from a fixed list that was settled before training" (line 302); "## Technical terms are split into more tokens than common words" (line 341); "## The network returns one score for every token in the list, because scoring is the only operation it performs" (line 379).
Why it fails: covered by the ledger's seven-step pipeline (spec slide 20), token (deck slides 6 and 8) and byte-pair encoding (Supp §S1), the empirical tokenisation block with verified `o200k_base` splits and IDs (deck slide 8), token ID vs token count with the `permeability`/`geotechnical` pair and a linear cost chart (deck slide 9), and logit/unembedding with $\mathbf{z}=W_U\mathbf{h}_k^{(N)}+\mathbf{b}_U$ (spec slide 18). The delivered versions carry recomputed numbers; this draft carries schematics with `TODO(capture)` on both tokeniser slides (lines 335, 374) and an unnumbered vocabulary claim that is wrong ([ch01-007]).
Fix direction: drop. The draft's pipeline diagram is a lower-resolution version of the ledger's capstone (no embedding step, no decoder blocks) and adds nothing.

### [ch01-004] R blocker — slides 12, 13, 14, 15
Quote: "## Attention is the weighted sum that decides which earlier tokens the next score leans on" (line 402); "## Softmax converts the scores into probabilities that add up to one" (line 426); "## Temperature sets how sharply the highest score wins" (line 460); "## Two runs of the same prompt give the same scores and can still give different answers" (line 498).
Why it fails: the ledger delivers self-attention with $\mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^\top/\sqrt{d_k})V$, the causal mask and a worked 3-token example (spec slide 17, Supp §S4); softmax with temperature as $P_T(v)=e^{z_v/T}/\sum_j e^{z_j/T}$ with $T\to0$, $T=1$, $T>1$ behaviour, shift invariance and "T acts before normalization" (spec slide 18, Supp §S7); and the sampling-step location of output variance (spec slide 19), which the ledger marks "**Explicitly marked as never re-derived after this slide**". Slide 15 re-derives exactly that. The hosted-hardware caveat in slide 15's notes (line 537) is also already carried by the ledger as the non-associative parallel floating-point point.
Fix direction: drop slides 12, 14 and 15. Slide 13 has two salvageable fragments — the two-token worked case with the arithmetic shown, and the Boltzmann note (line 455, see [ch01-015]).

### [ch01-005] R blocker — slides 16, 18, 20, 21
Quote: "## Each chosen token is appended and the whole program runs again on the longer text" (line 543); "## The network is given the tokens in the context window and nothing else" (line 600); "## The window is discarded when the session ends and the numbers are left as they were" (line 665); "## Six facts, and where each one is used later" (line 703).
Why it fails: covered by the ledger's decoding loop and `<eos>` (spec slide 20, Supp §S9), context window with $\mathbf{x}_{1:k_{max}}$, the VRAM bound and $O(k_{max}^2)$ (deck slide 5, closed at spec slide 17), static weights as the "Training Stops Here" boundary described as "the anchor for every later 'the model does not learn from your conversation' claim" (deck slide 7), and the seven-step pipeline capstone (spec slide 20), which does slide 21's job with each step labelled by its defining slide.
Fix direction: drop. Two fragments survive — the parallelism note on line 562 (see [ch01-016]) and slide 21's forward-thread column, which maps each fact to the chapter that spends it; the ledger's capstone maps steps to defining slides and slide-12/13 boxes, not to later chapters.

### [ch01-006] T major — slide 12
Quote: "**Transformer** is the name given to the arrangement of arithmetic built out of that operation. The word is borrowed from biology as well, and the paper that introduced the operation is about machine translation." (line 408)
Why it fails: two errors in one sentence. (i) Neither "transformer" nor "attention" is a biological borrowing; the sentence extends slide 7's borrowed-from-biology framing ("as well") to a word that does not belong to it. (ii) The cited paper did not introduce the operation — Vaswani et al. treat attention as prior art and propose only the architecture built from it.
Fix direction: delete the biology clause; attribute the operation to Bahdanau, Cho & Bengio, *Neural Machine Translation by Jointly Learning to Align and Translate* (arXiv:1409.0473), whose abstract proposes "to extend this by allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word" — also a machine-translation paper, so the machine-translation point survives; keep `vaswani2017` for the definition it does own. **CONFIRMED** — both abstracts fetched this review (logged in `REFERENCES.md`): Vaswani et al. state "We propose a new simple network architecture, the Transformer, based solely on attention mechanisms" and, of prior work, "The best performing models also connect the encoder and decoder through an attention mechanism"; the abstract carries no biological or neuroscience terminology. Not verified: whether "attention" as a term entered machine learning from cognitive psychology.

### [ch01-007] T major — slide 9
Quote: "the **vocabulary** — tens of thousands of entries" (line 310); speaker note "**Do not say:** a specific vocabulary size. \"Tens of thousands\" is safe; a number is a per-model claim and none is cited here." (line 336)
Why it fails: understates current tokenisers by roughly an order of magnitude, and the note instructs the presenter to repeat it as the safe form. The claim feeds directly into slide 11's "one score for every token in the list" — the size of the output distribution is the quantity a trainee is being handed here.
Fix direction: say "on the order of $10^5$", or "roughly one to two hundred thousand for current models". **CONFIRMED** — computed this review with `tiktoken` 0.14.0: `o200k_base` `n_vocab` = 200,019 and `cl100k_base` = 100,277. The delivered chapter uses `o200k_base` (`calibration-ch1.md` line 202) and the ledger's Supp §S1 already states $|\mathcal{V}|\sim10^5$, so the draft also contradicts the delivered curriculum.

### [ch01-008] R major — slide 19
Quote: "A **tool** is a program the system can run alongside the network. It fetches or computes, its result is written into the window as tokens, and the pass that follows is the one already described." (line 648)
Why it fails: the ledger fixes this boundary twice — API and MCP defined at deck slide 10, and the weights-vs-harness ledger of Supp §S16, which places all 22 session boxes and defines tool use as "token emission plus outside code" with the reading rule that a capability changeable without retraining lives in the harness or the context. The draft's account is the same claim with less mechanism.
Fix direction: drop the definition. Salvage the delivery device in the speaker note (line 659) — whether a number was predicted or computed depends on whether a code tool ran, the vendor documents the routing, and the transcript shows which happened, so it is a check the room can run. That is a usable classroom check the ledger does not carry.

### [ch01-009] R major — slides 13, 14
Quote: slide 13 figure "alt=\"Probability of the higher-scoring of two tokens against temperature, with three points marked\"" (line 433) and note "The three marked points on the figure are 0.881 at T = 0.5, 0.731 at T = 1.0 and 0.622 at T = 2.0" (line 454); slide 14 "## Temperature sets how sharply the highest score wins" (line 460) with figure "alt=\"One set of scores rendered as probabilities at four temperatures, sharpening as temperature falls\"" (line 462).
Why it fails: within-chapter. Temperature is delivered twice — slide 13's headline is softmax but its figure is a temperature sweep at three values, and slide 14 is the same sweep at four values over more tokens. The ledger row for temperature opens at 13 and closes at 14. Two slides make one point, against the exemplar's one-message-per-slide target.
Fix direction: keep one. If slide 13 is kept for the worked arithmetic, its figure should show the two-token softmax at $T=1$, not the temperature sweep; the sweep belongs to slide 14 alone.

### [ch01-010] C major — slide 8 (promise) and slide 9 (concept)
Quote: "**Token** — a chunk of characters from a fixed list, defined on the next slide. Every box here gets its own slide." (line 285); "**The network sees integers** / never letters" (lines 321–322); "layers of multiply-and-add, named after a biological analogy" (line 234).
Why it fails: the promise is unpaid for the network box, and the gap is not cosmetic. The chapter hands the network integers and describes it as layered multiply-and-add, then never says that a token ID is a label selecting a row rather than a quantity entering the arithmetic. A trainee is left to conclude that token 5231 is arithmetically larger than token 12 — the exact misconception the delivered chapter forecloses ("ID is internal bookkeeping", deck slide 9; "the token ID's one job is to select a row", Supp §S2 with the one-hot equivalence $E=I$).
Fix direction: one sentence on slide 9 — the integer is a label that selects a row of numbers, and it is never multiplied. `curriculum/ch01-term-audit.md` line 108 records embedding's exclusion as deliberate ("Not needed for any claim this chapter makes"); that exclusion is only safe once the label-not-quantity line is present, which the successor Beamer deck adds (term audit line 41) and this draft does not.

### [ch01-011] C major — slide 19
Quote: "A **tool** is a program the system can run alongside the network. It fetches or computes, its result is written into the window as tokens, and the pass that follows is the one already described." (line 648); diagram nodes "A[\"a tool that fetches —<br/>web search, a file\"] --> W[\"context window\"]" and "C[\"a tool that computes —<br/>code run, and its result\"] --> W" (lines 636–637).
Why it fails: contract field (2), input → output. The output half is specified (result → window, as tokens); the input half is absent, and the diagram positively excludes it — every arrow runs *into* the window and the network has no outgoing arrow to a tool. Nothing in the chapter says what triggers a call or in what form, so the slide cannot answer the first question it invites: how does it decide to search? This is the component's fullest treatment in the chapter, so the contract binds here under RUBRIC v1.1.
Fix direction: add the trigger — the network emits tokens the harness reads as a call, the harness runs the program, and the result is appended to the window as tokens. The ledger already holds this shape (Supp §S16, "token emission plus outside code").

### [ch01-012] F major — slide 11
Quote: "The raw scores are called **logits**. A higher score means the token fits the text so far better, according to the fitted numbers. One run of the network over the window is one **pass**." (line 385)
Why it fails: forward dependency. "The window" is used here with a definite article and is not defined until slide 18 (line 614, "The window is the input to one pass"). Seven slides separate use from definition, and the definition of **pass** on this slide is written in terms of the undefined object.
Fix direction: either define the window before slide 11, or say "every time the network runs" here — the fix the project itself applied to the same construction in the Beamer rebuild (`curriculum/ch01-term-audit.md` lines 67–68).

### [ch01-013] S4 major — slide 18
Quote: "**Standing instructions** are text placed in the window at the start of every session, which Chapter 10 is about." (line 614); diagram node "standing instructions" (line 605)
Why it fails: a coined term where a standard term exists. The standard term is **system prompt**, and the course uses it everywhere else — `slides/beamer/02-formation.tex` line 163 defines it as "standing text placed before your message", line 173 says "Define \\kw{system prompt} here, because Chapter 3 uses it from its second frame", and `slides/beamer/03-control.tex` line 95 asserts "Chapter 1 defined the \\kw{context window}; Chapter 2 defined the \\kw{system prompt}." The coinage also collapses two objects with different authors — the vendor-set system prompt and the user's own instruction file (Chapter 10) — which `03-control.tex` line 103 depends on being separate ("The system prompt is set by whoever built the product"). `curriculum/ch01-term-audit.md` line 39 registers "standing instructions" as a defined term without noting the collision.
Fix direction: use **system prompt** for the vendor-set block and name the user-written instruction file as a separate item in the window.

### [ch01-014] R minor — slide 2
Quote: "a question — the text you send is the **prompt**" (line 54); "**It writes** / left to right, in pieces" (lines 59–60)
Why it fails: both are ledger content at lower depth. The prompt is defined with an equation in the delivered chapter — the input token sequence $\mathbf{x}_{1:k}$ conditioning $P(\mathbf{x}_{k+1:j}|\mathbf{x}_{1:k})$ (deck slide 5) — and sequential emission is part of the inference definition on the same slide, made mechanically complete at spec slide 20.
Fix direction: drop the two definitions. The **opening device** — starting from the artefact every attendee has already seen, with the caveat that buffered interfaces hide the pieces (line 78) — is not in the ledger and is the salvageable part of this slide.

### [ch01-015] T minor — slide 13 (speaker note)
Quote: "**Worth naming:** the form is the Boltzmann distribution with the score standing in for negative energy over kT. Several people in the room will recognise it." (line 455)
Why it fails: the correspondence counts temperature twice. Softmax is $p_i \propto \exp(z_i/T)$; Boltzmann is $p_i \propto \exp(-E_i/(k_B T))$. Matching exponents gives $z_i = -E_i/k_B$ — the score stands in for negative energy over $k_B$, not over $k_B T$, because the $T$ is already carried explicitly in the softmax. The note is addressed to the part of the room most likely to check it.
Fix direction: "the score stands in for $-E_i/k_B$, and the softmax $T$ plays the role of the thermodynamic temperature." **CONFIRMED** — algebra executed above; no external source required.

### [ch01-016] T minor — slide 16 (speaker note)
Quote: "**Worth adding:** generation cannot be parallelised across positions, because pass four needs the token that pass three produced. Training can be, which is why training a model is fast relative to the text it has read and generation is not." (line 562)
Why it fails: the parallelism claim is correct; the gloss is not. What parallelises in training is the sequence dimension — latency, not arithmetic cost. Per token of text, training costs *more* than inference, not less, because it adds a backward pass. A trainee retaining "training is fast" will collide with Chapter 7's own compute accounting.
Fix direction: state the contrast as latency and parallelism, not speed: all positions of a training sequence are scored in one pass, while decoding is strictly sequential. **PLAUSIBLE** — I did not open Chapter 7's derivation; `PRIOR-REVIEW-SCOPE.md` line 165 records "the 6ND training accounting" as Chapter 7 content, which is the arithmetic that would settle it.

### [ch01-017] C minor — slide 2
Quote: "**This chapter** / what each piece costs to produce" (lines 65–66)
Why it fails: a stated promise with no payoff slide. No cost quantity appears anywhere in the chapter; slide 10's footer defers to a tokeniser run "before delivery" (line 366) and its notes to Chapters 7 and 13 (line 371), slide 16's note defers the price relationship to Chapters 7 and 13 (line 560), and slide 18's note explicitly refuses a window size and hands it to Chapter 7 (line 626).
Fix direction: change the promise to what the chapter pays — what produces each piece — or move the column to a chapter that carries a number.

### [ch01-018] F minor — slide 15
Quote: "&lt;Cite own=\"derived\" note=\"From the network on slide 4 and the sampler on slide 13.\" /&gt;" (line 529)
Why it fails: the pointer misses. Slide 13 is the softmax slide; the sampler appears nowhere before slide 15, which introduces it itself (line 523). The footer therefore conflates softmax — a deterministic transform — with the sampler — the stochastic draw — on the one slide whose entire argument depends on separating them.
Fix direction: correct the reference to this slide, and keep softmax and sampling verbally distinct in the footer as the slide body already does.

---

## Coverage checklist

| promise | where stated | status |
|---|---|---|
| "What a language model is" | subtitle, line 20 | paid at slides 3–7 |
| "and what one run of it computes" | subtitle, line 20 | paid at slides 8–16 |
| "Nothing in this chapter assumes you have seen any of it before." | line 31 | paid, with two exceptions — "window" ([ch01-012]) and "sampler" ([ch01-018]) are used before they are defined |
| "what each piece costs to produce" | line 66 | **unpaid** — [ch01-017] |
| "**Token** … defined on the next slide" | line 285 | paid at slide 9 |
| "Every box here gets its own slide." | line 285 | **partly unpaid** — the network box never gets one; how an integer enters the arithmetic is never stated ([ch01-010]) |
| "Six facts, and where each one is used later" | line 703 | paid on the same slide |

Not treated as a chapter promise: slide 7's "the appendix carries what it establishes" (line 246)
and slide 12's note "Chapter 8 relies on this definition" (line 417). `PRIOR-REVIEW-SCOPE.md`
lines 175–182 record Chapter 8 as dissolved and its deck as "Appendix, not delivered"; the draft's
own note (line 262) says it is distributed rather than presented.

---

## Topics exported

Marked for salvage: **[LEDGER]** = already delivered by `ch01-approved`, drop; **[SALVAGE]** = not
in the ledger, mine it.

- **[SALVAGE]** Progressive-output opening — the chapter opens on the artefact every attendee has already seen (the reply written left to right), with the caveat that some interfaces buffer and show it whole. Slide 2, lines 46–78.
- **[SALVAGE]** Training as least-squares curve fitting — residuals drawn, total squared error against slope, the minimum marked, with the caveat that the bowl is a one-dimensional slice of a billion-dimensional space. Slide 6, lines 188–221. The ledger's Case Study 1 goes straight to softmax + cross-entropy and carries no regression bridge for the objective.
- **[SALVAGE]** "Neural network" and "learning" given as borrowed names rather than claims, anchored on the fact that the numbers started as noise. Slide 7, lines 226–258.
- **[SALVAGE]** Brain-comparison closure with its literature — correlational, noise ceilings of 0.32, 0.17 and 0.20, an author of the original co-writing the re-analysis, and the instruction not to say the comparison has been refuted. Slide 7, lines 259–262, keyed `schrimpf2021` + `hadidi2026`, both `[V]`. The only place in this draft that carries evidence the ledger has nowhere.
- **[SALVAGE]** Greedy degeneration as a taught failure — the objective stated and then shown breaking. Slide 17. Transplantable only after [ch01-001]: as an observation citing `holtzman2020`, never as a derivation from determinism.
- **[SALVAGE]** Sequence-parallel training vs strictly sequential decoding — pass four needs pass three's token. Slide 16, line 562, after the correction in [ch01-016].
- **[SALVAGE]** Softmax as a Boltzmann distribution — a bridge for a physics-literate room. Slide 13, line 455, after the correction in [ch01-015].
- **[SALVAGE]** The predicted-or-computed check — whether a number was predicted or calculated depends on whether a code tool ran, the vendor documents the routing, and the transcript shows which happened. Slide 19, line 659, keyed `anthropic-code-exec` `[V]`.
- **[SALVAGE]** Session defined — "one continuous conversation, from opening it to closing it." Slide 5, line 171. The ledger uses the word throughout and never records a definition.
- **[SALVAGE]** Language models predate neural networks — word-frequency models. Slide 3, line 101.
- **[SALVAGE]** Forward-thread table — six facts each mapped to the chapter that spends it (Ch 2, 4, 5, 6, 7, 9, 10, 13). Slide 21, lines 722–730. The ledger's capstone maps steps to defining slides, not to later chapters.
- **[SALVAGE — production device, not content]** The per-slide speaker-note template: Says / From / Chapter / To / Say aloud / Caveat / Do not say, with "Do not say" naming the specific numbers the presenter must not invent (file size, parameter count, vocabulary size, window maximum).
- **[LEDGER]** AI / ML / NN / LLM nesting → ledger deck slide 2.
- **[LEDGER]** Model = parameters + program; parameters/weights/size; network → deck slide 6, spec slide 15.
- **[LEDGER]** Training, inference, knowledge cutoff, static weights → deck slides 5 and 7.
- **[LEDGER]** Pipeline preview and capstone → spec slide 20's seven-step pipeline.
- **[LEDGER]** Token, vocabulary, byte-pair encoding → deck slides 6 and 8, Supp §S1.
- **[LEDGER]** Technical vocabulary costs more tokens; token ID vs token count → deck slide 9.
- **[LEDGER]** Logits → spec slide 18.
- **[LEDGER]** Attention and Transformer → spec slide 17, Supp §S4.
- **[LEDGER]** Softmax and temperature → spec slide 18, Supp §S7.
- **[LEDGER]** Output variance located at the sampler → spec slide 19, marked never to be re-derived.
- **[LEDGER]** Decoding loop → spec slide 20, Supp §S9.
- **[LEDGER]** Context window and its maximum → deck slide 5, closed at spec slide 17.
- **[LEDGER]** Tools, API/MCP, the weights-vs-harness boundary → deck slide 10, Supp §S16.
- **[LEDGER]** Window discarded, parameters unchanged → deck slide 7.

---

## Checks not run

- **Slide 7's three numbers.** I did not open Schrimpf et al. 2021 or Hadidi et al. 2026, so the noise ceilings of 0.32, 0.17 and 0.20 and the Blank co-authorship claim (lines 259–260) are unverified by me. `ai-training/references.md` lines 393 and 407–409 record both papers as `[V]` and independently assert the co-authorship; that is the project's check, not mine.
- **The vendor routing rule.** I did not fetch the `anthropic-code-exec` page. The wording quoted in slide 19's note appears verbatim in `references.md` line 44, which I read; the term audit line 212 records its COI flag as still unverified.
- **Figures.** No `/figures/01-*.png` was opened. Claims that the fitting figure is a real least-squares fit (line 213), that the three marked softmax points are computed (line 447), and that schematic figures say so on their face were taken from the deck's own footers. I did verify the arithmetic those footers assert: $e^{2}/(e^{2}+e^{1}) = 7.389/10.107 = 0.7311$, and the sweep gives 0.8808 at $T=0.5$ and 0.6225 at $T=2.0$ — the printed 0.731, 0.881 and 0.622 all hold.
- **The successor deck.** I did not review `slides/beamer/01-substrate.tex` (24 frames). Statements that the rebuild already fixed something rest on `curriculum/ch01-term-audit.md`'s own account plus two greps, not on reading the source.
- **The ledger's underlying documents.** Overlap is judged against `TOPICS-LEDGER.md`'s descriptions. I did not open `AI_TRAINING.pdf`, `CH1_NETWORK_SLIDES.md` or `CH1_SUPPLEMENT.md`.
- **C-contract scoping.** This draft has no supplement, so under RUBRIC v1.1 every definitional slide is its component's fullest treatment and the five-field contract binds at each. I applied the so-what test and report only the two field misses that change what a trainee can do ([ch01-010], [ch01-011]). Token, logit, context window, temperature and greedy selection are all defined without complete five-field contracts; I judged those non-actionable for a superseded deck-only draft. That is a scoping decision, not an absence of instances.
- **Prior-review overlap.** Per instruction, cited not re-derived: `PRIOR-REVIEW-SCOPE.md` lines 99–109 record this chapter's premise graded **mis-scoped**, the entire front half as "used or implied, none defined", the brain-analogy opening device named for deletion, and cross-cutting A8 (the footer rule for definitional slides) anchored here — the same A8 conflict the term audit states as unresolvable at its lines 131–134. None of that is re-derived above. Note one internal inconsistency in that map, outside the five classes: line 177 says Chapter 8's surviving points went to Chapter 1, line 197 says a three-slide brain-analogy segment now opens Chapter 10. The salvage target for the brain material depends on which is current.
- **Not assessed:** the 32–38 minute delivery estimate, the figure count (frontmatter says 20 slides and 20 figures; the file holds 21 slides and 21 visuals), and the two empty animation slots. Outside the rubric's five classes.

---

## Verdict

**salvage-with-edits.**

Five unresolved R blockers rule out "usable-with-fixes", and they are not marginal: slides 3–5,
8–11, 12–15 and 16–21 restate `ch01-approved` at lower depth — one equation in twenty-one slides
against the delivered chapter's full forward pass, schematic tokeniser figures carrying
`TODO(capture)` against verified `o200k_base` splits, and a re-derivation of the sampling-variance
claim the ledger explicitly marks as never to be reopened. Delivering this would spend 32–38
minutes of a session on material the room already holds. "Rebuild" is equally wrong, because the
draft is already superseded by a 24-frame Beamer deck and nobody is going to rebuild it — the
live question is what deserves mining, and the answer is not nothing. Three structural properties
survive intact and are worth carrying into whatever consumes them: every one of the 21 slides has
a statable one-sentence Message, every headline is an assertion rather than a topic label, and the
speaker notes name the numbers the presenter is forbidden to invent. Eleven content items do not
appear in the ledger at all; four of them are load-bearing — the brain-comparison closure with two
`[V]` sources and its "do not say it was refuted" instruction, which is the only evidenced material
in this file and has no home in the delivered chapter; the least-squares bridge to the training
objective, which reaches this audience through a procedure they have already run; greedy
degeneration shown as the objective breaking; and the sequence-parallel versus sequential-decoding
contrast. Two of those four cannot be transplanted as written — [ch01-001] is a false derivation
labelled `derived`, and [ch01-015] double-counts temperature in the one bridge aimed at the
physicists in the room. Fix those two in transit, take the other nine, and discard the remaining
two-thirds of the file.
