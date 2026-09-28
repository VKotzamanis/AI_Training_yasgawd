## Neural network and learning are borrowed names for a search over numbers

\includegraphics[width=\linewidth]{01-what-training-changed.png}

\vspace{0.5em}

:::::::::::::: {.columns}
::: {.column width="32%"}
**Neural network**

layers of multiply-and-add, named after a biological analogy
:::
::: {.column width="32%"}
**Learning**

a search for values that lower the error
:::
::: {.column width="32%"}
**The brain comparison**

correlational; the appendix carries what it establishes
:::
::::::::::::::

\sourceline{Schrimpf, M., Blank, I.~A., Tuckute, G., et al., 2021. \emph{PNAS} 118(45):e2105646118 \quad Hadidi, N., Feghhi, E., Song, B.~H., Blank, I.~A. \& Kao, J.~C., 2026. \emph{Nature Communications} 17(1):5769}

## Softmax converts the scores into probabilities that add up to one

$$p_i \;=\; \frac{\exp\!\big(\overbrace{z_i}^{\text{score for token } i}\big/\underbrace{T}_{\text{temperature}}\big)}{\underbrace{\sum_j \exp(z_j/T)}_{\text{sum over every token, so the result adds to } 1}}$$

\vspace{0.3em}

:::::::::::::: {.columns}
::: {.column width="52%"}
\includegraphics[width=\linewidth]{01-softmax-T.png}
:::
::: {.column width="44%"}
**Worked case** — two tokens, scores 2.0 and 1.0, at $T=1$

$$p_1 = \frac{e^{2.0}}{e^{2.0}+e^{1.0}} = \frac{7.389}{7.389+2.718} = 0.731$$

All quantities dimensionless. $z$ and $T$ carry no units, and $p$ is a probability.
:::
::::::::::::::

\sourceline{No source. The equation is standard and the arithmetic is checked in \texttt{assets/figures/gen-figures.py}.}
