"""
Corrected activation function comparison.

Tier 1: Fixed ReLU (61 params)
Tier 2: PReLU — learnable negative slope per neuron (81 params)
Tier 3: B-spline activation — locally supported, learnable shape per neuron (301 params)

Three target functions: smooth, piecewise linear, oscillatory.
All: 20 neurons, 1 hidden layer, Adam, 3000 epochs, lr=1e-3.
"""

import torch, torch.nn as nn, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Liberation Serif", "DejaVu Serif"],
    "mathtext.fontset": "stix", "font.size": 12,
    "axes.linewidth": 0.7, "axes.unicode_minus": False,
})

torch.manual_seed(42); np.random.seed(42)
WIDTH, EPOCHS, LR = 20, 2000, 2e-3
TEAL, CORAL, SLATE = "#0F6E56", "#B5501F", "#3B5F6B"

# ── Targets ──────────────────────────────────────────────────────
targets = [
    (lambda x: torch.sin(x),
     r"$f(x) = \sin(x)$", "Smooth"),
    (lambda x: torch.abs(x) - 0.5*x,
     r"$f(x) = |x| - 0.5x$", "Piecewise Linear"),
    (lambda x: torch.sin(5*x)*torch.exp(-x**2),
     r"$f(x) = \sin(5x)\,e^{-x^2}$", "Oscillatory"),
]

# ── B-spline basis (locally supported, stable) ───────────────────
class BSplineBasis(nn.Module):
    def __init__(self, n_bases=12, degree=3, lo=-4.0, hi=4.0):
        super().__init__()
        self.degree = degree
        self.n_bases = n_bases
        knots = torch.linspace(lo, hi, n_bases + degree + 1)
        self.register_buffer("knots", knots)

    def forward(self, u):
        k = self.knots
        B = {}
        for i in range(len(k) - 1):
            B[(i, 0)] = ((u >= k[i]) & (u < k[i+1])).float()
        for p in range(1, self.degree + 1):
            for i in range(len(k) - p - 1):
                d1 = k[i+p] - k[i]; d2 = k[i+p+1] - k[i+1]
                left  = ((u - k[i]) / d1 * B[(i, p-1)]) if d1 > 0 else 0
                right = ((k[i+p+1] - u) / d2 * B[(i+1, p-1)]) if d2 > 0 else 0
                B[(i, p)] = left + right
        return torch.stack([B[(i, self.degree)] for i in range(self.n_bases)], dim=-1)

class BSplineActivation(nn.Module):
    def __init__(self, n_neurons, n_bases=12):
        super().__init__()
        self.basis = BSplineBasis(n_bases)
        self.coeffs = nn.Parameter(torch.zeros(n_neurons, n_bases))
        nn.init.normal_(self.coeffs, 0, 0.1)
        self.residual = nn.Parameter(torch.ones(n_neurons))
    def forward(self, u):
        B = self.basis(u)
        return (B * self.coeffs.unsqueeze(0)).sum(-1) + self.residual * u

# ── Networks ─────────────────────────────────────────────────────
class FixedReLU(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(1, WIDTH), nn.ReLU(), nn.Linear(WIDTH, 1))
    def forward(self, x): return self.net(x)

class PartialPReLU(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(1, WIDTH)
        self.act = nn.PReLU(num_parameters=WIDTH)
        self.fc2 = nn.Linear(WIDTH, 1)
    def forward(self, x): return self.fc2(self.act(self.fc1(x)))

class FullyLearnableBSpline(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(1, WIDTH)
        self.act = BSplineActivation(WIDTH, n_bases=12)
        self.fc2 = nn.Linear(WIDTH, 1)
    def forward(self, x): return self.fc2(self.act(self.fc1(x)))

models_spec = [
    (FixedReLU,             "Tier 1: Fixed \u03C6 (ReLU)",         SLATE),
    (PartialPReLU,          "Tier 2: Learnable Slope (PReLU)",   CORAL),
    (FullyLearnableBSpline, "Tier 3: Learnable Shape (B-Spline)",TEAL),
]

# ── Training ─────────────────────────────────────────────────────
x_train = torch.linspace(-3, 3, 400).unsqueeze(1)
x_test  = torch.linspace(-3, 3, 1000).unsqueeze(1)

results = {}
for ti, (fn, label, short) in enumerate(targets):
    y_train, y_test = fn(x_train), fn(x_test)
    for mi, (Cls, mname, _) in enumerate(models_spec):
        best_mse, best_pred = float("inf"), None
        for trial in range(1):                     # 3 random seeds, keep best
            torch.manual_seed(42 + trial * 7)
            model = Cls()
            opt = torch.optim.Adam(model.parameters(), lr=LR)
            for epoch in range(EPOCHS):
                loss = nn.MSELoss()(model(x_train), y_train)
                opt.zero_grad(); loss.backward(); opt.step()
            with torch.no_grad():
                pred = model(x_test).squeeze().numpy()
                mse = float(nn.MSELoss()(model(x_test), y_test))
            if mse < best_mse:
                best_mse, best_pred = mse, pred
                if Cls == FullyLearnableBSpline:
                    best_model = model
        results[(ti, mi)] = {"pred": best_pred, "mse": best_mse}
        print(f"  {short:20s} | {mname:40s} | MSE = {best_mse:.6f}")
    print()

print("Parameter counts:")
for Cls, mname, _ in models_spec:
    n = sum(p.numel() for p in Cls().parameters())
    print(f"  {mname:40s}: {n:5d}")

# ── Figure 1: 3x3 comparison grid ────────────────────────────────
fig, axes = plt.subplots(3, 3, figsize=(10.5, 9.5))
fig.subplots_adjust(left=0.08, right=0.97, bottom=0.065, top=0.935,
                    hspace=0.35, wspace=0.26)

x_np = x_test.squeeze().numpy()
for ti, (fn, label, short) in enumerate(targets):
    y_true = fn(x_test).squeeze().numpy()
    for mi, (_, mname, col) in enumerate(models_spec):
        ax = axes[ti, mi]
        ax.plot(x_np, y_true, "k-", lw=1.8, label="Target", zorder=3)
        pred = results[(ti, mi)]["pred"]
        mse  = results[(ti, mi)]["mse"]
        ax.plot(x_np, pred, "-", color=col, lw=1.6, alpha=0.9,
                label=f"Fit (MSE = {mse:.1e})", zorder=4)
        ax.fill_between(x_np, y_true, pred, color=col, alpha=0.08, zorder=2)
        ax.set_xlim(-3.1, 3.1)
        ax.legend(fontsize=8.8, frameon=False, loc="best")
        for s in ("top", "right"): ax.spines[s].set_visible(False)
        ax.tick_params(labelsize=9.5)
        if ti == 0:
            ax.set_title(mname, fontsize=11, pad=6, color=col, fontweight="bold")
        if mi == 0:
            ax.set_ylabel(label, fontsize=11.5)
        if ti == 2:
            ax.set_xlabel("$x$", fontsize=11.5)

fig.suptitle("Three Activation Strategies \u00d7 Three Target Functions",
             fontsize=13.5, y=0.98)

for ext in ("png", "svg", "pdf"):
    fig.savefig(f"/mnt/user-data/outputs/activation_comparison.{ext}",
                dpi=400, facecolor="white")

# ── Figure 2: learned B-spline shapes ────────────────────────────
fig2, axes2 = plt.subplots(1, 3, figsize=(10.5, 3.8))
fig2.subplots_adjust(left=0.06, right=0.97, bottom=0.14, top=0.82, wspace=0.25)

for ti, (fn, label, short) in enumerate(targets):
    ax = axes2[ti]
    torch.manual_seed(42)
    model = FullyLearnableBSpline()
    y_train = fn(x_train)
    opt = torch.optim.Adam(model.parameters(), lr=LR)
    for epoch in range(EPOCHS):
        loss = nn.MSELoss()(model(x_train), y_train)
        opt.zero_grad(); loss.backward(); opt.step()
    u_range = torch.linspace(-3, 3, 500)
    with torch.no_grad():
        for j in range(WIDTH):
            u_j = u_range.unsqueeze(1).expand(-1, WIDTH)
            phi = model.act(u_j)[:, j].numpy()
            ax.plot(u_range.numpy(), phi, lw=0.7, alpha=0.55, color=TEAL)
    ax.plot(u_range.numpy(), np.maximum(0, u_range.numpy()),
            "k--", lw=1.4, label="ReLU (Reference)")
    ax.set_title(short, fontsize=11.5)
    ax.set_xlabel("$u$ (Pre-Activation Value)", fontsize=10.5)
    if ti == 0: ax.set_ylabel(r"$\varphi(u)$", fontsize=11.5)
    ax.legend(fontsize=9, frameon=False)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.tick_params(labelsize=9.5)
    ax.set_xlim(-3.1, 3.1); ax.set_ylim(-3, 4)

fig2.suptitle("Tier 3: Learned B-Spline Activation Shapes (20 Neurons Each)",
              fontsize=12.5, y=0.95)
for ext in ("png", "svg", "pdf"):
    fig2.savefig(f"/mnt/user-data/outputs/learned_activations.{ext}",
                 dpi=400, facecolor="white")
print("\nDone.")
