# Chapter 1 Supplement — The Network in Full

Companion deck to Chapter 1, same template, sections numbered §S1–§S17. Purpose: every
component box on slides 11–13 of the main deck receives either its mathematical
definition or a row in the §S16 ledger, derivation where one exists, and the matching
lines of the live-demo lab (`llm_lab.m`) where the lab implements it. The main deck
stays at definition depth; everything heavier lands here. Each § is sized for one slide
(a few take two).

**Order.** The sections follow the slide-20 pipeline in signal order — tokenizer,
embedding, positions, attention, block, logits, distribution, sampling, loop — then the
theory the pipeline rests on, then how $\theta$ was set, then the parts that sit beside
the pipeline rather than inside it.

**Contract strip.** Every component section opens with the same five-row strip, before
any equation: what the component **is**, the **signal** it converts, what fails without
it, what it **enables** in the deployed product, and where it **sits**. Read the strip
first; the mathematics under it is the detail of the same statement.

Audience assumption carried over from the main deck: comfortable with linear algebra,
least squares, and MATLAB; no ML background. Notation continues the main deck exactly:
$\mathbf{x}_{1:k}$, $\theta$, $\mathcal{V}$ (vocabulary), $V$ (attention value matrix),
$\mathbf{z}$, $P(\cdot\,|\,\cdot;\theta)$, $\mathcal{L}(\theta)$, $\mathbf{h}$,
$\varphi$, $E$, $d_{\text{model}}$, $T$, $N$. Two conventions appear, and they differ
only by transposition. The main deck writes column vectors
($\mathbf{h}^{(\ell)}=\varphi(W\mathbf{h}^{(\ell-1)}+\mathbf{b})$, slide 15). §S4 and
§S12 stack positions or examples as *rows* to match MATLAB ($Z=HW+\mathbf{b}$). Read
$W$ in the row form as the transpose of $W$ in the column form.

---

## §S1 — The tokenizer (slide 11 box: *Tokenizer*; slide 12 box: *Tokenizer*)

| | |
|---|---|
| **Is** | a deterministic map from a text string to a sequence of integer IDs drawn from a fixed, finite vocabulary $\mathcal{V}$. |
| **Signal** | UTF-8 byte string, arbitrary length → $\mathbf{x}_{1:k}$, integers in $\{1,\dots,|\mathcal{V}|\}$, with $|\mathcal{V}|$ of order $10^{5}$. |
| **Needed because** | the output stage scores a finite set: §S6 emits one number per vocabulary entry and §S7 normalizes over that same set. Character strings supply no such fixed index, so with the tokenizer removed there is nothing for the network to put a distribution over. |
| **Enables** | any text at all is processable, misspellings and unseen strings included, because every byte is already a token; and it makes cost countable — slide 9's *Token Count → Costs \$ and time* is arithmetic on this output. |
| **Sits** | pipeline step 1 (slide 20); stage: applied at training and at inference; scope: one artifact per model, built before network training and then held fixed. |

Between the user's text, which it consumes as bytes, and the embedding matrix (§S2),
which expects integer row indices.

Slide 11 pairs this box with the functional label *Processing Input*: converting the
prompt into the model's own symbols is the whole of that function.

$$\mathcal{T}:\text{text}\to\mathcal{V}^{*}$$

Slides 8–9 showed what one produces — `stirrups` splitting into `stir + r + ups`, a
misspelling shattering into four IDs — without naming the procedure that produced it.
That procedure is **byte-pair encoding** (BPE; Sennrich et al., 2016):

1. Initialize $\mathcal{V}$ with the 256 byte values. This is why slide 8's stray `r`
   resolves to a raw byte: every byte is already a token, so no string is
   unrepresentable.
2. Count adjacent-pair frequencies across a reference corpus; merge the most frequent
   pair into a new token; add it to $\mathcal{V}$.
3. Repeat until $|\mathcal{V}|$ reaches the target (order $10^{5}$). The merge list *is*
   the tokenizer; encoding applies the merges greedily in learned order.

Consequences already shown on slides 8–9, now with a mechanism: frequent strings become
single tokens; rare strings shatter into pieces; a typo shatters further. $\mathcal{T}$
is trained on its own corpus, separately from $\theta$ — a token can exist in
$\mathcal{V}$ yet never occur in the network's training data, and its row in the
embedding matrix (§S2) then keeps its random initialization forever, because a row that
is never selected receives zero gradient. The lab's out-of-vocabulary experiment
reproduces this exactly (handout, "Out-of-vocabulary").

---

## §S2 — The embedding matrix

| | |
|---|---|
| **Is** | a learned lookup table with one row per vocabulary entry, converting a token ID into a real vector. |
| **Signal** | token ID $v\in\{1,\dots,|\mathcal{V}|\}$ → $\mathbf{e}_v\in\mathbb{R}^{d_{\text{model}}}$. Over a prompt: $\mathbf{x}_{1:k}$ → $H^{(0)}\in\mathbb{R}^{k\times d_{\text{model}}}$ once §S3 adds positions. |
| **Needed because** | the alternative encoding of a token ID is a one-hot vector of length $|\mathcal{V}|\sim10^{5}$, under which every pair of distinct tokens is equidistant. Nothing learned about one token transfers to any other, and each token's parameters are trained only on that token's own occurrences. |
| **Enables** | tokens used in similar contexts acquire nearby vectors, so `beam` and `girder` pool statistical evidence instead of being learned independently. |
| **Sits** | pipeline step 2 (slide 20); stage: parameters in $\theta$, set by §S12 and static at inference; scope: one matrix for the whole model, reused at the output when weights are tied (§S6). |

Between the tokenizer (§S1), which hands it integers, and the positional encoding
(§S3), which adds order information to the vectors it returns.

$$\mathbf{e}_v=\text{row }v\text{ of }E,\qquad
E\in\mathbb{R}^{|\mathcal{V}|\times d_{\text{model}}},\qquad
|\theta_E|=|\mathcal{V}|\cdot d_{\text{model}}$$

The lookup is a matrix product in disguise: $\mathbf{e}_v=\mathbf{1}_v^{\top}E$ with
$\mathbf{1}_v$ the one-hot indicator of token $v$. Two consequences follow directly.
First, the one-hot encoding is the special case $E=I$, which is what the live-demo lab
uses — the embedding step is present but frozen at the identity, and the lab therefore
demonstrates every other stage without it. Second, the gradient reaching row $v$ is
non-zero only on steps where token $v$ appears, which is the zero-gradient result of
§S1.

Geometry is learned, not designed: the training objective (§S12) rewards embeddings
that make the next token predictable, and tokens with interchangeable contexts end up
with small angles between their rows. No rule states the similarity; it is a by-product
of the loss.

---

## §S3 — Positional encoding (closing slide 16's $\mathbf{p}_i$)

| | |
|---|---|
| **Is** | a vector added to each token's embedding that encodes where in the sequence that token sits. |
| **Signal** | position index $i\in\{1,\dots,k\}$ → $\mathbf{p}_i\in\mathbb{R}^{d_{\text{model}}}$; combined, $\mathbf{h}_i^{(0)}=\mathbf{e}_{x_i}+\mathbf{p}_i$. |
| **Needed because** | attention (§S4) is permutation-invariant: permute the rows of $H$ and the output rows permute identically, with no other change. Without $\mathbf{p}_i$ the network receives "load causes deflection" and "deflection causes load" as the same input set. |
| **Enables** | word order to carry meaning — argument order, syntax, and the direction of a stated relation all become visible to the network. |
| **Sits** | pipeline step 2 (slide 20), applied with the embedding; stage: a fixed function (sinusoidal), parameters in $\theta$ (learned absolute), or a rotation applied inside attention at every block (RoPE); scope: every position, every forward pass. |

Between the embedding (§S2), which hands it order-blind vectors, and the first decoder
block (§S4), which would otherwise treat the prompt as a bag of tokens.

Three schemes in deployment history:

- **Sinusoidal** (Vaswani et al., 2017): fixed, not learned —
  $$p_{i,2m}=\sin\!\left(\frac{i}{10000^{2m/d_{\text{model}}}}\right),\qquad
  p_{i,2m+1}=\cos\!\left(\frac{i}{10000^{2m/d_{\text{model}}}}\right)$$
  Each dimension pair oscillates at its own wavelength; any position offset becomes a
  fixed linear map, which is what lets the network reason about relative order.
- **Learned absolute**: $\mathbf{p}_i$ is a trainable row of a position-embedding
  matrix (GPT-2 lineage).
- **Rotary (RoPE)** (Su et al., 2021/2023): positions enter as rotations applied to
  $\mathbf{q},\mathbf{k}$ pairs inside attention, so scores depend on relative offset
  $i-j$ directly. The common choice in current open models.

Deck-level takeaway stays as slide 16 stated it; this page exists so "how, exactly?"
has an answer with equations.

---

## §S4 — Self-attention, derived and worked (slides 12–13 box: *T-Decoder*, part 1)

| | |
|---|---|
| **Is** | a layer in which every position builds a new representation as a weighted average of the positions it is allowed to see, with the weights computed from the content of those positions. |
| **Signal** | $H\in\mathbb{R}^{k\times d_{\text{model}}}$ → $\mathbb{R}^{k\times d_{\text{model}}}$ (per head, $\mathbb{R}^{k\times d_k}$ before the $W_O$ reprojection). |
| **Needed because** | with attention removed, the influence of context is fixed by the architecture: a window of fixed length, with a separate weight block per position, exactly as in the live-demo lab. There is no content-based lookup, so a definition supplied earlier in the same prompt cannot be retrieved — the lab's absence of in-context learning is this absence. |
| **Enables** | long-range reference, and the use of definitions, examples and instructions given earlier in the session rather than only what training put in $\theta$. |
| **Sits** | pipeline step 3 (slide 20); stage: parameters in $\theta$; scope: the first sublayer of every one of the $N$ decoder blocks. |

Between a block's input vectors (§S3 for the first block, §S5's residual stream
thereafter) and the feed-forward sublayer (§S5), which expects one mixed vector per
position.

Stack the $k$ input vectors as rows of $H\in\mathbb{R}^{k\times d_{\text{model}}}$.
One attention head with head dimension $d_k$:

$$Q=HW_Q,\quad K=HW_K,\quad V=HW_V,\qquad
W_Q,W_K,W_V\in\mathbb{R}^{d_{\text{model}}\times d_k}$$

$$S=\frac{QK^{\top}}{\sqrt{d_k}}\in\mathbb{R}^{k\times k},\qquad
S^{\text{masked}}_{ij}=\begin{cases}S_{ij} & j\le i\\ -\infty & j>i\end{cases}$$

$$A=\mathrm{softmax}_{\text{rows}}\!\left(S^{\text{masked}}\right),\qquad
\text{output}=A\,V$$

Row $i$ of $A$ is a probability distribution over positions $1..i$: how much position
$i$ copies from each predecessor. The $-\infty$ mask entries zero out after softmax —
that is the causal constraint of slide 17 in matrix form.

**Why $\sqrt{d_k}$.** For $\mathbf{q},\mathbf{k}$ with independent zero-mean,
unit-variance components, $\mathrm{Var}(\mathbf{q}\cdot\mathbf{k})
=\sum_{m=1}^{d_k}\mathrm{Var}(q_m k_m)=d_k$. Raw scores therefore grow like
$\sqrt{d_k}$ in spread, pushing softmax into saturation (one weight $\approx 1$, the
rest $\approx 0$, gradients $\approx 0$). Dividing by $\sqrt{d_k}$ restores unit
variance. (Vaswani et al., 2017, §3.2.1.)

**Multi-head.** $h$ heads with separate $W_Q^{(m)},W_K^{(m)},W_V^{(m)}$, usually
$d_k=d_{\text{model}}/h$; outputs concatenate and reproject:
$\mathrm{MHA}(H)=\big[\text{head}_1\;\cdots\;\text{head}_h\big]\,W_O$. Without $W_O$ the
width does not return to $d_{\text{model}}$ and the block cannot be stacked.

**Worked example** ($k=3$, $d_{\text{model}}=d_k=2$, $W_Q=W_K=W_V=I$ for
transparency; the numbers below were recomputed in double precision and match). Inputs
$\mathbf{h}_1=(1,0)$, $\mathbf{h}_2=(0,1)$, $\mathbf{h}_3=(1,1)$. For position 3:
scores $\mathbf{q}_3\cdot\mathbf{k}_j=(1,\,1,\,2)$, scaled by $1/\sqrt{2}$:
$(0.7071,\,0.7071,\,1.4142)$; softmax gives
$\boldsymbol{\alpha}=(0.2483,\,0.2483,\,0.5035)$; output
$\sum_j\alpha_j\mathbf{v}_j=(0.7517,\,0.7517)$. Position 3 built its new
representation mostly from itself, partly from both predecessors — relevance became a
weighted average, with weights the network *learned* to produce.

**Cost.** $S$ has $k^2$ entries; per head, $O(k^2 d_k)$ multiplications. This is the
$O(k_{\max}^2)$ asserted on slide 5 and closed on slide 17, and it is why slide 5 lists
VRAM as the runtime limit: the score matrix and the cached keys and values occupy
memory that grows with context length. **KV cache:** at generation, $K,V$ rows of past
tokens are stored, so each new token costs $O(k)$ attention rather than recomputing
$O(k^2)$ — the standard inference optimization, and the reason long contexts consume
memory as well as compute.

### §S4a — Encoder, decoder, and which one an LLM is

An **encoder** block is the same construction with the mask removed — every position
attends to every other, which suits reading a complete input (classification,
retrieval, the multimodal encoders of §S14). A **decoder** block carries the causal
mask, which is what makes autoregressive generation trainable: every position may be
scored as a prediction target in the same forward pass, because no position has seen
its own answer. GPT-class LLMs are **decoder-only** stacks: the "T-Decoder" of slides
12–13 is $N$ masked blocks and nothing else. (The original transformer paired an
encoder stack with a decoder stack for translation; the LLM lineage kept the decoder.)

---

## §S5 — The block: residual, LayerNorm, feed-forward (*T-Decoder*, part 2)

| | |
|---|---|
| **Is** | the repeated unit of the decoder stack: an attention sublayer and a position-wise feed-forward sublayer, each wrapped in a residual connection and preceded by layer normalization. |
| **Signal** | $H\in\mathbb{R}^{k\times d_{\text{model}}}$ → $\mathbb{R}^{k\times d_{\text{model}}}$. The shape is preserved, which is what allows the unit to be stacked $N$ times. |
| **Needed because** | attention mixes *between* positions and computes nothing new *within* one — it returns a weighted average of vectors handed to it. Remove the feed-forward sublayer and the block loses its per-position non-linear computation and roughly two thirds of its parameters. Remove the residual connections and layer normalization and the gradient attenuates multiplicatively through $N\sim10^{2}$ blocks, so the deep stack does not train. |
| **Enables** | depth, which is where the capability of a large model lives; and the action of associations stored in $\theta$ on the mixed representation attention produces. |
| **Sits** | pipeline step 3 (slide 20), repeated $N$ times, with one final layer normalization after the last block; stage: parameters in $\theta$; scope: every decoder block. |

Between the embedded prompt (§S2–§S3), which enters the first block, and the
unembedding (§S6), which expects the last block's output at position $k$.

One block, pre-norm arrangement (the current standard):

$$\mathbf{h} \leftarrow \mathbf{h} + \mathrm{MHA}\!\left(\mathrm{LN}(\mathbf{h})\right),
\qquad
\mathbf{h} \leftarrow \mathbf{h} + \mathrm{FFN}\!\left(\mathrm{LN}(\mathbf{h})\right)$$

$$\mathrm{LN}(\mathbf{h})=\boldsymbol{\gamma}\odot\frac{\mathbf{h}-\mu}{\sqrt{\sigma^2+\epsilon}}+\boldsymbol{\beta},
\qquad \mu,\sigma^2 \text{ over the } d_{\text{model}} \text{ components (Ba et al., 2016)}$$

$$\mathrm{FFN}(\mathbf{h})=W_2\,\varphi(W_1\mathbf{h}+\mathbf{b}_1)+\mathbf{b}_2,
\qquad W_1\in\mathbb{R}^{d_{\text{ff}}\times d_{\text{model}}},\; d_{\text{ff}}\approx 4\,d_{\text{model}}$$

- The FFN is slide 15's network, width $d_{\text{ff}}$, depth 1, applied to each
  position independently; $\varphi$ is GELU in the GPT lineage. Roughly two thirds of
  a transformer's parameters live in the FFN blocks: per block, attention holds
  $4d_{\text{model}}^2$ ($W_Q,W_K,W_V,W_O$) against the FFN's
  $2d_{\text{model}}d_{\text{ff}}=8d_{\text{model}}^2$.
- **Residual connection** (He et al., 2016): the Jacobian of
  $\mathbf{h}+F(\mathbf{h})$ is $I+\partial F/\partial\mathbf{h}$ — the identity term
  gives gradients an unattenuated path through all $N$ blocks. This is the mechanism
  behind slide 17's "lets $N\sim10^2$ blocks train."
- **LayerNorm** keeps per-position activation scale fixed, so the same learning rate
  works at every depth.

Full decoder: embed (slide 16) → $N$ blocks → final LN → unembed (slide 18). That
sentence is the entire architecture.

---

## §S6 — Unembedding and logits

| | |
|---|---|
| **Is** | the linear map from the final hidden state at the predicted position to one score per vocabulary entry. |
| **Signal** | $\mathbf{h}_k^{(N)}\in\mathbb{R}^{d_{\text{model}}}$, after the final layer normalization → $\mathbf{z}\in\mathbb{R}^{|\mathcal{V}|}$. |
| **Needed because** | the stack's output is a vector of width $d_{\text{model}}$, whose components carry no per-token meaning. A distribution over the vocabulary requires one number per vocabulary entry, and no other stage changes the width. |
| **Enables** | a full-vocabulary score vector at every step — the object that softmax (§S7), the sampler (§S8) and the training loss (§S12) all consume. |
| **Sits** | pipeline step 4 (slide 20); stage: parameters in $\theta$; scope: once per forward pass, at the position being predicted. |

Between the last block's final layer normalization (§S5) and the softmax (§S7), which
needs a finite score vector to normalize.

$$\mathbf{z}=W_U\,\mathbf{h}_k^{(N)}+\mathbf{b}_U,\qquad
W_U\in\mathbb{R}^{|\mathcal{V}|\times d_{\text{model}}},\qquad
\mathbf{z}\in\mathbb{R}^{|\mathcal{V}|}$$

**Weight tying.** Many models set $W_U=E$, so that $z_v=\mathbf{e}_v\cdot
\mathbf{h}_k^{(N)}$: row $v$ of $E$ embeds token $v$ on the way in and scores it on the
way out. Under the column convention printed on slide 18 the tied matrix is $E$ itself,
not $E^{\top}$ — $E^{\top}$ has shape $d_{\text{model}}\times|\mathcal{V}|$ and does not
conform. ($E^{\top}$ is the correct form only if the slide were written with row
vectors, $\mathbf{z}=\mathbf{h}E^{\top}$.) Tying removes $|\mathcal{V}|\cdot
d_{\text{model}}$ parameters and forces the two uses of a token's vector to agree. The
bias $\mathbf{b}_U$ adds a term to each token's score that does not depend on the
context — a learned prior on token frequency — and the tied form $W_U=E$ carries none.

**Cost.** At $|\mathcal{V}|\sim10^{5}$ and $d_{\text{model}}\sim10^{4}$ this one matrix
product costs $\sim10^{9}$ multiply–adds, the same order as an entire block
($\approx 12\,d_{\text{model}}^{2}\approx1.2\times10^{9}$ from the accounting in §S5),
so the output stage carries a material share of the per-token compute budget.

---

## §S7 — Softmax and temperature

| | |
|---|---|
| **Is** | the map from a logit vector to a probability distribution over the vocabulary, with a positive scalar $T$ dividing the logits first. |
| **Signal** | $\mathbf{z}\in\mathbb{R}^{|\mathcal{V}|}$ and $T>0$ → $P_T$ with $P_T(v)>0$ and $\sum_{v\in\mathcal{V}}P_T(v)=1$. |
| **Needed because** | both consumers require a normalized distribution. The training loss is $-\log P$ of the observed token, which is a meaningless quantity unless the scores sum to one; the sampler draws $u\sim\mathcal{U}(0,1)$ against a cumulative sum, which requires the same. Raw logits satisfy neither condition. |
| **Enables** | a per-token distribution the operator can reshape without retraining — $T$ is the single operator-side control on how sharp that distribution is. |
| **Sits** | pipeline step 5 (slide 20); stage: a fixed function with no parameters, used at training ($T=1$) and at inference alike; scope: once per generated token. |

Between the logits (§S6), which are unnormalized and unbounded, and the sampler (§S8),
which draws from a distribution.

Slide 18 gives the definition and the effect of $T$. Three properties it does not
state, each of which matters in implementation or interpretation:

**Shift invariance.** For any scalar $c$,

$$\frac{e^{(z_v+c)/T}}{\sum_j e^{(z_j+c)/T}}
=\frac{e^{c/T}e^{z_v/T}}{e^{c/T}\sum_j e^{z_j/T}}
=P_T(v)$$

so only logit *differences* carry information. Every implementation subtracts
$\max_j z_j$ before exponentiating, which changes nothing and keeps the largest
exponent at zero, so no term overflows in floating point.

**Why this normalizer.** The pairing of softmax with the log loss is what produces the
gradient derived in §S12, $\nabla_{\mathbf{z}}\mathcal{L}=P-\mathbf{e}_y$: predicted
distribution minus observed one-hot, with no division by a small probability anywhere
in it. A normalizer chosen for convenience — dividing by the sum of positive scores,
say — gives a gradient that depends on the scores' scale and degrades when they are
small.

**$T$ acts before normalization, not after.** Dividing the logits rescales their
differences, so $T$ moves probability mass between tokens while preserving their order
for every $T>0$. Training always ran at $T=1$; a deployed $T\neq1$ therefore samples
from a distribution the loss never optimized, which is a deliberate operator choice and
not a property of $\theta$.

---

## §S8 — Sampling policies and the seed (slide 12 box: *Action Sampling*)

| | |
|---|---|
| **Is** | the rule that turns the distribution $P_T$ into one chosen token, together with the pseudo-random state that makes the choice repeatable. |
| **Signal** | $P_T$ over $\mathcal{V}$, plus a PRNG state → one token $\mathbf{x}_{k+1}\in\mathcal{V}$ and an advanced PRNG state. |
| **Needed because** | the network emits a distribution, so something must choose. Always taking the maximum degenerates into repetition on open-ended text (Holtzman et al., 2020), which is why the choice is made by a draw whose policy is configurable rather than by a fixed rule. |
| **Enables** | variety between regenerations, and reproducibility on demand: a fixed seed replays a run exactly. |
| **Sits** | pipeline step 6 (slide 20); stage: harness code, outside $\theta$; scope: once per generated token. |

Between the distribution (§S7), which it consumes, and the decoding loop (§S9), which
appends the chosen token and calls the network again.

All policies operate on the slide-18 logits $\mathbf{z}$, sorted descending as
$z_{(1)}\ge z_{(2)}\ge\dots$:

- **Greedy and temperature sampling** are slide 19's definitions unchanged. The one
  thing to add: greedy is the $T\to0$ limit of temperature sampling, not a separate
  rule.
- **Top-k**: sample from $P_T$ restricted to $\{v:\,z_v\ \text{among the}\ k\
  \text{largest}\}$, renormalized. The $k$ in this policy's name is the candidate
  count, unrelated to the context length $k$ of $\mathbf{x}_{1:k}$.
- **Top-p / nucleus** (Holtzman et al., 2020): restrict to the smallest set
  $S_p=\{(1),\dots,(m)\}$ with $\sum_{v\in S_p}P_T(v)\ge p$, renormalize, sample.
  Adapts the candidate count to the distribution's actual concentration, which fixed
  $k$ cannot.
- **The draw itself**: $u\sim\mathcal{U}(0,1)$ from a PRNG; select the first token
  whose cumulative probability exceeds $u$ (inverse-CDF sampling — slide 19's worked
  example executed this by hand). The seed initializes the PRNG state; everything
  downstream of the seed is deterministic.

Deployment note, one line: chat products fix these knobs server-side; APIs expose
`temperature`, `top_p`, and (sometimes) `seed` per request.

---

## §S9 — The decoding loop and `<eos>` (slide 13 boxes: *Agent Harness*, *Response*)

| | |
|---|---|
| **Is** | the program loop that appends each sampled token to the context, calls the network again, and applies the halting test. |
| **Signal** | prompt $\mathbf{x}_{1:k}$ → completion $\mathbf{x}_{k+1:j}$, plus a halt reason (`<eos>` sampled, or a length or budget limit reached). |
| **Needed because** | one forward pass yields one distribution over one next token. No part of $\theta$ produces a sequence and no part of it stops. Without the loop the model returns a first token and nothing else; without the halting test the output has no end. |
| **Enables** | variable-length answers whose length the model itself signals, rather than a length the operator fixes in advance. |
| **Sits** | pipeline step 7 (slide 20); stage: harness code, outside $\theta$; scope: once per response, wrapping steps 2–6. |

Between the sampler (§S8), which returns one token, and the response the user reads.

**The identity that joins slide 5 to slide 18.** Slide 5 defines inference as evaluating
$P(\mathbf{x}_{k+1:j}\mid\mathbf{x}_{1:k})$, a distribution over a *sequence*; slides
18–19 produce $P(\mathbf{x}_{k+1}\mid\mathbf{x}_{1:k})$, a distribution over one token.
The chain rule of probability makes them the same object:

$$P(\mathbf{x}_{k+1:j}\mid\mathbf{x}_{1:k})
=\prod_{t=k}^{j-1}P(\mathbf{x}_{t+1}\mid\mathbf{x}_{1:t};\theta)$$

The factorization is exact, not an approximation, and it is the reason a next-token
model is a sequence model at all. The loop below is that product evaluated left to
right, one factor per iteration:

```
x = tokenize(prompt)                      % step 1
for t = 1 : max_new_tokens
    z = unembed(blocks(embed(x)))         % steps 2-4, last position only
    P = softmax(z / T)                    % step 5
    v = sample(P, rng_state)              % step 6
    x = [x, v]                            % step 7
    if v == eos_id, break; end
end
```

**`<eos>`.** An ordinary vocabulary token, present in $\mathcal{V}$ like any other and
supplied as the training target at the end of each training document, so the model
learns to place probability mass on it where a document ends. The network never halts;
the `if` on the last line does. Which means the halting behaviour a user observes is a
property of the harness, and two harnesses running identical weights can disagree about
where an answer ends.

The live-demo lab illustrates the point by omitting the test: `llm_lab.m` generates a
fixed token count (`for k = 1:ND`) and never inspects the sampled token for `<eos>`,
even though `<eos>` is in its vocabulary and in its training targets. See §S17, and the
caution in slide 20's speaker note.

---

## §S10 — Why the activation function is load-bearing

| | |
|---|---|
| **Is** | a fixed non-linear scalar function applied elementwise between successive affine maps. |
| **Signal** | pre-activation $u\in\mathbb{R}$, elementwise over a vector → $a=\varphi(u)\in\mathbb{R}$, same shape. |
| **Needed because** | a composition of affine maps is a single affine map, proved below. With $\varphi$ removed, a network of any width and any depth reduces to one matrix and one bias vector, and every layer after the first is wasted. |
| **Enables** | a function family richer than linear regression, which is the precondition for the approximation result of §S11. |
| **Sits** | inside every feed-forward sublayer (§S5) and every hidden layer of the lab's network; stage: a fixed function with no parameters, identical at training and inference; scope: every hidden unit. |

Between a layer's affine map $W\mathbf{h}+\mathbf{b}$, which hands it a pre-activation
vector, and the next layer's affine map, which would otherwise absorb it.

Claim from slide 14: without $\varphi$, depth buys nothing. Proof in one line:

$$W_2(W_1\mathbf{x}+\mathbf{b}_1)+\mathbf{b}_2
=(W_2W_1)\,\mathbf{x}+(W_2\mathbf{b}_1+\mathbf{b}_2)$$

A stack of affine layers is one affine layer with $W=W_2W_1$. By induction, any depth
collapses. One non-linear $\varphi$ between layers breaks the collapse, and the network
family stops being linear regression.

Derivatives (used by §S12's backpropagation; each is why these functions are practical —
the derivative is available from the forward value at no extra cost):

$$\sigma'(u)=\sigma(u)\,(1-\sigma(u)), \qquad
\tanh'(u)=1-\tanh^2(u), \qquad
\mathrm{ReLU}'(u)=\mathbb{1}[u>0]$$

$$\mathrm{GELU}(u)=u\,\Phi(u), \qquad
\mathrm{GELU}'(u)=\Phi(u)+u\,\phi(u)
\quad (\Phi,\phi:\ \text{standard normal CDF, PDF})$$

Lab tie-in: `llm_lab.m` line 154 (`H = tanh(H*Ws{i} + Bs{i})`) is the forward use;
line 165 (`(1 - acts{i}.^2)`) is $\tanh'$ evaluated from the stored forward value.

---

## §S11 — Universal approximation, stated precisely

**Theorem (Cybenko, 1989; Hornik, 1991).** Let $\varphi$ be a non-constant, bounded,
continuous activation. For any continuous $f$ on a compact $K\subset\mathbb{R}^{d}$ and
any $\varepsilon>0$ there exist a width $m$ and parameters such that the one-hidden-layer
network $g(\mathbf{x})=\sum_{r=1}^{m} c_r\,\varphi(\mathbf{w}_r\cdot\mathbf{x}+b_r)$
satisfies $\sup_{\mathbf{x}\in K}|f(\mathbf{x})-g(\mathbf{x})|<\varepsilon$.

The two silences to teach alongside the statement:

1. $m$ is existential — the theorem permits astronomically wide networks and says
   nothing about how wide is enough for a given $f$ and $\varepsilon$.
2. Nothing guarantees that gradient descent on $\mathcal{L}(\theta)$ *finds* the
   approximating weights. Representability and trainability are separate questions —
   the lab's E4 grid (scale does not rescue a bad representation) is the demonstration.

---

## §S12 — Training mathematics (slide 11 boxes: *Unsupervised Training*, *Predictive Modeling*)

| | |
|---|---|
| **Is** | the procedure that sets $\theta$, by minimizing the mean negative log probability the model assigns to the token that actually followed each context in the corpus. |
| **Signal** | a corpus of token sequences (trillions of tokens, slide 7) → $\theta$, of order $10^{11}$ numbers. Per step: a minibatch of (context, target) pairs → an updated $\theta$. |
| **Needed because** | $\theta$ is initialized at random, so before training the output distribution is arbitrary. Nothing in the architecture supplies the corpus statistics on which the next-token distribution rests. |
| **Enables** | the baseline values of every parameter — slide 7's stage 1 — from which every later stage (§S13) is a comparatively small adjustment. |
| **Sits** | not a pipeline step; stage: training only, offline; scope: all of $\theta$. Its output is the *Static Weights* of slides 5 and 7. |

Between the corpus and the deployed parameter set. It consumes exactly the forward pass
of §S1–§S7 and returns a gradient to every matrix in it.

Slide 2 calls this stage *self-supervision*; slides 7 and 11 call it *Unsupervised
Training*. They name the same objective. Self-supervised is the more exact of the two:
nothing is hand-annotated, but every token is the label for the context preceding it,
so the supervision comes from the data's own order. Slide 11 pairs the box with the
functional label *Predictive Modeling*, which is that objective stated as a function.

The loss is the Case Study 1 slide's, restated once for reference — the empirical mean
of the per-example log loss, which is what slide 5's *Training (Empirical Risk
Minimization–ERM)* names:

$$\mathcal{L}(\theta)=-\frac{1}{n}\sum_{i=1}^{n}
\log P\!\left(\mathbf{x}_{k+1}^{(i)}\,\middle|\,\mathbf{x}_{1:k}^{(i)};\theta\right)$$

**The gradient at the logits — derived.** For one example with target token $y$:
$\mathcal{L}=-\log P_y$ and $P_v=e^{z_v}/\sum_j e^{z_j}$, so
$\log P_y=z_y-\log\sum_j e^{z_j}$ and

$$\frac{\partial \mathcal{L}}{\partial z_v}
=\frac{\partial}{\partial z_v}\!\left(\log\textstyle\sum_j e^{z_j}-z_y\right)
=\frac{e^{z_v}}{\sum_j e^{z_j}}-\delta_{vy}
=P_v-\delta_{vy}
\qquad\Longrightarrow\qquad
\boxed{\;\nabla_{\mathbf{z}}\mathcal{L}=P-\mathbf{e}_y\;}$$

Predicted distribution minus observed one-hot: the same object as the residual
$\hat{y}-y$ in least squares, promoted from scalar to distribution. In the lab this is
`G = P; G(idx) = G(idx) - 1;` (`llm_lab.m` line 162), and the live figure's fourth
panel plots it converging to zero.

**Backpropagation through a layer** (row-vector convention, matching MATLAB: examples
are rows, $Z=HW+\mathbf{b}$, upstream gradient $G=\partial\mathcal{L}/\partial Z$; this
is the transpose of slide 15's column form):

$$\frac{\partial\mathcal{L}}{\partial W}=H^{\top}G,\qquad
\frac{\partial\mathcal{L}}{\partial \mathbf{b}}=\textstyle\sum_{\text{rows}}G,\qquad
\frac{\partial\mathcal{L}}{\partial H}=G\,W^{\top}$$

and through $H=\tanh(U)$: multiply elementwise by $\tanh'(U)=1-H^{2}$ (§S10). The
lab's backward loop (`llm_lab.m` lines 163–167) is these three lines applied from the
output layer down — the chain rule as code:

```matlab
for i = L:-1:1
    dW = acts{i}'*G;  dB = sum(G,1);
    if i > 1, G = (G*Ws{i}') .* (1 - acts{i}.^2); end
    Ws{i} = Ws{i} - ETA*dW;  Bs{i} = Bs{i} - ETA*dB;
end
```

**The update.** Gradient descent: $\theta \leftarrow \theta-\eta\nabla_\theta
\mathcal{L}$, learning rate $\eta$ (`ETA`). *Stochastic* gradient descent — the term
slide 5 committed to — estimates $\nabla\mathcal{L}$ on a random minibatch per step;
the lab's corpus is small enough to use every example every step (the batch-equals-
corpus special case). Production training adds an adaptive step-size rule (Adam;
Kingma & Ba, 2015) and regularization such as dropout (Srivastava et al., 2014) —
named here so the terms are attached to the right stage, derivations out of scope.

**Initialization.** Weights start random with variance chosen so activations neither
explode nor vanish with depth: $\mathrm{Var}=2/d_{\text{in}}$ (He — derived for ReLU)
or $2/(d_{\text{in}}+d_{\text{out}})$ (Glorot — the classical pairing for tanh).
The "random numbers before training" note on the Case Study 1 slide is this step.

---

## §S13 — Post-training (slide 11 boxes: *Curated Training / SFT*, *RLHF / RLVR*, *Reward Model (RM)*, *Refusal Direction*)

| | |
|---|---|
| **Is** | the sequence of objectives applied to a pretrained $\theta$ that turns a text continuer into an assistant which follows instructions and declines a defined class of requests. |
| **Signal** | pretrained $\theta$, plus demonstration pairs, plus human preference comparisons, plus programmatic verifiers where they exist → an adjusted $\theta$ of identical shape. |
| **Needed because** | §S12 optimizes next-token likelihood over a corpus. A model trained only that way continues the prompt as text; it carries no objective that prefers an answer to a plausible continuation, and none that ranks two fluent answers against each other. |
| **Enables** | instruction-following, a consistent register, refusal behaviour, and measurable accuracy gains wherever an answer can be checked automatically. |
| **Sits** | not a pipeline step; stage: training only, after §S12 and before deployment; scope: $\theta$, using under 1% of the training data (slide 7). |

Between the pretrained parameter set of §S12 and the deployed model of slide 5, whose
static weights are this stage's output.

Slide 7 named stage two *Human Alignment*; these are its objectives.

- **Supervised fine-tuning (SFT)** — §S12's loss, unchanged, on a small curated corpus
  $\mathcal{D}_{\text{SFT}}$ of (prompt, demonstration) pairs written or selected by
  people. Needed because a pretrained model continues text and demonstrations are what
  teach it to answer instead; same mathematics, different data. This is what "Curated
  Training" on slide 11 names, and its functional pair on that slide is *Response
  Structuring* — the format and register of an answer are demonstrated here, then
  imitated.
- **Reward model (RM)** — a separate network $r_\phi(\mathbf{x},\mathbf{y})\to
  \mathbb{R}$ trained on human preference pairs ($\mathbf{y}_w$ preferred over
  $\mathbf{y}_l$) with the Bradley–Terry likelihood:
  $$\mathcal{L}(\phi)=-\,\mathbb{E}\!\left[\log\sigma\!\big(r_\phi(\mathbf{x},\mathbf{y}_w)-r_\phi(\mathbf{x},\mathbf{y}_l)\big)\right]$$
  Needed because the next stage scores millions of sampled responses and human
  judgment does not scale to that volume; a scalar proxy trained on a sample of it
  does. Signal: preference pairs $\to\phi$, then $(\mathbf{x},\mathbf{y})\to$ a scalar.
  The RM exists only during training and is discarded at deployment — slide 11 draws it
  outside the layer stack for exactly this reason, and pairs it with *Value-based
  Decision Making*, the function of scoring one response above another.
- **RLHF** (Ouyang et al., 2022) — reinforcement learning against the RM, constrained
  toward the pre-trained distribution $\pi_{\text{ref}}$:
  $$\max_{\pi}\ \mathbb{E}_{\mathbf{y}\sim\pi}\!\left[r_\phi(\mathbf{x},\mathbf{y})\right]
  -\beta\, D_{\mathrm{KL}}\!\big(\pi(\cdot|\mathbf{x})\,\|\,\pi_{\text{ref}}(\cdot|\mathbf{x})\big)$$
  Needed because imitation of demonstrations cannot express a preference between two
  fluent answers, and a preference objective can. The KL term penalizes movement away
  from the pretrained distribution, which is what stops the optimization from trading
  general capability for reward. Slide 11 pairs the *RLHF / RLVR* box with *Reward
  Signaling*.
- **DPO** (Rafailov et al., 2023) — the same preference objective folded into a single
  supervised loss on $\pi$ directly, removing the separate RM and the RL loop.
- **RLVR** — the RLHF loop with the learned reward replaced by a programmatic
  verifier: unit tests pass, the boxed answer matches, the proof checks. Needed because
  a learned reward is an estimate and can be gamed; where a verifier exists the reward
  is exact, which is where the reported gains on mathematics and code come from.
- **Refusal direction** (Arditi et al., 2024) — an empirical finding rather than a
  training stage: refusal behavior concentrates along a single direction
  $\hat{\mathbf{r}}$ in activation space, and ablating it
  ($\mathbf{h}\leftarrow\mathbf{h}-\hat{\mathbf{r}}\hat{\mathbf{r}}^{\top}\mathbf{h}$)
  suppresses refusals. It belongs on this page as evidence that safety behavior is
  learned structure inside $\theta$ with geometry that can be located — which enables
  auditing, and, as the same paper shows, removal. Slide 11's top layer pairs it with
  *Avoiding Harm*.

Two of slide 10's questions are answered on this page. A model's 'personality' is the
SFT corpus — format, register and refusal style are demonstrated, then imitated. Its
'morality' is the preference objective: what the reward model or the DPO loss scores
higher is what the deployed distribution shifts toward. Together with §S12 they also
answer the first: capabilities that are not harness features are acquired by gradient
descent on next-token prediction, then reshaped by these objectives. Slide 10's
"unified parameter space" is the result — SFT and the preference objectives write into
the same $\theta$ that §S12 initialized.

---

## §S14 — Multimodal encoders (slide 11 box: *Multimodal Encoders*; slide 10's "text, images, and sound at the same time")

| | |
|---|---|
| **Is** | a separate encoder network per non-text modality, mapping raw signal into vectors of the decoder's width. |
| **Signal** | an image ($H\times W\times3$ pixels) or audio (waveform → spectrogram frames) → a sequence of vectors in $\mathbb{R}^{d_{\text{model}}}$, placed in the context beside the token embeddings of §S2. |
| **Needed because** | the decoder consumes rows of width $d_{\text{model}}$ and nothing else. Pixels and audio samples have neither that width nor a vocabulary, so §S1 has no IDs to emit and $E$ has no row to look up. |
| **Enables** | images and audio in the same context stream as text, attended to by the same blocks, so a question about an image is answered by the same mechanism as a question about a paragraph. |
| **Sits** | alongside pipeline step 2 (slide 20), replacing the §S1–§S2 path for non-text input; stage: parameters in $\theta$ or in a separately trained encoder; scope: one encoder per modality. |

Between the raw media file and the first decoder block (§S4), which expects rows of $H$
it can attend over.

A vision transformer (Dosovitskiy et al., 2021) performs the mapping for images: split
the image into $P\times P$ pixel patches, flatten each, project linearly to
$d_{\text{model}}$, add positional encodings (§S3) — the image is now a sequence of
vectors, processed by encoder blocks (§S4a) and handed to the decoder as context. Audio
takes the same path via spectrogram frames. One decoder, one context stream, one
encoder per modality — which is the answer to slide 10's question. Slide 11 pairs this
box with *Processing Media*.

---

## §S15 — Beyond-scope box: mixture of experts (MoE)

Current frontier models widen the FFN sublayer economically: each block holds $E$
expert FFNs plus a learned router $g(\mathbf{h})$ that activates the top-$k$
(typically 1–2) per token (Shazeer et al., 2017; Fedus et al., 2021). Total parameters
multiply; per-token compute does not. Mentioned so that "an 800B model that runs like
a 40B model" parses when the audience meets one; nothing later in the course depends
on it.

---

## §S16 — The ledger: what is in the weights, what is around them

All 22 boxes on slides 12–13, sorted by where each one lives. This table is the
"how does each part connect to the LLM" answer in one place: the brain diagrams'
technical content, stated without the anatomy.

| box (slides 12–13) | lives in | mechanism |
|---|---|---|
| T-Decoder | $\theta$ | §S4–§S5: the $N$-block stack |
| Model | $\theta$ + program | slide 6's definition, now fully populated |
| Tokenizer | separate fixed artifact | §S1; trained apart from $\theta$ |
| Action Sampling | harness (decoding code) | §S8; operates on logits |
| System Prompt | context tokens | instructions prepended to $\mathbf{x}_{1:k}$; conditioning, not code |
| Behavioral Conditioning | context tokens | the functional label paired with *System Prompt* on slides 12 and 13: standing instructions that condition every turn |
| Session Context | context tokens | the running transcript inside the slide-5 context window |
| Multi-step Thinking / Chain-of-thought | generated tokens | the model's own output fed back as context — reasoning happens *in* the token stream |
| Sandbox Scratchpad | harness + context | workspace whose contents re-enter as tokens; where a reasoning span is written |
| APIs / MCPs (Peripheral Control) | harness | the model *emits* a structured tool-call as tokens; the harness executes it and returns the result as tokens. Tool use is token emission plus outside code |
| Context Retrieval | harness | the harness searches an external store with the current query, and inserts the retrieved passages into $\mathbf{x}_{1:k}$ as ordinary context tokens before the next forward pass |
| Guardrails | harness (+ §S13 for trained-in refusal) | a classifier or rule pass over the prompt and over the sampled response, run by the harness before the response is returned; distinct from refusal behavior learned into $\theta$ |
| Threat Interception | harness | the functional label paired with *Guardrails*: prompt and sampled response are screened by code outside $\theta$ |
| Token Balance (Resource Allocation) | harness accounting | budget arithmetic on token counts (slide 9) |
| Effort Level | harness configuration | caps how many tokens the model may generate into the *Multi-step Thinking* stream before the harness ends that stream and returns the response |
| Agent Harness / Task Delegation / Output Generation | harness | the slide-20 loop, plus loops that spawn further model calls |
| Response | sampled tokens | slide 20, steps 6–7, repeated to `<eos>` |

**Thinking token.** A thinking token is an ordinary generated token — steps 2–6 of
slide 20, identical to any other — that falls inside a span the harness has designated
as reasoning. Two things distinguish it, and both are harness decisions: the harness
may withhold the span from the displayed response, and it counts the span against a
separate budget. Slide 12's *Sandbox Scratchpad* is where the span is written; slide
13's *Effort Level* is the budget that ends it.

Slide 11 pairs the same way, one stage per row: the left box names the function, the
right box names the component that performs it.

| function (slide 11) | component (slide 11) | defined in |
|---|---|---|
| Processing Input | Tokenizer | §S1 |
| Predictive Modeling | Unsupervised Training | §S12 |
| Processing Media | Multimodal Encoders | §S14 |
| Response Structuring | Curated Training / SFT | §S13 |
| Reward Signaling | RLHF / RLVR | §S13 |
| Value-based Decision Making | Reward Model (RM) | §S13 |
| Avoiding Harm | Refusal Direction | §S13 |

The slide-11 pairings above were read off the slide's colour-matched connectors in the
PDF render; confirm them against the source PPTX before shipping.

Reading rule for both tables: **a capability that can be changed without retraining
lives in the harness or the context; $\theta$ holds only what training put there.**

---

## §S17 — Where the live-demo lab sits in this supplement

`llm_lab.m` implements §S12's core loop (loss, residual, backprop, plain full-batch
update — the code lines are quoted in §S12) and §S8's greedy row, on the §S10 neuron
with tanh, with one-hot inputs standing in for the slide-16 embedding step (the special
case $E=I$) and *no* §S4 attention. That placement is the honest frame for the demo,
condensed from the lab handout:

| present in the lab, identical to production | absent, and named when relevant |
|---|---|
| softmax output stage, logits, $P(v\,|\,\text{ctx})$ | attention (→ no in-context learning) |
| next-token cross-entropy training objective | learned embeddings, positional encoding |
| the residual $P-\mathbf{e}_y$, live on screen | residual connections, LayerNorm |
| autoregressive decoding loop; `<eos>` present in $\mathcal{V}$ and in the training targets | halting on `<eos>` — the loop runs a fixed token count (`llm_lab.m`, `for k = 1:ND`) — and scale ($\sim4\times10^{3}$ vs $\sim10^{11}$ parameters) |
| static weights at inference | post-training (§S13), sampling variety (§S8) |

---

## References block

Verified in `ai-training/references.md` at time of writing ([V] entries there):
Vaswani et al. 2017 (arXiv:1706.03762); Holtzman et al. 2020 (arXiv:1904.09751);
Ouyang et al. 2022 (arXiv:2203.02155); Rafailov et al. 2023 (arXiv:2305.18290).

- Fedus, W., Zoph, B. & Shazeer, N., 2021, *Switch Transformers: Scaling to Trillion
  Parameter Models with Simple and Efficient Sparsity*, arXiv:2101.03961; version of
  record JMLR 23(120):1–39, 2022 — verified in `ai-training/references.md` ([V]);
  three authors, not "et al.".

Verified by web search (bibliographic record confirmed — title, authors, venue,
identifier; each logged in the project's `REFERENCES.md` with its URL and timestamp):

- Cybenko, G., 1989, *Approximation by superpositions of a sigmoidal function*,
  Mathematics of Control, Signals, and Systems 2, 303–314. Confirmed 2026-08-27.
- Hornik, K., 1991, *Approximation capabilities of multilayer feedforward networks*,
  Neural Networks 4(2), 251–257, doi:10.1016/0893-6080(91)90009-T. Confirmed
  2026-08-27; single author.
- Sennrich, R., Haddow, B. & Birch, A., 2016, *Neural Machine Translation of Rare
  Words with Subword Units*, ACL 2016, P16-1162.
- Hendrycks, D. & Gimpel, K., 2016, *Gaussian Error Linear Units (GELUs)*,
  arXiv:1606.08415.
- Ba, J. L., Kiros, J. R. & Hinton, G. E., 2016, *Layer Normalization*,
  arXiv:1607.06450.
- He, K., Zhang, X., Ren, S. & Sun, J., 2016, *Deep Residual Learning for Image
  Recognition*, CVPR 2016, 770–778 (arXiv:1512.03385).
- Su, J., Lu, Y., Pan, S., Wen, B. & Liu, Y., 2021/2023, *RoFormer: Enhanced
  Transformer with Rotary Position Embedding*, arXiv:2104.09864.
- Bengio, Y., Ducharme, R., Vincent, P. & Jauvin, C., 2003, *A Neural Probabilistic
  Language Model*, JMLR 3, 1137–1155.
- Arditi, A., Obeso, O., Syed, A., Paleka, D., Rimsky, N., Gurnee, W. & Nanda, N.,
  2024, *Refusal in Language Models Is Mediated by a Single Direction*,
  arXiv:2406.11717.

Still cited from memory, **verification pending** before the deck ships (all are
one-line mentions with no equation resting on them): Kingma & Ba 2015 (Adam);
Srivastava et al. 2014 (dropout); Dosovitskiy et al. 2021 (ViT); Shazeer et al. 2017
(MoE); the RLVR term's origin (used in the Tülu 3 line of work) has no single canonical
citation confirmed here.
