# Chapter 1 — NETWORK & OUTPUT section: slide content, slides 14–20

Replaces the two placeholder slides (current 14 "Decision-making Math", 15 "Introducing
Variance"). Seven slides. The existing "Case Study 1: Setting up a LLM" follows slide 20
unchanged; PowerPoint renumbers it automatically.

Conventions in this file:

- **Message** — the one sentence the slide exists to convey. Not slide text; your compass
  while building it. If a bullet does not serve the Message, it goes to the Supplement.
- **Opens / Closes** — flow bookkeeping. A topic listed under *Closes* is finished and no
  later slide reopens it; a topic under *Opens* is a debt a named later slide must pay.
- **Body** — paste-able slide text, written in the deck's existing voice (❑ bullets,
  ❖ diamonds, green italic *Hints*). A defined term carries a superscript alias only where
  the alias is the formal technical name the headword lacks — the deck's convention since
  slide 5 ("Prompt (Conditioning Sequence)", "Inference (Autoregressive Decoding)").
- **Equations** — given in LaTeX for the PowerPoint equation editor. Notation is the
  deck's: context $\mathbf{x}_{1:k}$, parameters $\theta$, vocabulary $\mathcal{V}$ (the
  deck's symbol, from the Case Study 1 slide), logits $\mathbf{z}$, distribution
  $P(\mathbf{x}_{k+1}=v\,|\,\mathbf{x}_{1:k};\theta)$, loss $\mathcal{L}(\theta)$. New
  symbols introduced here and reused by the Supplement: hidden state $\mathbf{h}$,
  activation function $\varphi$, embedding matrix $E$, model width $d_{\text{model}}$,
  temperature $T$, block count $N$.
- **Speaker note** — for the notes pane.

Section flow in one line: *neuron → layer → embedding → decoder block → logits →
sampling → the assembled loop.* Each slide consumes only objects defined on earlier
slides. Slide 20 is the "everything clicks" slide the old placeholder asked for: it puts
the generation-path boxes of slides 12–13 on numbered steps, and Supplement §S16 places
the harness and context boxes that do not sit on that path.

---

## Slide 14 — Neural Network: The Neuron

**Message.** A neuron is a weighted sum, plus an offset, passed through a fixed
non-linear function — and with the identity function in that slot, it is exactly the
linear regression this audience already uses.

**Opens:** weights, bias, activation function. **Closes:** activation function —
including slide 2's "non-linear activation" and slide 6's "non-linear transformations",
which name $\varphi$ without giving it. The catalogue below is the complete treatment
at deck level; the derivatives are Supplement §S10 and the approximation theorem is §S11.
Nothing before this slide is reopened.

**Body.**

Framing line (italic, top, mirroring slide 14's current opener):
*Let's define the smallest unit of the **program** that calculates "**what would come
next**", using the **model's weights** and the **prompt**.*

$$a \;=\; \varphi\!\left(\mathbf{w}\cdot\mathbf{x} + b\right)$$

❑ **Weight**, $\mathbf{w}$: how strongly each input moves the output. Set in training
(slide 7).
❑ **Bias**, $b$: the output when every input is zero.
❑ **Activation Function**, $\varphi$: a fixed scalar function applied to the weighted
sum. *(Hint: $\varphi(u)=u$ turns the neuron into multiple linear regression,
$\hat{y}=\boldsymbol{\beta}\cdot\mathbf{x}+\beta_0$ — a model you already fit by least
squares.)*

❖ The activation is what stacking buys: compositions of purely affine maps collapse to
a single affine map, so every layer after the first would be wasted without $\varphi$.
*(One-line proof in Supplement §S10.)*

Activation catalogue (render as a 4-panel mini-plot, $u\in[-4,4]$, one curve each, the
equation under each panel):

| name | equation | range | where it is used |
|---|---|---|---|
| Sigmoid | $\sigma(u)=\dfrac{1}{1+e^{-u}}$ | $(0,1)$ | binary gates; the historical default |
| Tanh | $\tanh(u)=\dfrac{e^{u}-e^{-u}}{e^{u}+e^{-u}}$ | $(-1,1)$ | the live-demo lab's hidden layers |
| ReLU | $\mathrm{ReLU}(u)=\max(0,u)$ | $[0,\infty)$ | deep networks since ~2012 |
| GELU | $\mathrm{GELU}(u)=u\,\Phi(u)$, $\Phi$ = standard normal CDF | $\approx(-0.17,\infty)$ | the feed-forward blocks of GPT-class LLMs |

**Speaker note.** Anchor on the regression identity before showing the catalogue; the
audience fits $\hat{y}=\boldsymbol{\beta}\cdot\mathbf{x}+\beta_0$ weekly. The four
curves answer "what does the non-linearity look like"; which one a given architecture
uses is a design constant, not something the user tunes. Do not discuss derivatives
here — they matter only for training. Supplement §S10 lists them; §S12 uses them.

---

## Slide 15 — Neural Network: Layers, Width, Depth

**Message.** A layer is many neurons sharing the same input; a network is layers
composed; width and depth are the two independent size knobs, and together they set the
parameter count.

**Opens:** hidden state $\mathbf{h}$, width, depth, parameter count $|\theta|$.
**Closes:** "multi-layered" from slide 2's LLM definition and "layered architecture"
from slide 6's Network definition — both now have equations. **Debt forward:** where
these layers sit inside an LLM → slide 17.

**Body.**

Framing line: *Neurons in parallel form a layer; layers in series form the network.*

$$\mathbf{h}^{(0)}=\mathbf{x}, \qquad
\mathbf{h}^{(\ell)}=\varphi\!\left(W^{(\ell)}\mathbf{h}^{(\ell-1)}+\mathbf{b}^{(\ell)}\right),
\quad \ell=1,\dots,L$$

❑ **Hidden State**, $\mathbf{h}^{(\ell)}$: the vector of all neuron outputs at layer
$\ell$. Row $r$ of $W^{(\ell)}$ holds the weights of neuron $r$.
❑ **Width**: the length of $\mathbf{h}^{(\ell)}$.
❑ **Depth**: $L$.
❑ **Parameter count**: $|\theta|=\sum_{\ell} d_\ell\,(d_{\ell-1}+1)$ — every weight
plus every bias. *(Hint: this is the "7B" / "32B" in a model's name, counted the same
way.)* *(Slide 6 called the parameters "weights"; the count includes the biases, which
are parameters on the same footing.)*

❖ **Universal approximation** (Cybenko, 1989; Hornik, 1991): one hidden layer of
sufficient width can approximate any continuous function on a bounded domain to any
tolerance. Existence is guaranteed; the theorem is silent on how many units, and on
whether training finds the weights.
❖ Depth composes features — layer $\ell$ operates on what layer $\ell-1$ already
extracted. *(Hint: the live demo runs a width × depth grid — 8/32/128 against 0/1/2/3 —
and reports held-out accuracy in every cell. Hold this question for the lab.)*

**Speaker note.** The universal-approximation line carries two qualifiers
(width unspecified, trainability unaddressed) — read them aloud; they are what keeps
the theorem honest, and the lab's E4 grid is the empirical counterpart. Citations:
Cybenko (1989), Hornik (1991) — single author. Both bibliographic records are confirmed;
see the Supplement references block.

---

## Slide 16 — Neural Network: Embeddings (Tokens Become Vectors)

**Message.** The network computes with vectors; the embedding matrix is the learned
lookup table that turns a token ID into a vector, and position gets its own vector
added on top.

**Opens:** embedding matrix $E$, $d_{\text{model}}$, positional encoding.
**Closes:** the loose end from slide 9 — what the Token ID is *for* (it is the row
index into $E$); and slide 6's "Network multiplies against token vectors" (this slide
is where those vectors come from). Positional encoding is closed at deck level here;
its equations live in Supplement §S3.

**Body.**

Framing line: *The tokenizer (slides 8–9) delivers integers. The network needs
vectors. One matrix converts.*

$$\mathbf{e}_{v} = \text{row } v \text{ of } E, \qquad
E \in \mathbb{R}^{|\mathcal{V}|\times d_{\text{model}}}$$

$$\mathbf{h}_i^{(0)} = \mathbf{e}_{x_i} + \mathbf{p}_i, \qquad i = 1,\dots,k$$

❑ **Embedding**, $\mathbf{e}_v$: the vector standing for token $v$ everywhere inside
the network. Length $d_{\text{model}}$ (thousands, in frontier models). $E$ contributes
$|\mathcal{V}|\cdot d_{\text{model}}$ parameters — set in training like every other
weight.
❑ **Token ID → row index.** The ID from slide 9 does exactly one job: it selects a row
of $E$.
❑ **Positional Encoding**, $\mathbf{p}_i$: a vector encoding position $i$, added so
that the same token at different positions enters the network differently. *(Hint:
without $\mathbf{p}$, "load causes deflection" and "deflection causes load" would
present the network identical input sets.)*

❖ Proximity in embedding space is learned from co-occurrence: tokens used in similar
contexts acquire nearby vectors. This is why the network can treat 'beam' and 'girder'
similarly without a rule saying so.

**Speaker note.** The live-demo lab skips $E$ and feeds one-hot indicator vectors
directly — the special case $E=I$; the handout states it as "one-hot tokens". Mention it
during the demo, not here. Sinusoidal and rotary positional encodings: Supplement §S3.

---

## Slide 17 — Neural Network: The Transformer Decoder (T-Decoder)

**Message.** The T-Decoder box from slides 12–13 is a stack of N identical blocks,
each pairing self-attention (positions exchange information, weighted by learned
relevance) with a feed-forward layer (each position processed independently) — and
attention is where the context-window cost of slide 5 comes from.

**Opens:** attention, query/key/value, causal mask, multi-head, residual connection,
layer normalization, block count $N$. **Closes:** the *Transformer* name; slide 5's
$O(k_{\max}^2)$ compute claim (the quadratic term is attention's all-pairs score
matrix); the T-Decoder box of slides 12–13. Multi-head, residual, and layer norm are
closed at headline depth — Supplement §S4–S5 carries their full equations and the
worked numeric example. Why the stack is a *decoder* and not an encoder is Supplement
§S4a. **Debt backward paid on 18:** softmax is used in the attention equation below as
a black box — row-wise, it converts a row of scores into weights that are positive and
sum to one. Slide 18 defines it.

**Body.**

Framing line: *One architecture turned next-token prediction into a working
technology: the **Transformer** (Vaswani et al., 2017). LLMs use its decoder stack.*

Block structure (render as a diagram: input $\to$ [LayerNorm $\to$ Masked Multi-Head
Self-Attention $\to$ ⊕] $\to$ [LayerNorm $\to$ Feed-Forward $\to$ ⊕] $\to$ output;
"× N" bracket around the whole block):

$$\text{Attention}(Q,K,V)=\mathrm{softmax}\!\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V,
\qquad Q=HW_Q,\; K=HW_K,\; V=HW_V$$

Rows of $H$ are the $k$ hidden states entering this block — the transpose of slide
15's column form, which is how attention is written throughout. $d_k$ is the head's
width.

❑ **Self-Attention**: every position scores every earlier position for relevance and
takes the weighted average of what they carry. The row-wise softmax is what makes those
weights a weighted average: positive, summing to one (defined on slide 18). Row $i$ of
$Q$ asks; row $j$ of $K$ answers; row $j$ of $V$ is what position $j$ contributes if
selected. *(Hint: $V$ here is the attention value matrix. The vocabulary keeps the
deck's script symbol $\mathcal{V}$.)*
❑ **Causal Mask**^(Autoregressive Constraint): position $i$ may attend to positions
$j \le i$ only. This is the structural form of slide 5's Inference definition —
prediction uses the past, never the future.
❑ **Multi-Head**: $h$ attention maps run in parallel with separate learned $W_Q, W_K,
W_V$, then concatenate and reproject through $W_O$ back to $d_{\text{model}}$
(Supplement §S4). Each head is free to learn a different relation.
❑ **Feed-Forward Block**: the slide-15 network, width $\approx 4\,d_{\text{model}}$,
applied to each position separately. This is where GELU lives (slide 14).
❑ **Residual + LayerNorm**: each sub-layer's output is added to its input
($\mathbf{h} \leftarrow \mathbf{h}+\text{sublayer}(\mathrm{LN}(\mathbf{h}))$),
and layer normalization rescales activations. Together they let $N\sim 10^2$ blocks
train. *(Equations: Supplement §S5.)*

❖ **Cost closure:** the score matrix $QK^{\top}$ holds $k\times k$ entries — the
$O(k_{\max}^{2})$ context-window compute asserted on slide 5 is this matrix.

**Speaker note.** Depth budget of the slide: name each part, one clause of function,
where its math lives. The Supplement's §S4 has the 3-token, $d_k=2$ worked example for
anyone who wants numbers, plus the $\sqrt{d_k}$ variance derivation and the KV-cache
note. During the demo, state once: the lab has every output-stage ingredient and no
attention — that absence is what the handout's "Claims you can defend, and two you
cannot" leans on.

---

## Slide 18 — Neural Network: Logits, Softmax, Temperature

**Message.** The network's final act is a score per vocabulary token (the logit);
softmax turns scores into the probability distribution the whole deck has been
promising; temperature is a dial on that conversion's contrast.

**Opens:** logit $\mathbf{z}$ (as output of unembedding $W_U$), temperature $T$.
**Closes:** "what a logit is" (the old placeholder's demand); slide 6's "Output:
probability distribution per Token" (this is the mechanism). The **Case Study 1** slide
already prints this quotient without naming it; this slide is the name's definition
slot, and the case study becomes a use of it.

**Body.**

Framing line: *After N blocks and one final layer normalization, position $k$ holds a
vector $\mathbf{h}_k^{(N)}$ summarizing the whole prompt. One last matrix converts it
into scores over the vocabulary.*

$$\mathbf{z} = W_U\,\mathbf{h}_k^{(N)} + \mathbf{b}_U, \qquad \mathbf{z}\in\mathbb{R}^{|\mathcal{V}|}$$

$$P_T(\mathbf{x}_{k+1}=v \,|\, \mathbf{x}_{1:k};\theta) \;=\;
\frac{e^{z_v/T}}{\sum_{j\in\mathcal{V}} e^{z_j/T}}$$

❑ **Logit**, $z_v$: the raw score for token $v$. One number per vocabulary entry, every
step. *(Hint: logits are what the model actually computes; probabilities are an
interpretation layer on top.)*
❑ **Unembedding**, $W_U$: the matrix mapping the final hidden state onto the
vocabulary. *(Hint: many models set $W_U = E$ — **weight tying**. Row $v$ of $E$ embeds
token $v$ on the way in and scores it on the way out: one lookup table, read in both
directions.)*
❑ **Softmax**: exponentiate, normalize. Preserves the ranking of $\mathbf{z}$;
guarantees $P>0$ and $\sum_v P = 1$.
❑ **Temperature**, $T$: divides every logit before softmax. $T\to 0$: all mass on the
top logit. $T=1$: the distribution as trained. $T>1$: flatter, higher-entropy output.

**Speaker note.** Show the three-temperature bar chart on the next slide rather than
here — this slide defines, slide 19 computes. In the live demo, the bottom-left panel of
`llm_lab.m`'s live figure (the $P(v\,|\,\text{ctx})$ bar chart) is exactly $P_{T=1}$;
point at it and say "logits, after softmax."

---

## Slide 19 — Neural Network: Variance — Sampling, Temperature, Seeds

**Message.** The network is a deterministic function; the product is stochastic
because one pseudo-random draw per token selects from $P_T$ — so variance across
responses is a designed feature located entirely at the sampling step, and the seed
controls the draw.

**Opens:** sampling policies (greedy, temperature, top-k, top-p), seed. **Closes:**
the entire "Introducing Variance" placeholder: randomness, seeds, temperature — plus
the worked example it demanded. After this slide, output variance is never re-derived;
later chapters may only reference it.

**Body.**

Framing line: *Same weights, same prompt, same arithmetic → the same logits. The
variety you observe between regenerations is injected on purpose, here:*

$$\mathbf{x}_{k+1} \sim \mathrm{Categorical}\!\left(P_T(\cdot \,|\, \mathbf{x}_{1:k};\theta)\right)$$

❑ **Sampling policies** (all operate on the logits of slide 18):
&nbsp;&nbsp;❑ **Greedy**^(argmax): always the top token. Deterministic; repetitive on
open-ended text (Holtzman et al., 2020).
&nbsp;&nbsp;❑ **Temperature sampling**: draw from $P_T$.
&nbsp;&nbsp;❑ **Top-k**: keep the highest $k$ logits, renormalize, draw. *(The $k$ in
this policy's name is the candidate count, not the context length $k$ of
$\mathbf{x}_{1:k}$.)*
&nbsp;&nbsp;❑ **Top-p**^(Nucleus): keep the smallest token set whose cumulative
probability exceeds $p$, renormalize, draw.
❑ **Seed**^(PRNG State): the draw uses a pseudo-random number generator. Fixed seed →
identical draw sequence → reproducible output. *(Hint: hosted products don't expose
the seed. API access does — and even then $T=0$ across a provider's hardware is not
bit-reproducible: parallel floating-point addition is non-associative.)*

**Worked example** (right half of the slide, table + one bar chart per temperature).
Four-token vocabulary, logits $\mathbf{z} = (2.0,\; 1.0,\; 0.2,\; -1.0)$:

| | $v_1$ | $v_2$ | $v_3$ | $v_4$ |
|---|---|---|---|---|
| $P_{T=0.5}$ | 0.858 | 0.116 | 0.023 | 0.002 |
| $P_{T=1}$ | 0.632 | 0.232 | 0.104 | 0.031 |
| $P_{T=2}$ | 0.447 | 0.271 | 0.182 | 0.100 |

Draw $u \sim \mathcal{U}(0,1)$ from the seeded PRNG; walk the cumulative sums of
$P_{T=1}$: $(0.632,\; 0.864,\; 0.969,\; 1.000)$.
❖ $u = 0.22 \Rightarrow v_1$. &nbsp; ❖ $u = 0.71 \Rightarrow v_2$. &nbsp; ❖ Same
seed, same $u$, same token; new seed, new draw, same distribution.

**Speaker note.** The one-sentence takeaway to say out loud: *randomness is a dial the
operator sets, and it lives outside the network.* If someone asks why regenerating an
answer changes it while the weights are static (slide 7: *Static Weights*), this slide
is the complete answer. The planned lab extension adds exactly this draw to the prompt
loop so the class can watch $T$ work — see the demo-change list.

---

## Slide 20 — Neural Network: The Assembled Loop

**Message.** One pass of the pipeline produces one token; the loop that feeds each new
token back is ordinary code outside the network, and it — not the model — decides when
to stop. The five boxes that sit on the generation path — Tokenizer, T-Decoder, Action
Sampling, Token Balance, Agent Harness — land on numbered steps; Supplement §S16 places
the remaining seventeen.

**Opens:** decoding loop, `<eos>` token. **Closes:** the NETWORK & OUTPUT section:
slide 5's Inference definition is now mechanically complete; the T-Decoder / Action
Sampling / Tokenizer boxes of slides 12–13 land on numbered pipeline steps. Also closed
here, open until now: weights and bias (14); hidden state, width, depth and $|\theta|$
(15); $E$ and $d_{\text{model}}$ (16); attention, Q/K/V, causal mask and $N$ (17);
logit and $W_U$ (18). Sets up Case Study 1 with one sentence (training = how $\theta$
was chosen).

**Body.**

Framing line: *Seven steps, six of which you have already seen defined. The seventh is
a `while` loop.*

Pipeline (render as the section's capstone diagram — numbered chain, each stage
labeled with its slide of origin and the matching slide-12/13 box name):

1. **Tokenize** (slides 8–9 | box: *Tokenizer*): text $\to \mathbf{x}_{1:k}$
2. **Embed** (slide 16): $\mathbf{h}_i^{(0)} = \mathbf{e}_{x_i}+\mathbf{p}_i$
3. **N decoder blocks** (slide 17 | box: *T-Decoder*): $\to \mathbf{h}_k^{(N)}$
4. **Logits** (slide 18): $\mathbf{z} = W_U\,\mathbf{h}_k^{(N)}+\mathbf{b}_U$
5. **Distribution** (slide 18): $P_T = \mathrm{softmax}(\mathbf{z}/T)$
6. **Sample** (slide 19 | box: *Action Sampling*): $\mathbf{x}_{k+1}\sim\mathrm{Categorical}(P_T)$
7. **Append and repeat** (box: *Agent Harness / decoding loop*): $k \leftarrow k+1$,
   go to 2 — until the sampled token is **`<eos>`**^(End-of-Sequence) or a length limit
   trips.

❑ **`<eos>`** is an ordinary vocabulary token the model learned to emit. The *loop*
reads it and halts; the network only ever outputs a distribution.
❖ The stopping rule, the token budget (slide 12: *Token Balance*), and retries are
harness code. What the network contributes is steps 2–5; everything else on slides
12–13 is software arranged around those four steps.
❖ Steps 1–7 are **Inference** exactly as defined on slide 5. One pass of steps 2–6
gives $P(\mathbf{x}_{k+1}\mid\mathbf{x}_{1:k})$; step 7's loop is what turns that into
slide 5's $P(\mathbf{x}_{k+1:j}\mid\mathbf{x}_{1:k})$.

*(Transition line, bottom):* Every step above used weights already set. **Case Study
1** builds the machine that sets them, on the shortest network that still has a logit
vector: one affine map, $\mathbf{z}=\mathbf{W}\cdot\mathbf{x}_{1:k}+\mathbf{b}$, in
place of steps 2–4.

**Speaker note.** This is the "everything clicks" slide the placeholder asked for —
walk it slowly; it is also the map you return to during the live demo ("we are at
step 5; here is the bar chart"). The demo's decoder generates a fixed number of tokens
and ignores `<eos>`; a loop that honors it tells a different story — a strong
30-second aside at step 7. Caution from the peer review: the handout's eos-comparison
numbers have no shipped code behind them, so implement the 3-line break variant and
regenerate those numbers before quoting them
(`MATLAB_EXAMPLES/PEER_REVIEW_2026-08-27.md`).

---

## Coverage check — every term the section owes, and where it is paid

| term | defined at |
|---|---|
| neuron, weight, bias | 14 |
| activation function; sigmoid, tanh, ReLU, GELU | 14 (derivatives: Supp §S10) |
| layer, hidden state, width, depth, $|\theta|$ | 15 |
| universal approximation | 15 (statement; proof pointer Supp §S11) |
| embedding, $d_{\text{model}}$, token-ID-as-row-index | 16 (Supp §S2) |
| positional encoding | 16 (equations: Supp §S3) |
| transformer, decoder, self-attention, Q/K/V, causal mask | 17 (worked numbers: Supp §S4) |
| multi-head, residual, layer norm, feed-forward block | 17 (equations: Supp §S5) |
| $O(k^2)$ context cost | 17 (derivation: Supp §S4) |
| logit, unembedding, weight tying | 18 (Supp §S6) |
| softmax, temperature | 18 (limits and shift-invariance: Supp §S7) |
| sampling: greedy, temperature, top-k, top-p; seed, PRNG | 19 (math: Supp §S8) |
| decoding loop, `<eos>`, halting | 20 (sequence factorization: Supp §S9) |
| encoder (vs decoder), attention masks both ways | Supp §S4a |
| training math: cross-entropy gradient, backprop, SGD/minibatch | Supp §S12 (uses the Case Study 1 loss) |
| SFT, reward model, RLHF, DPO, RLVR, refusal direction | Supp §S13 |
| multimodal encoders | Supp §S14 |
| mixture-of-experts, KV cache | Supp §S4/§S15 (beyond-scope boxes) |
| weights-vs-harness ledger for every slide-11/12/13 box | Supp §S16 |

Citation status at time of writing: Vaswani 2017 and Holtzman 2020 — verified in
`ai-training/references.md` ([V]). Cybenko 1989 and Hornik 1991 — bibliographic records
confirmed 2026-08-27 and logged in the project's `REFERENCES.md`; the Supplement's
references block carries the full entries.
