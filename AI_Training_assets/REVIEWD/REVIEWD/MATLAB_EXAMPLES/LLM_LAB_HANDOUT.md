# LLM Lab — MATLAB Handout

A working language model in ~250 lines of base MATLAB. No toolboxes. Runs in GNU Octave.

Every number in this document was produced by running the code. Nothing is asserted from
memory or estimated. Where a result is uncertain or seed-dependent, it says so.

---

## Why this exists

The lecture argues that an LLM answers a maths question by **predicting tokens from corpus
statistics, not by computing**. That is easy to say and easy to disbelieve.

The lab is the proof. It implements exactly the equations on the slides, at a scale small
enough to inspect every number, and it fails in exactly the ways the lecture claims it will.

**It is a real language model.** Specifically, a neural n-gram language model (Bengio et al.,
2003): fixed context window, one-hot tokens, feed-forward layers, softmax over a vocabulary,
trained by next-token cross-entropy, decoded autoregressively.

- **Neural network** — yes, with `DEPTH ≥ 1`. At `DEPTH = 0` it is multinomial logistic
  regression, and should be called that.
- **Language model** — yes, unambiguously. A distribution over next tokens given previous
  tokens *is* the definition.
- **Large** — no. ~4,000 parameters against ~10¹¹.

**Identical to a production LLM:** the output stage (logits → softmax → categorical), the
training objective (next-token cross-entropy — this *is* the pretraining objective), the
residual (∂L/∂z = P − e_y), autoregressive decoding, learned embeddings, frozen weights at
inference.

**Absent:** attention — and therefore no induction heads, no content-based lookup, and **no
in-context learning**. Also no layer norm, no residual connections, no BPE, no scale, no
post-training, no sampling.

---

## The equations, and where they are in the code

| | equation | line in `llm_lab.m` |
|---|---|---|
| logits | z = W e + b | `Z = H*Ws{L} + Bs{L};` |
| distribution | P(v \| ctx) = e^{z_v} / Σ e^{z_j} | `E = exp(Zs); P = E ./ sum(E,2);` |
| loss | L(θ) = −(1/n) Σ log P(y_i \| ctx_i) | `Lh(t) = -sum(log(P(idx)))/n;` |
| residual | ∂L/∂z = P − e_y | `G = P; G(idx) = G(idx) - 1;` |
| update | θ ← θ − η∇L | `Ws{i} = Ws{i} - ETA*dW;` |

Six lines. That is the entire model — no branch on the value of x, no arithmetic unit,
nothing hidden. Showing them is what turns "trust me, it's just softmax and cross-entropy"
into something a room can verify at a glance.

`DEPTH = 0` reproduces `z = We + b` literally. `DEPTH > 0` inserts tanh layers.

---

## Files

| file | what it does | run it when |
|---|---|---|
| **`llm_lab.m`** | The instrument. Trains with a live four-panel figure, then drops into a prompt loop. | Demonstrating live |
| **`llm_lab_core.m`** | Headless engine. Same maths, returns accuracies. Called by the sweep. | Never directly |
| **`llm_lab_sweep.m`** | Runs experiments E1–E5, prints the result tables. Requires `llm_lab_core.m` on the path. | Reproducing the numbers below |
| **`llm_lab_compare.m`** | Capstone figure. Three rules side by side, with a whitelist-validated symbolic rule parser. | The closing slide |
| **`llm_lab_learn.m`** | Animates the learned character map and ŷ-vs-y during training. Free-text prompt at the end. | Showing *what* it learned |
| **`LLM_LAB_WORKSHEET.md`** | Student worksheet. Hypothesis before each run. | Assigning it |
| `superseded/` | Earlier drafts. **Do not use.** See "What didn't work". | Never |

### Parameters (top of `llm_lab.m`)

```matlab
RULE   = '2x+1';    % 'copy' 'reverse' 'x+7' '2x+1' '3x' 'x^2'
SPLIT  = 'parity';  % 'random' 'range' 'parity'
TOKENS = 'digit';   % 'digit' | 'word'
WIDTH  = 32;        % units per hidden layer
DEPTH  = 1;         % number of hidden layers (0 = the bare slide equation)
KMAX   = 6;         % context window, in tokens
NOISE  = 0.00;      % fraction of the corpus that violates the rule
ITER   = 8000;
ETA    = 0.5;
SEED   = 0;
```

**`WIDTH` is units per layer. `DEPTH` is number of layers.** They are different knobs with
different effects — a distinction the code makes and most explanations don't.

---

## The live figure in `llm_lab.m`

| panel | shows |
|---|---|
| top left | L(θ) vs t, train and held-out, **log-log** |
| top right | exact-match accuracy vs t, train and held-out |
| bottom left | P(v \| ctx) over the vocabulary, for a held-out probe |
| bottom right | **P − e_y** over the vocabulary — the residual |

The residual panel is the bridge to an engineering audience: `∂L/∂z = P − e_y` is *literally*
predicted minus target, the same object as (ŷ − y) in least squares, generalised from a
scalar to a distribution. It collapses toward zero on a learnable rule and stalls on one
that isn't.

Two implementation details worth knowing, because both were bugs before they were features:

- **The probe position is chosen by entropy.** Output position 1 is the most significant
  digit, which is `'0'` for every x below 50 — probing it shows a flat line. The script now
  computes the entropy of each output position across the corpus and probes the highest.
- **Checkpoints are log-spaced.** Training converges by t ≈ 180 of 8000. Linear checkpoints
  gave two data points joined by a straight line.

`ETA` controls the viewing window: 0.5 → L < 0.05 at t = 180; 0.1 → t = 897; 0.03 → t = 2987.

---

## Verified results

Parity split (train where tens + ones is even), mean of 3 seeds unless stated.

### E1 — tokenisation sets the ceiling

| TOKENS | \|θ\| | seen | held out |
|---|---|---|---|
| word (one token per number) | 34,232 | 100% | **0.0%** |
| digit / character | 2,957 | 100% | **100%** |

Ten times the parameters, zero generalisation. An unseen prompt's column of W receives
**zero gradient**. This is structural, not a training failure.

### E2 — rule difficulty, with per-token accuracy

| rule | held out | most-significant → least |
|---|---|---|
| copy | 100.0 | 100 / 100 |
| reverse digits | 100.0 | 100 / 100 |
| 2x+1 | 100.0 | 100 / 100 / 100 |
| x+7 | 10.7 | 95 / **37** / 55 |
| 3x | 9.3 | 87 / **15** / 87 |
| x² | 3.3 | 53 / 18 / 29 / 46 |

The ones digit is always near-perfect — a digit-local map. **All failure lives in the tens
digit**, which is where the carry is.

**Model difficulty is unrelated to human difficulty.** Reversing digits is annoying for a
person and free for the model; adding 7 is the reverse.

**Mechanism, verified.** On the parity split the carry bit and the parity of the tens digit
are *correlated in training*. The model learns the correlate, not the carry. On test the
correlation flips. That is a **confounded variable**, demonstrated in a system where ground
truth is fully controlled — the most transferable result in the lab for an engineering
audience.

### E3 — the split decides the verdict

| rule | random | range | parity |
|---|---|---|---|
| 2x+1 | 100.0 | 80.0 | 100.0 |
| x+7 | **66.7** | 0.0 | **10.7** |
| 3x | 35.1 | 0.0 | 9.3 |

Same model, same training, **56 points apart** on x+7.

Audited: **zero** unseen output classes in any structured split, so the collapse is genuine,
not a labelling artefact. A random split measures interpolation — every digit still appears
in training — and overstates generalisation badly.

### E4 — scale does not rescue a bad representation

x+7, parity, held-out:

| | depth 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| width 8 | 4.0 | 16.0 | 14.7 | 10.0 |
| width 32 | 4.0 | 10.7 | 9.3 | 14.0 |
| width 128 | 4.0 | 5.3 | 6.7 | 12.0 |

The **depth-0 column is identical across all widths** — correctly, since width does nothing
without a hidden layer. Good comprehension check for students.

Best cell in the grid: 16%. Iterations 12k / 40k / 120k all give **exactly 2.0%** — training
longer changes nothing to three significant figures.

**Depth beats width per parameter:** width 32 / depth 3 (5,069 params) reaches 14.0%;
width 512 / depth 1 (~130,000 params) reaches 12.7%. **26× fewer parameters.** That is a
one-line answer to "why are transformers deep rather than just wide."

### E5 — corpus reliability

| NOISE | seen | held out |
|---|---|---|
| 0.00 | 100.0 | 100.0 |
| 0.20 | 84.4 | 86.7 |
| 0.40 | 66.0 | 70.0 |

**L(θ) reaches ~0.0009 at every noise level, including 0.40.** The model drives training loss
to zero on a corpus that contradicts the rule 40% of the time.

*Training loss says nothing about correctness.*

(The corruption is deterministic per prompt, so the model memorises the wrong label. To get a
genuine entropy floor you would need repeated prompts with stochastic labels — see
`superseded/llm_toy_demo.m`, which does exactly that.)

### The capstone — `llm_lab_compare.m`

| rule | L_train | L_held | held out | x = 50 → | true |
|---|---|---|---|---|---|
| 2x+1 | 0.0004 | 0.0006 | **100%** | 101 | 101 |
| ln(x) | 0.0016 | **4.147** | **0%** | **4.078** | 3.912 |
| √x | 0.0018 | **5.005** | **0%** | **7.446** | 7.071 |
| x²+2x−1 | 0.0020 | 2.229 | 2% | 3559 | 2599 |

**The three training curves are indistinguishable.** 0.0004, 0.0016, 0.0018 — all flatlined,
all looking like textbook convergence.

ln|V| = **2.708**. The held-out loss for ln(x) and √x is **above the uniform-guess line** —
worse than a fair 15-sided die, because confident wrongness costs more than uncertainty. On
log-log axes you watch the curves cross it at t ≈ 300.

**`ln(50) → 4.078`** against a true 3.912 is the single best artefact in the deck: correctly
formatted, correctly signed, right magnitude, four plausible digits, wrong. It never declines
and never hedges.

**Why 2x+1 works and ln(x) doesn't** is **token locality**, not domain size. Retrained on
x ∈ 1…999 with three input digits, 2x+1 still scores 100% held-out. Each digit of 2x+1 depends
on a bounded window of input digits plus a carry. Each digit of ln(x) depends on the whole
input — ln(49) = 3.892, ln(50) = 3.912, ln(51) = 3.932 share no positional structure with
the input.

### `llm_lab_learn.m` — what the model actually learned

Character map, P(final character | input ones digit), on 2x+1:

| t | argmax per row | correct | mean max-prob |
|---|---|---|---|
| 1 | `1111111111` | 2/10 | 0.075 |
| 50 | `1357913579` | **10/10** | 0.592 |
| 8000 | `1357913579` | 10/10 | 1.000 |
| **true** | `1357913579` | | |

**The map is fully correct by step 50.** The remaining 7,950 steps only sharpen confidence
from 0.59 to 1.00. And the learned row is exactly (2d+1) mod 10, including the two-to-one
collision where inputs 0 and 5 both map to 1.

It found a **character map**, not a calculation.

### Out-of-vocabulary — feed it a word

With letters added to the vocabulary but never appearing in the corpus, their weight rows
receive **identically zero gradient** and stay at initialisation forever:

```
seed 0 : family -> 189    cat -> 135    dog -> 151
seed 1 : family -> 049    cat -> 1<eos>7 dog -> 179
seed 3 : family -> 167    cat -> 155    dog -> 155
```

**The value is not predictable.** The obvious hypothesis was tested and falsified: `l` and `y`
are nearest to digits `0` and `3` by cosine, but the model on `03` returns 007 while `ly`
returns 161. The cosines are only 0.2–0.3 — random high-dimensional vectors are near-orthogonal.

**The shape is predictable, absolutely.** 200 random letter strings; of the 122 producing a
clean 3-digit number:

- last digit odd: **122/122** — distribution `1:42, 3:15, 5:38, 7:15, 9:12`, and `0,2,4,6,8`
  **never once**
- first digit in {0,1}: **122/122**
- value inside the training range 3…199: **122/122**

> **The learned structure determines the form of the error. The untrained noise determines
> its value.**

This is why LLM errors are dangerous rather than merely wrong: they are
**constraint-satisfying**. A fabricated citation has the right author count, a plausible
journal, a valid-looking DOI, a year in range. An error that violated the format would be
caught instantly. These don't.

This is a controlled reproduction of the **glitch-token** phenomenon (SolidGoldMagikarp) at
10⁻⁷ scale — with the tokenizer/corpus mismatch created deliberately in one line instead of
arising by accident.

### `<eos>` and the decoder

`<eos>` is an ordinary token. **The model cannot stop** — it emits a distribution, and the
*decoding loop*, code outside the network, decides whether to halt.

The scripts generate a fixed number of characters and ignore `<eos>`. Adding the `break`
changes the story:

| decoder | result on 200 random words |
|---|---|
| fixed 3 characters | 122/200 clean 3-digit numbers |
| stops at `<eos>` | 122 full numbers, **73 single-character, 5 empty** |

**The fixed-length decoder was manufacturing plausible output.** The model was signalling
"nothing more to say" after one character and the loop discarded it. Whether you see a
model's distress signal depends on code written outside the model.

### Seeds

`rng(SEED)` controls three things and **not** stochastic training — training is full-batch
deterministic, so the same seed gives a bit-identical run.

1. weight initialisation
2. `randperm` for the split, only when `SPLIT = 'random'`
3. `rand` for corruption, only when `NOISE > 0`

Whether it matters depends on convexity:

| | seed 0 | seed 1 | seed 2 |
|---|---|---|---|
| DEPTH = 0 (convex) | L = 0.022528 | 0.022499 | 0.022506 |
| DEPTH = 1 (non-convex) | 0.000821 | 0.000837 | 0.000836 |

At DEPTH 0 the loss is convex — multinomial logistic with logits linear in θ — so any
starting point reaches the same minimum. That agreement is guaranteed, not luck.

### Training is not the bottleneck — proved, not asserted

For the lookup model the loss is convex and the minimiser is known in closed form,
P*(y|x) = C(y,x)/n_x:

```
gradient descent, 6000 steps : L = 0.375549
closed-form GLOBAL minimum   : L = 0.373699
gap                          :     1.85e-03
```

The optimiser is already at the bottom. More epochs, Adam, a tuned learning rate, ten times
the data — none of it moves the number. **The architecture is the constraint.**

Strongest framing available: *this model is optimal and still gets it wrong.*

---

## What didn't work — do not repeat

- **MSE loss on a token task.** Breaks the moment the corpus contains ("London", 2). You
  cannot subtract a word from a number. This is what forced the move to cross-entropy over
  discrete tokens, and it is the most important design decision in the lab.
- **`ŷ = P(x_{k+1} | x_{1:k}; θ)`.** Dimensionally invalid — ŷ is a token, P is a number.
  Two lines: the model outputs P(·|x); the token is argmax.
- **Parallel output heads.** All digits emitted simultaneously. Not what LLMs do, and it
  structurally cannot produce a wrong-length answer or show error propagation. Replaced with
  genuine autoregressive decoding.
- **Random train/test splits as evidence of generalisation.** Measures interpolation only.
  Overstates by up to 56 points.
- **Single-seed capacity numbers.** d=8 read 84.2% on one seed and 94.7% on another.
  Indefensible on a slide. Average over replicates.
- **Quoting numbers from the parallel-head engine.** The autoregressive rebuild changed them
  (2x+1 on the range split went from ~1% to 80%). Only use numbers from this document.
- **Deterministic per-prompt corpus noise to show an entropy floor.** It doesn't produce one —
  the model memorises the corrupted label.

The three files in `superseded/` are those earlier drafts. They are kept only because
`llm_toy_demo.m` contains the closed-form convexity proof and the stochastic-noise corpus that
does produce a real entropy floor (H = 0.3737, reached to 0.3755). Nothing else in that
folder should be shown.

---

## Claims you can defend, and two you cannot

**Defensible:**
- "This is the training objective and output mechanism of an LLM at 10⁻⁷ scale, without attention."
- "Tokenisation determines what is representable." — E1, 0% vs 100%
- "Training loss falling to zero is not evidence of correctness." — E5 and the capstone
- "Your test split determines what your validation actually validates." — E3, 56 points
- "The model learned the shape of the answer, not the quantity." — 122/122 odd last digits

**Not defensible, and someone will try:**
- *"This is how GPT works."* No attention, no scale.
- *"This proves LLMs can't do arithmetic."* Real models with attention generalise arithmetic
  considerably better, and production systems route it to a tool. This failure is *this
  architecture's* failure.

Safe form for a slide:

> Token prediction is a poor substrate for computation. This model shows the mechanism at a
> scale you can inspect. The failure mode it produces — a confidently formatted, plausible,
> wrong number with no signal of uncertainty — is the same failure mode observed in
> production systems.

---

## Before you present

1. **Run each worksheet cell yourself.** Which x values fail differs by machine — MATLAB's RNG
   is not NumPy's. Have two or three failing values in your pocket rather than fishing live.
2. **`SPLIT = 'random'` first, then `'parity'`.** Act one: it works. Act two: change one word,
   watch it collapse. Same model, same optimiser, same loss.
3. **Octave compatibility** was checked by static audit, not by execution — no Octave was
   available in the environment where these were written. If you plan to run Octave, test once
   beforehand. All known hazards were removed (`yline`, `xticks`, `sgtitle`, `drawnow limitrate`,
   `histc`, `uistack`).
