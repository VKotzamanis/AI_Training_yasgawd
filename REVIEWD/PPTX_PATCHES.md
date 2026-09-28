# PPTX patch list — `CH1_SLIDES_14-20.pptx`

Delta list for the slide builder, generated from the audit fixes applied to
`CH1_NETWORK_SLIDES.md` on 2026-08-27. **Scope: the deck only.** `CH1_SUPPLEMENT.md`
was rewritten in the same pass and is not a deck file; none of its changes appear here.

Each entry gives the slide, the element, the exact old text, and the exact new text.
Line breaks inside OLD blocks reproduce the wrapping of the source markdown; they are
not slide line breaks. Entries marked **spec only** change `CH1_NETWORK_SLIDES.md` but
have no PowerPoint element — apply them to the markdown, not to the deck.

Two changes touch every slide and are listed once, at the end, as global find/replace
entries: the vocabulary symbol and the superscript-alias convention. Both are also
itemised in place.

---

## §0 — Front matter (spec only, no PowerPoint element)

### 0.1 — Conventions, "Body" bullet — alias convention restated

OLD
```
- **Body** — paste-able slide text, written in the deck's existing voice (❑ bullets,
  ❖ diamonds, green italic *Hints*, defined terms carrying a superscript technical alias).
```
NEW
```
- **Body** — paste-able slide text, written in the deck's existing voice (❑ bullets,
  ❖ diamonds, green italic *Hints*). A defined term carries a superscript alias only where
  the alias is the formal technical name the headword lacks — the deck's convention since
  slide 5 ("Prompt (Conditioning Sequence)", "Inference (Autoregressive Decoding)").
```

### 0.2 — Conventions, "Equations" bullet — vocabulary symbol (audit E-6)

OLD
```
- **Equations** — given in LaTeX for the PowerPoint equation editor. Notation is the
  deck's: context $\mathbf{x}_{1:k}$, parameters $\theta$, vocabulary $V$, logits
  $\mathbf{z}$, distribution $P(\mathbf{x}_{k+1}=v\,|\,\mathbf{x}_{1:k};\theta)$, loss
  $\mathcal{L}(\theta)$.
```
NEW
```
- **Equations** — given in LaTeX for the PowerPoint equation editor. Notation is the
  deck's: context $\mathbf{x}_{1:k}$, parameters $\theta$, vocabulary $\mathcal{V}$ (the
  deck's symbol, from the Case Study 1 slide), logits $\mathbf{z}$, distribution
  $P(\mathbf{x}_{k+1}=v\,|\,\mathbf{x}_{1:k};\theta)$, loss $\mathcal{L}(\theta)$.
```

### 0.3 — Section-flow paragraph (audit E-3)

OLD
```
Slide 20 is the "everything clicks" slide the old placeholder asked for, and it
resolves every remaining box on slides 12–13.
```
NEW
```
Slide 20 is the "everything clicks" slide the old placeholder asked for: it puts
the generation-path boxes of slides 12–13 on numbered steps, and Supplement §S16 places
the harness and context boxes that do not sit on that path.
```

---

## Slide 14 — The Neuron

### 14.1 — Opens/Closes ledger (spec only) — audit E-19

OLD
```
**Opens:** weights, bias, activation function. **Closes:** activation function (the
catalogue below is the complete treatment at deck level; derivatives and the
approximation proof live in Supplement §S1–S2). Nothing before this slide is reopened.
```
NEW
```
**Opens:** weights, bias, activation function. **Closes:** activation function —
including slide 2's "non-linear activation" and slide 6's "non-linear transformations",
which name $\varphi$ without giving it. The catalogue below is the complete treatment
at deck level; the derivatives are Supplement §S10 and the approximation theorem is §S11.
Nothing before this slide is reopened.
```

### 14.2 — Body bullet 1 (Weight) — alias dropped, audit E-33

OLD
```
❑ **Weight**^(Learned Sensitivity), $\mathbf{w}$: how strongly each input moves the
output. Set in training (slide 7).
```
NEW
```
❑ **Weight**, $\mathbf{w}$: how strongly each input moves the output. Set in training
(slide 7).
```

### 14.3 — Body bullet 2 (Bias) — alias dropped, audit E-33

OLD
```
❑ **Bias**^(Learned Offset), $b$: the output when every input is zero.
```
NEW
```
❑ **Bias**, $b$: the output when every input is zero.
```

### 14.4 — Body bullet 3 (Activation Function) — alias dropped, audit E-33

OLD
```
❑ **Activation Function**^(Non-linearity), $\varphi$: a fixed scalar function applied
to the weighted sum.
```
NEW
```
❑ **Activation Function**, $\varphi$: a fixed scalar function applied to the weighted
sum.
```

### 14.5 — ❖ diamond, supplement pointer — supplement renumbering

OLD
```
*(One-line proof in Supplement §S1.)*
```
NEW
```
*(One-line proof in Supplement §S10.)*
```

### 14.6 — Speaker note, last sentence — audit E-9

OLD
```
Do not discuss derivatives
here — they matter only for training, and Supplement §S8 derives them.
```
NEW
```
Do not discuss derivatives
here — they matter only for training. Supplement §S10 lists them; §S12 uses them.
```

---

## Slide 15 — Layers, Width, Depth

### 15.1 — Body bullet 1 (Hidden State) — alias dropped, audit E-33

OLD
```
❑ **Hidden State**^(Layer Output), $\mathbf{h}^{(\ell)}$: the vector of all neuron
outputs at layer $\ell$. Row $r$ of $W^{(\ell)}$ holds the weights of neuron $r$.
```
NEW
```
❑ **Hidden State**, $\mathbf{h}^{(\ell)}$: the vector of all neuron outputs at layer
$\ell$. Row $r$ of $W^{(\ell)}$ holds the weights of neuron $r$.
```

### 15.2 — Body bullet 2 (Width) — alias dropped, audit E-33

OLD
```
❑ **Width**^(Units per Layer): the length of $\mathbf{h}^{(\ell)}$.
```
NEW
```
❑ **Width**: the length of $\mathbf{h}^{(\ell)}$.
```

### 15.3 — Body bullet 3 (Depth) — alias dropped, audit E-33

OLD
```
❑ **Depth**^(Number of Layers): $L$.
```
NEW
```
❑ **Depth**: $L$.
```

### 15.4 — Body bullet 4 (Parameter count), appended clause — audit E-20

OLD
```
❑ **Parameter count**: $|\theta|=\sum_{\ell} d_\ell\,(d_{\ell-1}+1)$ — every weight
plus every bias. *(Hint: this is the "7B" / "32B" in a model's name, counted the same
way.)*
```
NEW
```
❑ **Parameter count**: $|\theta|=\sum_{\ell} d_\ell\,(d_{\ell-1}+1)$ — every weight
plus every bias. *(Hint: this is the "7B" / "32B" in a model's name, counted the same
way.)* *(Slide 6 called the parameters "weights"; the count includes the biases, which
are parameters on the same footing.)*
```

### 15.5 — Hint on the depth ❖ diamond — audit E-11

OLD
```
*(Hint: the live demo measures depth against width at a fixed parameter
budget — hold this question for the lab.)*
```
NEW
```
*(Hint: the live demo runs a width × depth grid — 8/32/128 against 0/1/2/3 —
and reports held-out accuracy in every cell. Hold this question for the lab.)*
```

### 15.6 — Speaker note, citation clause — audit E-12, E-18

OLD
```
Citations:
Cybenko (1989), Hornik et al. (1991) — bibliography status: see Supplement references
block.
```
NEW
```
Citations:
Cybenko (1989), Hornik (1991) — single author. Both bibliographic records are confirmed;
see the Supplement references block.
```

---

## Slide 16 — Embeddings

### 16.1 — Opens/Closes ledger (spec only) — supplement renumbering

OLD
```
its equations live in Supplement §S4.
```
NEW
```
its equations live in Supplement §S3.
```

### 16.2 — Equation 1, vocabulary symbol — audit E-6

OLD
```
$$\mathbf{e}_{v} = \text{row } v \text{ of } E, \qquad
E \in \mathbb{R}^{|V|\times d_{\text{model}}}$$
```
NEW
```
$$\mathbf{e}_{v} = \text{row } v \text{ of } E, \qquad
E \in \mathbb{R}^{|\mathcal{V}|\times d_{\text{model}}}$$
```

### 16.3 — Body bullet 1 (Embedding) — alias dropped (E-33) and symbol (E-6)

OLD
```
❑ **Embedding**^(Learned Token Vector), $\mathbf{e}_v$: the vector standing for token
$v$ everywhere inside the network. Length $d_{\text{model}}$ (thousands, in frontier
models). $E$ contributes $|V|\cdot d_{\text{model}}$ parameters — set in training like
every other weight.
```
NEW
```
❑ **Embedding**, $\mathbf{e}_v$: the vector standing for token $v$ everywhere inside
the network. Length $d_{\text{model}}$ (thousands, in frontier models). $E$ contributes
$|\mathcal{V}|\cdot d_{\text{model}}$ parameters — set in training like every other
weight.
```

### 16.4 — Body bullet 3 (Positional Encoding) — alias dropped, audit E-33

OLD
```
❑ **Positional Encoding**^(Order Information), $\mathbf{p}_i$: a vector encoding
position $i$, added so that the same token at different positions enters the network
differently.
```
NEW
```
❑ **Positional Encoding**, $\mathbf{p}_i$: a vector encoding position $i$, added so
that the same token at different positions enters the network differently.
```

### 16.5 — Speaker note — audit E-27 and supplement renumbering

OLD
```
**Speaker note.** The live-demo lab skips $E$ and feeds one-hot indicator vectors
directly — the special case $E=I$, stated in the lab handout. Mention it during the
demo, not here. Sinusoidal and rotary positional encodings: Supplement §S4.
```
NEW
```
**Speaker note.** The live-demo lab skips $E$ and feeds one-hot indicator vectors
directly — the special case $E=I$; the handout states it as "one-hot tokens". Mention it
during the demo, not here. Sinusoidal and rotary positional encodings: Supplement §S3.
```

---

## Slide 17 — The Transformer Decoder (T-Decoder)

### 17.1 — Opens/Closes ledger (spec only) — audit E-1, E-25, renumbering

OLD
```
Multi-head, residual, and layer norm are
closed at headline depth — Supplement §S5–S6 carries their full equations and the
worked numeric example.
```
NEW
```
Multi-head, residual, and layer norm are
closed at headline depth — Supplement §S4–S5 carries their full equations and the
worked numeric example. Why the stack is a *decoder* and not an encoder is Supplement
§S4a. **Debt backward paid on 18:** softmax is used in the attention equation below as
a black box — row-wise, it converts a row of scores into weights that are positive and
sum to one. Slide 18 defines it.
```

### 17.2 — Attention equation — audit E-6, the prime removed

OLD
```
$$\text{Attention}(Q,K,V')=\mathrm{softmax}\!\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V',
\qquad Q=HW_Q,\; K=HW_K,\; V'=HW_V$$
```
NEW
```
$$\text{Attention}(Q,K,V)=\mathrm{softmax}\!\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V,
\qquad Q=HW_Q,\; K=HW_K,\; V=HW_V$$
```

### 17.3 — NEW body text block, inserted immediately below the attention equation and above the first ❑ bullet — audit E-15, E-18

OLD
```
(nothing — this is an insertion)
```
NEW
```
Rows of $H$ are the $k$ hidden states entering this block — the transpose of slide
15's column form, which is how attention is written throughout. $d_k$ is the head's
width.
```

### 17.4 — Body bullet 1 (Self-Attention) — audit E-1, E-6, E-33

OLD
```
❑ **Self-Attention**^(Content-based Lookup): every position scores every earlier
position for relevance and takes the weighted average of what they carry. Row $i$ of
$Q$ asks; row $j$ of $K$ answers; row $j$ of $V'$ is what position $j$ contributes if
selected. *(Hint: the prime on $V'$ keeps the value matrix distinct from the
vocabulary $V$ of slides 5–16.)*
```
NEW
```
❑ **Self-Attention**: every position scores every earlier position for relevance and
takes the weighted average of what they carry. The row-wise softmax is what makes those
weights a weighted average: positive, summing to one (defined on slide 18). Row $i$ of
$Q$ asks; row $j$ of $K$ answers; row $j$ of $V$ is what position $j$ contributes if
selected. *(Hint: $V$ here is the attention value matrix. The vocabulary keeps the
deck's script symbol $\mathcal{V}$.)*
```

### 17.5 — Body bullet 3 (Multi-Head) — audit E-39

OLD
```
❑ **Multi-Head**: $h$ attention maps run in parallel with separate learned $W_Q, W_K,
W_V$, then concatenate. Each head is free to learn a different relation.
```
NEW
```
❑ **Multi-Head**: $h$ attention maps run in parallel with separate learned $W_Q, W_K,
W_V$, then concatenate and reproject through $W_O$ back to $d_{\text{model}}$
(Supplement §S4). Each head is free to learn a different relation.
```

### 17.6 — Body bullet 5 (Residual + LayerNorm) — alias dropped (E-33), pointer renumbered

OLD
```
❑ **Residual + LayerNorm**^(Training Stabilizers): each sub-layer's output is added to
its input ($\mathbf{h} \leftarrow \mathbf{h}+\text{sublayer}(\mathrm{LN}(\mathbf{h}))$),
and layer normalization rescales activations. Together they let $N\sim 10^2$ blocks
train. *(Equations: Supplement §S6.)*
```
NEW
```
❑ **Residual + LayerNorm**: each sub-layer's output is added to its input
($\mathbf{h} \leftarrow \mathbf{h}+\text{sublayer}(\mathrm{LN}(\mathbf{h}))$),
and layer normalization rescales activations. Together they let $N\sim 10^2$ blocks
train. *(Equations: Supplement §S5.)*
```

### 17.7 — Speaker note — audit E-26 and supplement renumbering

OLD
```
The Supplement's §S5 has the 3-token, $d_k=2$ worked example for
anyone who wants numbers, plus the $\sqrt{d_k}$ variance derivation and the KV-cache
note. During the demo, state once: the lab has every output-stage ingredient and no
attention — that absence is what the handout's defensibility section leans on.
```
NEW
```
The Supplement's §S4 has the 3-token, $d_k=2$ worked example for
anyone who wants numbers, plus the $\sqrt{d_k}$ variance derivation and the KV-cache
note. During the demo, state once: the lab has every output-stage ingredient and no
attention — that absence is what the handout's "Claims you can defend, and two you
cannot" leans on.
```

---

## Slide 18 — Logits, Softmax, Temperature

### 18.1 — Opens/Closes ledger (spec only) — audit E-7, B-2/B-3

OLD
```
**Closes:** "what a logit is" (the old placeholder's demand); slide 6's "Output:
probability distribution per Token" (this is the mechanism). Softmax itself appeared on
slide 16's case-study preview — this slide is its *definition* slot; the case study
now *uses* it.
```
NEW
```
**Closes:** "what a logit is" (the old placeholder's demand); slide 6's "Output:
probability distribution per Token" (this is the mechanism). The **Case Study 1** slide
already prints this quotient without naming it; this slide is the name's definition
slot, and the case study becomes a use of it.
```

### 18.2 — Framing line — audit E-38, the final LayerNorm

OLD
```
Framing line: *After N blocks, position $k$ holds a vector $\mathbf{h}_k$ summarizing
the whole prompt. One last matrix converts it into scores over the vocabulary.*
```
NEW
```
Framing line: *After N blocks and one final layer normalization, position $k$ holds a
vector $\mathbf{h}_k^{(N)}$ summarizing the whole prompt. One last matrix converts it
into scores over the vocabulary.*
```

### 18.3 — Equation 1 (logits), vocabulary symbol — audit E-6

OLD
```
$$\mathbf{z} = W_U\,\mathbf{h}_k^{(N)} + \mathbf{b}_U, \qquad \mathbf{z}\in\mathbb{R}^{|V|}$$
```
NEW
```
$$\mathbf{z} = W_U\,\mathbf{h}_k^{(N)} + \mathbf{b}_U, \qquad \mathbf{z}\in\mathbb{R}^{|\mathcal{V}|}$$
```

### 18.4 — Equation 2 (softmax), summation index — audit E-6

OLD
```
$$P_T(\mathbf{x}_{k+1}=v \,|\, \mathbf{x}_{1:k};\theta) \;=\;
\frac{e^{z_v/T}}{\sum_{j\in V} e^{z_j/T}}$$
```
NEW
```
$$P_T(\mathbf{x}_{k+1}=v \,|\, \mathbf{x}_{1:k};\theta) \;=\;
\frac{e^{z_v/T}}{\sum_{j\in\mathcal{V}} e^{z_j/T}}$$
```

### 18.5 — Body bullet 1 (Logit) — alias dropped, audit E-33

OLD
```
❑ **Logit**^(Unnormalized Score), $z_v$: the raw score for token $v$. One number per
vocabulary entry, every step.
```
NEW
```
❑ **Logit**, $z_v$: the raw score for token $v$. One number per vocabulary entry, every
step.
```

### 18.6 — Body bullet 2 (Unembedding) — audit E-2 / E-34, the weight-tying error, plus alias dropped (E-33)

This is the one mathematically wrong line in the deck; do not paste the old form.

OLD
```
❑ **Unembedding**^(Output Projection), $W_U$: the matrix mapping the final hidden
state onto the vocabulary. *(Hint: many models reuse $E^{\top}$ here — one lookup
table, both directions.)*
```
NEW
```
❑ **Unembedding**, $W_U$: the matrix mapping the final hidden state onto the
vocabulary. *(Hint: many models set $W_U = E$ — **weight tying**. Row $v$ of $E$ embeds
token $v$ on the way in and scores it on the way out: one lookup table, read in both
directions.)*
```

### 18.7 — Body bullet 3 (Softmax) — alias dropped, audit E-33

OLD
```
❑ **Softmax**^(Score → Distribution): exponentiate, normalize. Preserves the ranking
of $\mathbf{z}$; guarantees $P>0$ and $\sum_v P = 1$.
```
NEW
```
❑ **Softmax**: exponentiate, normalize. Preserves the ranking of $\mathbf{z}$;
guarantees $P>0$ and $\sum_v P = 1$.
```

### 18.8 — Body bullet 4 (Temperature) — alias dropped, audit E-33 (removes the coinage "Contrast Dial")

OLD
```
❑ **Temperature**^(Contrast Dial), $T$: divides every logit before softmax.
$T\to 0$: all mass on the top logit. $T=1$: the distribution as trained. $T>1$:
flatter, higher-entropy output.
```
NEW
```
❑ **Temperature**, $T$: divides every logit before softmax. $T\to 0$: all mass on the
top logit. $T=1$: the distribution as trained. $T>1$: flatter, higher-entropy output.
```

### 18.9 — Speaker note, panel reference — audit E-28

OLD
```
In the live demo, panel 3 of `llm_lab.m`
(the $P(v\,|\,\text{ctx})$ bar chart) is exactly $P_{T=1}$; point at it and say
"logits, after softmax."
```
NEW
```
In the live demo, the bottom-left panel of
`llm_lab.m`'s live figure (the $P(v\,|\,\text{ctx})$ bar chart) is exactly $P_{T=1}$;
point at it and say "logits, after softmax."
```

---

## Slide 19 — Variance: Sampling, Temperature, Seeds

### 19.1 — Framing line — audit E-17, removes the self-contradiction with the slide's own hint

OLD
```
Framing line: *Same weights, same prompt → bit-identical logits, every time. The
variety you observe between regenerations is injected on purpose, here:*
```
NEW
```
Framing line: *Same weights, same prompt, same arithmetic → the same logits. The
variety you observe between regenerations is injected on purpose, here:*
```

### 19.2 — Body sub-bullet (Top-k) — audit E-16, the $k$ collision

OLD
```
&nbsp;&nbsp;❑ **Top-k**: keep the $k$ highest logits, renormalize, draw.
```
NEW
```
&nbsp;&nbsp;❑ **Top-k**: keep the highest $k$ logits, renormalize, draw. *(The $k$ in
this policy's name is the candidate count, not the context length $k$ of
$\mathbf{x}_{1:k}$.)*
```

### 19.3 — Speaker note — audit E-8, "frozen" is not the deck's word

OLD
```
If someone asks why regenerating an
answer changes it while the model is "frozen" (slide 7), this slide is the complete
answer.
```
NEW
```
If someone asks why regenerating an
answer changes it while the weights are static (slide 7: *Static Weights*), this slide
is the complete answer.
```

No change to the worked-example table, the cumulative sums, or the two draws — all
verified correct.

---

## Slide 20 — The Assembled Loop

### 20.1 — Message, third sentence — audit E-3 / C-5, the "every box" overclaim

OLD
```
Every box from slides 12–13 now has a place in the chain.
```
NEW
```
The five boxes that sit on the generation path — Tokenizer, T-Decoder, Action
Sampling, Token Balance, Agent Harness — land on numbered steps; Supplement §S16
places the remaining seventeen.
```

### 20.2 — Opens/Closes ledger (spec only) — audit E-29, balancing the ledger

OLD
```
Sets up
Case Study 1 with one sentence (training = how $\theta$ was chosen).
```
NEW
```
Also closed
here, open until now: weights and bias (14); hidden state, width, depth and $|\theta|$
(15); $E$ and $d_{\text{model}}$ (16); attention, Q/K/V, causal mask and $N$ (17);
logit and $W_U$ (18). Sets up Case Study 1 with one sentence (training = how $\theta$
was chosen).
```

### 20.3 — Second ❖ diamond — audit E-22, the slide-5 sequence/token bridge

OLD
```
❖ Steps 1–7 are **Inference** exactly as defined on slide 5 — now with every symbol
accounted for.
```
NEW
```
❖ Steps 1–7 are **Inference** exactly as defined on slide 5. One pass of steps 2–6
gives $P(\mathbf{x}_{k+1}\mid\mathbf{x}_{1:k})$; step 7's loop is what turns that into
slide 5's $P(\mathbf{x}_{k+1:j}\mid\mathbf{x}_{1:k})$.
```

### 20.4 — Transition line, bottom — audit E-21, the Case Study 1 logit collision

OLD
```
*(Transition line, bottom):* Every step above used weights already set. **Case Study
1** builds the machine that sets them.
```
NEW
```
*(Transition line, bottom):* Every step above used weights already set. **Case Study
1** builds the machine that sets them, on the shortest network that still has a logit
vector: one affine map, $\mathbf{z}=\mathbf{W}\cdot\mathbf{x}_{1:k}+\mathbf{b}$, in
place of steps 2–4.
```

No change to the seven numbered pipeline steps or to the speaker note.

---

## §99 — Coverage table and citation status (spec only, no PowerPoint element)

### 99.1 — Coverage table, every changed cell

| row | OLD right-hand cell | NEW right-hand cell |
|---|---|---|
| activation function; sigmoid, tanh, ReLU, GELU | `14 (derivatives: Supp §S8)` | `14 (derivatives: Supp §S10)` |
| universal approximation | `15 (statement; proof pointer Supp §S2)` | `15 (statement; proof pointer Supp §S11)` |
| embedding, $d_{\text{model}}$, token-ID-as-row-index | `16` | `16 (Supp §S2)` |
| positional encoding | `16 (equations: Supp §S4)` | `16 (equations: Supp §S3)` |
| transformer, decoder, self-attention, causal mask | `17 (worked numbers: Supp §S5)` | `17 (worked numbers: Supp §S4)` |
| multi-head, residual, layer norm, feed-forward block | `17 (equations: Supp §S6)` | `17 (equations: Supp §S5)` |
| $O(k^2)$ context cost | `17 (derivation: Supp §S5)` | `17 (derivation: Supp §S4)` |
| logit, unembedding, weight tying | `18` | `18 (Supp §S6)` |
| softmax, temperature | `18` | `18 (limits and shift-invariance: Supp §S7)` |
| sampling: greedy, temperature, top-k, top-p; seed, PRNG | `19 (math: Supp §S7)` | `19 (math: Supp §S8)` |
| decoding loop, `<eos>`, halting | `20` | `20 (sequence factorization: Supp §S9)` |
| encoder (vs decoder), attention masks both ways | `Supp §S5a` | `Supp §S4a` |
| training math: cross-entropy gradient, backprop, SGD/minibatch | `Supp §S8 (uses slide-16-case-study loss)` | `Supp §S12 (uses the Case Study 1 loss)` |
| SFT, reward model, RLHF, DPO, RLVR, refusal direction | `Supp §S9` | `Supp §S13` |
| multimodal encoders | `Supp §S10` | `Supp §S14` |
| mixture-of-experts, KV cache | `Supp §S5/§S11 (beyond-scope boxes)` | `Supp §S4/§S15 (beyond-scope boxes)` |
| weights-vs-harness ledger | `Supp §S12` | `Supp §S16` |

One left-hand cell also changes (audit E-6 and E-3):

OLD
```
| transformer, decoder, self-attention, Q/K/V′, causal mask | ... |
| weights-vs-harness ledger for every slide-12/13 box | ... |
```
NEW
```
| transformer, decoder, self-attention, Q/K/V, causal mask | ... |
| weights-vs-harness ledger for every slide-11/12/13 box | ... |
```

### 99.2 — Citation status block — audit E-12

OLD
```
Citation status at time of writing: Vaswani 2017, Holtzman 2020 — verified in
`ai-training/references.md` ([V]). Cybenko 1989 and Hornik 1991 — verification pass
pending; see the Supplement's references block before the deck ships.
```
NEW
```
Citation status at time of writing: Vaswani 2017 and Holtzman 2020 — verified in
`ai-training/references.md` ([V]). Cybenko 1989 and Hornik 1991 — bibliographic records
confirmed 2026-08-27 and logged in the project's `REFERENCES.md`; the Supplement's
references block carries the full entries.
```

---

## §100 — Global find/replace, for verification after the itemised patches

Both are already covered entry by entry above. Run them as a check, not as a
substitute.

### 100.1 — Vocabulary symbol (audit E-6)

| find | replace | where |
|---|---|---|
| `|V|` | `|\mathcal{V}|` | slides 16, 18 |
| `\sum_{j\in V}` | `\sum_{j\in\mathcal{V}}` | slide 18 |
| `V'` | `V` | slide 17 only (the attention value matrix) |
| `vocabulary $V$` | `vocabulary $\mathcal{V}$` | front matter |

Do **not** rewrite the standalone `V` in `Q/K/V`, `W_V`, or `HW_V` — those are the value
matrix and are correct unprimed after this change.

### 100.2 — Superscript aliases (audit E-33)

Removed on: Weight, Bias, Activation Function, Hidden State, Width, Depth, Embedding,
Positional Encoding, Self-Attention, Residual + LayerNorm, Logit, Unembedding, Softmax,
Temperature.

Kept unchanged, because in each the alias supplies the formal term the headword lacks:
`Causal Mask^(Autoregressive Constraint)` (17), `Greedy^(argmax)` (19),
`Top-p^(Nucleus)` (19), `Seed^(PRNG State)` (19), `` `<eos>`^(End-of-Sequence) `` (20).
