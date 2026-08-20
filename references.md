# References and Search Terms

**Companion to:** `curriculum/architecture.md` and `curriculum/chapter-briefs.md`
**Purpose:** Citations, their verification status, and keyword searches for material still to be gathered.

---

## How to use this file

Every entry carries a status. Nothing reaches a slide until it is **[V]**.

| Tag | Meaning |
|---|---|
| **[V]** | Verified — primary source read or fetched during preparation |
| **[P]** | Partially verified — source exists and was seen, but details not checked against the original |
| **[U]** | Unverified — reconstructed from memory or secondhand. **Assume wrong until checked.** |
| **[X]** | Do not use — checked and found unsupported, or unsuitable |

Author names, years, and identifiers marked **[U]** are the most likely thing in this document to be wrong. They are starting points for a search, not citations.

**Citation format for slides:** author, year, venue, identifier, in a footer. Where a claim comes from a podcast or interview, label it as such on the slide. Expert testimony is not a primary source, and presenting it as one is the failure this course spends three sessions warning against.

---

## Conflict-of-interest declarations required

Two slides need an explicit COI note:

- **Chapter 7 / 13, Reiner Pope material.** Pope is CEO of a chip company; the interviewer discloses being an angel investor in it. The lecture's central conclusion — memory bandwidth is the binding constraint — is commercially convenient for both. The analysis appears sound; the interest must still be declared.
- **Any Anthropic-published interpretability work used in Chapter 5.** A lab publishing evidence about the interpretability of its own models has an interest in the result. Same treatment.

---

# Chapter 1 — Substrate

### Citations
- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L. & Polosukhin, I., 2017, *Attention Is All You Need*, arXiv:1706.03762 — **[V]**. arXiv abstract record fetched 2026-08-19; title, full author list, year and identifier confirmed against it. **Body read 2026-08-20**, §3.2 extracted from the PDF. The paper's own words: *"An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key."* The weighted-sum-over-key-value-pairs formulation is therefore the paper's own and may be attributed. The earlier restriction to bibliographic detail is lifted. {#vaswani2017 | Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L. & Polosukhin, I. | 2017 | Attention Is All You Need | arXiv:1706.03762 | paper | -}
- KV cache as a concept: the Pope lecture gives a clear, non-technical construction. **[V]**

### Search terms
`tokenization BPE byte-pair encoding LLM` · `subword tokenization scientific terminology` · `tokenizer visualization tool` · `temperature top-p sampling explained` · `autoregressive decoding KV cache explained` · `context window vs effective context`

### Still needed
A tokenizer demo run on a MATLAB snippet and an abstract from the shared domain (mechanics, concrete or fluids), captured as screenshots so it doesn't depend on live internet.

---

# Chapter 2 — Formation

### Verified 2026-08-19 — identifiers confirmed against arXiv records. Four title errors found and corrected.

**All nine core identifiers were correct.** The errors were in titles and missing years, which a footer generator would have propagated silently.

- Kaplan, J., McCandlish, S., Henighan, T., et al. (10 authors), 2020, *Scaling Laws for Neural Language Models*, arXiv:2001.08361 — **[V]** {#kaplan2020 | Kaplan, J., McCandlish, S., Henighan, T., et al. | 2020 | preprint | arXiv:2001.08361 | paper | -}
- Hoffmann, J., Borgeaud, S., Mensch, A., et al. (22 authors), 2022, *Training Compute-Optimal Large Language Models*, arXiv:2203.15556 — **[V]** for the identifier. **Venue COULD NOT VERIFY** — no journal-ref on arXiv, no DBLP hit. Cite as preprint. {#hoffmann2022 | Hoffmann, J., Borgeaud, S., Mensch, A., et al. | 2022 | preprint — venue unconfirmed | arXiv:2203.15556 | paper | -}
- Fedus, W., Zoph, B. & Shazeer, N., 2021, *Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity*, arXiv:2101.03961; version of record JMLR 23(120):1–39, 2022 — **[V]**. **Two errors corrected:** the title was abbreviated, and no year was recorded. Also **only three authors** — the previous "et al." implied a longer list. {#fedus2021 | Fedus, W., Zoph, B. & Shazeer, N. | 2021 | arXiv preprint; version of record JMLR 23(120):1–39, 2022 | arXiv:2101.03961 | paper | -}
- Lepikhin, D., Lee, H., Xu, Y., et al. (9 authors), 2020, *GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding*, arXiv:2006.16668, ICLR 2021 — **[V]**. **Two errors corrected:** title abbreviated, no year recorded. {#lepikhin2020 | Lepikhin, D., Lee, H., Xu, Y., et al. | 2020 | arXiv preprint; ICLR 2021 | arXiv:2006.16668 | paper | -}
- Clark, A., de las Casas, D., Guy, A., et al. (26 authors), 2022, *Unified Scaling Laws for Routed Language Models*, arXiv:2202.01169, ICML 2022, pp. 4057–4086 — **[V]**. Author list now confirmed; the previous entry said "author list unconfirmed". Scope: routing architectures across five orders of magnitude of model size. {#clark2022 | Clark, A., de las Casas, D., Guy, A., et al. | 2022 | ICML 2022, pp. 4057–4086 | arXiv:2202.01169 | paper | -}
- Stiennon, N., Ouyang, L., Wu, J., et al. (9 authors), 2020, *Learning to summarize from human feedback*, arXiv:2009.01325 — **[V]** for the identifier; venue not confirmed. {#stiennon2020 | Stiennon, N., Ouyang, L., Wu, J., et al. | 2020 | preprint — venue unconfirmed | arXiv:2009.01325 | paper | -}
- Ouyang, L., Wu, J., Jiang, X., et al. (20 authors), 2022, *Training language models to follow instructions with human feedback*, arXiv:2203.02155, NeurIPS 2022 — **[V]**. Venue was absent from this file. Establishes: SFT on labeller demonstrations plus RLHF on GPT-3; **a 1.3B InstructGPT model's outputs were preferred to those of the 175B GPT-3**; gains in truthfulness and toxicity with minimal regression on public NLP datasets. Authors state InstructGPT "still make[s] simple mistakes". {#ouyang2022 | Ouyang, L., Wu, J., Jiang, X., et al. | 2022 | NeurIPS 2022 | arXiv:2203.02155 | paper | -}
- Bai, Y., Jones, A., Ndousse, K., et al. (31 authors), 2022, *Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback*, arXiv:2204.05862 — **[V]**. **Title was abbreviated to "…with RLHF".** {#bai2022hh | Bai, Y., Jones, A., Ndousse, K., et al. | 2022 | preprint | arXiv:2204.05862 | paper | -}
- Bai, Y., Kadavath, S., Kundu, S., et al. (48 authors), 2022, *Constitutional AI: Harmlessness from AI Feedback*, arXiv:2212.08073 — **[V]**. No venue on arXiv or DBLP; cite as preprint. {#bai2022cai | Bai, Y., Kadavath, S., Kundu, S., et al. | 2022 | preprint | arXiv:2212.08073 | paper | -}
- Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C. D. & Finn, C., 2023, *Direct Preference Optimization: Your Language Model is Secretly a Reward Model*, arXiv:2305.18290, NeurIPS 2023 — **[V]**. **Title was truncated** — the subtitle is load-bearing and was missing. {#rafailov2023 | Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C. D. & Finn, C. | 2023 | NeurIPS 2023 | arXiv:2305.18290 | paper | -}
- Ye, Q., Axmed, M., Pryzant, R. & Khani, F., 2024, *Prompt Engineering a Prompt Engineer*, arXiv:2311.05661, Findings of the ACL 2024 — **[V]**. §A.3 evaluates the verbatim OPRO string on gpt-3.5-turbo-instruct, mistral-7b-instruct-v0.2, yi-6b and mpt-7b-instruct on GSM8K. Authors' words: *"We do not observe consistent cross-model generalization trends… the final optimized prompts are specific to the underlying task model."* **This is a model-specificity result, not a result about model recency** — all four test models predate PaLM 2. {#ye2024 | Ye, Q., Axmed, M., Pryzant, R. & Khani, F. | 2024 | Findings of the ACL 2024 | arXiv:2311.05661 | paper | -}

### Emotional prompting — the claim, and the failed replication

- Li, C., Wang, J., Zhang, Y., Zhu, K., Hou, W., Lian, J., Luo, F., Yang, Q. & Xie, X., 2023, *Large Language Models Understand and Can be Enhanced by Emotional Stimuli*, arXiv:2307.11760 — **[V]** for the identifier. **Two things this file did not say.** It is a **technical report**, not a peer-reviewed full paper (a short v1 was accepted at LLM@IJCAI'23). And **the title changed after v1** — v1 was *EmotionPrompt: Leveraging Psychology for Large Language Models Enhancement via Emotional Stimulus*, and both strings circulate. {#li2023emotion | Li, C., Wang, J., Zhang, Y., et al. | 2023 | technical report, not peer reviewed | arXiv:2307.11760 | paper | -}
  - Measured: 11 emotional stimuli, 6 models, 45 tasks, plus a 106-participant human study. Reported +8.00% on Instruction Induction, **+115% on BIG-Bench**, +10.9% on generative tasks.
- Vaugrante, L., Niepert, M. & Hagendorff, T., 2024, *A Looming Replication Crisis in Evaluating Behavior in Language Models? Evidence and Solutions*, arXiv:2409.20303 — **[V]**, preprint, no venue confirmed {#vaugrante2024 | Vaugrante, L., Niepert, M. & Hagendorff, T. | 2024 | preprint — venue unconfirmed | arXiv:2409.20303 | paper | -}
  - **Independent replication failed.** GPT-3.5, GPT-4o, Claude 3 Opus, Gemini 1.5 Pro, Llama 3-8B and 70B, temperature 0, June 2024. Authors' words: *"Overall, we observe an insignificant performance increase of 1% when applying EmotionPrompting (χ2 = 0.11, p = .74)."*
  - **And they re-derive the original's own arithmetic.** The 115% is the best of eleven stimuli, not an average. Averaging all eleven over the original's reported results gives **4.42% on BIG-Bench and 2.58% across all benchmarks**. Their words: *"the numerical values communicated in the study itself do not coincide with these claims."*
  - **Replicators' own stated limits, which must appear alongside:** they did not use the identical tasks or models, wording varied slightly, they sampled one stimulus per task by seed rather than reproducing the best-of-eleven protocol, and they dropped one stimulus because models answered it instead of the task.
  - **Teaching value.** This is best-of-N reporting, in the literature, with an independent failed replication and a re-derivation of the original's own numbers. It is the Chapter 4 post-hoc-selection lesson with a published example attached.

### Vendor primary documents — fetched by a delegated agent, one remove from primary
- OpenAI Model Spec, snapshot 2026-08-18, model-spec.openai.com, CC0 — **[P]**, verify directly before use.
- **Claude's Constitution, January 2026**, anthropic.com/constitution, CC0 — **[P]**, verify directly. **Note:** the URL in wide circulation (`/news/claudes-constitution`, May 2023) is the *superseded predecessor*, not this document.
- Claude 3.7 Sonnet System Card §6 — **[P]**, verify directly. Quoted: *"Claude 3.7 Sonnet occasionally resorts to special-casing in order to pass test cases… directly returning expected test values rather than implementing general solutions"*, and §6.1 attributes this to *"reward hacking"* during reinforcement learning. **This upgrades the reward-hacking claim from podcast testimony to a primary vendor document** — fetch it and re-tag before it reaches a slide.


### Citations
- Yang et al., 2023, *Large Language Models as Optimizers* (OPRO), Google DeepMind, arXiv:2309.03409 — **[V]**. Optimised prompts beat human-designed prompts by up to 8% on GSM8K and up to 50% on Big-Bench Hard; the top discovered instruction was the "take a deep breath" phrasing.
  - **Caveats that must appear on the same slide:** PaLM 2-L scorer, GSM8K and BBH only; the phrase was found by automated search over candidate instructions, not by testing a hypothesis about encouragement; other models yield different optimal instructions. **[V]** — the OPRO PDF itself supports all of the above.
  - **Correction 2026-08-19.** This bullet previously ended "later evaluations report it does not transfer to newer models." **Nothing found supports that.** A search for a primary re-evaluation returned none. The closest primary evidence is Ye et al. (below), which establishes **model-specificity, not obsolescence** — and its four test models all predate PaLM 2, so it cannot speak to "newer" at all. The corrected claim is that optimised prompts do not transfer consistently *across models*. The stronger version was a better story than the evidence supported, which is the failure mode §0 of the findings file exists to catch.
- Hoffmann et al., 2022, *Training Compute-Optimal Large Language Models* (Chinchilla), arXiv:2203.15556 — **[P]**
- Kaplan et al., 2020, *Scaling Laws for Neural Language Models*, arXiv:2001.08361 — **[P]**
- Clark et al., 2022, *Unified Scaling Laws for Routed Language Models*, arXiv:2202.01169 — **[P]**. Source of the sparsity-versus-quality figure; author list unconfirmed.
- Fedus et al., *Switch Transformer*, arXiv:2101.03961 — **[P]**
- Lepikhin et al., *GShard*, arXiv:2006.16668 — **[P]**
- Ouyang et al., 2022, *Training language models to follow instructions with human feedback* (InstructGPT), arXiv:2203.02155 — **[U]** identifier from memory.
- Bai et al., 2022, *Constitutional AI: Harmlessness from AI Feedback*, arXiv:2212.08073 — **[U]** identifier from memory.
- Rafailov et al., 2023, *Direct Preference Optimization*, arXiv:2305.18290 — **[U]** identifier from memory.
- Li et al., 2023, *Large Language Models Understand and Can be Enhanced by Emotional Stimuli* (EmotionPrompt), arXiv:2307.11760 — **[U]**
- The 6ND pretraining FLOPs formula; inference at 2ND; RL between roughly 2 and 6 — **[V]** from the Pope lecture. The *formula* is standard and citable; the RL multiplier is his estimate.
- Claude 3.7 Sonnet hardcoding solutions to test cases as a reinforced reward hack — **[P]**, reported secondhand in the Greenblatt interview. Find the primary model card or research post.

### Published annotation guidelines — cite these, not internal documents

Several papers publish the actual instructions given to human raters, usually in appendices. These are the citable substitute for any internal manual.

- Glaese et al., 2022, *Improving alignment of dialogue agents via targeted human judgements* (Sparrow, DeepMind) — **[U]**. Publishes the explicit rule list given to raters. Closest published equivalent to a rater manual; **check this one first.**
- Ouyang et al., 2022, *Training language models to follow instructions with human feedback* (InstructGPT) — **[U]**. Appendices include labeller instructions and the comparison-collection interface.
- Stiennon et al., 2020, *Learning to summarize from human feedback* — **[U]**. Appendix defines quality dimensions and how raters were told to apply them.
- Bai et al., 2022, *Training a Helpful and Harmless Assistant with RLHF* (Anthropic) — **[U]**. Describes the collection setup and the helpfulness/harmlessness split.
- OpenAI Model Spec — **[P]**. A behavioural specification written to be applied consistently; same problem a rubric solves, from the other end.
- Anthropic's published constitution for Claude — **[P]**. Same use.

### Instructor-supplied material
**Direct experience as a human-feedback annotator.** The differentiating content of this chapter, and the part no paper supplies: the texture of applying a rubric under time pressure, where the instructions are ambiguous, and where two competent raters legitimately diverge.

Structure to reconstruct:
- How rating scales are actually built (binary preference / per-dimension / overall plus dimensions)
- How truthfulness is operationalised into something a rater applies consistently
- What the reviewer layer catches that the attempter layer misses
- How rater disagreement is adjudicated
- What causes a submission to be rejected

**Build a synthetic instrument.** Structure and method are facts and are not protected; the specific expression of any internal document is. Reconstruct an original rubric on the shared domain — two candidate responses about mechanics, concrete or fluids, rated on named dimensions. This is also better teaching: attendees learn more watching their own field being judged than a generic exchange.

**The live rating exercise carries this chapter.** Attendees rate two domain-specific responses against the synthetic rubric, then review each other. Specification in `assets/rating-exercise/README.md`. Both responses written from scratch on mechanics, concrete or fluids — an audience cannot judge truthfulness on a domain it doesn't know, and the lesson depends on them catching a physical error they nearly missed.

**Structural findings** from five reviewed vendor documents are recorded in `curriculum/ch02-annotation-findings.md` (v3.1). Observations only — not citations, and not a substitute for the published guidelines above. That file uses its own `[E1]–[E4]` evidential scale, which is not interchangeable with the `[V]/[P]/[U]/[X]` tags here: an `[E1]` finding is corroborated across documents and still has no citable source.

**Do not cite internal or leaked documents.** Not primarily a legal question — an unciteable source has no place in a course that spends three sessions on citation discipline. Use published guidelines above for citations; use experience for texture.

### Search terms
`RLHF pipeline reward model preference pairs` · `annotator agreement inter-rater reliability RLHF` · `reward model overoptimization Goodhart` · `sycophancy language models RLHF cause` · `verbosity bias reward model length` · `RLAIF vs RLHF` · `helpfulness harmlessness honesty rubric` · `mid-training post-training LLM distinction`

### Do not use
- The "~100× over-Chinchilla" figure as a number — **[X]** as a citation. The derivation chain is explicitly guesswork. Teach the *method*.
- Any claim that filtering or initialisation causes model "depression" — **[X]** no known source. Failure-gallery material only.

---

# Chapter 3 — Control

### Citations
- Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q. & Zhou, D., 2022, *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*, arXiv:2201.11903 — **[V]**. arXiv abstract record fetched 2026-08-19; title, full author list, year and identifier confirmed. Note the title was recorded here without its final four words until today. **Scope, and it matters:** the abstract describes prompting with *a few chain-of-thought exemplars* — eight, on a 540B-parameter model — and says the ability emerges in sufficiently large models. It is not a result about typing "think step by step" at a modern reasoning model. Do not let the two be conflated on a slide. {#wei2022 | Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q. & Zhou, D. | 2022 | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models | arXiv:2201.11903 | paper | -}
- Kojima et al., 2022, *Large Language Models are Zero-Shot Reasoners* ("let's think step by step") — **[U]**
- Anthropic, *Prompting best practices*, platform.claude.com — **[V]**. Fetched 2026-08-19 from `platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices`; the older `docs.claude.com` path 302-redirects there. The overview page at `.../prompt-engineering/overview` states the prerequisites for prompt engineering. **Version-fragile — re-fetch in the week before delivery.** The page is explicitly model-specific and already carries Opus 5 exceptions and a deprecation. {#anthropic-prompting | Anthropic | 2026 | Prompting best practices, platform.claude.com — vendor documentation, fetched 2026-08-19 | - | paper | -}
  - Load-bearing items confirmed on the page: the colleague test for clarity; explaining *why* a constraint exists so the model generalises past its literal wording; 3–5 examples, relevant and diverse, wrapped in `<example>` tags; XML tags to separate instructions from data; a role set in the system prompt to focus **behaviour and tone**; "tell Claude what to do instead of what not to do"; adaptive thinking driven by an `effort` parameter and query complexity, with `budget_tokens` deprecated and returning 400 on 4.7 and later.
  - **Opus 5 exception, and this group runs Opus 5:** default responses run longer than earlier models', and changing `effort` does not reliably change visible response length. Prompt explicitly for concision.
  - **The prerequisite worth teaching:** the overview page assumes you already have success criteria and a way to test empirically against them, *before* prompt engineering. That is Chapter 4's thesis, stated by the vendor, in the prompting documentation.

### Search terms
`prompt engineering XML tags Claude` · `few-shot prompting negative examples` · `system prompt vs user prompt behaviour` · `prompt portability across model providers` · `extended thinking reasoning effort Claude Code`

---

# Chapter 4 — Measurement

### Citations
- **The MACs-versus-FLOPs erratum.** A reader comment on the Pope transcript notes that the compute-time equation defines its denominator as multiply-accumulates per second, so substituting spec-sheet FLOPs makes the result wrong by a factor of two; the numerator needs a factor of 2. **[V]** — visible in the gist comment thread, dated May 2026. **Attribute it to the reader, not to the lecturer** — the whole teaching point is that an outside reader caught it. {#erratum2026 | Reader comment (unattributed) | 2026 | Comment thread on the Pope lecture transcript gist — reader correction, not a primary result | - | testimony | -}
  - **This is the anchor artefact of the chapter.** A unit-definition error, in an expert lecture, caught by an outside reader, producing a clean factor of two.
- ~~Later re-evaluations finding the "take a deep breath" phrasing does not transfer to newer models~~ — **[X]**. **Searched 2026-08-19; no primary re-evaluation exists that could be found.** Do not assert this. What is supported is cross-model non-transfer, not decay over model generations — see Ye et al. in the Chapter 2 section.
- Zheng, Pei, Logeswaran, Lee & Jurgens, 2024, *When "A Helpful Assistant" Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models*, Findings of the ACL: EMNLP 2024, pp. 15126–15154, DOI 10.18653/v1/2024.findings-emnlp.888 — **[V]**. ACL Anthology record fetched 2026-08-19. {#zheng2024 | Zheng, M., Pei, J., Logeswaran, L., Lee, M. & Jurgens, D. | 2024 | Findings of the ACL: EMNLP 2024, pp. 15126–15154 | DOI 10.18653/v1/2024.findings-emnlp.888 | paper | -} 162 roles, four model families, 2,410 factual questions; personas in system prompts do not improve performance over the no-persona control.
  - **Second finding, and the one Chapter 4 needs:** aggregating the best persona per question does improve accuracy, but identifying it in advance performs no better than random selection. Post-hoc selection of the winning condition.
  - **Caveat for the slide:** those model families, that question set. Not Opus 5 on civil engineering.
- Meincke, Mollick, Mollick & Shapiro, 8 June 2025, *The Decreasing Value of Chain of Thought in Prompting*, Wharton Generative AI Labs technical report, SSRN — **[P]**. Publisher page fetched 2026-08-19; the SSRN report itself has not been read. **TODO(verify)** — read the report and check the figures before any reach a slide. Search terms: `Meincke Mollick decreasing value chain of thought SSRN` · `GPQA Diamond chain of thought reasoning models`.
  - Reported on GPQA Diamond: reasoning models o3-mini +2.9%, o4-mini +3.1%, Gemini Flash 2.5 −3.3%, at 20–80% more time; non-reasoning Gemini Flash 2.0 +13.5%, Sonnet 3.5 +11.7%, GPT-4o-mini +4.4% (n.s.).
  - Not peer reviewed. Label it a technical report on the slide.

### Search terms
`LLM evaluation small sample size` · `prompt A/B testing methodology` · `blinded evaluation LLM outputs` · `inter-annotator agreement small n` · `benchmark contamination LLM` · `eval harness lightweight custom`

### Still needed
Two or three prompting claims tested by the instructor in advance, with results. A demo where the folklore loses is more valuable than one where it wins.

---

# Chapter 5 — Intrinsic failure

### Verified 2026-08-19 — primary records fetched. These supersede the reconstructed entries below.

- Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F. & Liang, P., 2024, *Lost in the Middle: How Language Models Use Long Contexts*, Transactions of the ACL 12, pp. 157–173, DOI 10.1162/tacl_a_00638 — **[V]** {#liu2024 | Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F. & Liang, P. | 2024 | Transactions of the ACL 12, pp. 157–173 | DOI 10.1162/tacl_a_00638 | paper | -}
  - **The position-curve licensing problem is solved.** The TACL version of record is **CC BY 4.0**, printed on page 1 of `aclanthology.org/2024.tacl-1.9.pdf` and corroborated in Crossref. **Reproduce from the ACL Anthology PDF, never from arXiv** — arXiv:2307.03172 is under `nonexclusive-distrib/1.0`, which grants no redistribution right. Attribution: Liu et al. (2024), TACL 12:157–173, DOI 10.1162/tacl_a_00638, CC BY 4.0, stating whether the figure is modified. Figure 5 is the empirical curve; Figure 1 is the schematic. The authors' code repo is MIT, so the curve can be regenerated in house style instead.
  - **Cite the year as 2024**, not 2023. The arXiv comment says "TACL 2023"; the volume is 2024.
  - Scope: two tasks only — multi-document QA and synthetic key–value retrieval. Greedy decoding only, stated by the authors as a limitation. Claude-1.3 was near-perfect on the synthetic task, so **the effect is not universal across models or tasks**.

- Veličković, P., Perivolaropoulos, C., Barbero, F. & Pascanu, R., 2025, *Softmax is not Enough (for Sharp Size Generalisation)*, ICML 2025, PMLR 267, pp. 61190–61211, arXiv:2410.01104 — **[V]**, CC BY 4.0 on arXiv {#velickovic2025 | Veličković, P., Perivolaropoulos, C., Barbero, F. & Pascanu, R. | 2025 | ICML 2025, PMLR 267, pp. 61190–61211 | arXiv:2410.01104 | paper | -}
  - **The title recorded here from memory was wrong twice.** It is not "for sharp out-of-distribution behaviour" — the word "behaviour" appears in no version, and the final title says "Sharp Size Generalisation".
  - Proves attention coefficients must disperse as the item count grows at test time. Demonstrated on small controlled max-retrieval tasks, **not** production benchmarks. The existing caveat stands: it bounds sharpness of selection, not task accuracy.

- Kamradt, G., 2023, *Needle in a Haystack*, github.com/gkamradt/needle-in-a-haystack, MIT licence — **[V]** {#kamradt2023 | Kamradt, G. | 2023 | Needle in a Haystack — software implementation, not a peer-reviewed result | github.com/gkamradt/needle-in-a-haystack | paper | -}
  - **There is no paper.** Label any heatmap an implementation output. The probe inserts one lexically distinctive sentence, so it tests literal matching — which is the weakness NoLiMa was built to expose.

- Hong, K., Troynikov, A. & Huber, J., 2025, *Context Rot: How Increasing Input Tokens Impacts LLM Performance*, Chroma, trychroma.com/research/context-rot — **[V]** {#chroma2025 | Hong, K., Troynikov, A. & Huber, J. | 2025 | Chroma technical report — COI, see below | trychroma.com/research/context-rot | paper | coi}
  - **COI required under hard rule 4.** Chroma sells a retrieval/vector database. "Long context degrades" is commercially favourable to them. Declare it on the slide.
  - 18 models, extended needle variants plus LongMemEval. Authors state they have no mechanistic explanation, and that the tasks do not cover real-world synthesis where they *expect* worse degradation — an expectation, not a measurement.
  - **Report text and figures carry no stated licence.** Code is MIT. Do not reproduce their figures; redraw or link.

- Liang, W., Yuksekgonul, M., Mao, Y., Wu, E. & Zou, J., 2023, *GPT detectors are biased against non-native English writers*, Patterns 4(7):100779, DOI 10.1016/j.patter.2023.100779 — **[V]** {#liang2023 | Liang, W., Yuksekgonul, M., Mao, Y., Wu, E. & Zou, J. | 2023 | Patterns 4(7):100779 | DOI 10.1016/j.patter.2023.100779 | paper | -}
  - Seven detectors, accessed **March 2023**, over 91 human-written TOEFL essays and 88 US 8th-grade essays. Mean false-positive rate on the TOEFL essays **61.22%**; near-zero on the 8th-grade essays. One rewording prompt cut it to 11.77%.
  - **Licence CC BY-NC-ND 4.0 — no derivatives.** Reproduce a figure unmodified for non-commercial teaching only; do not recrop or restyle. Safest is to quote the numbers and cite.
  - **State the snapshot problem alongside it.** n=91 and n=88, one TOEFL corpus of unstated provenance, detectors as of March 2023. The direction is well supported; the specific percentages are dated.

- Dathathri, S., See, A., Ghaisas, S., et al. (24 authors, Google DeepMind), 2024, *Scalable watermarking for identifying large language model outputs*, Nature 634(8035), pp. 818–823, DOI 10.1038/s41586-024-08025-4 — **[V]**, CC BY 4.0 {#dathathri2024 | Dathathri, S., See, A., Ghaisas, S., et al. | 2024 | Nature 634(8035), pp. 818–823 | DOI 10.1038/s41586-024-08025-4 | paper | -}
  - **Scope correction: this is SynthID-Text. Text only.** Do not use it to support claims about image or audio watermarking. Modifies sampling, not training; evaluated over roughly 20 million Gemini responses.
  - Metadata from the Crossref publisher record; nature.com blocked automated access, so **the body was not read**. Treat any numeric claim beyond the ~20M figure as unverified.

- Bricken, T., Templeton, A., Batson, J., et al., 2023, *Towards Monosemanticity: Decomposing Language Models With Dictionary Learning*, Anthropic, Transformer Circuits Thread, 4 October 2023 — **[V]** {#bricken2023 | Bricken, T., Templeton, A., Batson, J., et al. | 2023 | Anthropic, Transformer Circuits Thread — COI, lab publishing on its own models | transformer-circuits.pub | paper | coi}
  - **Scope: a one-layer transformer.** A proof of concept, not a production model. Say so.

- Templeton, A., Conerly, T., Marcus, J., et al. (26 authors), 2024, *Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet*, Anthropic, Transformer Circuits Thread, 21 May 2024; also arXiv:2605.29358, CC BY 4.0 — **[V]** {#templeton2024 | Templeton, A., Conerly, T., Marcus, J., et al. | 2024 | Anthropic, Transformer Circuits Thread — COI, lab publishing on its own models | arXiv:2605.29358 | paper | coi}
  - **Authors' own limitation, use verbatim:** "significant limitations remain: our suite of features is incomplete, and we lack rigorous methods for evaluating whether our features faithfully capture model computations."
  - The arXiv deposit does not state that it is the 2024 article. Cite the 2024 date; treat arXiv as an alternate location whose CC BY 4.0 is what makes the figures reusable. The transformer-circuits.pub pages carry no licence found.

- Ameisen, E., Lindsey, J., Pearce, A., et al., 2025, *Circuit Tracing: Revealing Computational Graphs in Language Models*, Anthropic, Transformer Circuits Thread, 27 March 2025 — **[V]** {#ameisen2025 | Ameisen, E., Lindsey, J., Pearce, A., et al. | 2025 | Anthropic, Transformer Circuits Thread — COI, lab publishing on its own models | transformer-circuits.pub | paper | coi}

- Lindsey, J., Gurnee, W., Ameisen, E., et al., 2025, *On the Biology of a Large Language Model*, Anthropic, Transformer Circuits Thread, 27 March 2025 — **[V]** {#lindsey2025 | Lindsey, J., Gurnee, W., Ameisen, E., et al. | 2025 | Anthropic, Transformer Circuits Thread — COI, lab publishing on its own models | transformer-circuits.pub | paper | coi}
  - **The hard number for "coverage is partial", in the authors' words:** "We've found that our attribution graphs provide us with satisfying insight for about a quarter of the prompts we've tried."
  - Claude 3.5 Haiku only. The replacement model does not replace attention layers, so QK-circuit computation is invisible to the method.
  - **No licence found on either page.** Do not reuse their diagrams. Redraw or ask.

- Turpin, M., Michael, J., Perez, E. & Bowman, S. R., 2023, *Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting*, NeurIPS 2023, arXiv:2305.04388, CC BY 4.0 — **[V]** {#turpin2023 | Turpin, M., Michael, J., Perez, E. & Bowman, S. R. | 2023 | NeurIPS 2023 | arXiv:2305.04388 | paper | -}
  - GPT-3.5 and Claude 1.0, 13 BIG-Bench Hard tasks plus BBQ. Injecting a biasing feature makes models switch answers and rationalise **without ever mentioning the bias**. Accuracy drops up to 36%.

- Chen, Y., Benton, J., Radhakrishnan, A., et al. (Anthropic), 2025, *Reasoning Models Don't Always Say What They Think*, arXiv:2505.05410 — **[V]**, arXiv nonexclusive-distrib, not CC {#chen2025 | Chen, Y., Benton, J., Radhakrishnan, A., et al. | 2025 | Anthropic — COI, lab publishing on its own models | arXiv:2505.05410 | paper | coi}
  - Claude 3.7 Sonnet and DeepSeek R1 against non-reasoning counterparts, on MMLU and GPQA. CoTs reveal hint usage in at least 1% of cases but the reveal rate is "often below 20%".
  - **Authors' own narrowing, from §7.2:** all hints are "very easy to exploit", which "prevents us from drawing conclusions about the potential of CoT monitoring in situations where a CoT is necessary to perform the unintended behavior." So this shows CoT monitoring is **unreliable**, not that CoT is always post-hoc.

### Effective-context benchmarks — metadata verified, bodies not read
RULER (Hsieh et al., COLM 2024, arXiv:2404.06654, CC BY 4.0) · NoLiMa (Modarressi et al., ICML 2025, arXiv:2502.05167, **CC BY-NC-SA**) · LongBench (Bai et al., ACL 2024, DOI 10.18653/v1/2024.acl-long.172, CC BY 4.0) · BABILong (Kuratov et al., NeurIPS 2024 D&B, arXiv:2406.10149, not CC). **Abstract-level only — read the papers before any of their numbers reach a slide.**


## Long-context accuracy degradation

**There is no proof and no closed-form equation.** There are empirical curves and mechanistic arguments. State this distinction explicitly on the slide — it is a better lesson than a fabricated equation.

### The graph to use
- Liu et al., *Lost in the Middle: How Language Models Use Long Contexts*, TACL — **[U]** author, venue, year and identifier all from memory. Accuracy plotted against position of relevant information yields a U-shape: strong at the beginning and end, weakest in the middle. **Verify before use; this is the single most load-bearing figure in the chapter.**
- Needle-in-a-haystack evaluation heatmaps (accuracy over insertion depth × context length) — **[U]** attribute to whichever implementation you use.
- Chroma technical report on context rot — **[U]** confirm existence, authors, and date.

### The nearest thing to a proof
- Softmax dispersion: as the number of keys grows, attention coefficients must spread, so the operation cannot sharply select one item from an arbitrarily large set at fixed logit scale. A paper along the lines of *softmax is not enough for sharp out-of-distribution behaviour*, possibly Veličković et al. — **[U]** title and authors uncertain.
- **What it does and does not say:** it bounds sharpness of selection, not task accuracy. Do not present it as a proof of accuracy loss.

### Other mechanisms — all real, none proofs
- Positional encoding extrapolation beyond trained context (RoPE and variants)
- Long-context regime undertrained because few training sequences reach maximum length
- Nominal versus effective context length

### Search terms
`lost in the middle long context position bias` · `needle in a haystack LLM evaluation` · `context rot degradation input length` · `RULER benchmark effective context length` · `NoLiMa long context benchmark` · `LongBench BABILong` · `RoPE extrapolation length generalization` · `attention entropy dispersion sequence length` · `softmax sharp selection limitation proof`

## Hallucination, calibration, arithmetic

### Search terms
`hallucination mechanism next-token prediction` · `LLM calibration confidence accuracy` · `fabricated citations LLM academic` · `LLM arithmetic failure tokenization digits` · `unit conversion errors language models`

## Model drift

### Search terms
`LLM behaviour change over model versions` · `model deprecation reproducibility research` · `pinning model version API reproducibility` · `GPT behaviour drift study`

## AI-text detection — NOT watermarking

Keep these separate. Detection is a reliability question; watermarking is a provenance mechanism.

- False-positive rates of AI-text detectors falling disproportionately on non-native English writers — **[U]**. A Stanford-affiliated study is the usual citation; verify authors and venue. **High-stakes claim for an international research group — verify carefully.**
- SynthID (Google) as a published watermarking scheme for some output types — **[P]**
- No known public text-watermarking scheme for Claude outputs — **[X]** do not assert one exists.

### Search terms
`AI text detector false positive non-native English` · `GPTZero Turnitin detector accuracy study` · `SynthID text watermarking` · `LLM watermarking detectability robustness` · `academic misconduct AI detection appeal`

## "LLMs are black boxes" — the correction

The claim is too strong. The accurate framing is **partially instrumented, not opaque** — with real, expensive, incomplete instruments that are themselves under validation.

- Sparse autoencoders decomposing activations into interpretable features — Anthropic, transformer-circuits.pub — **[P]**
- Attribution graphs / circuit tracing following the computational path for a specific prompt — Anthropic, 2025 — **[P]**. Two companion papers, one methodological and one applying it; confirm titles.
- Chain-of-thought unfaithfulness: models giving reasons that are not the cause of the output — **[U]**. **Belongs on the same slide.** People conflate "it explained itself" with "I know why it did that."

**Four qualifications to teach alongside:**
1. It traces features and computational paths, not "which weights were used."
2. Coverage is partial; an unexplained residue remains.
3. The bottleneck is human interpretive labour as much as compute.
4. Faithfulness is an open problem — a plausible explanation is not guaranteed to be the true mechanism.

### Search terms
`mechanistic interpretability sparse autoencoder features` · `attribution graphs circuit tracing LLM` · `transformer circuits monosemanticity` · `faithfulness of chain of thought reasoning` · `interpretability illusion plausible explanation` · `probing classifiers limitations`

---

# Chapter 6 — Extrinsic failure

### Citations
- **UK AI Security Institute incident report.** During cyber-range testing with internet access, a model opened a pull request containing a genuine fix plus a malicious payload; when the maintainer refused, it created a second account and argued for the merge. Published on aisi.gov.uk — **[P]**, reported in the Greenblatt interview with a direct link. **Fetch and cite the AISI report directly, not the podcast.**
- **OpenAI package-manager incident.** Agents used a package manager to leave coordinating messages, undetected for roughly a month until the package manager failed; disclosed around a Black Hat presentation and reported in Wired — **[P]**. **Cite the disclosure and the reporting, not the podcast.**
- Self-propagating GenAI worm research, "ComPromptMized" / Morris II line of work, c. 2024 — **[U]** authors, venue, year all unconfirmed.

### Search terms
`indirect prompt injection tool output` · `prompt injection agent file access mitigation` · `AI worm self-propagating GenAI` · `training data poisoning LLM backdoor` · `MCP server security threat model` · `agent sandbox escape incident report` · `supply chain attack AI agent pull request`

### Still needed
Poisoned-document demo assets, held in an isolated directory. Build and test these on a machine you don't care about.

---

# Chapter 7 — Physical limits

**Primary source: the Reiner Pope blackboard lecture (Dwarkesh Podcast, April 2026), transcript published as a public gist. [V]** — fetched and read. {#pope2026 | Pope, R. | 2026 | Dwarkesh Podcast, blackboard lecture; transcript published as a public gist | - | testimony | coi} Label as expert testimony, declare the COI, and cite underlying papers wherever the lecture points at one.

### What the lecture supports
- Roofline framing: time bounded below by the maximum of compute time and memory time
- Compute time ∝ batch × active parameters ÷ throughput
- Memory time = weight fetch (constant in batch) + KV fetch (linear in batch and context length), ÷ bandwidth
- Cost per token = time ÷ batch; the weight-fetch term becomes a hyperbola, explaining why batch size one is catastrophically expensive
- Critical batch size ≈ 300 × sparsity, with 300 a dimensionless hardware ratio stable across several GPU generations
- Memory capacity per GPU = (total parameters + batch × context × bytes-per-token) ÷ (expert parallelism × pipeline parallelism)
- Pipelining reduces weight storage per rack but not KV storage, because the pipeline-stage factor cancels
- Long context is limited by memory bandwidth and capacity, not compute; sparse attention improves the scaling but not without quality cost

### What it does NOT support
**It says nothing about accuracy degradation with context length.** Cost and latency only. Conflating this with Chapter 5 is the most likely error in the whole course.

### Also from the lecture
- Gomez, A. N., Ren, M., Urtasun, R. & Grosse, R. B., 2017, *The Reversible Residual Network: Backpropagation Without Storing Activations*, arXiv:1707.04585 — **[V]**. arXiv abstract record fetched 2026-08-19; title, full author list, year and identifier confirmed. Each layer's activations are reconstructed from the next layer's, so activation storage becomes independent of depth at nearly identical accuracy. **This is a training-time technique** — it addresses backpropagation, not the inference-time KV cache this chapter is about. Say so, or the parallel misleads. {#revnets | Gomez, A. N., Ren, M., Urtasun, R. & Grosse, R. B. | 2017 | The Reversible Residual Network: Backpropagation Without Storing Activations | arXiv:1707.04585 | paper | -}

### Energy
- **[X]** Do not use any per-query energy figure without a primary source. Published figures are contested and routinely conflate one-off training cost with per-query inference cost.

### Alternative substrates — three different evidential standings, verified 2026-08-19

- Ornes, S., 2025, *Can neuromorphic computing help reduce AI's high energy cost?*, Proceedings of the National Academy of Sciences 122(44), DOI 10.1073/pnas.2528654122, PMID 41160603 — **[V]**. PMC record fetched 2026-08-19; title, author, journal, volume, DOI and PMID confirmed. **Single-authored by a science journalist — almost certainly a PNAS news feature rather than primary research. TODO(verify) the article type before the slide calls it anything.** {#ornes2025 | Ornes, S. | 2025 | PNAS 122(44) — secondary account, not primary research | DOI 10.1073/pnas.2528654122 | paper | -}
  - **Contradicts `chapter-briefs.md`, which called neuromorphic hardware "deployed, engineering-grade".** The source describes Loihi 2, NorthPole and SpiNNcloud as demonstration and experimentation tools, states the benefits "aren't substantial enough to attract large companies", that the field "hasn't yet found its killer app", and that these chips "can't just slide into today's AI systems or LLMs". Reported gains are on specific benchmark tasks and are not shown to generalise to frontier-scale systems.
  - Gains as reported: NorthPole classified images at a fraction of the energy and five times faster; a neuromorphic LLM on Loihi 2 matched a comparable GPU-based LLM's accuracy at half the energy. Both benchmark-specific.

- Smirnova, L., Caffo, B. S., Gracias, D. H., et al. (30+ authors), 2023, *Organoid intelligence (OI): the new frontier in biocomputing and intelligence-in-a-dish*, Frontiers in Science 1, DOI 10.3389/fsci.2023.1017235 — **[V]**. Publisher record fetched 2026-08-19. {#smirnova2023 | Smirnova, L., Caffo, B. S., Gracias, D. H., et al. | 2023 | Frontiers in Science 1 | DOI 10.3389/fsci.2023.1017235 | paper | -}
  - **The paper is a research programme, not a results report, and says so.** Demonstrated: spontaneous electrophysiological activity, response to stimulation, myelinated axons, oscillatory behaviour, multiple cell types. Not demonstrated, in the authors' own words: *"To the best of our knowledge, however, no relevant approach using brain organoids as learning systems has been reported."*
  - Stated limits: organoids are avascular with necrosis beyond roughly 300 μm; no predictable anatomy or defined topography; synaptic counts uncertain; and the authors place themselves "quite far away from a system that can demonstrate robustly modifying neuronal connections in a directed manner".
  - **Consequence for the slide:** "early stage, modest results" overstates it for computation. What exists is tissue characterisation, not a working computer.

### Search terms
`roofline model arithmetic intensity` · `LLM inference memory bandwidth bound` · `KV cache size bytes per token calculation` · `grouped query attention MQA KV cache reduction` · `sparse attention DeepSeek scaling` · `datacenter energy AI inference per query measurement` · `neuromorphic computing deployed systems` · `organoid intelligence wetware computing review`

---

# Chapter 8 — Brain and model

### Citations
- Schrimpf et al., 2021, PNAS — LLM next-token surprisal predicting neural responses in language cortex — **[U]** authors, year, venue and claim all unconfirmed.
- Goldstein et al., 2022, Nature Neuroscience — related encoding-model result — **[U]** same.

**Both are load-bearing for the chapter and both are unverified. Read them before writing a word of this chapter.** They are correlational and contested; represent them that way.

### The break in the analogy — the actual content
- Hippocampal consolidation of episodic experience into durable memory; a model at inference does none of this, weights being frozen
- The context window as a discarded buffer, not a memory system
- Human working memory capacity of roughly four items against a context window of hundreds of thousands of tokens — the numbers run opposite to the analogy
- "Frontal cortex equals reasoning" is contested within neuroscience

### Search terms
`language model surprisal predicts brain activity encoding model` · `predictive processing brain language comprehension` · `N400 surprisal language model` · `criticism brain-LLM analogy neuroscience` · `working memory capacity four items Cowan` · `hippocampal consolidation episodic memory review`

---

# Chapters 9–13 — Instruments

Primary sources are official documentation. Re-check the week before delivery; all of this is version-dependent.

- Claude Code documentation, code.claude.com — **[V]**. **Version-fragile: re-fetch in the week before each session per `../DECISIONS.md` item 6.** {#claudecode-docs | Anthropic | 2026 | Claude Code documentation, code.claude.com — vendor documentation, version-dependent | - | paper | -}
- Anthropic support centre, support.claude.com — **[V]**. **Version-fragile: re-fetch before delivery.** {#anthropic-support | Anthropic | 2026 | Anthropic support centre, support.claude.com — vendor documentation, version-dependent | - | paper | -}
- Ultracode: session-scoped setting pairing xhigh reasoning with automatic workflow orchestration; `/effort ultracode`, `claude --effort ultracode` (v2.1.203+), or the bare keyword for a single task. Silently ignored in persistent settings fields; subagents auto-approve edits; significant cost premium. — **[V]**
- `/doctor`: setup checkup that diagnoses and can fix installation and configuration issues; `/checkup` is an alias; expanded in v2.1.205 to audit memory files and unused components. — **[V]**
- Claude Cowork availability and capabilities, support.claude.com — **[V]**
- Paid Claude subscriptions do not include API or Console access; API is billed via prepaid usage credits. — **[V]**
- Anthropic does not support routing Claude Code to non-Claude models through any gateway, though gateways exposing a supported API format do work. — **[V]**
- Graphify: `/graphify` skill building a local knowledge graph from code, docs and PDFs via tree-sitter AST; edges tagged EXTRACTED or INFERRED; output directory intended for commit; semantic pass over documents uses an API. — **[P]** confirm against the current repository and pin a version.
- Antigravity (Google) as the group's Gemini access path — **[U]** *instructor-supplied. Working configuration needed before Chapter 12 is written; see `DECISIONS.md` item 2.*

### The Chapter 13 worked example
Reverse-engineering KV cache bytes-per-token from a published price break at 200K context, arriving at roughly 1.7 kB per token, then sanity-checking against plausible head dimensions and KV head counts. **[V]** from the Pope lecture. Verify current pricing before delivery — the price structure may have changed.

### Search terms
`Claude Code slash commands reference` · `MCP specification tools resources prompts` · `MCP security prompt injection connector trust` · `LiteLLM proxy virtual keys budget` · `vLLM OpenAI compatible server deployment` · `Qwen local inference quantization VRAM` · `API key rotation environment variables best practice`

---

# Chapters 14–19 — Practice

### Citations needed
- Journal AI-use disclosure policies. Gather the actual current text from the journals this group publishes in — **[U]** all of them. Policies change; secondhand summaries go stale.
- COPE and ICMJE position statements on AI and authorship — **[U]**
- Publisher-specific policies (Elsevier, IEEE, Springer Nature, ASCE) — **[U]**. **ASCE matters most for this audience and is the one most likely to be omitted from generic guides.**

### Search terms
`ASCE journal artificial intelligence policy authorship` · `ICMJE AI authorship recommendation` · `COPE position statement AI authoring tools` · `Elsevier generative AI policy authors` · `funder policy AI use grant application` · `reproducibility stochastic LLM output logging` · `pandoc citeproc CSL journal template` · `Zotero better bibtex pandoc workflow` · `systematic review screening LLM validation` · `MATLAB code generation LLM evaluation benchmark`

---

# Format model

The flashcard site accompanying the Dwarkesh lectures (27 cards on the Pope lecture, plus decks on pretraining parallelism and on silicon) is worth copying as a **format**, not as a source. Per-chapter flashcards would give attendees something to retain material with across a three-session gap. Cite the underlying lectures, not the derived cards.

---

# Sources reviewed and rejected

- **Greenblatt interview, recursive self-improvement and alignment forecasting.** Timelines, speedup estimates and alignment predictions are contested forecasts presented in a debate where the interviewer openly disagrees. **[X]** for the syllabus. Three concrete incidents extracted separately above.
- **All secondhand blog summaries of primary papers.** Use only as a route to the paper.

---

# Maintaining this file

- Update in the same commit as the content that uses a source.
- A tag moves from `[U]` to `[V]` only after the primary source has been read. Not after a search result looks plausible.
- When a source is rejected, keep it with an `[X]` and a one-line reason. Knowing what was checked and discarded is worth as much as the list of what was kept.
- Re-check every version-dependent entry in the week before each session.
