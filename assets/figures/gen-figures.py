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


def fig_position_schematic():
    """SCHEMATIC of the position effect. This is a drawn shape, not data.

    The measured curves are Liu et al. (2024), TACL 12:157-173, Figure 5, which is
    CC BY 4.0 via the ACL Anthology PDF and may be reproduced with attribution.
    This schematic exists so the deck can show the shape without implying it is a
    measurement, and so nothing is traced from the source figure.
    """
    x = np.linspace(0, 1, 400)
    # a drawn U: high at both ends, lowest in the middle. No data behind it.
    y = 0.55 + 0.45 * (2 * (x - 0.5)) ** 2
    y = y - 0.06 * x                      # recency slightly below primacy, as described

    fig, ax = plt.subplots(figsize=(7.4, 3.6))
    ax.plot(x, y, color=ACCENT[0], lw=2.6)
    ax.fill_between(x, 0, y, color=ACCENT[0], alpha=.07)
    ax.annotate("primacy", xy=(0.02, y[0]), xytext=(0.06, 0.62),
                fontsize=10, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=.9))
    ax.annotate("recency", xy=(0.98, y[-1]), xytext=(0.74, 0.60),
                fontsize=10, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=.9))
    ax.annotate("worst in the middle", xy=(0.5, y[200]), xytext=(0.36, 0.30),
                fontsize=10, color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=.9))
    ax.set_xlabel("position of the relevant information within the context  [normalised]")
    ax.set_ylabel("accuracy  [arbitrary]")
    ax.set_xlim(0, 1); ax.set_ylim(0, 1.15)
    ax.set_yticks([])
    ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["start", "middle", "end"])
    ax.grid(True, axis="x", color=GRID, linewidth=.6); ax.set_axisbelow(True)
    ax.set_title("SCHEMATIC — the shape only. Not measured data.",
                 fontsize=11, pad=10, color="#97591A")
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "05-position-schematic.png", dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("wrote 05-position-schematic.png")




def fig_scores():
    """Logits, then probabilities. Two panels: the raw scores the network emits,
    and the same scores after softmax. Values are illustrative and labelled as such."""
    labels = ["the", "a", "this", "each", "any", "such", "one", "its"]
    z = np.array([4.2, 3.6, 2.9, 2.1, 1.7, 1.0, 0.4, -0.3])
    p = softmax(z, 1.0)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.5, 3.2))
    x = np.arange(len(labels))
    a1.bar(x, z, color=ACCENT[1], edgecolor=INK, linewidth=.6)
    a1.set_title("1. the network emits a score per token", fontsize=11, pad=8)
    a1.set_ylabel("logit  [—]")
    a2.bar(x, p, color=ACCENT[0], edgecolor=INK, linewidth=.6)
    a2.set_title("2. the same scores turned into probabilities", fontsize=11, pad=8)
    a2.set_ylabel("probability  [—]"); a2.set_ylim(0, 1)
    for a in (a1, a2):
        a.set_xticks(x); a.set_xticklabels(labels, rotation=60, ha="right", fontsize=9)
        a.yaxis.grid(True, color=GRID, linewidth=.6); a.set_axisbelow(True)
    a2.annotate("they now sum to 1", xy=(0, p[0]), xytext=(2.6, .72), fontsize=9.5, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=.9))
    fig.suptitle("illustrative values — the transform is exact", fontsize=9.5, y=1.04, color="#97591A")
    fig.tight_layout()
    for d in (OUT, PUB): fig.savefig(d / "01-scores.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-scores.png")


def fig_token_cost():
    """Why token count matters: a schematic comparison of how many tokens a common
    word and a technical term take. SCHEMATIC — no tokeniser was run."""
    terms = ["the", "and", "concrete", "prestressed", "consolidation", "hydrodynamic"]
    counts = [1, 1, 2, 3, 4, 4]                      # schematic, not measured
    fig, ax = plt.subplots(figsize=(10.2, 3.1))
    cols = [ACCENT[3] if c <= 1 else ACCENT[0] for c in counts]
    ax.barh(range(len(terms)), counts, color=cols, edgecolor=INK, linewidth=.6)
    ax.set_yticks(range(len(terms))); ax.set_yticklabels(terms, fontsize=11)
    ax.invert_yaxis()
    ax.set_xlabel("tokens per word  [—]"); ax.set_xticks(range(0, 6))
    ax.xaxis.grid(True, color=GRID, linewidth=.6); ax.set_axisbelow(True)
    ax.set_title("SCHEMATIC — no tokeniser was run. Capture real splits before delivery.",
                 fontsize=10, pad=10, color="#97591A")
    fig.tight_layout()
    for d in (OUT, PUB): fig.savefig(d / "01-token-cost.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-token-cost.png")


# ---------------------------------------------------------------------------
# Chapter 1 figures, added 2026-08-20 for the teach-from-zero rebuild.
# Every one of these is drawn or computed here. Nothing is traced from a source
# figure and no generated imagery is used. Where a figure needs values that were
# not measured, the figure says SCHEMATIC on its own face.
# ---------------------------------------------------------------------------
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch

WARN = "#97591A"


def _blank(ax):
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)


def fig_chat_artefact():
    """The artefact the room already owns: a chat panel with an answer part-written.

    No words are put in the tool's mouth. The assistant's reply is drawn as
    written and not-yet-written text, because the only claim the figure makes is
    one every attendee has already observed - the answer arrives a piece at a time.
    """
    fig, ax = plt.subplots(figsize=(10.8, 4.0))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5.4); _blank(ax)

    ax.add_patch(FancyBboxPatch((0.15, 0.2), 9.7, 5.0, boxstyle="round,pad=0.08",
                                fc="white", ec=GRID, lw=1.4))
    # user turn
    ax.add_patch(FancyBboxPatch((3.9, 3.85), 5.7, 0.95, boxstyle="round,pad=0.08",
                                fc="#E0EDEF", ec=ACCENT[0], lw=1.1))
    ax.text(6.75, 4.32, "what does lowering the water/cement\nratio do to compressive strength?",
            ha="center", va="center", fontsize=10, color=INK)
    ax.text(9.55, 3.62, "you typed this", ha="right", va="center", fontsize=8.5,
            color=INK, alpha=.7)

    # assistant turn, part written
    ax.add_patch(FancyBboxPatch((0.45, 1.15), 6.6, 2.2, boxstyle="round,pad=0.08",
                                fc="#F7F9F9", ec=GRID, lw=1.1))
    written = [(0.75, 2.95, 5.9), (0.75, 2.55, 6.0), (0.75, 2.15, 4.3)]
    for x, y, w in written:                       # already-written lines
        ax.add_patch(Rectangle((x, y), w, 0.16, fc=ACCENT[1], ec="none", alpha=.55))
    ax.add_patch(Rectangle((0.75, 1.75), 1.9, 0.16, fc=ACCENT[1], ec="none", alpha=.55))
    ax.add_patch(Rectangle((2.72, 1.73), 0.09, 0.21, fc=INK, ec="none"))   # cursor
    for x, y, w in [(2.95, 1.75, 3.7), (0.75, 1.35, 4.9)]:                 # still to come
        ax.add_patch(Rectangle((x, y), w, 0.16, fc=GRID, ec="none", alpha=.55))

    ax.annotate("written so far", xy=(3.6, 2.6), xytext=(7.5, 2.75), fontsize=9.5,
                color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=.9))
    ax.annotate("not written yet", xy=(4.4, 1.83), xytext=(7.5, 1.35), fontsize=9.5,
                color=INK, arrowprops=dict(arrowstyle="->", color=INK, lw=.9))
    ax.text(5.0, 0.6, "the answer arrives a piece at a time, left to right",
            ha="center", va="center", fontsize=11, color=ACCENT[0])
    ax.set_title("SCHEMATIC of the interface  —  capture a real screenshot before delivery",
                 fontsize=9.5, pad=8, color=WARN)
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-chat-artefact.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-chat-artefact.png")


def fig_what_is_ai():
    """Nested sets: AI contains machine learning contains neural networks contains
    large language models. Each band is inset from the top only, so every band keeps
    a clear strip for its own label and for what sits in it and NOT in the band
    inside it - which is what answers 'is all AI an LLM?'.

    The nesting is a definitional relation, not a measurement: a large language model
    is a neural network, which is fitted from data, which is a method people call AI.
    """
    bands = [
        ("artificial intelligence", "the umbrella word. It has no single technical definition.",
         "rules written by hand: expert systems, search and planning, constraint solvers", ACCENT[3]),
        ("machine learning", "behaviour fitted from data instead of written down as rules.",
         "regression, decision trees, clustering, random forests", ACCENT[2]),
        ("neural networks", "fitted functions built from layers of weighted sums.",
         "image classifiers, load forecasters, surrogate models", ACCENT[1]),
        ("large language models", "a neural network fitted to predict text. The subject of this course.",
         "", ACCENT[0]),
    ]
    tops = [5.35, 4.20, 3.05, 1.90]
    fig, ax = plt.subplots(figsize=(12.6, 5.0))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5.9); _blank(ax)
    for i, (name, defn, examples, colour) in enumerate(bands):
        x = 0.30 + i * 0.38
        w = 9.40 - 2 * i * 0.38
        ax.add_patch(FancyBboxPatch((x, 0.30), w, tops[i] - 0.30, boxstyle="round,pad=0.05",
                                    fc=colour, ec=INK, lw=1.1, alpha=.32 if i < 3 else .55))
        if i < 3:                       # innermost band is labelled centrally instead
            ax.text(x + 0.20, tops[i] - 0.30, name, fontsize=12.5 - i * 0.5, weight="bold",
                    color=INK, va="center")
            ax.text(x + 0.20, tops[i] - 0.62, defn, fontsize=8.6, color=INK,
                    va="center", alpha=.9)
        if examples:
            ax.text(x + 0.20, tops[i] - 0.90, "in here and not in the band below:  " + examples,
                    fontsize=8.0, color=INK, va="center", alpha=.72)
    ax.text(5.0, 1.05, "large language models", fontsize=13, weight="bold",
            ha="center", color=INK)
    ax.text(5.0, 0.68, "a neural network fitted to predict text — the subject of this course",
            fontsize=9.2, ha="center", color=INK)
    ax.set_title("Every band contains the one inside it. Not all artificial intelligence "
                 "is a language model.", fontsize=11, pad=10, color=INK)
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-what-is-ai.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-what-is-ai.png")


def fig_model_artefact():
    """A model as a concrete object: a long list of numbers, and the program that
    does arithmetic with them. No file size is asserted - the count is left as a
    symbol, because a specific figure would be a claim about a specific model."""
    fig, ax = plt.subplots(figsize=(11.4, 3.9))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4.4); _blank(ax)

    ax.add_patch(FancyBboxPatch((0.3, 1.15), 4.5, 2.55, boxstyle="round,pad=0.08",
                                fc="#E0EDEF", ec=ACCENT[0], lw=1.4))
    ax.text(2.55, 3.42, "the parameters", fontsize=12, weight="bold", ha="center", color=INK)
    ax.text(2.55, 3.04, "one long list of numbers", fontsize=9.5, ha="center", color=INK, alpha=.85)
    nums = ["-0.0412", "0.9037", "0.1188", "-1.2740", "0.0006", "0.4451",
            "-0.3319", "0.7702", "0.0925", "-0.0187", "1.1046", "-0.6538"]
    for i, v in enumerate(nums):
        ax.text(0.72 + (i % 4) * 1.06, 2.55 - (i // 4) * 0.36, v, fontsize=8.6,
                family="monospace", color=INK, alpha=.9)
    ax.text(2.55, 1.42, "...  and so on, counted in billions", fontsize=9,
            ha="center", color=INK, alpha=.7, style="italic")

    ax.add_patch(FancyBboxPatch((5.4, 1.15), 4.3, 2.55, boxstyle="round,pad=0.08",
                                fc="#F8F1E7", ec=WARN, lw=1.4))
    ax.text(7.55, 3.42, "the program", fontsize=12, weight="bold", ha="center", color=INK)
    ax.text(7.55, 3.04, "the arithmetic that uses them", fontsize=9.5, ha="center", color=INK, alpha=.85)
    steps = ["read the numbers from the list",
             "multiply and add them against the\ninput, layer after layer",
             "hand back one score per token"]
    for i, s in enumerate(steps):
        ax.text(5.75, 2.60 - i * 0.48, f"{i+1}.  {s}", fontsize=8.8, color=INK, va="top")
    ax.text(5.0, 0.55, "Both are files on a disk. Together they are the model.",
            fontsize=11.5, ha="center", color=ACCENT[0])
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-model-artefact.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-model-artefact.png")


def fig_train_vs_run():
    """Timeline: the numbers change during training, then stop changing. Every
    session the audience will ever run sits to the right of the line."""
    fig, ax = plt.subplots(figsize=(11.2, 3.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4.0); _blank(ax)
    ax.annotate("", xy=(9.9, 0.55), xytext=(0.2, 0.55),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.6))
    ax.text(9.9, 0.18, "time", fontsize=10, ha="right", color=INK)

    ax.add_patch(Rectangle((0.35, 1.05), 3.5, 1.55, fc=ACCENT[1], ec=INK, lw=1.0, alpha=.45))
    ax.text(2.1, 2.05, "training", fontsize=12.5, weight="bold", ha="center", color=INK)
    ax.text(2.1, 1.45, "the numbers are\nbeing changed", fontsize=9.5, ha="center",
            va="center", color=INK)
    ax.plot([4.05, 4.05], [0.45, 3.35], color=WARN, lw=2.2)
    ax.text(4.18, 3.42, "training stops. the numbers are frozen from here on.",
            fontsize=10.5, color=WARN, va="center")

    for i, lab in enumerate(["your session\non Monday", "your session\non Tuesday",
                             "a colleague's\nsession"]):
        x = 4.85 + i * 1.75
        ax.add_patch(FancyBboxPatch((x, 1.25), 1.45, 1.15, boxstyle="round,pad=0.06",
                                    fc="#F7F9F9", ec=GRID, lw=1.1))
        ax.text(x + 0.72, 1.82, lab, fontsize=8.8, ha="center", va="center", color=INK)
        ax.plot([x + 0.72, x + 0.72], [1.25, 0.65], color=INK, lw=.9, ls=":")
        ax.plot([x + 0.72], [0.55], "o", color=INK, ms=4.5)
    ax.set_title("Nothing to the right of the line changes anything to the left of it.",
                 fontsize=11, pad=8, color=INK)
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-train-vs-run.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-train-vs-run.png")


def fig_fitting():
    """The discipline bridge. Left: a straight line fitted to data by choosing two
    numbers. Right: the error as a function of one of those numbers, with the
    minimum marked - which is what 'training' searches for.

    Data are drawn from a fixed seed and the fit is a real least-squares fit, so
    the marked minimum is computed rather than drawn."""
    rng = np.random.default_rng(7)
    x = np.linspace(0.5, 9.5, 14)
    y = 0.62 * x + 1.1 + rng.normal(0, 0.55, x.size)
    m, c = np.polyfit(x, y, 1)                       # least-squares fit, exact

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.6, 3.5))
    a1.plot(x, y, "o", color=ACCENT[1], ms=6, mec=INK, mew=.6)
    xs = np.linspace(0, 10, 100)
    a1.plot(xs, m * xs + c, color=ACCENT[0], lw=2.2)
    for xi, yi in zip(x, y):                          # residuals, the thing minimised
        a1.plot([xi, xi], [yi, m * xi + c], color=WARN, lw=1.0, alpha=.8)
    a1.set_xlabel("measured input  [—]"); a1.set_ylabel("measured output  [—]")
    a1.set_title(f"two numbers chosen: slope {m:.2f}, intercept {c:.2f}",
                 fontsize=10.5, pad=8)
    a1.text(0.4, y.max() + 0.35, "orange bars are the error being minimised",
            fontsize=8.8, color=WARN)
    a1.grid(True, color=GRID, lw=.6); a1.set_axisbelow(True)

    slopes = np.linspace(m - 0.75, m + 0.75, 300)
    sse = np.array([np.sum((y - (s * x + c)) ** 2) for s in slopes])
    a2.plot(slopes, sse, color=ACCENT[0], lw=2.2)
    a2.plot([m], [np.sum((y - (m * x + c)) ** 2)], "o", color=WARN, ms=8, zorder=5)
    a2.annotate("the value training searches for", xy=(m, sse.min()),
                xytext=(m - 0.72, sse.max() * 0.62), fontsize=9.5, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=.9))
    a2.set_xlabel("value of the slope  [—]"); a2.set_ylabel("total squared error  [—]")
    a2.set_title("training is a search for the bottom of this bowl", fontsize=10.5, pad=8)
    a2.grid(True, color=GRID, lw=.6); a2.set_axisbelow(True)
    fig.suptitle("A language model does exactly this with billions of numbers instead of two, "
                 "and the data is text.", fontsize=10.5, y=1.05, color=ACCENT[0])
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-fitting.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-fitting.png")


def fig_tokens():
    """One sentence cut into tokens, with the integer each one becomes.
    SCHEMATIC - no tokeniser was run; the split and the integers are drawn."""
    pieces = ["The", " pre", "stress", "ed", " beam", " showed", " cre", "ep", "."]
    ids = [791, 864, 42928, 291, 24001, 8710, 1706, 752, 13]      # illustrative
    fig, ax = plt.subplots(figsize=(10.4, 3.0))
    ax.set_xlim(0, 10.4); ax.set_ylim(0, 3.0); _blank(ax)
    ax.text(2.05, 2.28, "what you typed", fontsize=9.5, ha="right", va="center",
            color=INK, alpha=.78)
    ax.text(2.05, 1.28, "what the model\nis handed", fontsize=9.5, ha="right",
            va="center", color=INK, alpha=.78)
    xpos = 2.20
    for piece, tid in zip(pieces, ids):
        w = max(0.52, 0.145 * len(piece) + 0.34)
        ax.add_patch(FancyBboxPatch((xpos, 2.02), w, 0.52, boxstyle="round,pad=0.03",
                                    fc="#E0EDEF", ec=ACCENT[0], lw=1.0))
        ax.text(xpos + w / 2, 2.28, piece.replace(" ", "\u2423"), fontsize=9.5,
                ha="center", va="center", family="monospace", color=INK)
        ax.add_patch(FancyBboxPatch((xpos, 1.02), w, 0.52, boxstyle="round,pad=0.03",
                                    fc="#F8F1E7", ec=WARN, lw=1.0))
        ax.text(xpos + w / 2, 1.28, str(tid), fontsize=8.8, ha="center", va="center",
                family="monospace", color=INK)
        ax.annotate("", xy=(xpos + w / 2, 1.60), xytext=(xpos + w / 2, 1.96),
                    arrowprops=dict(arrowstyle="->", color=INK, lw=.8))
        xpos += w + 0.08
    ax.text(2.20, 0.50, "\u2423 marks a leading space, which belongs to the token. "
                        "Nine tokens for five words.", fontsize=10, color=INK)
    ax.set_title("SCHEMATIC — no tokeniser was run. Capture a real split before delivery.",
                 fontsize=9.5, pad=6, color=WARN)
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-tokens.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-tokens.png")


def fig_attention():
    """Which earlier tokens the score for the next one leans on. Arc thickness is the
    weight, and the arcs are drawn below the sentence so no word is obscured.
    ILLUSTRATIVE - the weights are drawn to show the operation, not extracted."""
    words = ["The", "beam", "failed", "in", "shear", "because", "the", "stirrups", "were"]
    weights = [0.02, 0.24, 0.09, 0.01, 0.28, 0.03, 0.01, 0.30, 0.02]

    fig, ax = plt.subplots(figsize=(11.6, 3.6))
    ax.set_xlim(0, 11.0); ax.set_ylim(0, 3.6); _blank(ax)
    xs, xpos = [], 0.25
    for w in words:
        width = 0.125 * len(w) + 0.30
        ax.add_patch(FancyBboxPatch((xpos, 2.72), width, 0.46, boxstyle="round,pad=0.03",
                                    fc="#F7F9F9", ec=GRID, lw=1.0))
        ax.text(xpos + width / 2, 2.95, w, fontsize=9.5, ha="center", va="center", color=INK)
        xs.append(xpos + width / 2); xpos += width + 0.10
    ax.add_patch(FancyBboxPatch((xpos, 2.72), 0.80, 0.46, boxstyle="round,pad=0.03",
                                fc="#E0EDEF", ec=ACCENT[0], lw=1.8))
    ax.text(xpos + 0.40, 2.95, "?", fontsize=13, ha="center", va="center",
            weight="bold", color=ACCENT[0])
    target = xpos + 0.40
    ax.text(target, 3.42, "the next token\nbeing scored", fontsize=8.8, ha="center",
            va="center", color=ACCENT[0])

    t = np.linspace(0, 1, 120)
    for x, wt in zip(xs, weights):
        sag = 0.45 + 1.15 * (target - x) / max(target - xs[0], 1e-9)   # longer reach, deeper arc
        cx, cy = (x + target) / 2, 2.66 - sag
        bx = (1 - t) ** 2 * x + 2 * (1 - t) * t * cx + t ** 2 * target
        by = (1 - t) ** 2 * 2.66 + 2 * (1 - t) * t * cy + t ** 2 * 2.66
        ax.plot(bx, by, color=ACCENT[0], lw=0.5 + 12 * wt, alpha=0.25 + 2.2 * wt,
                solid_capstyle="round")
        ax.plot([bx[-3]], [by[-3]], marker=(3, 0, -55), ms=3.4 + 13 * wt,
                color=ACCENT[0], alpha=0.25 + 2.2 * wt)
    ax.text(5.5, 0.62, "Thicker arc, larger share of the weighted sum. "
                       "The weights are recomputed for every new token.",
            fontsize=10, ha="center", color=INK)
    ax.set_title("ILLUSTRATIVE weights — drawn to show the operation, not read out of a model.",
                 fontsize=9.5, pad=6, color=WARN)
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-attention.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-attention.png")


def fig_softmax_curve():
    """Probability of the higher-scoring of two tokens against temperature, for
    scores 2.0 and 1.0. Computed exactly; the three marked points are the three
    rows of the worked table on the slide, so the slide and the figure cannot drift."""
    T = np.linspace(0.12, 3.0, 400)
    p = 1.0 / (1.0 + np.exp(-(2.0 - 1.0) / T))       # exact for two logits
    fig, ax = plt.subplots(figsize=(7.4, 3.5))
    ax.plot(T, p, color=ACCENT[0], lw=2.4)
    ax.axhline(0.5, color=GRID, lw=1.0, ls="--")
    ax.text(2.92, 0.525, "0.5 — the two become equally likely", fontsize=8.8,
            ha="right", color=INK, alpha=.75)
    for t in (0.5, 1.0, 2.0):
        pv = 1.0 / (1.0 + np.exp(-1.0 / t))
        ax.plot([t], [pv], "o", color=WARN, ms=7, zorder=5)
        ax.annotate(f"T = {t}\np = {pv:.3f}", xy=(t, pv), xytext=(t + 0.12, pv + 0.055),
                    fontsize=9, color=INK)
    ax.set_xlabel("temperature  T  [—]")
    ax.set_ylabel("probability of the token scoring 2.0  [—]")
    ax.set_xlim(0, 3.0); ax.set_ylim(0.45, 1.02)
    ax.grid(True, color=GRID, lw=.6); ax.set_axisbelow(True)
    ax.set_title("Two tokens, scores 2.0 and 1.0. Computed exactly.", fontsize=11, pad=9)
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-softmax-T.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-softmax-T.png")


def fig_loop():
    """Four passes of the loop. Each row shows the tokens supplied so far and the
    distribution over the next one as a proportional strip, with the token that was
    chosen picked out. ILLUSTRATIVE - the distributions are drawn, not measured."""
    seq = ["the", " shear", " capacity", " of"]
    cands = [[" shear", " span", " force", " wall"],
             [" capacity", " stress", " force", " key"],
             [" of", " is", " was", " can"],
             [" the", " a", " this", " reinforced"]]
    dists = [[.52, .21, .17, .10], [.61, .18, .13, .08],
             [.47, .29, .15, .09], [.66, .17, .11, .06]]
    pick = 0                                  # the sampler happened to take the top one

    fig, axes = plt.subplots(4, 1, figsize=(12.4, 5.0))
    for r, ax in enumerate(axes):
        ax.set_xlim(0, 10); ax.set_ylim(0, 1); _blank(ax)
        ax.text(0.05, 0.5, f"pass {r+1}", fontsize=9.5, va="center", color=INK, alpha=.7)
        xpos = 0.95
        for tok in seq[:r + 1]:
            w = 0.115 * len(tok) + 0.32
            ax.add_patch(FancyBboxPatch((xpos, 0.28), w, 0.46, boxstyle="round,pad=0.02",
                                        fc="#E0EDEF", ec=ACCENT[0], lw=.9))
            ax.text(xpos + w / 2, 0.51, tok.strip(), fontsize=9, ha="center",
                    va="center", family="monospace", color=INK)
            xpos += w + 0.06
        ax.text(xpos + 0.16, 0.51, "\u2192", fontsize=13, va="center", color=INK)

        # proportional strip: 3.6 units wide, split by probability
        x0, span = 5.35, 3.05
        for i, (c, pv) in enumerate(zip(cands[r], dists[r])):
            col = ACCENT[0] if i == pick else ACCENT[3]
            ax.add_patch(Rectangle((x0, 0.30), span * pv, 0.42, fc=col, ec=INK, lw=.6))
            if span * pv > 0.55:
                ax.text(x0 + span * pv / 2, 0.51, f"{c.strip()}  {pv:.2f}", fontsize=7.8,
                        ha="center", va="center", color="white" if i == pick else INK)
            x0 += span * pv
        if r == 0:
            ax.text(5.35, 0.13, "scores for the next token, as probabilities",
                    fontsize=7.6, color=INK, alpha=.7)
        ax.text(9.95, 0.51, "took " + cands[r][pick].strip(), fontsize=9,
                ha="right", va="center", color=ACCENT[0], weight="bold")
    fig.suptitle("ILLUSTRATIVE — the same frozen numbers are read on every pass. "
                 "Only the text handed to them has grown.",
                 fontsize=10, y=1.02, color=WARN)
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-loop.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-loop.png")


def fig_persistence():
    """Three sessions over time. The window fills and vanishes each time; the
    parameter list below it never changes."""
    fig, ax = plt.subplots(figsize=(11.2, 3.7))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4.2); _blank(ax)
    for i, lab in enumerate(["session 1", "session 2", "session 3"]):
        x = 0.6 + i * 3.1
        ax.text(x + 1.15, 3.86, lab, fontsize=10, ha="center", color=INK, alpha=.8)
        for j, h in enumerate([0.35, 0.75, 1.15, 1.55]):
            ax.add_patch(Rectangle((x + j * 0.58, 1.95), 0.46, h,
                                   fc=ACCENT[1], ec=INK, lw=.6, alpha=.55))
        ax.text(x + 1.15, 1.72, "the window fills", fontsize=8.6, ha="center",
                color=INK, alpha=.75)
        ax.plot([x + 2.52, x + 2.88], [2.42, 2.78], color=WARN, lw=2.2)
        ax.plot([x + 2.52, x + 2.88], [2.78, 2.42], color=WARN, lw=2.2)
        ax.text(x + 2.7, 2.15, "gone", fontsize=8.4, ha="center", color=WARN)
    ax.add_patch(Rectangle((0.4, 0.55), 9.2, 0.72, fc="#E0EDEF", ec=ACCENT[0], lw=1.4))
    ax.text(5.0, 0.91, "the parameters — identical before, during and after every one of them",
            fontsize=10.5, ha="center", va="center", color=INK)
    ax.set_title("Talking to it changes the window. Nothing changes the numbers.",
                 fontsize=11, pad=8, color=INK)
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-persistence.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-persistence.png")


def fig_what_training_changed():
    """What training actually did: it moved the numbers. Values are drawn from a fixed
    seed and labelled illustrative; the point the figure makes is that the parameters
    started as noise and finished somewhere else, and that nothing else changed.

    This is the slide that meets the brain analogy at the moment the audience will
    reach for it - straight after being told the thing is a "neural network" that
    "learns"."""
    rng = np.random.default_rng(21)
    start = rng.uniform(-1, 1, 6)
    end = start + rng.normal(0, 0.55, 6)

    fig, ax = plt.subplots(figsize=(13.2, 3.7))
    ax.set_xlim(0, 11); ax.set_ylim(0, 4.2); _blank(ax)

    ax.add_patch(FancyBboxPatch((0.35, 1.35), 3.6, 2.45, boxstyle="round,pad=0.07",
                                fc="#F7F9F9", ec=GRID, lw=1.3))
    ax.text(2.15, 3.55, "at the start of training", fontsize=11, weight="bold",
            ha="center", color=INK)
    ax.text(2.15, 3.22, "the numbers are random", fontsize=9, ha="center",
            color=INK, alpha=.8)

    ax.add_patch(FancyBboxPatch((7.05, 1.35), 3.6, 2.45, boxstyle="round,pad=0.07",
                                fc="#E0EDEF", ec=ACCENT[0], lw=1.4))
    ax.text(8.85, 3.55, "when training stopped", fontsize=11, weight="bold",
            ha="center", color=INK)
    ax.text(8.85, 3.22, "and they never move again", fontsize=9, ha="center",
            color=INK, alpha=.8)

    for i, (a, b) in enumerate(zip(start, end)):
        y = 2.80 - i * 0.24
        ax.text(2.15, y, f"{a:+.4f}", fontsize=10.5, family="monospace",
                ha="center", va="center", color=INK, alpha=.85)
        ax.text(8.85, y, f"{b:+.4f}", fontsize=10.5, family="monospace",
                ha="center", va="center", color=INK)
    # one arrow rather than eight, so the label has somewhere to sit
    ax.annotate("", xy=(6.90, 2.30), xytext=(4.10, 2.30),
                arrowprops=dict(arrowstyle="-|>", color=ACCENT[0], lw=2.6,
                                mutation_scale=22))
    ax.text(5.5, 2.72, "training", fontsize=12, ha="center", color=ACCENT[0], weight="bold")
    ax.text(5.5, 2.00, "a search for the values\nthat make the error smallest",
            fontsize=8.8, ha="center", va="top", color=INK, alpha=.85)

    ax.add_patch(FancyBboxPatch((0.35, 0.35), 10.3, 0.70, boxstyle="round,pad=0.05",
                                fc="#F8F1E7", ec=WARN, lw=1.2))
    ax.text(5.5, 0.70, "the program that reads them — identical before, during and after",
            fontsize=10.5, ha="center", va="center", color=INK)
    ax.set_title("ILLUSTRATIVE values, drawn from a fixed seed. The movement is the point, "
                 "not the numbers.", fontsize=9.5, pad=8, color=WARN)
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-what-training-changed.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-what-training-changed.png")


if __name__ == "__main__":
    fig_temperature()
    fig_kv_growth()
    fig_position_schematic()
    fig_scores()
    fig_token_cost()
    # Chapter 1 teach-from-zero rebuild
    fig_chat_artefact()
    fig_what_is_ai()
    fig_model_artefact()
    fig_train_vs_run()
    fig_fitting()
    fig_what_training_changed()
    fig_tokens()
    fig_attention()
    fig_softmax_curve()
    fig_loop()
    fig_persistence()
