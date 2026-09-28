# Audit — CH1_NETWORK_SLIDES.md and CH1_SUPPLEMENT.md against AI_TRAINING.pdf

**Auditor role only.** No file other than this report was modified.

**Materials, as read:**

- `REVIEWD/AI_TRAINING.pdf` — 17 pages, PowerPoint export, `pdfinfo` 2304×1296 pt.
  Text extracted page-by-page with `pdftotext -layout`; pages 8–16 additionally rendered
  at 100 dpi and read visually, because the slide-11/12/13 box labels and their
  colour-matched connectors do not survive text extraction as a layout.
- `REVIEWD/CH1_NETWORK_SLIDES.md` — 389 lines.
- `REVIEWD/CH1_SUPPLEMENT.md` — 405 lines.

**Corroborating files opened** (to adjudicate cross-references the two markdown files
make): `REVIEWD/MATLAB_EXAMPLES/LLM_LAB_HANDOUT.md`,
`REVIEWD/MATLAB_EXAMPLES/PEER_REVIEW_2026-08-27.md`, `llm_lab.m` (extracted from
`LLM_Lab_MATLAB.zip`), `ai-training/references.md`, `REFERENCES.md`. The MATLAB lab
itself was **not** reviewed — only the specific line numbers and section names the
supplement cites.

**Independent numerical verification performed** (Python, double precision):
slide 19's three-temperature table and cumulative sums; §S5's 3-token attention example;
the GELU range claim. All correct — see §D, "Checks that passed".

---

# A. Coverage matrix

## A.0 Method and the box census

Slide 10 carries **no labelled boxes** — it is four bullet questions plus the API and
MCP definitions. The labelled boxes are on slides 11, 12 and 13, and each slide has two
columns: a **functional** column (bold, connected by a coloured line to a brain region)
and a **component** column (italic, on the right, naming an LLM part). The two columns
are paired one-to-one by connector colour.

Census taken from the 100 dpi renders:

| slide | functional boxes | component boxes |
|---|---|---|
| 11 | Response Structuring; Avoiding Harm; Reward Signaling; Processing Media; Predictive Modeling; Processing Input; Value-based Decision Making (7) | Refusal Direction; Reward Model (RM); RLHF / RLVR; Multimodal Encoders; Curated Training / SFT; Unsupervised Training; Tokenizer (7) |
| 12 | Resource Allocation; Chain-of-thought; Action Sampling; Peripheral Control; Threat Interception; Behavioral Conditioning (6) | Token Balance; Sandbox Scratchpad; T-Decoder; Model; APIs / MCPs; Tokenizer; Guardrails; System Prompt (8) |
| 13 | Multi-step Thinking; Output Generation; Task Delegation; Peripheral Control; Context Retrieval; Behavioral Conditioning (6) | Response; Agent Harness; Sandbox Scratchpad; T-Decoder; Model; APIs / MCPs; Effort Level; Session Context; System Prompt (9) |

**Distinct boxes on slides 12–13: 22** (10 functional + 12 component). **Distinct across
11–13: 36.** These counts matter for finding A-1 and B-5/B-6/B-7 below.

The slide-11 colour pairing, read off the render (author should confirm against the
source PPTX): Processing Input↔Tokenizer (dark teal); Predictive Modeling↔Unsupervised
Training (pink); Processing Media↔Multimodal Encoders (blue); Response
Structuring↔Curated Training / SFT (orange); Reward Signaling↔RLHF / RLVR (purple);
Avoiding Harm↔Refusal Direction (salmon); Value-based Decision Making↔Reward Model (RM)
(green). Slide 12: Resource Allocation↔Token Balance (orange);
Chain-of-thought↔Sandbox Scratchpad (teal); Action Sampling↔T-Decoder (green);
Peripheral Control↔APIs/MCPs (brown); Threat Interception↔Guardrails (violet);
Behavioral Conditioning↔System Prompt (magenta). Slide 13: Multi-step Thinking↔Effort
Level (olive); Output Generation↔Response (pink); Task Delegation↔Agent Harness (blue);
Peripheral Control↔APIs/MCPs (brown); Context Retrieval↔Session Context (orange);
Behavioral Conditioning↔System Prompt (magenta).

## A.1 Slide-11 boxes

| box | column | defined where | treatment | verdict |
|---|---|---|---|---|
| Refusal Direction | component | §S9 | mechanism: ablation $\mathbf{h}\leftarrow\mathbf{h}-\hat{\mathbf{r}}\hat{\mathbf{r}}^{\top}\mathbf{h}$, Arditi et al. 2024 | COVERED |
| Reward Model (RM) | component | §S9 | mechanism: Bradley–Terry likelihood, plus the "does not ship" point that explains the slide's geometry | COVERED |
| RLHF / RLVR | component | §S9 | mechanism: KL-regularised objective; RLVR = programmatic verifier in place of $r_\phi$ | COVERED |
| Multimodal Encoders | component | §S10 | mechanism: patch → linear projection → positional encoding → encoder blocks | COVERED |
| Curated Training / SFT | component | §S9 | mechanism: §S8 loss on $\mathcal{D}_{\text{SFT}}$; names the slide-11 label explicitly | COVERED |
| Unsupervised Training | component | §S8 | full training mathematics | COVERED (but see B-9 / A-4: never reconciled with slide 2's "self-supervision") |
| Tokenizer | component | §S3 | mechanism: BPE merge procedure | PARTIAL — the definition is complete, but the *name* BPE arrives with no bridge (B-10) |
| Predictive Modeling | functional | §S8 header names it | mechanism by pairing | COVERED |
| Processing Input | functional | nowhere | name never used in either file | MISSING |
| Processing Media | functional | nowhere | name never used | MISSING |
| Response Structuring | functional | nowhere | name never used | MISSING |
| Reward Signaling | functional | nowhere | name never used | MISSING |
| Avoiding Harm | functional | nowhere | name never used | MISSING |
| Value-based Decision Making | functional | nowhere | name never used | MISSING |

The six MISSING items are all slide-11 functional labels. Their paired components are
each fully covered, so the *content* exists; what is absent is any statement that the
pairing is the point. §S12 does this job for slides 12–13 and names six functional
labels there (Peripheral Control, Resource Allocation, Chain-of-thought, Multi-step
Thinking, Task Delegation, Output Generation) — so the omission is an inconsistency in
the ledger's own scope, not a decision. Fix E-24.

## A.2 Slide-12 and slide-13 boxes

| box | column | defined where | treatment | verdict |
|---|---|---|---|---|
| T-Decoder | component | slide 17 + §S5/§S5a/§S6 | full: attention, mask, multi-head, residual, LayerNorm, FFN, worked numbers | COVERED |
| Action Sampling | functional | slide 19 + slide 20 step 6 + §S7 | full: four policies, PRNG draw, worked example | COVERED |
| Tokenizer | component | §S3 | see A.1 | PARTIAL (B-10) |
| Model | component | slide 6 + §S12 | slide 6's definition, now populated | COVERED |
| Response | component | slide 20 + §S12 | steps 6–7 repeated to `<eos>` | COVERED |
| Agent Harness | component | slide 20 step 7 + §S12 | the decoding loop as ordinary code | COVERED |
| System Prompt | component | §S12 | mechanism at ledger depth: "instructions prepended to $\mathbf{x}_{1:k}$; conditioning, not code" | COVERED |
| Session Context | component | §S12 | "the running transcript inside the slide-5 context window" | COVERED |
| APIs / MCPs | component | slide 10 + §S12 | mechanism: model emits a structured call as tokens, harness executes, result returns as tokens | COVERED |
| Token Balance | component | §S12 | "budget arithmetic on token counts (slide 9)" | COVERED |
| Sandbox Scratchpad | component | §S12 | "workspace whose contents re-enter as tokens" — mechanism, one line | COVERED (ledger depth) |
| Guardrails | component | §S12 | "external filters and rules" — a *category*, not a mechanism; nothing says what runs, on what, when | PARTIAL |
| Effort Level | component | §S12 | "caps the thinking-token budget before sampling resumes" — the term *thinking token* is used and never defined anywhere | PARTIAL |
| Resource Allocation | functional | §S12 (parenthetical on the Token Balance row) | mechanism by pairing | COVERED |
| Chain-of-thought | functional | §S12 | "the model's own output fed back as context" — a real mechanism | COVERED |
| Multi-step Thinking | functional | §S12 | same row | COVERED |
| Task Delegation | functional | §S12 | "loops that spawn further model calls" | COVERED |
| Output Generation | functional | §S12 | same row | COVERED |
| Peripheral Control | functional | §S12 (parenthetical on the APIs/MCPs row) | mechanism by pairing | COVERED |
| Context Retrieval | functional | §S12 | "fetched text enters as context tokens" — placement given, retrieval mechanism not | PARTIAL |
| **Threat Interception** | functional | **nowhere** | name absent from both files; §S12 claims to list every slide-12/13 box | **MISSING** |
| **Behavioral Conditioning** | functional | **nowhere** | name absent from both files; appears on slides 12 *and* 13 | **MISSING** |

## A.3 Coverage summary

- COVERED: 22 of 36 boxes.
- PARTIAL: 4 (Tokenizer, Guardrails, Effort Level, Context Retrieval).
- MISSING: 8 (six slide-11 functional labels, plus Threat Interception and Behavioral
  Conditioning).

## A.4 Technical terms the deck *uses*, slides 1–13

Ranked with the unresolved items first.

| term, and where the deck says it | where the new content pays it | verdict |
|---|---|---|
| **slide 2: "trained via **self-supervision**"** (the only occurrence of the word on the deck — grep count 1) | nowhere; §S8 and slides 7/11 say "Unsupervised Training" (grep count 2) throughout | **MISSING** — two names for one stage, never reconciled, and the field's name for next-token pre-training is the one slide 2 already uses |
| **§S12: "thinking-token budget"** | nowhere | **MISSING** — term used, never defined |
| slide 2: "Non-linear ML models … function fitting through **non-linear activation**" | slide 14 defines $\varphi$; the ledger closes "activation function" but never quotes slide 2 or slide 6 | PARTIAL |
| slide 6: "**non-linear transformations**" (Network definition) | as above | PARTIAL |
| slide 7: "**Human Alignment**" (the deck's name for stage two) | §S9, retitled "Post-training: aligning the distribution"; §S9 says only "Slide 7 gave the two-stage story" | PARTIAL — silent rename |
| slides 5 and 7: "**static weights**" / "**Static Weights**" (grep: "frozen" = 0 on the deck) | slide 19's speaker note calls the model "frozen" (slide 7) | PARTIAL — silent rename (B-9) |
| slide 5: "**Training (Empirical Risk Minimization–ERM)**" | §S8 gives $\mathcal{L}(\theta)$ as the empirical mean of the log loss — which *is* ERM — but never names the connection | PARTIAL |
| slide 5: "Inference … to evaluate $P(\mathbf{x}_{k+1:j}\mid\mathbf{x}_{1:k})$" (a *sequence* distribution) | slides 18–19 use the single-token $P(\mathbf{x}_{k+1}=v\mid\cdot)$; slide 20's loop is the reconciliation but never says so | PARTIAL |
| slide 6: "**Parameters**: Also called weights." | slide 15 counts $|\theta|=\sum_\ell d_\ell(d_{\ell-1}+1)$ — "every weight plus every bias" | PARTIAL — slide 6 equates parameters with weights; slide 15 silently widens the set |
| slide 8: "**Corpus Vocabulary**" (the only "Vocabulary" on the deck) | never reconciled with $V$/$\mathcal{V}$; the two mean different things | PARTIAL — and it is the root of B-1 |
| slide 8: "'r' isn't a word, but it is a **raw byte** (i.e., 81)" | §S3 step 1 ("Initialize $V$ with the 256 byte values") is exactly the mechanism, but the link is never drawn | PARTIAL — a free win |
| slide 5: "Limited by **VRAM** in runtime" | §S5's KV-cache note ("the reason long contexts consume memory as well as compute") is the mechanism; never linked | PARTIAL |
| slide 10: "consolidates these learned behaviors into a **unified parameter space**" | §S9's SFT/RLHF updates to $\theta$ are the mechanism; never linked | PARTIAL |
| slide 10, Q1/Q3/Q4 ("How do they acquire them?", "'personality' and 'morality'", "how to **structure** its response") | answered in substance by §S8 and §S9, but only Q2 is explicitly closed (§S10: "which is the answer to slide 10's question") | PARTIAL ×3 |
| slide 5: "**backpropagation**" | §S8 — full derivation, correctly pointed from the coverage table | COVERED (deferred, pointed) |
| slide 5: "**Stochastic Gradient Descent (SGD)**" | §S8, which quotes the anchor: "the term slide 5 committed to" | COVERED |
| slide 5: "empirical **loss function**" | §S8 + Case Study 1 slide | COVERED |
| slide 5: "**Prompt** (Conditioning Sequence), $\mathbf{x}_{1:k}$" | slides 16, 18, 20 | COVERED |
| slide 5: "**Context Window** … $O(k_{\max}^2)$" | slide 17's cost closure + §S5's count | COVERED |
| slide 6: "**Token**" | slides 8–9 (existing) | COVERED |
| slide 6: "**Network**: The layered architecture performing weighted sums…" | slide 15, explicitly closed | COVERED |
| slide 6: "**Network multiplies against token vectors**" | slide 16, explicitly closed, exact quote | COVERED |
| slide 6: "**Output: Probability distribution per Token**" | slide 18, explicitly closed, exact quote | COVERED |
| slide 9: "**Token ID** → Internal Bookkeeping" | slide 16, explicitly closed | COVERED |
| slide 9: "**Token Count** → Costs \$ and time" | §S12's Token Balance row | COVERED |
| slides 12–13: "**T-Decoder**" (an abbreviation the deck never expands) | slide 17's title expands it | COVERED |
| slide 10: **API**, **MCP** | defined on slide 10; placed by §S12 | COVERED |
| slide 2: "function approximation" / "function fitting" | slide 15's universal-approximation statement + §S2 | COVERED |
| slides 4–5: Corpus, Reliability, Knowledge Cutoff | outside the NETWORK & OUTPUT remit | not applicable |

---

# B. Backward-anchor audit

Every backward reference, every Opens/Closes claim, and every "slide N" reference was
checked against the extracted page text. **22 are BROKEN.** They are listed high
severity first. Everything not listed here was checked and is ANCHORED; the ANCHORED
set is given in B.2 so the clean verdicts are on the record too.

## B.1 BROKEN — adjudicated

### B-21 (highest severity: mathematically wrong, not merely a mis-reference)
**Where:** `CH1_NETWORK_SLIDES.md` line 244–245, slide 18.
**Claim:** "*(Hint: many models reuse $E^{\top}$ here — one lookup table, both
directions.)*"
**Against its own slide:** the same slide writes $\mathbf{z} = W_U\,\mathbf{h}_k^{(N)} +
\mathbf{b}_U$ with $\mathbf{z}\in\mathbb{R}^{|V|}$ — a **column** convention, so
$W_U\in\mathbb{R}^{|V|\times d_{\text{model}}}$. Slide 16 line 138–139 sets
$E\in\mathbb{R}^{|V|\times d_{\text{model}}}$ and $\mathbf{e}_v=\text{row }v\text{ of }E$.
Weight tying means $z_v=\mathbf{e}_v\cdot\mathbf{h}$, i.e. $(W_U)_{v,:}=E_{v,:}$, i.e.
$W_U = E$ — **not** $E^{\top}$, whose shape is $d_{\text{model}}\times|V|$ and does not
conform. $E^{\top}$ is correct only in the row-vector form $\mathbf{z}=\mathbf{h}E^{\top}$,
which is not the form printed on the slide.
**Verdict:** BROKEN. Fix E-2.

### B-1
**Where:** line 193–194, slide 17.
**Claim:** "*(Hint: the prime on $V'$ keeps the value matrix distinct from the vocabulary
$V$ of slides 5–16.)*"
**Against the deck:** slide 5 contains no vocabulary symbol at all — its symbols are
$\mathbf{x}_{1:k}$, $P(\mathbf{x}_{k+1:j}|\mathbf{x}_{1:k})$, $\mathbf{x}_{1:k_{max}}$,
$O(k_{max}^2)$. Grep over the whole deck: "vocabulary" = 0 hits; "Vocabulary" = 1 hit,
and that one is slide 8's "**Corpus Vocabulary**", a different concept. The deck's only
vocabulary symbol is the script $\mathcal{V}$ in the Case Study 1 softmax denominator,
$\sum_{j\in\mathcal{V}}e^{z_j}$.
**Consequence:** the prime on $V'$ is being justified by a collision with a symbol the
deck does not use. Adopting the deck's $\mathcal{V}$ removes the collision and the prime
together.
**Verdict:** BROKEN. Fix E-6.

### B-5, B-6, B-7, B-8 — the "every box" family
Four separate overclaims of the same fact.

- **B-5** — line 316, slide 20 **Message**: "Every box from slides 12–13 now has a place
  in the chain." Slide 20's pipeline names five: *Tokenizer* (step 1), *T-Decoder*
  (step 3), *Action Sampling* (step 6), *Agent Harness* (step 7), *Token Balance* (❖
  bullet). **Five of 22.** BROKEN.
- **B-6** — line 26, file preamble: "it resolves every remaining box on slides 12–13."
  Same count. BROKEN.
- **B-7** — `CH1_SUPPLEMENT.md` line 326, §S12: "Every box from slides 12–13, sorted by
  where it actually lives." The table has 15 rows covering 20 of the 22 boxes.
  **Threat Interception** and **Behavioral Conditioning** have no row. BROKEN.
- **B-8** — `CH1_SUPPLEMENT.md` line 4–5: "every component named on slides 11–13 of the
  main deck receives its mathematical definition." Two omissions as above; and Guardrails,
  Effort Level, Sandbox Scratchpad and Context Retrieval receive a one-line ledger entry,
  which is not a mathematical definition. BROKEN on both counts.

Note the honest sentence already in slide 20's own body, line 344–345: "everything else
on slides 12–13 is **software arranged around those four steps**." That is a *category*
resolution and it is correct. The Message and the preamble promise a per-box resolution
the body does not attempt. Fix E-3.

### B-16
**Where:** `CH1_SUPPLEMENT.md` line 366, §S13 table, **left** column ("present in the
lab, identical to production"): "autoregressive decoding loop, `<eos>` semantics".
**Against the shipped code:** `llm_lab.m` line 386–390 is
```matlab
for k = 1:ND
    P = fwd(encode(pad_ctx(S,KMAX,Vi), NV), Ws,Bs,DEPTH,L);
    Psteps(k,:) = P;
    [~, nx] = max(P);  toks(k) = nx;  S = [S, nx];
end
```
— a fixed token count with no `<eos>` test.
**Against the project's own peer review:** `PEER_REVIEW_2026-08-27.md` line 93 —
"`<eos>` trained-but-ignored"; line 65 — "**Major — four handout experiments have no
shipped code:** the `<eos>`-honouring…".
**Against the sibling file:** slide 20's speaker note (line 355–356) states it correctly:
"The demo's decoder generates a fixed number of tokens and ignores `<eos>`."
**Verdict:** BROKEN — and it is the one defect here that would put a false statement in
front of the class while the correct statement sits in the speaker note of the same
section. Fix E-4.

### B-10 — the nominated suspect, adjudicated
**Where:** `CH1_SUPPLEMENT.md` line 65, §S3: "Byte-pair encoding (BPE; Sennrich et al.,
2016) builds it:".
**Against the deck:** grep over all 17 pages — "byte-pair" = **0**, "BPE" = **0**. Slides
8–9 name the artefact only: the footnote on both pages reads "*Based on OpenAI's
tokenizer (GPT-4o-o200k_base). Different models → Different tokenizer.*" The slides show
phenomena — "stirrups → **stir** + **r** +**ups**?", "Occurrence frequency in the corpus
is **too low**", "'r' isn't a word, but it is a **raw byte** (i.e., 81)", the
`Reinforcment` → 17855, 1938, 66, 508 shatter — and never name a procedure.
**Verdict:** BROKEN as flagged. The supplement introduces an algorithm name as if
already known. §S3 line 72 does say "Consequences already shown on slides 8–9, now with
a mechanism", but that sentence comes *after* the name and points backward from it; the
name still lands cold. The bridge must precede the name. Fix E-5, which also draws the
free link from §S3 step 1 (256 byte values) to slide 8's raw-byte bullet.

**One thing I did not verify:** whether `o200k_base` is specifically a BPE tokenizer.
That is a claim about a third-party artefact and I did not search for it. The proposed
bridging sentence in E-5 is written so that it does **not** depend on that claim; if the
author wants to add it, it needs a source first.

### B-17 — citation-status contradiction between the two files
**Where:** `CH1_NETWORK_SLIDES.md` lines 387–389: "Cybenko 1989 and Hornik 1991 —
verification pass **pending**; see the Supplement's references block before the deck
ships." Versus `CH1_SUPPLEMENT.md` lines 377–383: "**Verified by web search 2026-08-27**
(bibliographic record confirmed — title, authors, venue, identifier; logged in the
project's `REFERENCES.md`)" listing both Cybenko and Hornik.
**Against `REFERENCES.md`:** the file contains a Cybenko line (two, in fact — Springer
and Semantic Scholar) dated 2026-08-27 21:50. It contains **no Hornik line at all.**
**Verdict:** BROKEN in both directions — the two files disagree, and the supplement's
"logged in the project's `REFERENCES.md`" is false for Hornik. Under the project's own
data-integrity rule this is the finding to fix first among the citation items. Fix E-12.

### B-18
**Where:** line 116, slide 15 speaker note: "Citations: Cybenko (1989), **Hornik et al.**
(1991)".
**Against the supplement's own references block** (line 382–383): "Hornik, K., 1991,
*Approximation capabilities of multilayer feedforward networks*, Neural Networks 4(2),
251–257" — **single author**. The slide's own bullet (line 105) gets it right: "(Cybenko,
1989; Hornik, 1991)".
**Verdict:** BROKEN. Fix E-12.

### B-22
**Where:** `CH1_SUPPLEMENT.md` line 318 (§S11) "(Shazeer et al., 2017; Fedus et al.,
2022)" and line 402–403, which lists "Fedus et al. 2022 (MoE)" as **verification
pending**.
**Against `ai-training/references.md` line 78:** "Fedus, W., Zoph, B. & Shazeer, N.,
**2021**, *Switch Transformers: Scaling to Trillion Parameter Models with Simple and
Efficient Sparsity*, arXiv:2101.03961; version of record JMLR 23(120):1–39, 2022 —
**[V]**. **Two errors corrected:** the title was abbreviated, and no year was recorded.
Also **only three authors** — the previous 'et al.' implied a longer list."
**Verdict:** BROKEN — the status is stale (it is verified), the primary year is 2021, and
the project file explicitly records that "et al." is wrong for this three-author paper.
Fix E-12.

### B-2
**Where:** line 227–228, slide 18 **Closes**: "Softmax itself appeared on slide 16's
case-study preview".
**Against the deck:** grep — "softmax" = **0**, "Softmax" = **0** across all 17 pages.
What appears on the Case Study 1 slide is the *quotient*
$P(\mathbf{x}_{k+1}=\boldsymbol{v}\mid\mathbf{x}_{1:k};\theta)=e^{z_v}/\sum_{j\in\mathcal{V}}e^{z_j}$,
unnamed.
**Verdict:** BROKEN as worded. The formula appeared; the name did not. The distinction
matters because slide 18's whole Closes claim is about which slide owns the *name*.
Fix E-7.

### B-3 and B-4 — slide-number collision on insertion
**B-3:** line 227, "slide 16's case-study preview". **B-4:** line 381, coverage table,
"Supp §S8 (uses slide-16-case-study loss)".
**The problem:** in the deck as it stands, slide 16 *is* "Case Study 1: Setting up a
LLM". But this file's own opening lines (3–5) insert seven slides at 14–20, so the case
study renumbers to 21 — and the new **slide 16 is "Neural Network: Embeddings"**. Both
references become wrong at the moment the change they describe is applied. The file
itself notes "PowerPoint renumbers it automatically" (line 5), which is exactly why a
by-number reference to the case study cannot survive.
**Verdict:** BROKEN-on-insert. Refer to it by title. Fix E-7.

### B-9
**Where:** line 306, slide 19 speaker note: "why regenerating an answer changes it while
the model is \"frozen\" (slide 7)".
**Against the deck:** grep — "frozen" = **0**. Slide 7's box reads "**Static Weights**";
slide 5's Inference definition reads "evaluated across the **static weights**
(parameters)". The quotation marks imply the deck's word is being quoted; it is not.
**Verdict:** BROKEN — silent rename. Fix E-8.

### B-11
**Where:** `CH1_SUPPLEMENT.md` line 358, §S13: "one-hot inputs standing in for
**§S16-style** embeddings ($E=I$)".
**Against the supplement:** the supplement runs §S1–§S13. **There is no §S16.** The
intended referent is slide 16.
**Verdict:** BROKEN. Fix E-10.

### B-12 and B-13 — derivatives pointed to the wrong section
**B-12:** line 74, slide 14 speaker note: "Do not discuss derivatives here … and
**Supplement §S8** derives them." **B-13:** line 368, coverage table: "activation
function; sigmoid, tanh, ReLU, GELU | 14 (**derivatives: Supp §S8**)".
**Against the supplement:** the derivatives $\sigma'$, $\tanh'$, $\mathrm{ReLU}'$,
$\mathrm{GELU}'$ are in **§S1**, lines 28–37. §S1 itself says so: "Derivatives (used by
§S8's backpropagation…)". §S8 *uses* them; §S1 *gives* them.
**Verdict:** BROKEN ×2 — a reader sent to §S8 for a derivative table will not find one.
Fix E-9.

### B-14
**Where:** line 110–111, slide 15: "*(Hint: the live demo measures depth against width
**at a fixed parameter budget** — hold this question for the lab.)*"
**Against the handout:** `LLM_LAB_HANDOUT.md` lines 166–174, §E4, is a free grid —
widths 8 / 32 / 128 crossed with depths 0 / 1 / 2 / 3. Parameter count varies across
every cell; nothing is held fixed. The handout's own reading of the grid is the opposite
one: "The **depth-0 column is identical across all widths** — correctly, since width
does nothing without a hidden layer."
**Verdict:** BROKEN. Fix E-11.

### B-15
**Where:** `CH1_SUPPLEMENT.md` line 58, §S2: "the lab's E4 grid (**scale fails to rescue
a bad tokenization**) is the demonstration."
**Against the handout:** the E4 heading (line 166) is "### E4 — scale does not rescue a
bad **representation**". The tokenisation claim belongs to a different experiment — the
handout's defensible-claims list (line 365) reads "'Tokenisation determines what is
representable.' — **E1**, 0% vs 100%".
**Verdict:** BROKEN — the parenthetical attributes E1's claim to E4. Fix E-11.

### B-19
**Where:** line 158–160, slide 16 speaker note: "the special case $E=I$, **stated in the
lab handout**."
**Against the handout:** the handout's phrasing (line 19) is "fixed context window,
**one-hot tokens**, feed-forward layers, softmax over a vocabulary". The equation $E=I$
appears nowhere in it.
**Verdict:** BROKEN (overclaim). Low severity — the physics is identical, the attribution
is not. Fix E-27.

### B-20
**Where:** line 214, slide 17 speaker note: "that absence is what the **handout's
defensibility section** leans on."
**Against the handout:** there is no section by that name. The heading (line 361) is
"## Claims you can defend, and two you cannot", and the load-bearing line under it is
"'This is the training objective and output mechanism of an LLM at 10⁻⁷ scale, **without
attention**.'"
**Verdict:** BROKEN (renamed section title). Lowest severity of the set — the substance
is right. Fix E-26.

## B.2 ANCHORED — checked and correct

Recorded so the clean verdicts are on the record. Each was matched against the extracted
page text.

| claim | anchor text on the earlier slide | verdict |
|---|---|---|
| line 3–4: replaces "current 14 *Decision-making Math*, 15 *Introducing Variance*" | slide 14 title "Neural Network: Decision-making Math"; slide 15 title "Neural Network: Introducing Variance" | ANCHORED |
| line 4: "The existing *Case Study 1: Setting up a LLM* follows slide 20 unchanged" | slide 16 title "Case Study 1: Setting up a LLM" | ANCHORED |
| line 42, slide 14: framing line "mirroring slide 14's current opener" | slide 14: "Let's define a program that calculates \"what would come next\", using the model's weights and the prompt." | ANCHORED |
| line 49, slide 14: "Set in training (slide 7)" | slide 7: "The list of parameters is calculated and set during model training, in two stages" | ANCHORED |
| line 86, slide 15: closes "multi-layered" from slide 2 | slide 2: "**Multi-layered** neural network trained via self-supervision and human alignment…" | ANCHORED |
| line 86–87, slide 15: closes "layered architecture" from slide 6 | slide 6: "❑ Network: The **layered architecture** performing weighted sums and non-linear transformations." | ANCHORED |
| line 102–103, slide 15: "the \"7B\" / \"32B\" in a model's name" | slide 6: "Represents model size (e.g., **Qwen 32B**)." | ANCHORED |
| line 128–129, slide 16: closes "the loose end from slide 9 — what the Token ID is *for*" | slide 9: "❑ Token ID → Internal Bookkeeping." | ANCHORED |
| line 129–130, slide 16: closes slide 6's "Network multiplies against token vectors" | slide 6: "2. **Network multiplies against token vectors**" — exact | ANCHORED |
| line 135–136, slide 16: "The tokenizer (slides 8–9) delivers integers" | slides 8–9 footnote "OpenAI's **tokenizer**"; IDs 117657 / 17855, 1938, 66, 508 | ANCHORED |
| line 168–169, slide 17: "the context-window cost of slide 5" | slide 5: "Compute grows non-linearly $O(k_{max}^2)$" | ANCHORED |
| line 195–197, slide 17: causal mask is "the structural form of slide 5's Inference definition" | slide 5: "Inference (**Autoregressive Decoding**)… evaluated across the static weights… (Hint: **Word by word prediction**.)" | ANCHORED (the gloss "past, never the future" is the new content's, not a quote — acceptable) |
| line 226–227, slide 18: closes slide 6's "Output: probability distribution per Token" | slide 6: "3. **Output: Probability distribution per Token**" — exact | ANCHORED |
| line 225, slide 18: closes "what a logit is (the old placeholder's demand)" | slide 14 placeholder: "What a logit is, randomess,seeds, temperature" | ANCHORED |
| line 266–268, slide 19: closes "the entire *Introducing Variance* placeholder" | slide 15 placeholder: "Equations 1-2 of HOW the output is produced (temperature/seeds) slides and then A WORKED example…" | ANCHORED — and slide 19 delivers all four demands |
| line 343–344, slide 20: "the token budget (slide 12: *Token Balance*)" | slide 12 component box "Token Balance" | ANCHORED |
| line 319–320, slide 20: "the T-Decoder / Action Sampling / Tokenizer boxes of slides 12–13" | all three boxes present (Action Sampling on 12 only; Tokenizer on 11 and 12; T-Decoder on 12 and 13) | ANCHORED |
| line 357–359, slide 20 speaker note: peer-review caution on eos numbers | `PEER_REVIEW_2026-08-27.md` line 65 and line 93 | ANCHORED |
| §S3 line 72: "Consequences already shown on slides 8–9" | slide 8's frequency / shatter / typo bullets | ANCHORED |
| §S5 line 143: "$O(k_{\max}^2)$ asserted on slide 5 and closed on slide 17" | slide 5 as above | ANCHORED |
| §S6 line 180: "the mechanism behind slide 17's \"lets $N\sim10^2$ blocks train\"" | slide 17 line 204: "Together they let $N\sim 10^2$ blocks train." — exact | ANCHORED |
| §S8 line 215: "The loss is the case-study slide's" | Case Study 1: $\mathcal{L}(\theta)=-\frac1n\sum_{i=1}^{n}\log P(\mathbf{x}^{(i)}_{k+1}\mid\mathbf{x}^{(i)}_{1:k};\theta)$ — exact | ANCHORED |
| §S8 line 256–257: "*Stochastic* gradient descent — the term slide 5 committed to" | slide 5: "updated via backpropagation and **Stochastic Gradient Descent (SGD)**" | ANCHORED |
| §S8 line 266: "The \"random numbers before training\" note on the case-study slide" | Case Study 1: "The weights and bias are **random numbers before training**." — exact | ANCHORED |
| §S9 line 272: "Slide 7 gave the two-stage story" | slide 7: "set during model training, **in two stages**" | ANCHORED (but see A.4 — "Human Alignment" is never quoted) |
| §S9 line 276–277: "this is what \"Curated Training\" on slide 11 names" | slide 11 box "Curated Training / SFT" | ANCHORED |
| §S9 line 282: "slide 11 draws it outside the layer stack for exactly this reason" | render confirms the Reward Model (RM) box sits outside the cylinder stack, top right | ANCHORED |
| §S9 line 297: "Slide 11's top layer names this" | render confirms Refusal Direction connects to the topmost disc of the stack | ANCHORED |
| §S10 line 302: "slide 10's \"text, images, and sound at the same time\"" | slide 10: "How are they able to understand **text, images, and sound at the same time**?" — exact | ANCHORED |
| §S12: "Session Context … inside the slide-5 context window" | slide 5: "Context Window(Sequence Length)" | ANCHORED |
| §S12: "Token Balance … budget arithmetic on token counts (slide 9)" | slide 9: "**Token Count → Costs \$ and time.**" | ANCHORED |
| §S12: "Model … slide 6's definition, now fully populated" | slide 6: "Model is the package that consists of the parameters and a program that processes said parameters." | ANCHORED |
| §S1 line 39–40, §S8 line 233 and 247–253: `llm_lab.m` line citations | verified against the extracted source: line 154 `H = tanh(H*Ws{i} + Bs{i});`, line 165 `(1 - acts{i}.^2)`, line 162 `G = P;  G(idx) = G(idx) - 1;`, lines 163–167 the backward loop verbatim | ANCHORED — all five correct |
| slide 18 speaker note: "panel 3 … the $P(v\mid\text{ctx})$ bar chart" | handout line 95: "bottom left | P(v \| ctx) over the vocabulary" — subplot index 3 in a 2×2 is bottom-left | ANCHORED (but see E-28: the handout names panels by position, not number) |

---

# C. Internal flow of slides 14–20

Ranked by severity.

### C-1 — Forward dependency: softmax is consumed on slide 17 and defined on slide 18
**Evidence.** Slide 17, line 187: $\text{Attention}(Q,K,V')=\mathrm{softmax}\!\left(QK^{\top}/\sqrt{d_k}\right)V'$.
Slide 18, line 227: "this slide is its *definition* slot".
**Against the file's own rule,** line 24: "Each slide consumes only objects defined on
earlier slides."
No earlier definition exists to fall back on: the deck never uses the word (grep = 0),
and the Case Study 1 slide — which prints the quotient — comes *after* slide 20.
**Severity: highest C-class defect.** It is the one place where the section's stated
architecture is violated by its own content. Fix E-1.

### C-2 — Undefined symbols on slide 17: $H$ and $d_k$
Slide 17 writes $Q=HW_Q,\;K=HW_K,\;V'=HW_V$ and $\sqrt{d_k}$. Neither $H$ nor $d_k$ is
defined on the slide. Both are defined in §S5 ("Stack the $k$ input vectors as rows of
$H\in\mathbb{R}^{k\times d_{\text{model}}}$"; "head dimension $d_k$"). The speaker note
points to §S5 for "the 3-token, $d_k=2$ worked example", which incidentally exposes $d_k$
but never defines it; $H$ is not pointed to at all. Fix E-15.

### C-3 — Row/column convention switches silently between slides 15/18 and slide 17
Slide 15: $\mathbf{h}^{(\ell)}=\varphi(W^{(\ell)}\mathbf{h}^{(\ell-1)}+\mathbf{b}^{(\ell)})$
with "Row $r$ of $W^{(\ell)}$ holds the weights of neuron $r$" — column vectors,
$W\in\mathbb{R}^{d_\ell\times d_{\ell-1}}$.
Slide 17: $Q=HW_Q$ — row vectors, $W_Q\in\mathbb{R}^{d_{\text{model}}\times d_k}$.
Slide 18: $\mathbf{z}=W_U\mathbf{h}_k^{(N)}+\mathbf{b}_U$ — back to column.
§S8 flags its own switch ("row-vector convention, matching MATLAB") but never says it is
the transpose of slide 15's; §S5 and slide 17 do not flag it at all.
For a MATLAB-literate audience this is precisely the transposition trap that produces
silently wrong code. It is also what makes B-21 easy to commit. Fix E-18.

### C-4 — Slide 19's Message and framing line are contradicted by its own hint
Message (line 261): "The network is a **deterministic function**".
Framing line (line 273): "*Same weights, same prompt → **bit-identical logits, every
time**.*"
Hint (line 287–288): "*even then $T=0$ across a provider's hardware is **not
bit-reproducible**: parallel floating-point addition is non-associative.*"
The hint denies the framing line's exact word. Both statements are individually true —
they differ in whether the arithmetic is held fixed — but the slide never says so, and
as written the slide carries two messages. Fix E-17.

### C-5 — Slide 20's Message is not delivered by slide 20's body
Message (line 316): "Every box from slides 12–13 now has a place in the chain."
Body: five boxes appear. This is B-5 restated as a Message-delivery failure, which is the
form the author's own convention (line 9–10: "the one sentence the slide exists to
convey") makes it a defect. Fix E-3.

### C-6 — $k$ is overloaded on slide 19
The same slide carries $P_T(\cdot\mid\mathbf{x}_{1:k};\theta)$ and
$\mathbf{x}_{k+1}\sim\mathrm{Categorical}(\cdot)$ — $k$ = context length, the deck's
meaning since slide 5 — and, six lines later, "**Top-k**: keep the $k$ highest logits".
§S7 line 197–198 repeats the collision. Fix E-16.

### C-7 — §S7 reopens slide 19 at deck depth
Slide 19 **Closes** (line 266–270): "the entire *Introducing Variance* placeholder …
After this slide, output variance is never re-derived; later chapters may only reference
it."
§S7 then restates greedy, temperature, top-k and top-p as four bullets at approximately
the same depth. Its genuine additions are: greedy as the $T\to0$ limit, top-p's
adaptivity argument, the name "inverse-CDF sampling", and the deployment note. Roughly
half the section is restatement of a closed topic. Under the file's own rule this is a
reopen. Fix E-30.

### C-8 — The Opens/Closes ledger is systematically unbalanced
The convention (lines 11–12): "a topic under *Opens* is a debt **a named later slide must
pay**." Tracing every Opens entry:

| opened | on | closed by a named slide? |
|---|---|---|
| weights, bias | 14 | no |
| hidden state $\mathbf{h}$, width, depth, $|\theta|$ | 15 | no ("Debt forward" names slide 17, but only for *where layers sit*) |
| embedding matrix $E$, $d_{\text{model}}$ | 16 | no |
| positional encoding | 16 | **yes** — closed on the same slide at deck level, §S4 pointed |
| attention, Q/K/V, causal mask, $N$ | 17 | no |
| multi-head, residual, layer norm | 17 | **yes** — "closed at headline depth", §S5–S6 pointed |
| logit $\mathbf{z}$, $W_U$ | 18 | no |
| temperature $T$ | 18 | **yes** — slide 19 |
| sampling policies, seed | 19 | **yes** — same slide |
| decoding loop, `<eos>` | 20 | implicitly, not listed |

Ten opened items have no named payer. Slide 20 is the natural closer and its Closes list
should enumerate them. Fix E-29.

### C-9 — Slide 17's title rests on a distinction only the supplement makes
The title is "The Transformer **Decoder** (T-Decoder)" and the Closes list claims "the
*Transformer* name". Why it is a *decoder* — the causal mask, and the contrast with an
encoder — is §S5a, and slide 17 never points there. The coverage table does (line 380),
but a coverage table is not slide content. Fix E-25.

### C-10 — The Case Study 1 logit equation is never reconciled with slide 18's
Case Study 1 prints $\mathbf{z}=\mathbf{W}\cdot\mathbf{x}_{1:k}+\mathbf{b}$ — a single
affine map from context to logits. Slide 18 prints
$\mathbf{z}=W_U\mathbf{h}_k^{(N)}+\mathbf{b}_U$. Same symbol, different map, no sentence
connecting them, and the case study is the very next slide after 20. The placeholder
slide 14 carried the same equation and is being deleted, so after the change the case
study is its only surviving instance and the collision is newly exposed. Fix E-21.

### C-11 — Slide 5's Inference is a sequence distribution; slides 18–19 give a token distribution
Slide 5 twice writes $P(\mathbf{x}_{k+1:j}\mid\mathbf{x}_{1:k})$. The new content uses
$P(\mathbf{x}_{k+1}=v\mid\mathbf{x}_{1:k};\theta)$ throughout and the file's notation
preamble (line 17) calls this "the deck's" — it is the *Case Study 1* slide's, not slide
5's. Slide 20's loop is exactly the bridge between the two forms, and slide 20 line 346
comes within one clause of saying so. Fix E-22.

### C-12 — Two small omissions in the 17→18 hand-off
- The **final LayerNorm** before unembedding exists only in §S6 line 184 ("embed → $N$
  blocks → **final LN** → unembed"). Slide 17's block diagram ends at "output" and slide
  18's framing line says "After N blocks, position $k$ holds a vector $\mathbf{h}_k$" —
  no final LN in either. Fix E-38.
- **Multi-head output projection $W_O$**: slide 17 line 198–199 says heads "concatenate"
  and stops. §S5 line 130 adds "outputs concatenate and reproject:
  $\mathrm{MHA}(H)=[\text{head}_1\cdots\text{head}_h]W_O$", and §S6's block equation then
  uses $\mathrm{MHA}$. Without $W_O$ the dimensions on slide 17 do not return to
  $d_{\text{model}}$. Fix E-39.

### C-13 — $h$ (head count, slide 17) collides with $\mathbf{h}$ (hidden state, slide 15)
Distinguished only by boldface, on a projected slide, three bullets apart. Lower severity
than C-6 because the field uses $h$ for head count as standard; noted so the author can
decide. No fix proposed — flagging is enough.

### C-14 — Style-rule observations
- **Alias convention inverted.** The deck's convention, from slide 5, is *informal
  headword* ^(*formal technical alias*): "Training(Empirical Risk Minimization-ERM)",
  "Knowledge Cutoff (Temporal Distribution Boundary)", "Prompt(Conditioning Sequence)",
  "Context Window(Sequence Length)", "Inference (Autoregressive Decoding)". All five put
  the *more* technical term in the alias slot. The new slides invert this for at least
  ten items — Weight^(Learned Sensitivity), Bias^(Learned Offset), Activation
  Function^(Non-linearity), Hidden State^(Layer Output), Width^(Units per Layer),
  Depth^(Number of Layers), Embedding^(Learned Token Vector), Positional Encoding^(Order
  Information), Logit^(Unnormalized Score), Temperature^(Contrast Dial), Residual +
  LayerNorm^(Training Stabilizers) — putting a plain-English gloss in a slot the deck
  reserves for the formal name. Four items do follow the deck: Top-p^(Nucleus),
  Seed^(PRNG State), `<eos>`^(End-of-Sequence), Causal Mask^(Autoregressive Constraint).
  "Contrast Dial" and "Learned Sensitivity" are coinages, which the style rules forbid.
  Fix E-33 — presented as a recommendation, since the author may have chosen the
  inversion deliberately for a non-ML audience.
- **Two aphorisms carrying no technical content.** §S10 line 309: "several **front
  doors**". §S12 line 328: "the brain diagrams' **cash value**". Fix E-31.
- **Ungrammatical reading rule.** §S12 line 349–350: "only what training set lives in
  $\theta$." Fix E-32.
- **Define-by-subtraction:** checked all seven slides and §S1–§S13. **None found.** The
  closest constructions — slide 20's "`<eos>` is an ordinary vocabulary token the model
  learned to emit. The *loop* reads it and halts" and §S12's Guardrails row — both give
  the positive definition first. Clean.
- **Coinages other than the two aliases above:** none found. "T-Decoder", "Token
  Balance", "Effort Level" are the deck's own labels, correctly quoted as such rather
  than adopted as field terms.

### C-15 — Messages delivered
Checked one by one. Slides 14, 16, 17, 18 deliver their Message in the body. Slide 15's
Message asserts width and depth are "**two independent** size knobs" and the body never
shows the independence — a small gap, not a failure. Slide 19 delivers but carries a
second, contradicting message (C-4). Slide 20 does not deliver (C-5).

---

# D. Technical completeness rating

Ambition, as stated by the brief and by the supplement's own audience assumption
(line 9–10: "comfortable with linear algebra, least squares, and MATLAB; no ML
background"): after reading, the reader understands how an LLM is set up and produces
output, neuron through sampled token, with every named component defined.

Deferral-with-a-pointer is **not** counted as a deduction, per the brief.

## D.1 The seven slides alone — **6.5 / 10**

The chain is complete: neuron → layer → embedding → decoder block → logits → sampling →
loop, with no link absent. Deductions are for defects inside that chain, not gaps in it.

| # | deduction | weight |
|---|---|---|
| 1 | Softmax consumed on slide 17, defined on slide 18 — no earlier definition exists anywhere in the deck (C-1) | −0.75 |
| 2 | $W_U=E^{\top}$ weight-tying hint is wrong under the slide's own convention (B-21) | −0.50 |
| 3 | $H$ used and never defined or pointed to on slide 17 (C-2) | −0.40 |
| 4 | Row/column convention switches between slides 15/18 and 17, unflagged (C-3) | −0.25 |
| 5 | Slide 19's framing line contradicted by its own hint (C-4) | −0.25 |
| 6 | Slide 20's Message overclaims — 5 of 22 boxes placed (C-5) | −0.30 |
| 7 | $k$ overloaded on slide 19 (C-6) | −0.25 |
| 8 | Slide 15's E4 description is wrong against the handout (B-14) | −0.20 |
| 9 | Encoder/decoder distinction underpinning slide 17's title is neither given nor pointed (C-9) | −0.15 |
| 10 | Final LayerNorm and $W_O$ dropped from the 17→18 hand-off without a pointer (C-12) | −0.15 |
| 11 | Slide 2's "non-linear activation" and slide 6's "non-linear transformations" never explicitly closed (A.4) | −0.15 |
| 12 | Opens/Closes ledger leaves ten items with no named payer (C-8) | −0.15 |
| 13 | Case Study 1's $\mathbf{z}$ unreconciled with slide 18's $\mathbf{z}$ (C-10) | −0.15 |
| | **total** | **−3.50** |

## D.2 Slides plus supplement §S1–§S10 — **7.5 / 10**

The supplement repairs deductions 3, 9 and 10 outright (§S5 defines $H$ and $d_k$; §S5a
gives the encoder/decoder distinction; §S6 supplies the final LN and $W_O$) and softens 4
(§S8 flags its own convention). Coverage across the two documents is close to complete:
of the 36 boxes, 22 are COVERED and only 8 MISSING, and the eight are labels rather than
mechanisms. What holds the combined rating to 7.5 is that the supplement introduces its
own consistency defects at roughly the rate it removes the slides' — every one of them a
one-line fix.

| # | deduction | weight |
|---|---|---|
| 1 | Softmax ordering unrepaired — the supplement does not change the slide sequence (C-1) | −0.40 |
| 2 | $W_U=E^{\top}$ error uncorrected in §S5/§S6 (B-21) | −0.40 |
| 3 | "Every box" claimed four times, false each time; Threat Interception and Behavioral Conditioning have no home (B-5/6/7/8) | −0.30 |
| 4 | §S13 states the lab honours `<eos>`; the shipped loop does not, and slide 20's speaker note says so (B-16) | −0.25 |
| 5 | Citation integrity: Hornik claimed logged in `REFERENCES.md` and is not; the two files disagree on Cybenko/Hornik status; "Hornik et al." for a single-author paper; Fedus status and year stale against `ai-training/references.md` (B-17, B-18, B-22) | −0.25 |
| 6 | Broken internal pointers: phantom "§S16"; activation derivatives sent to §S8 twice when they are in §S1 (B-11, B-12, B-13) | −0.20 |
| 7 | BPE named with no bridge from slides 8–9 (B-10) | −0.20 |
| 8 | Deck terms silently renamed and never reconciled: "self-supervision"→"Unsupervised Training"; "Human Alignment"→"post-training"; "static weights"→"frozen" (A.4, B-9) | −0.20 |
| 9 | Lab mis-citations: E4 is "a bad representation", not "a bad tokenization"; E4 is not run at a fixed parameter budget (B-14, B-15) | −0.15 |
| 10 | $k$ overloaded on slide 19 and in §S7 (C-6) | −0.15 |
| | **total** | **−2.50** |

Deliberate deferrals verified as **properly pointed, and therefore not deducted**:
activation derivatives and the affine-collapse proof (§S1, pointed from slide 14 line 58,
though §S8-vs-§S1 is misnamed — counted under deduction 6, not as a missing concept);
universal approximation in full (§S2, pointed line 105–108); positional-encoding
equations (§S4, pointed line 130–131 and 160); attention worked numbers, $\sqrt{d_k}$,
KV cache (§S5, pointed line 175–176 and 211–213); block equations (§S6, pointed line
205); training mathematics and Case Study 1 (§S8, pointed by the coverage table and by
slide 20's transition line).

## D.3 Checks that passed — recorded so the clean verdicts stand

State the check, then the outcome:

- **Slide 19's temperature table must reproduce softmax at $T=0.5,1,2$ on
  $\mathbf{z}=(2.0,1.0,0.2,-1.0)$ to three decimals.** Computed:
  $T{=}0.5\to(0.858268, 0.116154, 0.023451, 0.002127)$;
  $T{=}1\to(0.631726, 0.232399, 0.104424, 0.031452)$;
  $T{=}2\to(0.447181, 0.271229, 0.181810, 0.099780)$. Every printed value correct.
- **Cumulative sums at $T=1$ must match $(0.632, 0.864, 0.969, 1.000)$.** Computed
  $(0.631726, 0.864125, 0.968548, 1.000000)$. Correct. Both worked draws follow:
  $u=0.22<0.632\Rightarrow v_1$; $0.632<0.71<0.864\Rightarrow v_2$.
- **§S5's attention example must reproduce $\boldsymbol{\alpha}$ and the output.**
  Computed raw scores $(1,1,2)$, scaled $(0.7071,0.7071,1.4142)$,
  $\boldsymbol{\alpha}=(0.2483,0.2483,0.5035)$, output $(0.7517,0.7517)$. Exact match.
- **GELU range $\approx(-0.17,\infty)$.** Minimising $u\Phi(u)$ by ternary search:
  argmin $u=-0.751792$, min $=-0.169971$. Correct.
- **§S6's "roughly two thirds of a transformer's parameters live in the FFN blocks."**
  Per block, attention $=4d^2$ ($W_Q,W_K,W_V,W_O$), FFN $=2d\cdot d_{\text{ff}}=8d^2$ at
  $d_{\text{ff}}=4d$; share $=8/12=2/3$. Correct.
- **§S8's logit gradient, backprop identities, and initialisation variances.**
  $\nabla_{\mathbf{z}}\mathcal{L}=P-\mathbf{e}_y$; $\partial\mathcal{L}/\partial W=H^\top G$;
  $2/d_{\text{in}}$ (He) and $2/(d_{\text{in}}+d_{\text{out}})$ (Glorot). All correct as
  stated.
- **§S9's Bradley–Terry loss, the KL-regularised RLHF objective, and the refusal
  projection $\mathbf{h}-\hat{\mathbf{r}}\hat{\mathbf{r}}^{\top}\mathbf{h}$.** All correct.
- **§S5's $\mathrm{Var}(\mathbf{q}\cdot\mathbf{k})=d_k$ and the $O(k^2d_k)$ / $O(k)$
  KV-cache costs.** Correct.
- **§S15's… (no such section) — and every `llm_lab.m` line number cited.** Lines 154,
  162, 165 and the 163–167 block all match the extracted source verbatim.

No fabricated numbers were found anywhere in the two files.

---

# E. Fix list

Paste-ready. Grouped by file, ordered by severity within each group. Every replacement is
written in the register of the file it lands in and obeys the binding style rules.

**Note on the style rules:** I searched `ai-training/CLAUDE.md`, `ai-training/DECISIONS.md`
and `START_HERE.md` for a written statement of the deck's style rules (one message per
slide, no reopening, no definition by subtraction, no contentless analogies, standard
terms only, direct declarative sentences) and **found none**. The rules as applied here
come from the audit brief, which I have treated as authoritative.

## E.1 `CH1_NETWORK_SLIDES.md`

### E-1 — Softmax forward dependency (C-1)
**At line 173–176,** slide 17's ledger, append a debt line after "…worked numeric
example.":

> **Debt backward paid on 18:** softmax is used in the attention equation above as a
> black box — row-wise, it converts a row of scores into weights that are positive and
> sum to one. Slide 18 defines it.

**And at line 190–194,** append one clause to the Self-Attention bullet, after "…takes
the weighted average of what they carry.":

> The row-wise softmax is what makes those weights a weighted average: positive, summing
> to one (defined on slide 18).

Rationale for not reordering: steps must stay in pipeline order, and giving softmax a
second definition on 17 would violate the one-message rule and reopen it on 18.

### E-2 and E-34 — the weight-tying error and the missing term (B-21)
**Replace line 244–245:**

```
❑ **Unembedding**^(Output Projection), $W_U$: the matrix mapping the final hidden
state onto the vocabulary. *(Hint: many models reuse $E^{\top}$ here — one lookup
table, both directions.)*
```

**with:**

```
❑ **Unembedding**^(Output Projection), $W_U$: the matrix mapping the final hidden
state onto the vocabulary. *(Hint: many models set $W_U = E$ — **weight tying**. Row
$v$ of $E$ embeds token $v$ on the way in and scores it on the way out: one lookup
table, read in both directions.)*
```

This also pays the coverage table's line-376 promise of "weight tying", which the current
body never names.

### E-3 — the "every box" overclaims (B-5, B-6, C-5)
**Replace line 316** (slide 20 Message, third sentence):

```
Every box from slides 12–13 now has a place in the chain.
```

**with:**

```
The five boxes that sit on the generation path — Tokenizer, T-Decoder, Action
Sampling, Token Balance, Agent Harness — land on numbered steps; Supplement §S12
places the remaining seventeen.
```

**Replace line 25–26** (file preamble):

```
Slide 20 is the "everything clicks" slide the old placeholder asked for, and it
resolves every remaining box on slides 12–13.
```

**with:**

```
Slide 20 is the "everything clicks" slide the old placeholder asked for: it puts the
generation-path boxes of slides 12–13 on numbered steps, and Supplement §S12 places
the harness and context boxes that do not sit on that path.
```

### E-17 — slide 19's self-contradiction (C-4)
**Replace line 273–274:**

```
Framing line: *Same weights, same prompt → bit-identical logits, every time. The
variety you observe between regenerations is injected on purpose, here:*
```

**with:**

```
Framing line: *Same weights, same prompt, same arithmetic → the same logits. The
variety you observe between regenerations is injected on purpose, here:*
```

The hint's floating-point caveat then refines the framing line instead of denying it.

### E-15 and E-18 — undefined $H$, $d_k$, and the convention switch (C-2, C-3)
**Insert after the attention equation, line 188:**

```
Rows of $H$ are the $k$ hidden states entering this block — the transpose of slide
15's column form, which is how attention is written throughout. $d_k$ is the head's
width.
```

### E-16 — the $k$ collision (C-6)
**Replace line 282:**

```
&nbsp;&nbsp;❑ **Top-k**: keep the $k$ highest logits, renormalize, draw.
```

**with:**

```
&nbsp;&nbsp;❑ **Top-k**: keep the highest $k$ logits, renormalize, draw. *(The $k$ in
this policy's name is the candidate count, not the context length $k$ of
$\mathbf{x}_{1:k}$.)*
```

### E-7 — slide-number collisions and the softmax-name claim (B-2, B-3, B-4)
**Replace line 226–228** (slide 18 Closes):

```
**Closes:** "what a logit is" (the old placeholder's demand); slide 6's "Output:
probability distribution per Token" (this is the mechanism). Softmax itself appeared on
slide 16's case-study preview — this slide is its *definition* slot; the case study
now *uses* it.
```

**with:**

```
**Closes:** "what a logit is" (the old placeholder's demand); slide 6's "Output:
probability distribution per Token" (this is the mechanism). The **Case Study 1** slide
already prints this quotient without naming it; this slide is the name's definition
slot, and the case study becomes a use of it.
```

**Replace line 381** (coverage table cell):

```
| training math: cross-entropy gradient, backprop, SGD/minibatch | Supp §S8 (uses slide-16-case-study loss) |
```

**with:**

```
| training math: cross-entropy gradient, backprop, SGD/minibatch | Supp §S8 (uses the Case Study 1 loss) |
```

Rule for the author: never refer to the case study by number in these files — the
insertion renumbers it.

### E-6 — the vocabulary symbol (B-1)
**Recommended fix (removes the prime entirely).** Adopt the deck's own $\mathcal{V}$.

- **Line 16–17,** notation preamble: change `vocabulary $V$` to `vocabulary
  $\mathcal{V}$ (the deck's symbol, from the Case Study 1 slide)`, and delete `$V'$` from
  the "New symbols" sentence.
- **Slide 17:** change `V'` to `V` at lines 187, 188, 193; change $\mathbb{R}$-shapes
  accordingly.
- **Replace line 193–194:**

```
*(Hint: the prime on $V'$ keeps the value matrix distinct from the
vocabulary $V$ of slides 5–16.)*
```

**with:**

```
*(Hint: $V$ here is the attention value matrix. The vocabulary keeps the deck's script
symbol $\mathcal{V}$.)*
```

- **Slides 16 and 18:** `|V|` → `|\mathcal{V}|`; `\sum_{j\in V}` → `\sum_{j\in\mathcal{V}}`.
- **`CH1_SUPPLEMENT.md` line 11:** `$V$ (vocabulary), $V'$ (attention value matrix)` →
  `$\mathcal{V}$ (vocabulary), $V$ (attention value matrix)`; then §S3 and §S5
  accordingly.

**Minimal alternative,** if the author will not touch the symbol: keep $V'$ and replace
the hint with `*(Hint: the prime on $V'$ keeps the value matrix distinct from the
vocabulary $\mathcal{V}$ of the Case Study 1 slide.)*` — which at least stops citing a
slide that has no vocabulary symbol.

### E-9 — the derivative pointer (B-12, B-13)
**Replace line 73–74** (slide 14 speaker note, last sentence):

```
Do not discuss derivatives
here — they matter only for training, and Supplement §S8 derives them.
```

**with:**

```
Do not discuss derivatives
here — they matter only for training. Supplement §S1 lists them; §S8 uses them.
```

**Replace line 368** (coverage table cell): `14 (derivatives: Supp §S8)` → `14
(derivatives: Supp §S1)`.

### E-8 — "frozen" (B-9)
**Replace line 305–307,** slide 19 speaker note:

```
If someone asks why regenerating an
answer changes it while the model is "frozen" (slide 7), this slide is the complete
answer.
```

**with:**

```
If someone asks why regenerating an
answer changes it while the weights are static (slide 7: *Static Weights*), this slide
is the complete answer.
```

### E-11 — the E4 description (B-14)
**Replace line 110–111:**

```
*(Hint: the live demo measures depth against width at a fixed parameter
budget — hold this question for the lab.)*
```

**with:**

```
*(Hint: the live demo runs a width × depth grid — 8/32/128 against 0/1/2/3 — and
reports held-out accuracy in every cell. Hold this question for the lab.)*
```

### E-12 — citation integrity (B-17, B-18, B-22)
**Replace line 387–389:**

```
Citation status at time of writing: Vaswani 2017, Holtzman 2020 — verified in
`ai-training/references.md` ([V]). Cybenko 1989 and Hornik 1991 — verification pass
pending; see the Supplement's references block before the deck ships.
```

**with:**

```
Citation status at time of writing: Vaswani 2017 and Holtzman 2020 — verified in
`ai-training/references.md` ([V]). Cybenko 1989 — bibliographic record confirmed
2026-08-27 and logged in the project's `REFERENCES.md`. Hornik 1991 — the record is
stated in the Supplement's references block but **is not logged in `REFERENCES.md`**;
log the source line or downgrade the citation before the deck ships.
```

**Replace line 116** (slide 15 speaker note): `Cybenko (1989), Hornik et al. (1991)` →
`Cybenko (1989), Hornik (1991) — single author`.

### E-21 — the Case Study 1 logit collision (C-10)
**Replace line 349–350:**

```
*(Transition line, bottom):* Every step above used weights already set. **Case Study
1** builds the machine that sets them.
```

**with:**

```
*(Transition line, bottom):* Every step above used weights already set. **Case Study
1** builds the machine that sets them, on the shortest network that still has a logit
vector: one affine map, $\mathbf{z}=\mathbf{W}\cdot\mathbf{x}_{1:k}+\mathbf{b}$, in
place of steps 2–4.
```

### E-22 — the slide-5 Inference bridge (C-11)
**Replace line 346–347:**

```
❖ Steps 1–7 are **Inference** exactly as defined on slide 5 — now with every symbol
accounted for.
```

**with:**

```
❖ Steps 1–7 are **Inference** exactly as defined on slide 5. One pass of steps 2–6
gives $P(\mathbf{x}_{k+1}\mid\mathbf{x}_{1:k})$; step 7's loop is what turns that into
slide 5's $P(\mathbf{x}_{k+1:j}\mid\mathbf{x}_{1:k})$.
```

### E-19 — close slide 2 and slide 6's activation phrasing (A.4)
**Replace line 36–38:**

```
**Opens:** weights, bias, activation function. **Closes:** activation function (the
catalogue below is the complete treatment at deck level; derivatives and the
approximation proof live in Supplement §S1–S2). Nothing before this slide is reopened.
```

**with:**

```
**Opens:** weights, bias, activation function. **Closes:** activation function —
including slide 2's "non-linear activation" and slide 6's "non-linear transformations",
which name $\varphi$ without giving it. The catalogue below is the complete treatment
at deck level; the derivatives are Supplement §S1 and the approximation theorem is §S2.
Nothing before this slide is reopened.
```

### E-20 — parameters versus weights (A.4)
**Append to the parameter-count bullet, line 103,** after the existing hint:

```
*(Slide 6 called the parameters "weights"; the count includes the biases, which are
parameters on the same footing.)*
```

### E-25 — point slide 17 at §S5a (C-9)
**Append to line 176,** end of slide 17's Closes paragraph:

```
Why the stack is a *decoder* and not an encoder is Supplement §S5a.
```

### E-29 — balance the ledger (C-8)
**Append to line 320,** slide 20's Closes paragraph:

```
Also closed here, open until now: weights and bias (14); hidden state, width, depth and
$|\theta|$ (15); $E$ and $d_{\text{model}}$ (16); attention, Q/K/V, causal mask and $N$
(17); logit and $W_U$ (18).
```

### E-38 — the final LayerNorm (C-12)
**Replace line 232–233:**

```
Framing line: *After N blocks, position $k$ holds a vector $\mathbf{h}_k$ summarizing
the whole prompt. One last matrix converts it into scores over the vocabulary.*
```

**with:**

```
Framing line: *After N blocks and one final layer normalization, position $k$ holds a
vector $\mathbf{h}_k^{(N)}$ summarizing the whole prompt. One last matrix converts it
into scores over the vocabulary.*
```

### E-39 — the output projection (C-12)
**Replace line 198–199:**

```
❑ **Multi-Head**: $h$ attention maps run in parallel with separate learned $W_Q, W_K,
W_V$, then concatenate. Each head is free to learn a different relation.
```

**with:**

```
❑ **Multi-Head**: $h$ attention maps run in parallel with separate learned $W_Q, W_K,
W_V$, then concatenate and reproject through $W_O$ back to $d_{\text{model}}$
(Supplement §S5). Each head is free to learn a different relation.
```

### E-26, E-27, E-28 — three speaker-note attributions (B-20, B-19, ANCHORED-but-loose)
- **Line 214:** `the handout's defensibility section` → `the handout's "Claims you can
  defend, and two you cannot"`.
- **Line 159–160:** `the special case $E=I$, stated in the lab handout` → `the special
  case $E=I$; the handout states it as "one-hot tokens"`.
- **Line 254–255:** `panel 3 of \`llm_lab.m\`` → `the bottom-left panel of \`llm_lab.m\`'s
  live figure` — matching the handout's own panel table, which names panels by position.

### E-33 — the alias convention (C-14), recommendation
The deck reserves the superscript slot for the *formal* term. Where the headword is
already the field's formal name, the alias adds nothing and two of them are coinages.
Recommended: **drop** the alias on Weight, Bias, Activation Function, Hidden State,
Width, Depth, Embedding, Positional Encoding, Logit, Softmax, Temperature, Self-Attention,
Unembedding, Residual + LayerNorm. **Keep** Top-p^(Nucleus), Seed^(PRNG State),
`<eos>`^(End-of-Sequence), Causal Mask^(Autoregressive Constraint) — in each of those the
alias is the formal term the headword lacks. If the author prefers to keep plain-English
glosses for a non-ML audience, that is defensible, but "Contrast Dial" and "Learned
Sensitivity" should still go: they are invented names, and the rules forbid coinages.

## E.2 `CH1_SUPPLEMENT.md`

### E-5 — the BPE bridge (B-10), highest priority in this file
**Replace line 64–65:**

```
A tokenizer is a deterministic map $\mathcal{T}:\text{text}\to V^{*}$, built before
network training and frozen. Byte-pair encoding (BPE; Sennrich et al., 2016) builds it:
```

**with:**

```
A tokenizer is a deterministic map $\mathcal{T}:\text{text}\to \mathcal{V}^{*}$, built
before network training and then held fixed. Slides 8–9 showed what one produces —
`stirrups` splitting into `stir + r + ups`, a misspelling shattering into four IDs —
without naming the procedure that produced it. That procedure is **byte-pair encoding**
(BPE; Sennrich et al., 2016):
```

**And append to step 1, line 66,** so slide 8's raw-byte bullet is closed too:

```
1. Initialize $\mathcal{V}$ with the 256 byte values. This is why slide 8's stray `r`
   resolves to a raw byte: every byte is already a token, so no string is
   unrepresentable.
```

Before adding any claim that `o200k_base` is specifically a BPE tokenizer, verify it
against a source — it is not established by anything in this project's files.

### E-3 (cont.) — the two missing §S12 rows and the scope claim (B-7, B-8)
**Insert two rows into the §S12 table,** after the Guardrails row (line 342):

```
| Threat Interception | harness | the functional label paired with *Guardrails*: prompt and sampled response are screened by code outside $\theta$ |
| Behavioral Conditioning | context tokens | the functional label paired with *System Prompt*: standing instructions that condition every turn |
```

**Replace line 4–5:**

```
Companion deck to Chapter 1, same template, sections numbered §S1–§S13. Purpose: every
component named on slides 11–13 of the main deck receives its mathematical definition,
```

**with:**

```
Companion deck to Chapter 1, same template, sections numbered §S1–§S13. Purpose: every
component box on slides 11–13 of the main deck receives either its mathematical
definition or a row in the §S12 ledger,
```

### E-4 — the §S13 `<eos>` row (B-16)
**Replace line 366:**

```
| autoregressive decoding loop, `<eos>` semantics | scale ($\sim4\times10^{3}$ vs $\sim10^{11}$ parameters) |
```

**with:**

```
| autoregressive decoding loop; `<eos>` present in $\mathcal{V}$ and in the training targets | halting on `<eos>` — the loop runs a fixed token count (`llm_lab.m`, `for k = 1:ND`) — and scale ($\sim4\times10^{3}$ vs $\sim10^{11}$ parameters) |
```

**And replace line 367's left cell:** `frozen weights at inference` → `static weights at
inference`, matching the deck's term.

### E-10 — the phantom §S16 (B-11)
**Replace line 357–358:**

```
`llm_lab.m` implements §S8 completely (loss, residual, backprop, update — the code
lines are quoted in §S8) and §S7's greedy row, on the §S1 neuron with tanh, with
one-hot inputs standing in for §S16-style embeddings ($E=I$) and *no* §S5 attention.
```

**with:**

```
`llm_lab.m` implements §S8's core loop (loss, residual, backprop, plain full-batch
update — the code lines are quoted in §S8) and §S7's greedy row, on the §S1 neuron with
tanh, with one-hot inputs standing in for the slide-16 embedding step (the special case
$E=I$) and *no* §S5 attention.
```

"completely" → "'s core loop" is deliberate: §S8 also carries Adam, dropout and He/Glorot
initialisation, none of which the lab uses.

### E-11 (cont.) — the E4 attribution (B-15)
**Replace line 58:**

```
   the lab's E4 grid (scale fails to rescue a bad tokenization) is the demonstration.
```

**with:**

```
   the lab's E4 grid (scale does not rescue a bad representation) is the demonstration.
```

### E-12 (cont.) — the references block (B-17, B-22)
**Insert into the verified list** (after the Sennrich entry, line 386):

```
- Fedus, W., Zoph, B. & Shazeer, N., 2021, *Switch Transformers: Scaling to Trillion
  Parameter Models with Simple and Efficient Sparsity*, arXiv:2101.03961; version of
  record JMLR 23(120):1–39, 2022 — verified in `ai-training/references.md` ([V]);
  three authors, not "et al.".
```

**Replace line 318** (§S11): `(Shazeer et al., 2017; Fedus et al., 2022)` → `(Shazeer et
al., 2017; Fedus et al., 2021)`.

**Replace line 400–404** (the pending list), removing Fedus and flagging Hornik:

```
Still cited from memory, **verification pending** before the deck ships (all are
one-line mentions with no equation resting on them): Kingma & Ba 2015 (Adam);
Srivastava et al. 2014 (dropout); Dosovitskiy et al. 2021 (ViT); Shazeer et al. 2017
(MoE); the RLVR term's origin (used in the Tülu 3 line of work) has no single canonical
citation confirmed here. Separately: the Hornik 1991 entry above states a confirmed
record but **has no line in the project's `REFERENCES.md`** — add one or downgrade the
entry.
```

### E-13 — reconcile "self-supervision" with "Unsupervised Training" (A.4)
**Insert after the §S8 header, before line 215:**

```
Slide 2 calls this stage *self-supervision*; slides 7 and 11 call it *Unsupervised
Training*. They name the same objective. Self-supervised is the more exact of the two:
nothing is hand-annotated, but every token is the label for the context preceding it,
so the supervision comes from the data's own order.
```

### E-14 — reconcile "Human Alignment" (A.4)
**Replace line 272:**

```
Slide 7 gave the two-stage story; these are the stage-two objectives.
```

**with:**

```
Slide 7 named stage two *Human Alignment*; these are its objectives.
```

### E-23 — close slide 10's remaining questions (A.4)
**Append to §S9, after the Refusal direction bullet (line 298):**

```
Two of slide 10's questions are answered on this page. A model's 'personality' is the
SFT corpus — format, register and refusal style are demonstrated, then imitated. Its
'morality' is the preference objective: what the reward model or the DPO loss scores
higher is what the deployed distribution shifts toward. Together with §S8 they also
answer the first: capabilities that are not harness features are acquired by gradient
descent on next-token prediction, then reshaped by these objectives.
```

### E-24 — the slide-11 pairing ledger (A.1, six MISSING items)
**Insert into §S12, immediately after the existing table (line 346), before the reading
rule:**

```
Slide 11 pairs the same way, one stage per row: the left box names the function, the
right box names the component that performs it.

| function (slide 11) | component (slide 11) | defined in |
|---|---|---|
| Processing Input | Tokenizer | §S3 |
| Predictive Modeling | Unsupervised Training | §S8 |
| Processing Media | Multimodal Encoders | §S10 |
| Response Structuring | Curated Training / SFT | §S9 |
| Reward Signaling | RLHF / RLVR | §S9 |
| Value-based Decision Making | Reward Model (RM) | §S9 |
| Avoiding Harm | Refusal Direction | §S9 |
```

The pairings above were read off the slide's colour-matched connectors in the PDF
render; confirm them against the source PPTX before shipping.

### E-30 — trim §S7's reopen (C-7)
**Replace lines 194–196:**

```
- **Greedy**: $\mathbf{x}_{k+1}=\arg\max_v z_v$. The $T\to0$ limit. Deterministic;
  degenerately repetitive on open-ended text (Holtzman et al., 2020).
- **Temperature**: $\mathbf{x}_{k+1}\sim P_T$, $P_T(v)\propto e^{z_v/T}$.
```

**with:**

```
- **Greedy and temperature sampling** are slide 19's definitions unchanged. The one
  thing to add: greedy is the $T\to0$ limit of temperature sampling, not a separate
  rule.
```

Keep the top-k, top-p, draw and deployment bullets — those carry content slide 19 does
not.

### E-36 and E-37 — two ledger rows that state a category, not a mechanism (A.2)
**Replace the Guardrails row, line 342:**

```
| Guardrails | harness (+ §S9 for trained-in refusal) | external filters and rules; distinct from refusal behavior learned into $\theta$ |
```

**with:**

```
| Guardrails | harness (+ §S9 for trained-in refusal) | a classifier or rule pass over the prompt and over the sampled response, run by the harness before the response is returned; distinct from refusal behavior learned into $\theta$ |
```

**Replace the Effort Level row, line 344:**

```
| Effort Level | harness configuration | caps the thinking-token budget before sampling resumes |
```

**with:**

```
| Effort Level | harness configuration | caps how many tokens the model may generate into the *Multi-step Thinking* stream before the harness ends that stream and returns the response |
```

This also removes the undefined term "thinking token".

### E-31 — two contentless aphorisms (C-14)
**Replace line 308–309** (§S10, last sentence):

```
One architecture, one context
stream, several front doors — which is the answer to slide 10's question.
```

**with:**

```
One decoder, one context
stream, one encoder per modality — which is the answer to slide 10's question.
```

**Replace line 327–328** (§S12, second sentence):

```
This table is the
"how does each part connect to the LLM" answer in one place — the brain diagrams' cash
value.
```

**with:**

```
This table is the
"how does each part connect to the LLM" answer in one place: the brain diagrams'
technical content, stated without the anatomy.
```

### E-32 — the reading rule's grammar (C-14)
**Replace line 348–350:**

```
Reading rule for the whole table: **if a capability can be changed without
retraining, it lives in the harness or the context; only what training set lives in
$\theta$.**
```

**with:**

```
Reading rule for the whole table: **a capability that can be changed without retraining
lives in the harness or the context; $\theta$ holds only what training put there.**
```

### E-18 (cont.) — flag the convention switch in the supplement's notation block (C-3)
**Append to line 13,** end of the notation paragraph:

```
Two conventions appear, and they differ only by transposition. The main deck writes
column vectors ($\mathbf{h}^{(\ell)}=\varphi(W\mathbf{h}^{(\ell-1)}+\mathbf{b})$, slide
15). §S5 and §S8 stack positions or examples as *rows* to match MATLAB ($Z=HW+\mathbf{b}$).
Read $W$ in the row form as the transpose of $W$ in the column form.
```

---

# What this audit did not do

Stated so the omissions do not read as completeness.

- **The MATLAB lab was not reviewed.** Only five line-number citations, the `<eos>`
  handling in the decode loop, and four handout section names were checked, because the
  supplement makes factual claims about them.
- **`o200k_base` was not verified to be a BPE tokenizer.** No search was run. E-5 is
  written so it does not depend on that claim.
- **Slides 1–7 were read but not audited for internal correctness** — only for the
  anchor text the new content cites. Slide 3's hydrostatics example and slide 4's
  reliability framing were not evaluated.
- **The slide-11/12/13 connector pairings were read off a 100 dpi PDF render, not the
  source PPTX.** Colour matching was unambiguous in every case, but the PPTX is the
  authority and E-24 depends on those pairings.
- **The rendered figures on slides 8 and 9 are partly empty in the PDF export** — slide
  8's "What your prompt is:" and "What the model* sees:" rows show no content, and slide
  9's cost chart has axes but no bars. I could not determine whether this is an export
  artefact or missing content, so I made no finding about it. It should be checked in
  PowerPoint.
- **Citations were checked for internal consistency against the project's own files, not
  re-verified against primary sources.** Kingma & Ba 2015, Srivastava et al. 2014,
  Dosovitskiy et al. 2021, Shazeer et al. 2017 and the RLVR origin all remain
  unverified — the supplement says so itself, and I did not change that status.
- **No claim was made about whether the seven slides fit their time slot,** or about the
  diagrams' visual design.
```
