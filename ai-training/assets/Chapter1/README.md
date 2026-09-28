# Chapter 1 — per-slide assets
One folder per slide. Each contains the rendered slide and the source figures used on it.
Figures with no file are drawn in LaTeX (TikZ) and exist only as part of the rendered slide.

| Slide | Title | Source figures |
|---|---|---|
| 01 | Title page | — |
| 02 | The answer arrives a piece at a time | — |
| 03 | Language models are one branch of AI | 01-what-is-ai.png |
| 04 | Reliability follows how much was written | 01-corpus-density.png |
| 05 | A model is numbers plus a program | 01-model-artefact.png |
| 06 | Training set those numbers and then stopped | 01-train-vs-run.png |
| 07 | Training searches for the smallest total error | 01-fitting.png |
| 08 | Training changed the numbers, nothing else | 01-what-training-changed.png |
| 09 | Text becomes numbers, then scores, then text | TikZ |
| 10 | Tokens come from a fixed list | 01-tokens.png |
| 11 | Token count follows frequency, not length | 01-token-cost.png |
| 12 | Training minimises surprise at the next token | 01-surprise.png |
| 13 | The network returns one score per token | 01-logits.png |
| 14 | Attention decides which earlier tokens matter | 01-attention.png |
| 15 | Softmax turns scores into probabilities | — |
| 16 | Always taking the top token repeats | — |
| 17 | The token is drawn, not taken | 01-scores.png |
| 18 | Temperature sets how sharply the top score wins | 01-temperature.png, 01-softmax-T.png |
| 19 | Each token is appended and everything reruns | 01-loop.png |
| 20 | Everything given sits in the context window | TikZ |
| 21 | The session ends and the window goes | 01-persistence.png |
| 22 | Your brain divides the work into parts | 01-brain-human.png |
| 23 | One set of weights does every job | 01-brain-model.png |
| 24 | What we covered, and what is still open | — |
