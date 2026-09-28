# Topics ledger — what each chapter has already said
# Sequential reviewers: read this before reviewing; append your chapter's
# "Topics exported" section verbatim under a "## chNN <filename>" heading
# after writing your report. One line per topic. Do not edit earlier entries.

## ch01-approved (AI_TRAINING.pdf slides 1–13+16, CH1_NETWORK_SLIDES.md 14–20, CH1_SUPPLEMENT.md)

Chapter 1 as delivered = the approved deck (slides 1–13 and 16; 14–15 are placeholders,
17 is empty) + the seven-slide replacement spec for 14–20 + the §S1–§S17 supplement.
Depth markers below: **named** = term introduced, no mechanism; **defined** = one-sentence
definition, alias where one exists; **equation** = symbolic statement on a slide;
**derived** = worked through in the supplement with algebra or numbers.

- AI / ML / NN / LLM hierarchy — defined as four nested method families, each by its own mechanism (goal-directed inference / function approximation / layered weighted inputs with non-linear activation / self-supervised + human-aligned text prediction), with a consumer example at each level. Deck slide 2. Do not re-derive the nesting.
- AI as a non-analytical method family — delivered as the framing of slide 2's headline: these methods fit functions from data rather than solving a closed form. Named only; no contrast with analytical methods is worked.
- Contextual text prediction ≠ ground truth — delivered as a live two-agent failure on a sealed-base hydrostatics question, with root cause (memorized textbook phrasing beats first-principles calculation) and the confidence risk. Deck slide 3. The failure mode is established; the deck does not name which of the two answers is correct.
- Confidently correct / confidently wrong / blissfully ignorant — defined as three answer regimes indexed by how well the topic is covered in the corpus. Deck slide 4. Note for reviewers: the reliability axis on that slide carries a direction error (calibration finding [cal-002]) — do not propagate the arrow's claim.
- Corpus — defined: "the general and unstructured collection of training material used to develop an LLM's baseline knowledge (i.e., training data)". Deck slide 4. Definition depth only, no size figures.
- Reliability — defined as a dimension of AI trustworthiness: consistently maintaining intended behaviour and satisfying performance criteria under expected operational distributions. Deck slide 4.
- Training (Empirical Risk Minimization) — defined as the phase where parameters are iteratively updated by backpropagation and SGD to minimize an empirical loss. Deck slide 5 (name + alias); mechanism at slide 16 and Supp §S12.
- Knowledge cutoff (Temporal Distribution Boundary) — defined as the last date of the training corpus, bounding parametric knowledge, with the "ask the model" probe. Deck slide 5.
- Prompt (Conditioning Sequence) — defined with equation: the input token sequence $\mathbf{x}_{1:k}$ conditioning $P(\mathbf{x}_{k+1:j}|\mathbf{x}_{1:k})$. Deck slide 5.
- Context window (Sequence Length) — defined with equation: max tokens $\mathbf{x}_{1:k_{max}}$ per pass, VRAM-limited at runtime, compute $O(k_{max}^2)$. Deck slide 5; the quadratic term is attributed to the attention score matrix at spec slide 17 and derived in Supp §S4.
- Inference (Autoregressive Decoding) — defined with equation: input sequence evaluated across static weights to produce $P(\mathbf{x}_{k+1:j}|\mathbf{x}_{1:k})$, emitting tokens sequentially. Deck slide 5; made mechanically complete at spec slide 20.
- Model = parameters + program — defined as the package: a long array of numbers plus the processing algorithm that reads them into memory, multiplies against token vectors, and outputs a per-token probability distribution. Deck slide 6, with a literal numeric array shown.
- Parameters / weights / model size — defined as the same object under three names, set in training, counted as the "32B" in a model's name. Deck slide 6; the count formula $|\theta|=\sum_\ell d_\ell(d_{\ell-1}+1)$ including biases is spec slide 15.
- Token — defined: "the fundamental unit of text (word or piece of word) processed by the model". Deck slide 6, re-quoted as the section opener on slide 8.
- Network — defined as the layered architecture performing weighted sums and non-linear transformations. Deck slide 6 at name depth; equations at spec slides 14–15.
- Two-stage parameter setting — defined as a flow diagram plus two numbered stages: unsupervised next-token training over trillions of unlabeled tokens sets baseline values, then human alignment (experts rank responses, weights shift toward high-quality answers) using under 1% of the training data. Deck slide 7.
- Static weights / training stops before your prompt — delivered as the diagram's explicit "Training Stops Here" boundary between the trained artifact and the user's prompt. Deck slide 7. This is the anchor for every later "the model does not learn from your conversation" claim.
- Tokenization behaviour, empirical — delivered with verified o200k_base numbers: `' stirrups'` → `' stir' + 'r' + 'ups'` with `r` as raw byte ID 81; a misspelling shattering one token into four; frequency in the corpus decides. Deck slide 8. All splits and IDs on slides 8–9 were recomputed and hold (see calibration-ch1.md).
- Token ID vs token count — defined and separated: ID is internal bookkeeping, count is what costs money and time; letter count does not predict token count (`permeability` and `geotechnical` are both twelve letters, 1 vs 3 tokens); deciding factors are training, frequency and typos. Deck slide 9, with a linear cost chart.
- Multi-stage training and the unified parameter space — delivered as three claims: training involves specialized networks (encoders, reward models) with independent weights; the deployed model consolidates those learned behaviours into one parameter space; capability extends by calling other algorithms. Deck slide 10; ratified and mechanised in Supp §S13.
- API and MCP — both defined at slide 10. API: a defined interface specifying available operations, request/response format and semantics. MCP: an open protocol standardizing how external tools and data sources are made available to an LLM's operating environment. Deck slide 10; their harness location is fixed in Supp §S16.
- Training-time component map — delivered as slide 11's brain-to-stack diagram pairing seven functions with seven components: Processing Input↔Tokenizer, Predictive Modeling↔Unsupervised Training, Processing Media↔Multimodal Encoders, Response Structuring↔Curated Training/SFT, Reward Signaling↔RLHF/RLVR, Value-based Decision Making↔Reward Model, Avoiding Harm↔Refusal Direction. Each pairing is discharged in Supp §S12–§S14.
- Session component maps — delivered as slides 12 (what exists before you type: tokenizer, guardrails, system prompt, sampler, APIs/MCPs, scratchpad, token balance, T-Decoder) and 13 (what runs when the prompt arrives: context retrieval, multi-step thinking, task delegation, peripheral control, output generation, agent harness, effort level). Twenty-two boxes total, every one placed in the Supp §S16 ledger.
- Training as an optimization problem — delivered as Case Study 1: assume a program with random weights and bias, $\mathbf{z}=\mathbf{W}\cdot\mathbf{x}_{1:k}+\mathbf{b}$; convert to probabilities by softmax; define $\mathcal{L}(\theta)=-\frac{1}{n}\sum\log P(\mathbf{x}^{(i)}_{k+1}|\mathbf{x}^{(i)}_{1:k};\theta)$; evaluate over corpus pairs $\mathcal{D}$. Deck slide 16, with the hot-and-cold analogy standing in for gradient feedback.
- Neuron — defined with equation $a=\varphi(\mathbf{w}\cdot\mathbf{x}+b)$, plus weight (how strongly each input moves the output) and bias (the output when every input is zero), anchored on the identity that $\varphi(u)=u$ makes it multiple linear regression. Spec slide 14.
- Activation function catalogue — sigmoid, tanh, ReLU, GELU delivered with equation, range and where each is used; derivatives in Supp §S10; the collapse proof (compositions of affine maps are one affine map) in §S10.
- Layer, width, depth, hidden state, parameter count — defined with equation $\mathbf{h}^{(\ell)}=\varphi(W^{(\ell)}\mathbf{h}^{(\ell-1)}+\mathbf{b}^{(\ell)})$ and $|\theta|=\sum_\ell d_\ell(d_{\ell-1}+1)$. Spec slide 15. Closes slide 2's "multi-layered" and slide 6's "layered architecture".
- Universal approximation — stated at slide level (spec 15) and precisely in Supp §S11 (Cybenko 1989; Hornik 1991), always with its two silences: the width is existential, and nothing guarantees gradient descent finds the weights.
- Embedding matrix — defined with equation: $\mathbf{e}_v$ is row $v$ of $E\in\mathbb{R}^{|\mathcal{V}|\times d_{\text{model}}}$, contributing $|\mathcal{V}|\cdot d_{\text{model}}$ parameters; the token ID's one job is to select a row. Spec slide 16, derived in Supp §S2 including the one-hot equivalence $E=I$ and the zero-gradient consequence for unseen tokens.
- Positional encoding — defined as $\mathbf{p}_i$ added to the embedding, motivated by attention's permutation invariance. Spec slide 16; the three deployed schemes (sinusoidal with equations, learned absolute, RoPE) in Supp §S3.
- Transformer, decoder-only — delivered as the architecture name (Vaswani et al., 2017) and the block-stack diagram; why LLMs use the decoder stack rather than an encoder is Supp §S4a. Spec slide 17. Closes the "T-Decoder" box of deck slides 12–13.
- Self-attention, Q/K/V, causal mask — defined with equation $\mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^\top/\sqrt{d_k})V$ and the mask $j\le i$. Spec slide 17; derived in Supp §S4 with a 3-token $d_k=2$ worked example and the $\sqrt{d_k}$ variance argument.
- Multi-head, residual connection, layer normalization, feed-forward block — named with function at spec slide 17; full equations, the pre-norm arrangement, the FFN's ~two-thirds parameter share, and the Jacobian argument for residuals in Supp §S5.
- Attention cost and KV cache — the $O(k_{max}^2)$ of deck slide 5 is closed at spec slide 17 as the $k\times k$ score matrix; the KV cache and its $O(k)$-per-token consequence are Supp §S4.
- Logit and unembedding — defined with equation $\mathbf{z}=W_U\mathbf{h}_k^{(N)}+\mathbf{b}_U$, $\mathbf{z}\in\mathbb{R}^{|\mathcal{V}|}$, plus weight tying ($W_U=E$) and its parameter saving. Spec slide 18; cost accounting in Supp §S6.
- Softmax and temperature — defined with equation $P_T(v)=e^{z_v/T}/\sum_j e^{z_j/T}$, with $T\to0$, $T=1$ and $T>1$ behaviour. Spec slide 18; shift invariance, the max-subtraction implementation trick, and "T acts before normalization" in Supp §S7.
- Sampling policies — greedy, temperature, top-k, top-p/nucleus all defined at spec slide 19, with the warning that top-k's $k$ is not the context length $k$; greedy shown as the $T\to0$ limit in Supp §S8.
- Seed, PRNG, reproducibility — defined at spec slide 19 with a worked inverse-CDF draw over a four-token vocabulary at three temperatures, plus the caveat that $T=0$ across a provider's hardware is not bit-reproducible (non-associative parallel floating-point addition).
- Output variance is located at the sampling step — delivered as the closing claim of spec slide 19: the network is a deterministic function, variance is injected on purpose at one place, and the seed controls it. Explicitly marked as never re-derived after this slide.
- Decoding loop and `<eos>` — defined at spec slide 20: `<eos>` is an ordinary vocabulary token the model learned to emit; the loop reads it and halts; the network never halts. Supp §S9 gives the loop as code and the harness-disagreement consequence.
- The seven-step pipeline — delivered as spec slide 20's capstone: tokenize → embed → N decoder blocks → logits → distribution → sample → append and repeat, each step labelled with its defining slide and its slide-12/13 box. This is the assembled generation path; later chapters can reference step numbers.
- Byte-pair encoding — derived in Supp §S1: initialize with 256 byte values, merge the most frequent adjacent pair, repeat to $|\mathcal{V}|\sim10^5$; the merge list is the tokenizer; encoding applies merges greedily. Explains every slide 8–9 observation, including why a stray `r` is a raw byte.
- Encoder vs decoder — Supp §S4a: an encoder block is the same construction with the mask removed; the causal mask is what makes autoregressive generation trainable; GPT-class LLMs are decoder-only stacks.
- Chain-rule sequence factorization — Supp §S9 proves $P(\mathbf{x}_{k+1:j}|\mathbf{x}_{1:k})=\prod_t P(\mathbf{x}_{t+1}|\mathbf{x}_{1:t};\theta)$ exactly, joining slide 5's sequence-level inference definition to the single-token distribution of slides 18–19.
- Training mathematics — Supp §S12 derives $\nabla_\mathbf{z}\mathcal{L}=P-\mathbf{e}_y$ from softmax + log loss, gives the three backpropagation formulas for a layer, the SGD update with learning rate, and names Adam and dropout at the right stage; initialization variance ($2/d_{in}$ He, $2/(d_{in}+d_{out})$ Glorot) is attached to Case Study 1's "random numbers before training".
- Post-training stages — Supp §S13 defines SFT (§S12's loss on curated demonstration pairs), the reward model (Bradley–Terry preference likelihood, discarded at deployment), RLHF (KL-constrained reward maximization), DPO, RLVR (programmatic verifier replacing the learned reward) and the refusal direction (Arditi et al., 2024) with the ablation formula. Answers slide 10's 'personality' and 'morality' questions explicitly.
- Multimodal encoders — Supp §S14: one encoder network per non-text modality mapping raw signal into $d_{\text{model}}$ vectors placed in the same context stream; a vision transformer patchifies, flattens, projects and adds positional encodings. This is the answer to slide 10's "text, images, and sound at the same time".
- Mixture of experts — Supp §S15, marked beyond-scope: expert FFNs plus a learned router activating the top 1–2 per token; parameters multiply, per-token compute does not. Delivered so "an 800B model that runs like a 40B model" parses; nothing later depends on it.
- Weights-vs-harness ledger — Supp §S16 places all 22 boxes of deck slides 12–13 into $\theta$, context tokens, generated tokens, a separate artifact, or harness code, with the reading rule: **a capability that can be changed without retraining lives in the harness or the context; $\theta$ holds only what training put there.** Tool use is defined here as token emission plus outside code; guardrails are separated from trained-in refusal; the thinking token is defined as an ordinary token inside a harness-designated span.
- Live-demo lab scope — Supp §S17 and the spec's speaker notes fix what `llm_lab.m` does and does not contain: softmax output stage, cross-entropy objective, the live residual $P-\mathbf{e}_y$, autoregressive loop and static weights are present; attention, learned embeddings, positional encoding, residual/LayerNorm, `<eos>` halting, post-training and sampling variety are absent and named as absent.
- Notation and symbol conventions — fixed chapter-wide and reused: $\mathbf{x}_{1:k}$ context, $\theta$ parameters, $\mathcal{V}$ vocabulary (script) vs $V$ attention value matrix, $\mathbf{z}$ logits, $\mathcal{L}(\theta)$ loss, $\mathbf{h}$ hidden state, $\varphi$ activation, $E$ embedding matrix, $d_{\text{model}}$ width, $T$ temperature, $N$ block count. Deck uses column vectors; Supp §S4 and §S12 use row-stacked form to match MATLAB, and say so.

**Count: 51 topics.** Chapter 1 owns the full forward pass, the sampling step, the training
objective and its gradient, the post-training stages, and the weights-vs-harness boundary.
A later chapter re-explaining any of the above is repeating Chapter 1, not building on it.

**Known open items in ch01** (do not treat as gaps for later chapters to fill): the deck's
SUMMARY & TIPS section has no payoff slide; slide 3 does not name which agent answer is
correct; slide 4's reliability arrow points the wrong way. All three are recorded in
`calibration-ch1.md` as [cal-005], [cal-001] and [cal-002].

## ch01 01-substrate.md (SUPERSEDED DRAFT — topics listed for salvage reference only, NOT delivered curriculum)

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

## ch02 02-formation.md

Source: `FOR-REVIEW/rubric-reports/ch02-review.md` (2026-08-27). **Reviewed file is the superseded
Slidev draft**; a 33-frame Beamer rebuild `slides/beamer/02-formation.tex` exists and was not
reviewed. Verdict: salvage-with-edits. Lines below are the report's "Topics exported" section verbatim.

- **The post-training pipeline as a taught sequence** — pretraining → supervised fine-tuning → reward model → RLHF, each stage named by what it consumes. Slides 2, 5, 6, 9. Overlaps ch01 Supp §S13, which already derives all four; ch02 adds the ordering as a spine, not new mechanism.
- **The pretrained model as autocomplete** — a base model continues a question with more questions rather than answering it. Slide 2, lines 41–42. Not in ch01. Asserted, never shown.
- **Scaling laws and the compute-optimal correction** — loss falls predictably with size, data and compute (`kaplan2020`); for a fixed compute budget models were undertrained relative to their size, so more data and a smaller model (`hoffmann2022`); both are empirical fits over a tested range, extrapolated since. Slide 3. Not in ch01.
- **Sparsity as the total-to-active parameter ratio** — slide 4, the same definition Chapter 7 uses at its critical-batch-size derivation. The routing mechanism itself is ch01 Supp §S15.
- **Supervised fine-tuning teaches format, not quality** — "Everything after this is about **quality**, not about format." Slide 5, line 126. The cleanest statement of the SFT/RLHF division of labour in the curriculum.
- **The reward model as a model of a rater** — a function fitted to a finite set of comparisons made by particular people under particular instructions, which then scores any response. Slide 6, lines 155–156. The framing is ch02's own and is the chapter's thesis; the mechanism is ch01 Supp §S13. **Its stage is never stated — later chapters must not assume the room knows it is training-time only.**
- **The six rated dimensions** — truthfulness, instruction following, harmlessness, formatting, verbosity, tone — with the course thread each returns on, and the claim that they conflict. Slide 7. Provenance not stated; see [ch02-013].
- **Rater disagreement is information, not noise** — an ambiguous dimension produces disagreement no amount of rater training fixes, and unresolved disagreement enters the preference data as inconsistency the reward model fits. Slide 8.
- **The adjacent-band audit rule** — one instrument fails a rating only when two assignments land in opposite bands. Explicitly one document of five and explicitly not an industry standard. Slide 8.
- **The InstructGPT preference result** — a 1.3B post-trained model's outputs preferred to a 175B base model's, credited to supervised fine-tuning *plus* RLHF rather than the reinforcement step alone, with the authors' own "still make[s] simple mistakes". Slide 9. The gain is in preference, not correctness.
- **Helpfulness and harmlessness as separately collected, conflicting signals** — the tension is the method, not a bug in it. Slide 10. The trained-in-versus-harness half of that slide is ch01 Supp §S16's.
- **Constitutional AI and RLAIF** — written principles applied by the model in the rater's place; the published version generates harmlessness signals from AI feedback rather than human feedback. Slide 11. **Not delivered by ch01 — this is ch02's own component.** Its pipeline location is not stated.
- **The machine-checkable criterion rule** — once a written criterion is applied by a machine, it must be checkable without context, which strips it to the observable surface. Slides 11 and 18. This is the chapter's hinge and the sentence later chapters should cite.
- **Direct preference optimisation** — preference data updates the policy directly, no explicit reward model, and the human comparisons remain the input. Slide 12. ch01 Supp §S13 already defines DPO.
- **Behaviour traced to mechanism, with evidential standing printed per row** — firm refusal (published); agreement under pushback (plausible, not evidenced in the documents); long structured answers (mechanism not known, and the folk explanation is contradicted by two instruments, one breaking ties toward brevity and one deleting length as a grading category). Slide 13. The table format — what you see / where it comes from / standing — is the reusable object.
- **Optimised prompts do not transfer consistently across models** — OPRO's winning instruction is specific to the model it was scored on (`yang2023`, `ye2024`). Slide 14. This narrower claim explicitly replaces "does not transfer to newer models", which no primary re-evaluation supports.
- **Best-of-N reported as the result** — EmotionPrompt's +115% headline is the best of eleven stimuli; averaged over all eleven the original's own numbers give 4.42% on that suite and 2.58% across all benchmarks; an independent replication found about 1%, from a design that deliberately did not run best-of-eleven, which is why the two numbers do not contradict. Slide 15. Chapter 4 reuses the trap.
- **The five-document evidential basis and its band vocabulary** — corroborated across independent documents / stated once as a rule / inferred from structure, with the supporting count printed on the slide; five documents, two of unverified provenance, are not a sample; these observations never become citations and carry no source footer. Slide 17. The underlying `[E1]`–`[E4]` scale is not shown to the room.
- **Nine annotation findings** — house style as a written edit specification (three of five); the repaired text collected (two of five); equivalence engineered out by opposite mechanisms (two of five); one instrument collecting comparisons only where a model has already failed, so its preference data is conditioned on failure; the judge's blindness dictating criterion design, so every criterion must carry its own context (two of five); the human made to attempt the task before judging it (three of five); staleness designed against at both ends; instruments diverging structurally more than lexically, with only instruction-following and truthfulness recurring; two incompatible labour models — generalist raters and domain professionals — doing work described in the same vocabulary. Slides 18–19.
- **The instrument rebuilt mid-collection** — grading categories deleted, task authorship moved, mandatory rewrites imposed, in one week; data gathered a fortnight apart graded by materially different instruments with nothing in the output to distinguish them. One changelog. Slide 20.
- **The hallucination band** — contributors are aimed at the band between common knowledge, where the model is reliable, and genuinely obscure material, where it declines: the band where it believes it knows. Slide 20. The generating rule for Chapter 5's failure gallery and the explanation for why the tool feels reliable on textbook material and erratic on the room's own research.
- **Ranking by evidence rather than by force** — the most memorable finding ranks eighth of fourteen; the ordering is deliberately not the order of interest. Slide 21.
- **The rating exercise design** — two responses, one synthetic rubric on the room's own mechanics/concrete/fluids domain, eight minutes under visible time pressure, a score per dimension plus a preference plus a confidence self-report, verification time-boxed at two minutes with an *unassessable* band, and no preference permitted without a named specific failure. Slides 23–24, with the six-step schedule and the instruction to cut step 5 first.
- **"Unassessable" is the correct action on an unverifiable claim — and is exactly how a fabricated citation passes into a dataset as acceptable.** Slide 25, line 757.
- **Five or six raters is a tally, not a distribution.** Slide 25, line 755. The course does not present six points as one.
- **The room's own preference is a reward signal at scale** — eight minutes of rating is eight minutes of generating training data. Slide 25, lines 763–765. The chapter's payload.
- **The sample-size question handed to Chapter 4** — "how many raters would we have needed before that tally meant anything?" Slide 25, lines 771–772.


## ch03 03-control.md

Source: `FOR-REVIEW/rubric-reports/ch03-review.md` (2026-08-28). **Reviewed file is the superseded
Slidev draft**; a 23-frame Beamer rebuild `slides/beamer/03-control.tex` exists and was not reviewed.
Verdict: salvage-with-edits. Lines below are the report's "Topics exported" section verbatim.

- **Prompting technique is taught as steering, not as tricks** — each lever is justified by the
  rated dimension it acts on, and a technique with no rated dimension behind it is meant to be
  flagged rather than taught. Slides 1–2, lines 15–16 and 35–41. The chapter states the rule; see
  [ch03-001] for how far it applies it.
- **The three prerequisites before tuning a prompt** — success criteria, a way to test
  empirically against them, and a draft to improve; the middle one is what most prompting advice
  omits. Slide 3, lines 60–69. Vendor documentation, `anthropic-prompting`.
- **The colleague test for specificity** — show the prompt to someone with minimal context and
  ask them to follow it. Slide 4, lines 96–98. Maps to instruction following: "A vague prompt
  cannot be failed on instruction following, because there was no instruction to follow."
- **A constraint carrying its reason generalises; a bare rule does not** — the units example, with
  the claim that the model generalises from the explanation. Slide 5, lines 130–154.
- **Tagged input separates instruction from data** — XML-style `<instructions>` / `<context>` /
  `<input>`, consistent descriptive names, nested where the hierarchy is real. Slide 6, lines
  168–189. Named as the first partial defence against prompt injection, with the term itself
  undefined ([ch03-011]) and the payoff handed to Chapter 6.
- **Example criteria: relevant, diverse, structured, three to five** — examples steer format,
  tone and structure more reliably than instructions. Slide 7, lines 207–214. The 3–5 bound is
  vendor-documented and was not re-verified here.
- **A negative example still enters the window as an instance of the unwanted pattern** — hence
  the documented rule, tell it what to do instead of what not to do; and if a negative example is
  used, label it and pair it with the correction. Slide 8, lines 239–245.
- **The role claim, split in two** — the documentation claims a role focuses *behaviour and tone*;
  it does not claim a persona improves *accuracy*. The accuracy claim is separate, testable, and
  deliberately left open for Chapter 4. Slide 9, lines 266–277. This split is the chapter's
  cleanest object and later chapters should reuse the form.
- **Chain-of-thought's published scope versus the folk version** — the result rests on supplied
  worked exemplars; "think step by step" at a model that already reasons is a different
  proposition and is not what was tested. Slide 10, lines 293–301. Carry the correction in
  [ch03-005] with it: the zero-shot form must not be described as having the published result
  behind it, and the sufficiently-large-model condition belongs on the claim.
- **Asking for the working leaves an auditable artefact** — which on this room's own tasks may
  matter more than the accuracy question. Slide 10, line 300; restated at slide 14. Chapter 5
  owns the limit: stated reasoning is not proof that the reasoning caused the answer (lines
  441–443).
- **Adaptive thinking and the effort setting** — the model decides when and how much to think,
  biased by an effort setting and by query difficulty; more thinking costs tokens and latency
  (Chapter 7's material, Chapter 13's bill). Slide 11, lines 327–329. Version-fragile:
  `budget_tokens` is deprecated and errors on recent models. **Where `effort` is settable is not
  stated — see [ch03-006]; do not let a later chapter assume this room can reach the dial.**
- **The rating loop closes on the prompt writer** — rewarded behaviour becomes preference data,
  becomes trained behaviour, and a prompt can invite it back. Slide 12, lines 355–365. **Export
  the structure, not the instances:** the confidence and agreement arms carry Chapter 2's
  standing marks, and the length/verbosity arm is contradicted by Chapter 2 — [ch03-002].
- **Three anti-patterns as levers pulled backwards** — the leading question (a preferred answer
  visible in the wording invites the rewarded agreement, and you will not notice because the
  answer agrees with you); asking for a verdict (a judgement can be delivered confidently on no
  evidence, an analysis can be checked); constraint stacking (conflicting requirements are
  satisfied selectively and the rest dropped without report, so name which constraint wins).
  Slides 13–15. The constraint-stacking slide also exports the mirror of Chapter 2's
  over-specified rubric, seen from the author's side.
- **Prompts do not port** — tag conventions, role handling, thinking and effort controls and
  default verbosity are provider-specific and several are version-specific; a prompt moved to
  another model is an untested prompt, not a working one. Slide 16, lines 492–498. This is what
  Chapter 12 inherits.
- **Standing printed per technique** — five techniques documented, two claims (role improves
  accuracy; "think step by step" helps a modern reasoning model) marked not established and
  handed to Chapter 4. Slide 17, lines 524–539. The table form — claim against standing — is
  reusable and is the chapter's contract with Chapter 4.


## ch04 04-measurement.md

Source: `FOR-REVIEW/rubric-reports/ch04-review.md` (2026-08-28). **Reviewed file is the Slidev
draft `slides/04-measurement.md`; no Beamer rebuild exists for this chapter, so this is the live
draft rather than a superseded one.** Verdict: salvage-with-edits, with two unresolved blockers.
Lines below are the report's "Topics exported" section verbatim.

- **The folklore diagnosis, as three named defects** — one run, a pass criterion chosen after seeing the output, and no control condition. Slide 2, lines 33–35. The frame later chapters should use when a prompting claim arrives without a method.
- **The MACs-versus-FLOPs erratum as the course's anchor artefact** — a unit-definition error in expert material, producing a clean factor of two, caught by an outside reader after publication; one MAC is two FLOP, and the numerator needs the factor or the denominator does. Slides 3–4, lines 57–72. `erratum2026`, `[V]`, attributed to the reader and not the lecturer.
- **"You cannot check a claim whose terms are undefined"** — slide 4, line 98. The chapter's own justification for pre-defining the pass criterion, and the sentence the rest of the course's verification thread rests on.
- **The minimal eval** — five frozen cases from the room's own work, one binary pass criterion per case fixed before any output is seen and checkable without seeing the other condition, run A, run B, count. Slide 5, lines 116–118. Full specification, including the four criterion-writing rules, is `assets/eval-worksheet/README.md` §4.
- **Case calibration by difficulty** — a case the model always passes or always fails has zero power at any sample size; write ten candidates, run each three times at baseline, discard 3/3 and 0/3, keep the five nearest the middle. Slide 6, lines 142–144. **Carry [ch04-005] with it: the selection is not free, and the noise floor measured on the survivors overstates the instrument's movement on ordinary work.**
- **A′, the repeated baseline** — a repeatability check on an instrument, read before any A-versus-B result; if A and A′ disagree on k of five, treat any A–B difference of k or fewer as inside the noise. Slides 7–8, lines 170 and 197. **Two caveats travel with it: the B arms carry no replicate, so their spread is assumed rather than measured ([ch04-004]); and the session policy that makes "with nothing changed" true is stated only in the worksheet ([ch04-008]).**
- **Blinding, with its limit disclosed rather than solved** — strip condition labels, opaque IDs, shuffle, grade pass/fail, unblind afterwards; discard the thinking transcript at capture because it identifies B3 with certainty; insert duplicates to measure grader drift, which A′ does not. It is not a blind against the person who designed the conditions, and closing that needs a second grader who does not exist. Slide 9, lines 221–232. The disclose-rather-than-oversell form is the reusable object.
- **A paired sign test on five cases cannot reach two-sided *p* < 0.05 under any outcome; six is the minimum, and power at α = 0.05 is exactly zero** — combinatorial, not an estimate. Slide 10, lines 247–261. Every value in the p-value table was recomputed here and is exact.
- **The best obtainable result is weak and rare** — under a +20-point effect on a 50% baseline, about 2.5 of five cases are expected to be discordant; the 5–0 sweep carries a likelihood ratio of 5.4 and occurs 0.5% of the time even when the effect is real; 103 cases are needed for 80% power. Slide 11, lines 280–284. **All five figures assume zero within-case correlation between the arms — state it ([ch04-003]) — and the 103 is exact while the "discreteness" explanation beside it is not ([ch04-011]).**
- **State the limit before showing the result** — slide 11, line 291. The chapter's rhetorical thesis and the reason its audience grants it credibility; later chapters presenting weak evidence should follow the same order.
- **Five cases buy a screen, a noise floor and a habit — not a finding.** Slide 12, lines 308–310. The honest scope of every small eval in the course.
- **Declare every arm** — reporting only the interesting arm is post-hoc selection of the winning condition. Slide 13, lines 334 and 340–341. **Export the rule, not the number: the 18% family-wise figure is wrong by about 30× ([ch04-002]).**
- **Two disagreements out of five gives a 95% interval of roughly (0.05, 0.85)** — the noise floor is a conservative screen, not an instrument. Slide 13, line 333. Clopper–Pearson, recomputed here as (0.0527, 0.8534).
- **The persona accuracy claim, settled** — 162 roles, four model families, 2,410 factual questions; personas in system prompts did not improve performance over no persona. Its scope is those families and that question set, not Opus 5 and not civil engineering. Slide 15, lines 386–388. `zheng2024`, `[V]`. This closes the claim ch03 left open.
- **Post-hoc selection of the winning condition, named and generalised** — picking the best persona per question helps, but identifying it in advance is no better than chance; the same mechanism will manufacture a result out of five cases. Slide 15, lines 394–397. The paper establishes it for persona selection; the generalisation to prompting folklore is the course's own.
- **The chain-of-thought claim is not settled, and the room's own eval is what settles it.** Slide 16. The `[P]` re-evaluation is withheld under `TODO(verify)` rather than quietly used. **Do not let a later chapter cite this chapter as having resolved it — and see [ch04-006]: the scope argument itself belongs to ch03 unless it is moved.**
- **Record the version or you have recorded nothing** — model ID and date beside every result, plus the settings that change behaviour (thinking, effort, fresh session or not); a working prompt is a measurement and measurements expire, so re-test before relying on it again. Slide 17, lines 444–446. **"Fresh session" is undefined in the delivered curriculum ([ch04-008]) and the effort dial may be unreachable from the room's surface ([ch04-010]).**
- **Verification thread opened** — prompts here, sources in Chapter 14, arguments in Chapter 17, the logging discipline in Chapter 18. Slide 17, lines 452–453.
- **Not exported: "extended thinking off" as a runnable condition.** The B3 arm as written is not a valid configuration at the eval's own `xhigh` baseline ([ch04-001]). No later chapter may assume this room has a thinking on/off switch independent of effort.
