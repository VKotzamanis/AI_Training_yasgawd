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
- Vaswani et al., 2017, *Attention Is All You Need*, arXiv:1706.03762 — **[P]** widely known; confirm the identifier.
- KV cache as a concept: the Pope lecture gives a clear, non-technical construction. **[V]**

### Search terms
`tokenization BPE byte-pair encoding LLM` · `subword tokenization scientific terminology` · `tokenizer visualization tool` · `temperature top-p sampling explained` · `autoregressive decoding KV cache explained` · `context window vs effective context`

### Still needed
A tokenizer demo run on a MATLAB snippet and a wave-energy abstract, captured as screenshots so it doesn't depend on live internet.

---

# Chapter 2 — Formation

### Citations
- Yang et al., 2023, *Large Language Models as Optimizers* (OPRO), Google DeepMind, arXiv:2309.03409 — **[V]**. Optimised prompts beat human-designed prompts by up to 8% on GSM8K and up to 50% on Big-Bench Hard; the top discovered instruction was the "take a deep breath" phrasing.
  - **Caveats that must appear on the same slide:** PaLM 2-L scorer, GSM8K and BBH only; the phrase was found by automated search over candidate instructions, not by testing a hypothesis about encouragement; other models yield different optimal instructions; later evaluations report it does not transfer to newer models. **[P]**
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

**Build a synthetic instrument.** Structure and method are facts and are not protected; the specific expression of any internal document is. Reconstruct an original rubric on this group's own domain — two candidate responses about wave energy conversion, rated on named dimensions. This is also better teaching: attendees learn more watching their own field being judged than a generic exchange.

**The live rating exercise carries this chapter.** Attendees rate two domain-specific responses against the synthetic rubric, then review each other. Specification in `assets/rating-exercise/README.md`. Both responses written from scratch on wave energy, PTO or experimental testing — an audience cannot judge truthfulness on a domain it doesn't know, and the lesson depends on them catching a physical error they nearly missed.

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
- Wei et al., 2022, *Chain-of-Thought Prompting Elicits Reasoning*, arXiv:2201.11903 — **[U]** {#wei2022 | Wei et al. | 2022 | Chain-of-Thought Prompting Elicits Reasoning | arXiv:2201.11903 | paper | -}
- Kojima et al., 2022, *Large Language Models are Zero-Shot Reasoners* ("let's think step by step") — **[U]**
- Anthropic prompt engineering documentation, docs.claude.com — **[V]**

### Search terms
`prompt engineering XML tags Claude` · `few-shot prompting negative examples` · `system prompt vs user prompt behaviour` · `prompt portability across model providers` · `extended thinking reasoning effort Claude Code`

---

# Chapter 4 — Measurement

### Citations
- **The MACs-versus-FLOPs erratum.** A reader comment on the Pope transcript notes that the compute-time equation defines its denominator as multiply-accumulates per second, so substituting spec-sheet FLOPs makes the result wrong by a factor of two; the numerator needs a factor of 2. **[V]** — visible in the gist comment thread, dated May 2026.
  - **This is the anchor artefact of the chapter.** A unit-definition error, in an expert lecture, caught by an outside reader, producing a clean factor of two.
- Later re-evaluations finding the "take a deep breath" phrasing does not transfer to newer models — **[P]**. Find a primary re-evaluation rather than a blog summary.
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
- Feistel networks and RevNets, arXiv:1707.04585 — **[P]** — trading compute for memory by making the network invertible. {#revnets | TODO(cite) author unverified | TODO(cite) | RevNets, reached via the Pope lecture | arXiv:1707.04585 | paper | -} Optional; a nice engineering parallel.

### Energy
- **[X]** Do not use any per-query energy figure without a primary source. Published figures are contested and routinely conflate one-off training cost with per-query inference cost.

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

- Claude Code documentation, code.claude.com — **[V]**
- Anthropic support centre, support.claude.com — **[V]**
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
