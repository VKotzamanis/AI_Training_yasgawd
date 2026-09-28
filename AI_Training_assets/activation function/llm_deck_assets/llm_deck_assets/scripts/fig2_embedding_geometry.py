"""
Figure 2. Embedding geometry before and after training.
Panel (a): 100-dimensional vectors drawn from N(0, 0.02^2), the standard
           initialisation of an embedding matrix.
Panel (b): the same 16 words as pretrained GloVe-100 vectors
           (Pennington et al., 2014; 6B-token corpus).
Each panel is projected to its own first two principal components.

Font: 'Times New Roman' is requested first; falls back to Liberation Serif,
which is metrically identical.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scipy.spatial import ConvexHull
from scipy.interpolate import splprep, splev

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Liberation Serif", "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "font.size": 12.5,
    "axes.linewidth": 0.7,
    "xtick.direction": "out", "ytick.direction": "out",
    "xtick.major.width": 0.7, "ytick.major.width": 0.7,
    "xtick.major.size": 3.0, "ytick.major.size": 3.0,
    "axes.unicode_minus": False,
})

TEAL, CORAL, GREY, RED = "#0F6E56", "#B5501F", "#6E6E6E", "#A32020"

WORDS = ["beam", "shear", "load", "stress", "truss",
         "stir", "fried", "sauce", "simmer", "wok",
         "the", "on", "were", "of", "and", "stirrups"]
GROUPS = [("Structural Terms", range(0, 5), TEAL, "o"),
          ("Cooking Terms", range(5, 10), CORAL, "s"),
          ("Function Words", range(10, 15), GREY, "^")]

# hand-tuned label offsets (points); leader lines drawn when the offset is large
OFF = {"stress": (-5, -1, "right"), "load": (-5, -1, "right"),
       "beam": (-5, -1, "right"), "shear": (6, -1, "left"),
       "truss": (6, -1, "left"), "stir": (0, -13, "center"),
       "fried": (-6, -1, "right"), "sauce": (6, -6, "left"),
       "simmer": (6, -1, "left"), "wok": (6, -1, "left"),
       "the": (-14, 12, "right"), "on": (8, 14, "left"),
       "of": (17, -3, "left"), "were": (-14, -13, "right"),
       "and": (7, -15, "left"), "stirrups": (7, -2, "left")}

IS = WORDS.index("stirrups")


def pca2(X):
    Xc = X - X.mean(0)
    U, S, _ = np.linalg.svd(Xc, full_matrices=False)
    ev = 100.0 * S ** 2 / np.sum(S ** 2)
    return U[:, :2] * S[:2], ev[:2]


def blob(ax, P, color, pad=0.11):
    """Smooth, padded closed curve around a group of points."""
    span = np.ptp(P, axis=0).max()
    r = pad * max(span, 1e-9) + 0.25 * span
    H = P[ConvexHull(P).vertices] if len(P) >= 3 else P
    c = H.mean(0)
    d = H - c
    E = H + r * d / np.linalg.norm(d, axis=1, keepdims=True)
    tck, _ = splprep([np.r_[E[:, 0], E[0, 0]], np.r_[E[:, 1], E[0, 1]]],
                     s=0, per=True)
    x, y = splev(np.linspace(0, 1, 400), tck)
    ax.fill(x, y, color=color, alpha=0.07, zorder=1)
    ax.plot(x, y, color=color, lw=0.9, ls=(0, (5, 3)), alpha=0.85, zorder=2)


G = np.load("/home/claude/glove_sub.npy")
rng = np.random.default_rng(11)
R = rng.normal(0.0, 0.02, size=G.shape)

fig, axes = plt.subplots(1, 2, figsize=(7.48, 4.35))
fig.subplots_adjust(left=0.105, right=0.985, bottom=0.235, top=0.925, wspace=0.30)

for ax, X, tag, title in zip(axes, [R, G], ["(a)", "(b)"],
                             ["Random Initialisation",
                              "After Training (GloVe Word Vectors)"]):
    Y, ev = pca2(X)
    for _, idx, col, mk in GROUPS:
        P = Y[list(idx)]
        blob(ax, P, col)
        ax.plot(P[:, 0], P[:, 1], mk, ms=5.2, mfc=col, mec=col, lw=0, zorder=4)
        if tag == "(b)":
            for (x, y), w in zip(P, [WORDS[i] for i in idx]):
                dx, dy, ha = OFF[w]
                far = abs(dx) > 12 or abs(dy) > 12
                ax.annotate(w, (x, y), textcoords="offset points", ha=ha,
                            xytext=(dx, dy), fontsize=10.6, color=col, zorder=5,
                            arrowprops=dict(arrowstyle="-", color=col, lw=0.5,
                                            shrinkA=1, shrinkB=3) if far else None)
    ax.plot(Y[IS, 0], Y[IS, 1], "D", ms=6.2, mfc="none", mec=RED, mew=1.3,
            zorder=6)
    if tag == "(b)":
        ax.annotate("stirrups", (Y[IS, 0], Y[IS, 1]), textcoords="offset points",
                    xytext=(7, -2), fontsize=10.6, color=RED, zorder=6)

    ax.set_xlabel(f"PC 1: Direction of Largest Spread\n({ev[0]:.1f} % of Variance)",
                  fontsize=11.5, linespacing=1.35)
    ax.set_ylabel(f"PC 2: Next Largest\n({ev[1]:.1f} %)",
                  fontsize=11.5, linespacing=1.35)
    ax.set_title(title, fontsize=12.5, pad=7)
    ax.tick_params(labelsize=10.5)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.margins(0.14)

# quantitative annotation: 'stir' is unrelated to 'stirrups'
Yg, _ = pca2(G)
i_stir = WORDS.index("stir")
c = (G[IS] @ G[i_stir]) / (np.linalg.norm(G[IS]) * np.linalg.norm(G[i_stir]))
axes[1].annotate("", xy=Yg[IS], xytext=Yg[i_stir],
                 arrowprops=dict(arrowstyle="-", color=RED, lw=0.8,
                                 ls=(0, (3, 3)), shrinkA=5, shrinkB=6))
axes[1].text(1.15, 0.05, f"cosine similarity\n= {c:+.2f}", fontsize=10.8,
             color=RED, ha="right", va="center", linespacing=1.35)

handles = [Line2D([], [], marker=m, ls="", mfc=c_, mec=c_, ms=5.6, label=n)
           for n, _, c_, m in GROUPS]
handles.append(Line2D([], [], marker="D", ls="", mfc="none", mec=RED, mew=1.2,
                      ms=6.2, label="Fragment Token"))
axes[0].legend(handles=handles, fontsize=10.4, frameon=False, loc="lower left",
               handletextpad=0.35, borderpad=0.1, labelspacing=0.28)

fig.text(0.5, 0.028,
         "GloVe: publicly released word vectors, trained by counting how often "
         "words occur near each other in a 6-billion-word corpus.",
         ha="center", fontsize=9.8, color="#444444", style="italic")

for ext in ("png", "svg", "pdf"):
    fig.savefig(f"/mnt/user-data/outputs/fig2_embedding_geometry.{ext}",
                dpi=600, facecolor="white")
print(f"cos(stir, stirrups) = {c:+.4f}")
