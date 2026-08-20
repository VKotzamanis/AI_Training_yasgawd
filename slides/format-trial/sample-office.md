## Neural network and learning are borrowed names for a search over numbers

![](01-what-training-changed.png)

**Neural network**

layers of multiply-and-add, named after a biological analogy

**Learning**

a search for values that lower the error

**The brain comparison**

correlational; the appendix carries what it establishes

Source: Schrimpf, M., Blank, I. A., Tuckute, G., et al., 2021. *PNAS* 118(45):e2105646118   Hadidi, N., Feghhi, E., Song, B. H., Blank, I. A.   Kao, J. C., 2026. *Nature Communications* 17(1):5769

## Softmax converts the scores into probabilities that add up to one

$$p_i \;=\; \frac{\exp\!\big(\overbrace{z_i}^{\text{score for token } i}\big/\underbrace{T}_{\text{temperature}}\big)}{\underbrace{\sum_j \exp(z_j/T)}_{\text{sum over every token, so the result adds to } 1}}$$

![](01-softmax-T.png)

**Worked case** — two tokens, scores 2.0 and 1.0, at $T=1$

$$p_1 = \frac{e^{2.0}}{e^{2.0}+e^{1.0}} = \frac{7.389}{7.389+2.718} = 0.731$$

All quantities dimensionless. $z$ and $T$ carry no units, and $p$ is a probability.

Source: No source. The equation is standard and the arithmetic is checked in \texttt{assets/figures/gen-figures.py}.
