import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = ["Times New Roman", "Liberation Serif", "DejaVu Serif"]
plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["axes.unicode_minus"] = False

RED, TEAL, TEAL_D, TEAL_L = "#C00000", "#0F6E56", "#085041", "#E1F5EE"
SLATE, GREY_B, INK = "#3B5F6B", "#909090", "#000000"


def canvas(w_in, W, H):
    fig = plt.figure(figsize=(w_in, w_in * H / W))
    ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H)
    ax.set_aspect("equal"); ax.axis("off")
    return fig, ax


def rbox(ax, x, y, w, h, ec, fc="white", lw=1.6, r=7, z=3):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                 boxstyle=f"round,pad=0,rounding_size={r}", linewidth=lw,
                 edgecolor=ec, facecolor=fc, zorder=z, mutation_aspect=1))


def txt(ax, x, y, s, size, color=INK, weight="normal", style="normal",
        ha="center", va="center", z=6):
    ax.text(x, y, s, fontsize=size, color=color, fontweight=weight,
            fontstyle=style, ha=ha, va=va, zorder=z)


def arrow(ax, x1, y1, x2, y2, color=SLATE, lw=1.6):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                 mutation_scale=16, linewidth=lw, color=color, zorder=4,
                 shrinkA=0, shrinkB=0))


# ======================================================================
# FIGURE 1 : token id -> row of E -> input tensor
# ======================================================================
W, H = 1000.0, 360.0
fig, ax = canvas(10.0, W, H)

rows = [275, 195, 115]
toks = ["stir", "r", "ups"]
ids = ["32362", "81", "14409"]
vecs = ["[ 0.02   \u22120.31   \u2026   0.14 ]",
        "[ \u22120.45   0.08   \u2026   \u22120.62 ]",
        "[ 0.31   0.62   \u2026   0.27 ]"]

MX0, MX1, MY0, MY1 = 375.0, 655.0, 55.0, 335.0
GUT = MX0 + 72.0
XX0, XX1, BH = 730.0, 995.0, 54.0

vals = {275: ["0.02", "\u22120.31", "0.77", "\u2026"],
        195: ["\u22120.45", "0.08", "0.19", "\u2026"],
        115: ["0.31", "0.62", "\u22120.05", "\u2026"]}
filler = {315: ["\u2026", "\u2026", "\u2026", "\u2026"],
          235: ["0.14", "0.55", "\u22120.72", "\u2026"],
          155: ["\u22120.09", "\u22120.41", "0.36", "\u2026"],
          75: ["\u2026", "\u2026", "\u2026", "\u2026"]}

ax.add_patch(Rectangle((MX0, MY0), MX1 - MX0, MY1 - MY0, facecolor="white",
                       edgecolor=TEAL, linewidth=1.6, zorder=2))
ax.add_patch(Rectangle((MX0, MY0), GUT - MX0, MY1 - MY0, facecolor="#F4F4F4",
                       edgecolor="none", zorder=2.1))
for k in range(1, 7):
    y = MY0 + k * (MY1 - MY0) / 7.0
    ax.plot([MX0, MX1], [y, y], color="#D8D8D8", lw=0.7, zorder=2.4)
for k in range(1, 4):
    x = GUT + k * (MX1 - GUT) / 4.0
    ax.plot([x, x], [MY0, MY1], color="#E8E8E8", lw=0.6, zorder=2.4)
ax.plot([GUT, GUT], [MY0, MY1], color="#C0C0C0", lw=1.0, zorder=2.5)

CW = (MX1 - GUT) / 4.0
for cy, row in filler.items():
    for j, v in enumerate(row):
        txt(ax, GUT + CW * (j + 0.5), cy, v, 12.5, "#9A9A9A")

for cy, tk, tid in zip(rows, toks, ids):
    rbox(ax, 15, cy - BH / 2, 125, BH, RED)
    txt(ax, 77, cy, tk, 20, RED, weight="bold")
    arrow(ax, 145, cy, 167, cy, GREY_B, 1.2)
    rbox(ax, 172, cy - BH / 2, 135, BH, RED)
    txt(ax, 239, cy, tid, 19, RED, weight="bold")
    arrow(ax, 312, cy, MX0 - 5, cy)
    ax.add_patch(Rectangle((MX0, cy - 20), MX1 - MX0, 40, facecolor=TEAL_L,
                           edgecolor=TEAL, linewidth=1.3, zorder=3))
    txt(ax, (MX0 + GUT) / 2, cy, tid, 12.5, TEAL_D, weight="bold")
    for j, v in enumerate(vals[cy]):
        txt(ax, GUT + CW * (j + 0.5), cy, v, 13.5, TEAL_D, weight="bold")
    arrow(ax, MX1 + 5, cy, XX0 - 5, cy)
    rbox(ax, XX0, cy - BH / 2, XX1 - XX0, BH, TEAL, TEAL_L)
    txt(ax, (XX0 + XX1) / 2, cy,
        "[  " + "   ".join(vals[cy][:3]) + "   \u2026  ]", 14, TEAL_D)

txt(ax, (MX0 + MX1) / 2, 34, "E   (200,019 \u00d7 d)", 17, TEAL_D)
txt(ax, (MX0 + MX1) / 2, 11, "Every Number Here Is a Trained Weight", 14, INK,
    style="italic")
txt(ax, (XX0 + XX1) / 2, 34, "X   (n \u00d7 d)", 17, TEAL_D)
txt(ax, (XX0 + XX1) / 2, 11, "Copies, Rebuilt for Every Prompt", 14, INK,
    style="italic")

for ext in ("png", "svg", "pdf"):
    fig.savefig(f"/mnt/user-data/outputs/fig1_token_to_row.{ext}", dpi=600,
                facecolor="white")

