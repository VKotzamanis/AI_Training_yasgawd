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

# Four kinds of number appear in Chapter 1 and a review found they were conflated.
# Each gets one colour, used identically in every figure. Colour is a redundant cue:
# a coloured number always carries its word too, so nothing depends on hue alone.
TOKENID = "#54585A"   # Slate  — a label, no magnitude
PARAM   = "#B97800"   # Ocher  — the fitted numbers the model is made of
LOGIT   = "#00B388"   # Teal   — raw scores out of the network
PROB    = "#C8102E"   # UH Red — probabilities, the quantity the chapter builds toward

plt.rcParams.update({
    "font.size": 11, "axes.edgecolor": INK, "axes.labelcolor": INK,
    "text.color": INK, "xtick.color": INK, "ytick.color": INK,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": "white", "axes.facecolor": "white",
})

# The running example, fixed by curriculum/ch01-animation-slots.md so every figure
# that needs the sentence or its candidates draws from one place, not a retyped copy.
# "The beam failed in shear because the stirrups were ▁▁▁"
RUNNING_WORDS = ["The", "beam", "failed", "in", "shear", "because", "the", "stirrups", "were"]
CANDIDATES = [" absent", " corroded", " undersized", " blue"]
CAND_PROBS = [0.41, 0.27, 0.19, 0.02]          # illustrative; deliberately do not sum to 1
# Ordinary-English fillers for panels that need low-probability company for the four
# candidates. Chosen to be unremarkable completions nobody would rank highly here.
FILLERS = [" purple", " hungry", " triangular", " sleepy"]


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
    """The four running candidates plus four fillers, one softmax, four temperatures.

    Logits are the natural log of a chosen T = 1 probability table (the candidates
    at their table values; fillers making up the rest to 1 exactly), so
    softmax(logits, 1.0) reproduces that table exactly - the transform is applied,
    not just labelled. Temperature scaling divides every logit by the same T, which
    preserves rank order, so `absent` stays the largest bar at every temperature
    shown; only the margin over the rest changes."""
    labels = CANDIDATES + FILLERS
    filler_p = [0.04, 0.03, 0.02, 0.02]           # illustrative; sums with CAND_PROBS to 1.00
    p1 = np.array(CAND_PROBS + filler_p)
    assert abs(p1.sum() - 1.0) < 1e-9, "T=1 table must sum to 1 for the log-inverse trick"
    logits = np.log(p1)                            # exact inverse of softmax at T = 1
    temps = [0.2, 0.7, 1.0, 1.8]

    fig, axes = plt.subplots(1, 4, figsize=(11.6, 3.55), sharey=True)
    x = np.arange(len(labels))
    for ax, T in zip(axes, temps):
        p = softmax(logits, T)
        # same PROB hex everywhere per the colour-code rule; fillers are de-emphasised
        # by alpha, not by a second colour, so "one colour, used identically" holds.
        alphas = [1.0 if i < 4 else 0.40 for i in range(len(labels))]
        for xi, pi, ai in zip(x, p, alphas):
            ax.bar([xi], [pi], color=PROB, edgecolor=INK, linewidth=.6, alpha=ai)
        ax.set_title(f"T = {T}", fontsize=12, pad=8)
        ax.set_xticks(x)
        ax.set_xticklabels([t.strip() for t in labels], rotation=60, ha="right", fontsize=8.3)
        ax.set_ylim(0, 1.0)
        ax.yaxis.grid(True, color=GRID, linewidth=.6)
        ax.set_axisbelow(True)
        ax.text(.97, .93, f"p(absent) {p[0]:.2f}", transform=ax.transAxes,
                ha="right", va="top", fontsize=8.3, color=PROB, weight="bold")
    axes[0].set_ylabel("probability")
    fig.suptitle("Same eight candidates, four temperatures — logits are log(table probability), "
                 "so softmax at T = 1 reproduces the table exactly",
                 fontsize=9.4, y=1.09, color=INK)
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
    """Logits, then probabilities, for the running example. Two panels: the raw
    scores the network emits, and probabilities for the same eight candidates.

    The probability panel is NOT softmax(logits shown) - softmax over a closed set
    of 8 numbers necessarily sums to 1, which would misstate the point. Instead the
    four running candidates carry their fixed table values (0.41 + 0.27 + 0.19 + 0.02
    = 0.89) and the four fillers carry small illustrative values, so the eight shown
    bars total under 1 and the remainder is explicitly the unshown vocabulary. The
    exact softmax transform, applied honestly to a closed two-token set, is
    fig_softmax_curve; this figure is a wide-vocabulary sketch, not a computation.
    """
    labels = CANDIDATES + FILLERS
    logits = np.array([3.9, 3.2, 2.6, 0.3, -0.5, -0.9, -1.4, -1.9])      # illustrative
    filler_p = [0.012, 0.008, 0.005, 0.003]                              # illustrative
    probs = np.array(CAND_PROBS + filler_p)
    shown_total = probs.sum()

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.0, 3.55))
    x = np.arange(len(labels))
    a1.bar(x, logits, color=LOGIT, edgecolor=INK, linewidth=.6)
    a1.set_title("1. logits — raw scores out of the network", fontsize=10.5, pad=8)
    a1.set_ylabel("logit  [—]")
    a2.bar(x, probs, color=PROB, edgecolor=INK, linewidth=.6)
    a2.set_title("2. probabilities", fontsize=10.5, pad=8)
    a2.set_ylabel("probability  [—]"); a2.set_ylim(0, 0.5)
    for a in (a1, a2):
        a.set_xticks(x); a.set_xticklabels([t.strip() for t in labels],
                                            rotation=60, ha="right", fontsize=9)
        a.yaxis.grid(True, color=GRID, linewidth=.6); a.set_axisbelow(True)
    a2.annotate(f"these eight sum to {shown_total:.2f}, not 1 —\nthe rest of the "
                f"vocabulary carries\nthe other {1 - shown_total:.2f}",
                xy=(3, probs[3]), xytext=(3.3, 0.30), fontsize=8.6, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=.9))
    fig.suptitle("illustrative — probabilities are assigned directly here, not derived "
                 "by softmax from the logits shown", fontsize=9.2, y=1.05, color=WARN)
    fig.tight_layout()
    for d in (OUT, PUB): fig.savefig(d / "01-scores.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-scores.png")


def fig_token_cost():
    """Why token count matters: token count tracks how often a string appeared in
    the training corpus, not how long the string is. SCHEMATIC — no tokeniser was
    run. "rebar" (5 letters, rare in general text) costs more tokens than
    "international" (13 letters, common) - the pairing a length-based ordering
    would hide, so it is annotated explicitly rather than left for the reader to spot."""
    terms = ["the", "concrete", "international", "stirrup", "rebar", "screed", "poroelastic"]
    counts = [1, 1, 2, 2, 3, 3, 4]                      # schematic, not measured
    letters = [len(t) for t in terms]
    labels = [f"{t}   ({n} letters)" for t, n in zip(terms, letters)]
    fig, ax = plt.subplots(figsize=(10.6, 3.75))
    cols = [WARN if t in ("rebar", "international") else ACCENT[0] for t in terms]
    ax.barh(range(len(terms)), counts, color=cols, edgecolor=INK, linewidth=.6)
    ax.set_yticks(range(len(terms))); ax.set_yticklabels(labels, fontsize=10)
    ax.invert_yaxis()
    ax.set_xlabel("tokens per word  [—]"); ax.set_xticks(range(0, 6))
    ax.xaxis.grid(True, color=GRID, linewidth=.6); ax.set_axisbelow(True)
    i_reb, i_int = terms.index("rebar"), terms.index("international")
    ax.annotate("shorter, but rarer in the corpus — costs more tokens",
                xy=(counts[i_reb], i_reb), xytext=(3.15, i_int + 0.55), fontsize=9,
                color=WARN, arrowprops=dict(arrowstyle="->", color=WARN, lw=1.1))
    ax.annotate("", xy=(counts[i_int] + 0.05, i_int), xytext=(3.15, i_int + 0.45),
                arrowprops=dict(arrowstyle="->", color=WARN, lw=1.1))
    ax.set_title("Token count follows how often a word was written, not how long it is.",
                 fontsize=10.8, pad=10, color=INK)
    ax.text(0.0, -0.24, "SCHEMATIC — no tokeniser was run. Capture real splits before delivery.",
            transform=ax.transAxes, fontsize=8.6, color=WARN, style="italic")
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

    The outermost boundary is dashed, not solid like the three inside it. "Artificial
    intelligence" is a label applied inconsistently in practice - a route planner or a
    game opponent gets called "AI" by some and refused the label by others, because the
    boundary is a matter of usage, not a fitted or measured line. The three inner
    boundaries are solid because those categories nest by definition: every neural
    network is fitted from data (so it is machine learning), and every large language
    model is a neural network.
    """
    bands = [
        ("artificial intelligence", "the umbrella word. It has no single technical definition.",
         "a robot vacuum planning a route, the opponent in a video game, "
         "a chess engine, a route planner", ACCENT[3]),
        ("machine learning", "behaviour fitted from data instead of written down as rules.",
         "regression, decision trees, clustering, random forests", ACCENT[2]),
        ("neural networks", "fitted functions built from layers of weighted sums.",
         "image classifiers, load forecasters, surrogate models", ACCENT[1]),
        ("large language models", "a neural network fitted to predict text. The subject of this course.",
         "", ACCENT[0]),
    ]
    tops = [5.35, 4.20, 3.05, 1.90]
    fig, ax = plt.subplots(figsize=(12.6, 4.55))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5.9); _blank(ax)
    for i, (name, defn, examples, colour) in enumerate(bands):
        x = 0.30 + i * 0.38
        w = 9.40 - 2 * i * 0.38
        ax.add_patch(FancyBboxPatch((x, 0.30), w, tops[i] - 0.30, boxstyle="round,pad=0.05",
                                    fc=colour, ec=INK, lw=1.3 if i == 0 else 1.1,
                                    ls="--" if i == 0 else "-",
                                    alpha=.32 if i < 3 else .55))
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
    ax.text(9.60, 5.62, "dashed = a boundary drawn by usage, not by definition — "
                        "\"artificial intelligence\" is applied inconsistently",
            fontsize=8.2, ha="right", va="center", color=INK, style="italic", alpha=.85)
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
    ax.text(2.55, 3.42, "the parameters", fontsize=12, weight="bold", ha="center", color=PARAM)
    ax.text(2.55, 3.04, "one long list of numbers", fontsize=9.5, ha="center", color=INK, alpha=.85)
    nums = ["-0.0412", "0.9037", "0.1188", "-1.2740", "0.0006", "0.4451",
            "-0.3319", "0.7702", "0.0925", "-0.0187", "1.1046", "-0.6538"]
    for i, v in enumerate(nums):
        ax.text(0.72 + (i % 4) * 1.06, 2.55 - (i // 4) * 0.36, v, fontsize=8.6,
                family="monospace", color=PARAM, alpha=.95)
    ax.text(2.55, 1.42, "...  and so on, counted in billions", fontsize=9,
            ha="center", color=PARAM, alpha=.8, style="italic")

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

    Data are round numbers a reader can check by hand: x = 1..5, y = 3,5,7,9,11,
    which is exactly y = 2x + 1. The least-squares fit is real (np.polyfit), and
    because the data lie exactly on a line, the fit recovers slope 2 and intercept 1
    with zero residual - a property of this constructed example, not of fitting in
    general. A real fit almost never lands on zero residual; that is stated on the
    figure so the clean arithmetic is not mistaken for the typical case.
    """
    x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    y = np.array([3.0, 5.0, 7.0, 9.0, 11.0])          # exactly y = 2x + 1
    m, c = np.polyfit(x, y, 1)                        # least-squares fit, exact
    resid = y - (m * x + c)                           # exactly zero here, to float precision

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10.6, 3.5))
    a1.plot(x, y, "o", color=ACCENT[1], ms=7, mec=INK, mew=.7, zorder=5)
    xs = np.linspace(0, 6, 100)
    a1.plot(xs, m * xs + c, color=ACCENT[0], lw=2.2)
    for xi, yi, ri in zip(x, y, resid):               # residuals, the thing minimised
        if abs(ri) > 1e-9:
            a1.plot([xi, xi], [yi, m * xi + c], color=WARN, lw=1.2, alpha=.85)
    a1.set_xlabel("x  [—]"); a1.set_ylabel("y  [—]")
    a1.set_xlim(0, 6); a1.set_ylim(0, 13)
    a1.set_title("the two parameters chosen by the fit", fontsize=10.5, pad=8, color=INK)
    a1.text(0.30, 12.55, "the two parameters:", fontsize=9.5, color=PARAM, weight="bold",
            ha="left", va="top")
    a1.text(0.30, 11.75, f"slope = {m:.2f}     intercept = {c:.2f}", fontsize=10.5,
            color=PARAM, weight="bold", ha="left", va="top")
    a1.text(0.30, 10.75, "orange = residual; none here — an exact fit", fontsize=7.8,
            color=INK, alpha=.85, ha="left", va="top", style="italic")
    a1.grid(True, color=GRID, lw=.6); a1.set_axisbelow(True)

    slopes = np.linspace(m - 1.5, m + 1.5, 300)
    sse = np.array([np.sum((y - (s * x + c)) ** 2) for s in slopes])
    a2.plot(slopes, sse, color=ACCENT[0], lw=2.2)
    a2.plot([m], [np.sum((y - (m * x + c)) ** 2)], "o", color=WARN, ms=8, zorder=5)
    a2.annotate(f"minimum at slope = {m:.2f}\n(the value training searches for)",
                xy=(m, 0.0), xytext=(m - 1.42, sse.max() * 0.62), fontsize=9.2, color=INK,
                va="bottom", arrowprops=dict(arrowstyle="->", color=INK, lw=.9,
                connectionstyle="arc3,rad=0.15"))
    a2.set_xlabel("value of the slope  [—]"); a2.set_ylabel("total squared error  [—]")
    a2.set_title("training is a search for the bottom of this bowl", fontsize=10.5, pad=8)
    a2.grid(True, color=GRID, lw=.6); a2.set_axisbelow(True)
    fig.suptitle("y = 2x + 1 exactly — chosen so slope 2.00 and intercept 1.00 can be verified "
                 "by hand. A real fit does not land on zero residual.",
                 fontsize=10, y=1.06, color=ACCENT[0])
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-fitting.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-fitting.png")


def fig_tokens():
    """The running sentence cut into tokens, with the integer each one becomes.
    SCHEMATIC - no tokeniser was run; the split and the integers are drawn. The split
    deliberately breaks two words mid-string (" she"/"ar" for "shear", " stir"/"rups"
    for "stirrups") because that is what a real subword tokeniser does to a word its
    vocabulary has not stored whole - the same phenomenon fig_token_cost explains."""
    pieces = ["The", " beam", " failed", " in", " she", "ar", " because",
              " the", " stir", "rups", " were"]
    ids = [791, 24001, 8710, 304, 1364, 277, 1606,
           279, 2941, 32516, 1051]                                # illustrative
    fig, ax = plt.subplots(figsize=(11.9, 3.95))
    ax.set_xlim(0, 12.6); ax.set_ylim(0, 3.0); _blank(ax)
    ax.text(1.55, 2.28, "what you typed", fontsize=9.5, ha="right", va="center",
            color=INK, alpha=.78)
    ax.text(1.55, 1.28, "what the model\nis handed", fontsize=9.5, ha="right",
            va="center", color=INK, alpha=.78)
    xpos = 1.70
    for piece, tid in zip(pieces, ids):
        w = max(0.50, 0.128 * len(piece) + 0.30)
        ax.add_patch(FancyBboxPatch((xpos, 2.02), w, 0.52, boxstyle="round,pad=0.03",
                                    fc="#E0EDEF", ec=ACCENT[0], lw=1.0))
        ax.text(xpos + w / 2, 2.28, piece.replace(" ", "\u2423"), fontsize=9.2,
                ha="center", va="center", family="monospace", color=INK)
        ax.add_patch(FancyBboxPatch((xpos, 1.02), w, 0.52, boxstyle="round,pad=0.03",
                                    fc="#F0F1F1", ec=TOKENID, lw=1.0))
        ax.text(xpos + w / 2, 1.28, str(tid), fontsize=8.4, ha="center", va="center",
                family="monospace", color=TOKENID, weight="bold")
        ax.annotate("", xy=(xpos + w / 2, 1.60), xytext=(xpos + w / 2, 1.96),
                    arrowprops=dict(arrowstyle="->", color=INK, lw=.8))
        xpos += w + 0.065
    ax.text(1.70, 0.62, "\u2423 marks a leading space, which belongs to the token. "
                        "\"shear\" and \"stirrups\" split mid-word \u2014 eleven token IDs, "
                        "in slate, for nine words.", fontsize=9.0, color=INK)
    ax.text(1.70, 0.14, "* Not only text. An image or a PDF page is cut into small "
                        "squares and turned into numbers in the same window.",
            fontsize=8.0, color=INK, alpha=.75, style="italic")
    ax.set_title("SCHEMATIC — no tokeniser was run. Capture a real split before delivery.",
                 fontsize=9.5, pad=6, color=WARN)
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-tokens.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-tokens.png")


def fig_attention():
    """Which earlier tokens the score for the next one leans on. Arc thickness is the
    weight, and the arcs are drawn below the sentence so no word is obscured.
    ILLUSTRATIVE - the weights are drawn to show the operation, not extracted. A right
    column lists the running example's four candidates with their table probabilities,
    in PROB, `absent` at the top - the arcs feed the scoring that produces this list."""
    words = ["The", "beam", "failed", "in", "shear", "because", "the", "stirrups", "were"]
    weights = [0.02, 0.24, 0.09, 0.01, 0.28, 0.03, 0.01, 0.30, 0.02]

    fig, ax = plt.subplots(figsize=(12.0, 4.05))
    ax.set_xlim(0, 13.2); ax.set_ylim(0, 3.6); _blank(ax)
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
    ax.text(4.9, 0.62, "Thicker arc, larger share of the weighted sum. "
                       "The weights are recomputed for every new token.",
            fontsize=9.5, ha="center", color=INK)

    # right column: the running example's four candidates, absent at the top
    panel_x = 10.75
    ax.plot([panel_x - 0.20, panel_x - 0.20], [0.42, 3.30], color=GRID, lw=1.1)
    ax.text(panel_x, 3.12, "resulting candidates", fontsize=9.2, ha="left", va="center",
            color=INK, weight="bold")
    for i, (c, pv) in enumerate(zip(CANDIDATES, CAND_PROBS)):
        y = 2.55 - i * 0.56
        ax.add_patch(FancyBboxPatch((panel_x, y - 0.21), 2.30, 0.42, boxstyle="round,pad=0.03",
                                    fc="#FBEAEC" if i == 0 else "#F7F9F9",
                                    ec=PROB, lw=1.7 if i == 0 else 0.8))
        ax.text(panel_x + 0.12, y, c.strip(), fontsize=9.7, ha="left", va="center",
                family="monospace", color=INK, weight="bold" if i == 0 else "normal")
        ax.text(panel_x + 2.16, y, f"{pv:.2f}", fontsize=9.7, ha="right", va="center",
                color=PROB, weight="bold")
    ax.set_title("ILLUSTRATIVE weights — drawn to show the operation, not read out of a model.",
                 fontsize=9.5, pad=6, color=WARN)
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-attention.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-attention.png")


def fig_softmax_curve():
    """p( absent ) against temperature, restricted to the two-candidate case where the
    denominator is checkable by hand: `absent` scores 2.0, `corroded` scores 1.0 - the
    only other candidate in this restricted pair. Computed exactly; the three marked
    points are the three rows of the worked table on the slide, so the slide and the
    figure cannot drift. Values unchanged from the original derivation."""
    T = np.linspace(0.12, 3.0, 400)
    p = 1.0 / (1.0 + np.exp(-(2.0 - 1.0) / T))       # exact for two logits
    fig, ax = plt.subplots(figsize=(8.2, 3.15))
    ax.plot(T, p, color=ACCENT[0], lw=2.4)
    ax.axhline(0.5, color=GRID, lw=1.0, ls="--")
    ax.text(2.92, 0.525, "0.5 — absent and corroded become equally likely", fontsize=8.5,
            ha="right", color=INK, alpha=.75)
    for t in (0.5, 1.0, 2.0):
        pv = 1.0 / (1.0 + np.exp(-1.0 / t))
        ax.plot([t], [pv], "o", color=WARN, ms=7, zorder=5)
        ax.annotate(f"T = {t}\np = {pv:.3f}", xy=(t, pv), xytext=(t + 0.12, pv + 0.055),
                    fontsize=9, color=INK)
    ax.set_xlabel("temperature  T  [—]")
    ax.set_ylabel("p( absent )  [—]")
    ax.set_xlim(0, 3.0); ax.set_ylim(0.45, 1.02)
    ax.grid(True, color=GRID, lw=.6); ax.set_axisbelow(True)
    ax.set_title("p( absent ) vs. temperature — absent scores 2.0, corroded 1.0. Computed exactly.",
                 fontsize=10.3, pad=9)
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-softmax-T.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-softmax-T.png")


def fig_loop():
    """Four passes of the loop on the running sentence: The -> The beam ->
    The beam failed -> The beam failed in. Each row shows the tokens supplied so far
    and the distribution over the next one as a proportional strip, with the token
    that was chosen picked out. ILLUSTRATIVE - the distributions are drawn, not
    measured, and are a different prediction task at each position, so they are not
    the running example's four-candidate table (that table is specific to the
    completed sentence's final blank; see fig_scores and fig_attention)."""
    seq = ["The", " beam", " failed", " in"]
    cands = [[" beam", " report", " project", " study"],
             [" failed", " was", " is", " showed"],
             [" in", " due", " because", " under"],
             [" shear", " bending", " flexure", " compression"]]
    dists = [[.55, .20, .15, .10], [.62, .18, .12, .08],
             [.58, .20, .13, .09], [.50, .24, .16, .10]]
    pick = 0                                  # the sampler happened to take the top one

    fig, axes = plt.subplots(4, 1, figsize=(12.8, 4.55))
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

        # proportional strip: 3.05 units wide, split by probability, in PROB
        x0, span = 5.35, 3.05
        for i, (c, pv) in enumerate(zip(cands[r], dists[r])):
            ax.add_patch(Rectangle((x0, 0.30), span * pv, 0.42, fc=PROB,
                                   ec=INK, lw=.6, alpha=1.0 if i == pick else .35))
            if span * pv > 0.55:
                ax.text(x0 + span * pv / 2, 0.51, f"{c.strip()}  {pv:.2f}", fontsize=7.8,
                        ha="center", va="center", color="white" if i == pick else INK)
            x0 += span * pv
        if r == 0:
            ax.text(5.35, 0.13, "probabilities for the next token", fontsize=7.6,
                    color=INK, alpha=.7)
        ax.text(9.95, 0.51, "took " + cands[r][pick].strip(), fontsize=9,
                ha="right", va="center", color=PROB, weight="bold")
    fig.suptitle("ILLUSTRATIVE — the same frozen numbers are read on every pass. "
                 "Only the text handed to them has grown.",
                 fontsize=10, y=1.03, color=WARN)
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

    fig, ax = plt.subplots(figsize=(11.6, 4.05))
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
                ha="center", va="center", color=PARAM, alpha=.85)
        ax.text(8.85, y, f"{b:+.4f}", fontsize=10.5, family="monospace",
                ha="center", va="center", color=PARAM)
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


def fig_corpus_density():
    """STANDALONE - reused unchanged by Chapter 5, so nothing here names a chapter or
    a running example. The argument: a model is reliable in proportion to how much
    has been written about a topic, not how important the topic is. Three bands
    along one axis - common knowledge, an uncertain middle, and genuinely obscure
    territory - with a marker for roughly where a reader's own research literature
    falls. Band widths are an ordering, not a measured scale; nothing here is
    calibrated against a citation count or a token-frequency count."""
    bands = [
        (0.0, 4.0, "common knowledge", "reliable", ACCENT[0]),
        (4.0, 7.3, "the band between", "believes it knows, gets it wrong", WARN),
        (7.3, 10.0, "genuinely obscure", "usually declines, or says so", "#9AA0A0"),
    ]
    fig, ax = plt.subplots(figsize=(11.8, 3.85))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4.3); _blank(ax)
    strip_y, strip_h = 1.55, 0.95
    for x0, x1, name, sub, colour in bands:
        ax.add_patch(Rectangle((x0, strip_y), x1 - x0, strip_h, fc=colour, ec=INK,
                               lw=1.1, alpha=.60))
        ax.text((x0 + x1) / 2, strip_y + strip_h + 0.26, name, fontsize=11.3,
                weight="bold", ha="center", color=INK)
        ax.text((x0 + x1) / 2, strip_y + strip_h / 2, sub, fontsize=8.6, ha="center",
                va="center", color=INK)

    ax.annotate("", xy=(9.9, strip_y - 0.32), xytext=(0.1, strip_y - 0.32),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3))
    ax.text(9.9, strip_y - 0.62, "how much has been written about it", fontsize=9.3,
            ha="right", color=INK)
    ax.text(0.1, strip_y - 0.62, "very little", fontsize=8.3, ha="left", color=INK, alpha=.72)

    pin_x = 5.35                      # inside "the band between"
    ax.plot([pin_x, pin_x], [strip_y + strip_h, 3.55], color=INK, lw=1.2)
    ax.plot([pin_x], [strip_y + strip_h], marker="v", color=INK, ms=8, zorder=5)
    ax.text(pin_x, 3.68, "roughly where your own research\nliterature sits",
            fontsize=8.6, ha="center", va="bottom", color=INK, weight="bold")

    ax.set_title("Reliability tracks how much has been written, not how important the topic is.",
                 fontsize=10.8, pad=10, color=INK)
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-corpus-density.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-corpus-density.png")


def fig_surprise():
    """The chapter's central argument, in three panels. During training the true next
    token is known (panel 1); the model's probability for it starts low (panel 2,
    illustrative, `absent` at about 0.05) and training repeatedly pushes that one bar
    up (panel 3, the table value, 0.41). "Surprise" is only definable relative to a
    probability the model assigned - which is why the output of training has to be a
    distribution, not a single guess. Before/after values are illustrative; the after
    values are the fixed running-example table so this figure and fig_scores agree."""
    before_p = [0.05, 0.33, 0.31, 0.21]     # illustrative — early in training
    after_p = CAND_PROBS                     # [0.41, 0.27, 0.19, 0.02] — the fixed table
    x = np.arange(len(CANDIDATES))

    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(13.4, 3.85))

    # Panel 1 — the training sentence, next word hidden
    a1.set_xlim(0, 10); a1.set_ylim(0, 4); _blank(a1)
    a1.text(5.0, 2.65, "The beam failed in shear because", fontsize=10.2, ha="center", color=INK)
    a1.text(5.0, 2.20, "the stirrups were", fontsize=10.2, ha="center", color=INK)
    a1.add_patch(FancyBboxPatch((6.10, 1.94), 0.62, 0.46, boxstyle="round,pad=0.03",
                                fc="#F0F1F1", ec=TOKENID, lw=1.3))
    a1.text(6.41, 2.17, "\u2423", fontsize=12, ha="center", va="center",
            color=TOKENID, weight="bold")
    a1.text(5.0, 1.05, "during training, the true\nnext token is known", fontsize=9.2,
            ha="center", color=INK, style="italic")
    a1.set_title("1. a training example", fontsize=10.5, pad=8, color=INK)

    # Panel 2 — probability assigned to the true token, early: low
    for i, (c, pv) in enumerate(zip(CANDIDATES, before_p)):
        true_tok = (i == 0)
        a2.bar([i], [pv], color=PROB, edgecolor=INK,
               linewidth=1.8 if true_tok else .6, alpha=1.0 if true_tok else .40)
    a2.set_xticks(x); a2.set_xticklabels([c.strip() for c in CANDIDATES], fontsize=9)
    a2.set_ylim(0, 0.5); a2.set_ylabel("probability")
    a2.yaxis.grid(True, color=GRID, lw=.6); a2.set_axisbelow(True)
    a2.annotate("surprise = how low\nthis bar was", xy=(0, before_p[0]),
                xytext=(0.55, 0.34), fontsize=8.8, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=.9))
    a2.set_title("2. early in training", fontsize=10.5, pad=8, color=INK)

    # Panel 3 — same bars, after many updates: absent now high
    for i, (c, pv) in enumerate(zip(CANDIDATES, after_p)):
        true_tok = (i == 0)
        a3.bar([i], [pv], color=PROB, edgecolor=INK,
               linewidth=1.8 if true_tok else .6, alpha=1.0 if true_tok else .40)
    a3.set_xticks(x); a3.set_xticklabels([c.strip() for c in CANDIDATES], fontsize=9)
    a3.set_ylim(0, 0.5)
    a3.yaxis.grid(True, color=GRID, lw=.6); a3.set_axisbelow(True)
    a3.annotate("training pushes this bar up,\nbillions of times, over\nbillions of sentences",
                xy=(0, after_p[0]), xytext=(0.55, 0.34), fontsize=8.6, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=.9))
    a3.set_title("3. after training", fontsize=10.5, pad=8, color=INK)

    fig.text(0.5, -0.06, "You cannot define \"surprised\" without a probability. "
                          "The distribution is what training shaped.",
             fontsize=10.5, ha="center", color=INK, weight="bold")
    fig.tight_layout()
    for d in (OUT, PUB):
        fig.savefig(d / "01-surprise.png", dpi=200, bbox_inches="tight")
    plt.close(fig); print("wrote 01-surprise.png")


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
    fig_corpus_density()
    fig_surprise()

    # ---------------------------------------------------------------------
    # Aspect-ratio audit. Reads every PNG this run just wrote (OUT, not PUB -
    # the two are byte-identical copies) and reports width, height and the
    # w:h ratio actually achieved after bbox_inches="tight" cropping, which
    # is the only place that ratio is decided - figsize is a starting point,
    # not the final word once tight-bbox has trimmed whitespace.
    # ---------------------------------------------------------------------
    from PIL import Image
    print("\n--- aspect-ratio audit (target 2.6:1 to 3.4:1) ---")
    rows = []
    for png in sorted(OUT.glob("*.png")):
        with Image.open(png) as im:
            w, h = im.size
        ratio = w / h
        ok = 2.6 <= ratio <= 3.4
        rows.append((png.name, w, h, ratio, ok))
    name_w = max(len(r[0]) for r in rows)
    for name, w, h, ratio, ok in rows:
        flag = "PASS" if ok else "OUT OF RANGE"
        print(f"{name:<{name_w}}  {w:5d} x {h:4d} px   {ratio:5.2f} : 1   {flag}")
