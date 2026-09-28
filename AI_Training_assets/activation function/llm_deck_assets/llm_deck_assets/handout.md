# How Large Language Models Work — Session Handout

## Project Goal

Build an educational PowerPoint deck that explains, sequentially and defensibly,
how modern large language models process text. The deck is aimed at an
engineering-literate audience (graduate level) and must withstand technical
cross-examination. Every claim should be traceable to a verifiable source or
reproducible computation.

The presentation covers tokens, embeddings, activation functions, attention,
and output prediction. This session produced the assets for the first three
topics.


## Slides Produced So Far

| Slide | Title | Status |
|-------|-------|--------|
| 1 | What Is a Token? (1/3) | Done (user's own) |
| 2 | Token ID ≠ Token Count | Done (user's own) |
| 3 | Token ID → Row ID in the Embedding Matrix | Figures produced this session |
| 4 | Embedding Geometry Before and After Training | Figure produced this session |
| 5 | The Nonlinear Activation Function | Figures produced this session |
| 6+ | Attention, output head, generation | Not yet started |


## Assets Delivered

### Scripts (Python, all self-contained)

| File | What it produces | Dependencies |
|------|-----------------|--------------|
| `fig1_token_to_row.py` | Fig 1: token ID → embedding row → input tensor | matplotlib, numpy |
| `fig2_embedding_geometry.py` | Fig 2: PCA of GloVe embeddings, random vs trained | matplotlib, numpy, scipy, gensim |
| `activation_comparison.py` | Fig 3–4: three activation strategies × three targets | matplotlib, numpy, torch |

Each script writes PNG (300–600 dpi), SVG, and PDF to the working directory.
Insert SVG into PowerPoint for vector-quality scaling.

### Figures

| Figure | File stem | Format |
|--------|-----------|--------|
| Token ID to embedding row lookup | `fig1_token_to_row` | png, svg, pdf |
| Embedding geometry (random vs trained) | `fig2_embedding_geometry` | png, svg, pdf |
| 3×3 activation comparison grid | `activation_comparison` | png, svg, pdf |
| Learned B-spline activation shapes | `learned_activations` | png, svg, pdf |


## Key Decisions and Their Justifications

### 1. Token IDs come from o200k_base (V = 200,019)

The IDs on slides 1–2 (32362, 81, 14409 for " stirrups") were verified against
OpenAI's `o200k_base` tokenizer using the `tiktoken` library. The embedding
matrix dimensions in Figure 1 use V = 200,019 to match. Do not mix these IDs
with Llama 3's vocabulary (V = 128,256) or its parameter counts.

### 2. GloVe vectors as a stand-in for LLM embeddings

Figure 2 uses GloVe-100 (Pennington et al., 2014; 6-billion-token corpus)
because it is small enough to download, inspect, and plot. The geometric claim
(similar tokens cluster after training) holds in both GloVe and LLM embedding
matrices. If challenged, state that GloVe is a real embedding matrix trained on
a simpler objective, not a simulation.

### 3. "Columns do not mean smell or texture"

The claim that individual columns of the embedding matrix encode human-readable
features (smell, texture, etc.) is a teaching myth from popular videos.
Individual coordinate axes are arbitrary; meaning sits in directions that mix
all d coordinates (the linear representation hypothesis). We avoided labelling
axes in Figure 2 for this reason.

### 4. Cosine similarity between "stir" and "stirrups" is −0.07

Measured in the full 100-dimensional GloVe space. Random 100-d vectors have
expected cosine 0 with standard deviation ≈ 0.1, so −0.07 is statistically
indistinguishable from an unrelated pair. This quantifies the claim on slide 1:
tokenizer fragmentation destroys word-level semantics at the embedding level.

### 5. Activation function comparison: polynomial vs B-spline

The first implementation used degree-5 polynomial activations inside an MLP.
This produced a misleading result (fixed ReLU outperformed learnable
activations on all targets) because global polynomials suffer from Runge-type
instability. The corrected implementation uses locally-supported B-spline basis
functions, which match the KAN literature's approach. Corrected results:

| Target       | Fixed ReLU (61 params) | PReLU (81) | B-Spline (321) |
|-------------|----------------------|-----------|---------------|
| Smooth       | 2.3e-4               | 1.9e-4    | 8.0e-6        |
| Piecewise    | 2.2e-4               | 1.7e-4    | 2.9e-4        |
| Oscillatory  | 1.1e-3               | 5.2e-4    | 1.6e-6        |

B-spline activations win on smooth and oscillatory targets; ReLU wins on
piecewise-linear targets (which are in ReLU's native function class). Production
LLMs still use fixed activations because the parameter cost of learnable
activations at billions-of-neurons scale is prohibitive, not because they are
less expressive.


## Glossary of Terms (Slide-Ready Definitions)

### From the Token and Embedding Slides

**Token ID** (t_i): The integer index assigned to a token by the tokenizer,
bounded by the vocabulary, t_i ∈ {0, …, V−1}. It is an address, not a
magnitude. (Hint: Bookkeeping → Row Number.)

**Vocabulary Size** (V): The total number of distinct tokens the tokenizer can
emit; fixed when the tokenizer is trained, before the model exists.
(e.g., V = 200,019 for o200k_base, V = 128,256 for Llama 3.)

**Model Width** (d, also d_model or embedding dimension): The number of values
used to represent a single token, and the width of every tensor flowing through
the network. An architectural choice, not a learned quantity.
(e.g., d = 4,096 in Llama-3-8B.)

**Sequence Length** (n): The number of tokens in the current prompt. The only
quantity in Figure 1 that changes between queries; bounded above by the context
window.

**Embedding Matrix** (E ∈ R^{V×d}): The learned parameter block mapping each
token ID to a vector, one row per vocabulary entry. It is a weight matrix, set
during training, and the only one the model reads by address rather than by
multiplication. (Hint: Lookup Table = First Layer's Weights.)

**One-Hot Matrix** (T ∈ {0,1}^{n×V}, also indicator or selection matrix): A
matrix of zeros with a single 1 per row, marking which vocabulary entry each
position holds, T_{ij} = 1 if j = t_i. Carries no information of its own and
is never materialised in memory.

**Embedding Lookup** (X = TE, equivalently X_{ik} = E_{t_i,k}): The operation
retrieving one row of E per token. Formally a matrix product; computationally a
memory copy, since all but one term per row is multiplied by zero.

**Token Embedding** (x_i = E[t_i,:] ∈ R^d): The vector representing a single
token before any context is applied. Identical for every occurrence of that
token, at every position, in every prompt.

**Input Tensor** (X ∈ R^{n×d}): The stack of n token embeddings, and the object
entering layer 1 of the network. An activation, not a parameter (recomputed for
every prompt and discarded afterwards, unlike E).

### From the Embedding Geometry Slide

**Initialisation** (E_{jk} ~ N(0, σ²), typically σ ≈ 0.02): The random values
assigned to E before training. No row carries meaning at this stage; geometry
emerges from training, not from design.

**Sparse Gradient** (∂L/∂E nonzero only in rows {t_i}): Only the rows of
tokens present in a training batch receive an update, since the one-hot
structure zeroes the rest. (Hint: Corpus Frequency → Update Count → Row Quality.)

**GloVe** (Global Vectors for Word Representation): Publicly released word
vectors from Stanford, fitted so that vector dot products reproduce how often
words co-occur across a 6-billion-word corpus. Used in Figure 2 as a small,
inspectable stand-in for an LLM's E.

**Principal Component Analysis** (PCA; X_c = USV^T): A rotation of the data
onto the orthogonal directions of greatest variance, used to project
d-dimensional vectors down to two plottable ones. PC 1 is the direction of
largest spread, PC 2 the largest direction perpendicular to it.

**Explained Variance** (λ_k / Σ λ_j, reported as %): The share of total
scatter captured by a given principal component. Low and flat indicates no
dominant structure; concentrated indicates learned structure.

**Cosine Similarity** (cos θ = a^T b / (||a|| ||b||) ∈ [−1,1]): The
angle-based measure of alignment between two embeddings, computed in the full
d-dimensional space, not on the projection.

### From the Activation Function Slides

**Pre-Activation Value** (u = w^T x + b): The dot product of one neuron's
weight vector with its input, plus bias. A single scalar asking one yes/no
question of the input.

**Activation Function** (φ): A fixed, nonlinear, scalar function applied to u.
It decides how much of u to pass through. Common forms:
  ReLU:  φ(u) = max(0, u)
  SiLU:  φ(u) = u / (1 + e^{-u})
  GeLU:  φ(u) ≈ 0.5 u (1 + tanh[√(2/π) (u + 0.044715 u³)])

**Width** (m neurons per layer): How many questions a single layer asks of its
input in parallel. Each row of W is a different question.
(e.g., m = 14,336 in Llama-3-8B's FFN.)

**Depth** (L layers): How many times the network refines its answer. Each layer
sees the previous layer's answers, not the raw input. Depth is useful only
because φ prevents layers from collapsing into one.

**Collapse Proof**: Without φ (i.e., φ(u) = u), any number of layers reduces
to a single linear map: h_L = (W_L … W_1) x + bias. Every parameter beyond the
first layer is wasted. The activation function makes depth worth paying for.

**Black Box**: Not secrecy. Every weight is in the file, every activation
function is on a napkin. The opacity is that understanding the parts does not
give understanding of the whole: 8 billion weights composed through 32
nonlinear steps produce behaviour no human can trace from input to output. The
field of mechanistic interpretability exists to close this gap and remains an
open research problem.


## What Comes Next

| Topic | Key question it answers |
|-------|------------------------|
| Positional encoding (RoPE) | How does the model know word order? |
| Self-attention | How do tokens communicate with each other? |
| Feed-forward network | Where does 70% of the computation happen? |
| Layer norm / residual stream | How does information flow without degrading? |
| Output head + softmax | How does a vector become a probability over words? |
| Sampling (temperature, top-p) | How does the model choose one word from the distribution? |


## Reproducibility Notes

- All scripts use fixed random seeds (torch.manual_seed(42), np.random.seed(42))
- Font: scripts request Times New Roman first; fall back to Liberation Serif
  (metrically identical) if TNR is not installed
- Token IDs verified with tiktoken (pip install tiktoken)
- GloVe vectors: gensim downloads glove-wiki-gigaword-100 (~128 MB)
- PyTorch required for activation_comparison.py (CPU-only is sufficient)
