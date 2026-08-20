#!/usr/bin/env python3
"""Figures for the deck. Run: python3 assets/figures/gen-figures.py

Every figure here is computed, not drawn. Where a figure needs input values that
are not measured, they are labelled illustrative on the figure itself and the
*transform* applied to them is exact. Nothing is traced from a source figure.
"""
import matplotlib
matplotlib.use("Agg")               # headless; no display on the build machine
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent
# Slidev serves images from slides/public/. Canonical copy stays in assets/figures/;
# the build copy is derived and gitignored, so there is one source of truth.
PUB = Path(__file__).parents[2] / "slides" / "public" / "figures"
PUB.mkdir(parents=True, exist_ok=True)
INK, GRID = "#14201F", "#C8D2D2"
ACCENT = ["#0E5C68", "#3F7C87", "#7BA6AE", "#B4CBD0"]

plt.rcParams.update({
    "font.size": 11, "axes.edgecolor": INK, "axes.labelcolor": INK,
    "text.color": INK, "xtick.color": INK, "ytick.color": INK,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": "white", "axes.facecolor": "white",
})


def softmax(z, T):
    """Softmax with temperature. p_i = exp(z_i/T) / sum_j exp(z_j/T).

    Identical in form to the Boltzmann distribution p_i = exp(-E_i/kT)/Z under
    the identification z_i = -E_i/k_B. Dimensionless throughout: logits z are
    dimensionless, T is dimensionless, p is a probability.
    """
    z = np.asarray(z, dtype=float)
    e = np.exp((z - z.max()) / T)   # shift for numerical stability; exact
    return e / e.sum()


def fig_temperature():
    """One logit vector, four temperatures. The logits are illustrative; the
    softmax applied to them is exact."""
    labels = ["the", "a", "this", "each", "any", "such", "one", "its"]
    logits = [4.2, 3.6, 2.9, 2.1, 1.7, 1.0, 0.4, -0.3]   # illustrative
    temps = [0.2, 0.7, 1.0, 1.8]

    fig, axes = plt.subplots(1, 4, figsize=(11.5, 2.9), sharey=True)
    x = np.arange(len(labels))
    for ax, T, c in zip(axes, temps, ACCENT):
        p = softmax(logits, T)
        ax.bar(x, p, color=c, edgecolor=INK, linewidth=.6)
        ax.set_title(f"T = {T}", fontsize=12, pad=8)
        ax.set_xticks(x)
        ax.set_xticklabels(labels, rotation=60, ha="right", fontsize=8.5)
        ax.set_ylim(0, 1.0)
        ax.yaxis.grid(True, color=GRID, linewidth=.6)
        ax.set_axisbelow(True)
        ax.text(.97, .93, f"max {p.max():.2f}", transform=ax.transAxes,
                ha="right", va="top", fontsize=8.5, color=INK, alpha=.75)
    axes[0].set_ylabel("probability")
    fig.suptitle("One set of logits, four temperatures  —  logits illustrative, softmax exact",
                 fontsize=10.5, y=1.06, color=INK)
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-temperature.png", dpi=200, bbox_inches="tight")
    plt.close(fig)                  # 16 GB machine; close every figure
    print("wrote 01-temperature.png")


def fig_kv_growth():
    """Weight memory is constant in context length; KV memory is linear in it.
    Plotted in units of the weight term, so no model-specific byte count is
    invented. The linearity, not the slope, is the claim."""
    L = np.linspace(0, 200_000, 500)          # context length, tokens
    weights = np.ones_like(L)                 # normalised: weight term = 1
    slopes = [1 / 50_000, 1 / 100_000, 1 / 200_000]   # KV per token, relative

    fig, ax = plt.subplots(figsize=(7.2, 3.9))
    ax.plot(L, weights, color=INK, lw=2, ls="--", label="weights — constant in context length")
    for s, c in zip(slopes, ACCENT):
        kv = s * L
        ax.plot(L, kv, color=c, lw=2, label=f"KV cache — crossover at {1/s:,.0f} tokens")
        xc = 1 / s
        if xc <= L.max():
            ax.plot([xc], [1.0], "o", color=c, ms=6, zorder=5)
    ax.set_xlabel("context length  L  [tokens]")
    ax.set_ylabel("memory, in units of the weight term  [—]")
    ax.set_xlim(0, L.max()); ax.set_ylim(0, 4)
    ax.xaxis.set_major_formatter(lambda v, _: f"{v/1000:.0f}k")
    ax.grid(True, color=GRID, linewidth=.6); ax.set_axisbelow(True)
    ax.legend(fontsize=9, loc="upper left", frameon=True, facecolor="white",
              edgecolor=GRID, framealpha=.95)
    ax.set_title("KV memory is linear in context length. Weights are not.",
                 fontsize=11.5, pad=10)
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-kv-growth.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("wrote 01-kv-growth.png")


if __name__ == "__main__":
    fig_temperature()
    fig_kv_growth()
