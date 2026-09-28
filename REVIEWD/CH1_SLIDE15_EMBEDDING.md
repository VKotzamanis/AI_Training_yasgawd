# Slide 15 — Neural Network: Embedding & Hidden State

Rebuilt 2026-09-10 after the first draft was rejected: confusing, and no technical content.

**Structure, applied to every block on this slide:** scientific term first → plain explanation
in the register Cohen uses → the graphic or live demo that makes it move.

**Every number on this slide is GPT-2 small and was verified locally**, not taken from a
secondary source: `tiktoken.get_encoding("gpt2")` gives `n_vocab = 50257`, `" apple" = 17180`,
`" pear" = 25286`, `" spaceship" = 40663`. Config `n_layer = 12`, `n_embd = 768`,
`n_positions = 1024` confirmed against HuggingFace's GPT-2 docs. GPT-2 is the teaching model
because the audience can download it and reproduce every figure here.

---

## Message

The model never computes with a token. It computes with one 768-number vector per token —
created by a table lookup, then rewritten by every block, until it stops describing the token
it came from and starts describing the token that comes next.

## Pipeline position

`token ID → [ EMBEDDING ] → N decoder blocks → logits → probability → sampled token`

## Framing line (italic, top)

*Slide 14 gave one neuron and called its input the activation vector, **x**. Here is where the
first **x** comes from, and what happens to it afterwards.*

---

# Block 1 — Embedding Matrix

### Term

**Embedding Matrix**, `E ∈ ℝ^(|𝒱| × d_model)`. In GPT-2 small this is the layer named `wte`
(word token embeddings), shape **50,257 × 768**.
**In:** one token ID, an integer. **Out:** one vector of **768** floating-point numbers.

$$\mathbf{e}_{v} = \text{row } v \text{ of } E, \qquad E \in \mathbb{R}^{50257 \times 768}$$

### Explanation

Tokenization handed you one integer per token. One integer cannot hold a relationship. In
GPT-2, `" apple"` is **17180** and `" pear"` is **25286**. Those two numbers know nothing about
fruit, and their difference — 8,106 — means nothing at all. `" spaceship"` is **40663**, which
is *closer* to `" pear"` than `" apple"` is.

The embedding matrix throws the arithmetic away. The token ID has exactly one job left: pick a
row. What comes back is 768 numbers, and those 768 numbers are the only thing the rest of the
model will ever see.

The table is not small. `50,257 × 768 = 38,597,376` parameters — roughly a third of GPT-2
small — and every one of them was learned by gradient descent alongside every other weight.
Nothing about the embedding table is privileged. It starts as random numbers like everything
else.

### Graphic / demo

**Figure A — the whole matrix as a heatmap.** Tokens across, the 768 dimensions down, colour =
coordinate value. Horizontal stripes are visible: some dimensions sit positive for nearly every
token in the vocabulary.

**Live:** cosine similarity between rows. `" apple"` vs `" pear"` against `" apple"` vs
`" spaceship"`. The participant picks two words and reads one number between −1 and +1.

---

# Block 2 — Positional Encoding

### Term

**Positional Encoding**, `p_i`. In GPT-2 a *second* learned table named `wpe` (word position
embeddings), shape **1024 × 768** — indexed by position instead of by token.
**In:** the position index. **Out:** one vector of 768 floats.

$$\mathbf{h}_i^{(0)} = \underbrace{\texttt{wte}[\,x_i\,]}_{\text{which token}} \;+\; \underbrace{\texttt{wpe}[\,i\,]}_{\text{which slot}}$$

`1024 × 768 = 786,432` parameters. The 1024 is GPT-2's context limit: there is no row for
position 1025, which is the whole reason the model has a maximum context length.

### Explanation

The row lookup is blind to where the token sits. Feed the model *"load causes deflection"* and
*"deflection causes load"* and the same three rows come back both times, in a different order.

That would be survivable if anything downstream could see the order. Nothing can. Attention —
the next slide — sums over positions with learned weights, and a sum does not care what order
you add things in. Reorder the inputs and you get the same outputs, reordered: the property is
called **permutation equivariance**.

So position is not metadata bolted onto the vector. It is *added into* the vector, before the
first block runs, because the numbers are all there is.

### Graphic / demo

**Figure B — the reversal test.** Both sentences, their three rows, and the resulting sums, in
two columns. A switch marked `wpe: on / off`. With it off, the two columns are identical and the
page says so with a computed check, not a caption. With it on, they differ, and by how much.

---

# Block 3 — Hidden State

### Term

**Hidden State**, `h^(ℓ)` — the activation vector at layer ℓ. Ask GPT-2 small for its hidden
states and you get **13** tensors, not 12: `h^(0)` is the embedding, then one per transformer
block. Each is `[batch × tokens × 768]`.
**In:** `h^(ℓ−1)`, 768 numbers. **Out:** `h^(ℓ)`, 768 numbers.

$$\mathbf{h}^{(\ell)} = \mathbf{h}^{(\ell-1)} + \Delta^{(\ell)}, \qquad \ell = 1,\dots,12$$

### Explanation

It is the same vector. This is the part that gets taught badly: the hidden state is not a new
object the network builds, it is the embedding vector after something has been added to it. No
block replaces the vector — each one computes a small correction and adds it on.

In GPT-2 the vector is adjusted **four times per block**: two normalizations, one attention
output, one MLP output. Twelve blocks, 48 adjustments, and the width never moves — 768 in, 768
out, from the tokenizer to the logits.

What changes is what the vector *describes*. At layer 0 it describes the token it came from. At
layer 12 it describes the token the model predicts comes next. That swap is the entire job of
the stack, and it is why a model with the embedding wired straight to the unembedding would do
nothing but return its own input.

Two consequences worth saying out loud:

- **The vector drifts; it does not lurch.** Cosine similarity between one token's hidden state
  at different layers stays above roughly **0.8** all the way through. Every block is a nudge.
- **Same weights and same preceding tokens give the same 768 numbers, every time.** No random
  draw happens anywhere in the stack. Regeneration variance comes later, at sampling.

### Graphic / demo

**Figure C — a 13 × 13 cosine-similarity matrix** for one token, layer against layer. Bright
diagonal, values falling smoothly with layer distance, floor around 0.8. Read the colour bar
aloud — the drift looks dramatic until you see the scale starts at 0.8.

**Live demo — the interpolation experiment** (adapted from Cohen's; ours is on-domain):

> `The beam is made of ___`

Take the embedding row for `" steel"` and the row for `" concrete"` and mix them:
`v = p·wte[" steel"] + (1−p)·wte[" concrete"]`. Sweep `p` from 0 to 1 and plot the output
probability of the tokens that follow. The prediction moves *smoothly* between them.

That is the payoff of the whole slide: the embedding is a **position in a space**, not a label
in a lookup, and you can stand between two words. Requires a real pretrained model — Python, not
the MATLAB lab. Pre-render it if the room has no GPU.

---

## Closing line

Every block from here on is one way of computing that small correction, `Δ^(ℓ)`. The next slide
is the first of them: attention.

---

## Speaker notes

**Why GPT-2.** It is open, it is 124 M parameters, and the audience can reproduce every number
on this slide on a laptop. Frontier models are the same shape and wider. Do not quote a width
for a closed model — the numbers are not published.

**The myth, if someone raises it.** "king − man + woman = queen" is not a real property of
embedding spaces; it holds for a small number of hand-picked pairs and does not generalise.
Cohen has a full post arguing this. **I have not verified the underlying critique yet** — do not
put it on the slide until I have.

**Slide 14 wording.** Slide 14 says the vector updates "every time it passes through a neuron".
Strictly it updates every time it passes through a *layer*; a neuron returns one number, which
becomes one coordinate. Say it that way if asked — it reinforces slide 14 rather than
contradicting it. Your call whether to change the slide; I have not.

**Do not call `e` a "static embedding".** The first draft did. It fights slide 14, which already
says the vector gets updated, and it fights this slide's whole argument. The vector is dynamic
from block 1 onward.

**Numbers to recompute if you change models.** 50,257 · 768 = 38,597,376. 1024 · 768 = 786,432.
Both are arithmetic, not citations — redo them, don't carry them.

---

## Sources

- GPT-2 token IDs and vocabulary size: `tiktoken` 0.14.0, `get_encoding("gpt2")`, executed
  locally 2026-09-10. Primary — the encoder's own output.
- GPT-2 architecture (`n_layer`, `n_embd`, `n_positions`, `wte`, `wpe`): HuggingFace transformers
  GPT-2 documentation.
- Explanatory structure, the four-adjustments-per-block count, the ~0.8 cosine floor, and the
  embedding-interpolation experiment: Mike X Cohen, *Dissecting LLMs with ML*, posts 3/6
  (Embeddings) and 4/6 (Transformer outputs). Studied for method; all prose here is original and
  all numbers were re-derived or independently confirmed. **Credit him on the deck's credits
  slide.**
