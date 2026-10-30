import csv
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, NullLocator
from common import f17, save_text, EPS, U, RESULTS, PLOTS

# Prediction: Delta+(x) ~ x * 2^-52 (slope 1 on log-log); q(x) stays in (1/2, 1]

# ---- Task 2: compute the spacing at 100 log-spaced points ----
xs = np.logspace(-300, 300, 100, dtype=np.float64)
rows = []
for xv in xs:
    x = float(xv)                        # the stored value we analyse
    succ = math.nextafter(x, math.inf)   # next float above x
    dplus = succ - x                     # absolute spacing
    r = dplus / x                        # relative spacing
    q = r / EPS                          # normalized relative spacing
    rows.append((x, succ, dplus, r, q))

with open(RESULTS / "spacing.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["x", "successor", "delta_plus", "r", "q"])
    for row in rows:
        w.writerow([f17(v) for v in row])

X = np.array([row[0] for row in rows])
D = np.array([row[2] for row in rows])
R = np.array([row[3] for row in rows])
Q = np.array([row[4] for row in rows])

# Matplotlib's automatic log ticks overflow near 1e308, so set them by hand
DECADES = [10.0**k for k in range(-300, 301, 100)]

def fix_log_axis(axis, lo, hi):
    axis.set_major_locator(FixedLocator(DECADES))
    axis.set_minor_locator(NullLocator())

# Figure 1: absolute spacing (log-log)
fig, ax = plt.subplots(figsize=(6.5, 4.2))
ax.loglog(X, D, "o", ms=3)
ax.set_xlim(1e-305, 1e305); ax.set_ylim(1e-318, 1e290)
fix_log_axis(ax.xaxis, 0, 0); fix_log_axis(ax.yaxis, 0, 0)
ax.set_xlabel("x (stored binary64 value)")
ax.set_ylabel(r"Absolute spacing $\Delta^+(x)$")
ax.set_title("Absolute spacing of binary64 numbers")
ax.grid(True, alpha=0.4)
fig.tight_layout(); fig.savefig(PLOTS / "fig1_absolute_spacing.png", dpi=150)

# ---- Task 3: relative spacing ----
# Figure 2: normalized relative spacing q(x)
fig, ax = plt.subplots(figsize=(6.5, 4.2))
ax.semilogx(X, Q, "o", ms=3, label="samples")
ax.axhline(1.0, color="C3", ls="--", label=r"1  ($\epsilon_{mach}$)")
ax.axhline(0.5, color="C2", ls="--", label=r"1/2  ($u$)")
ax.set_xlim(1e-305, 1e305); ax.set_ylim(0.45, 1.05)
fix_log_axis(ax.xaxis, 0, 0)
ax.set_xlabel("x (stored binary64 value)")
ax.set_ylabel("Relative spacing / machine epsilon")
ax.set_title("Normalized relative spacing")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=3, frameon=False)
ax.grid(True, alpha=0.4)
fig.tight_layout(); fig.savefig(PLOTS / "fig2_relative_spacing.png", dpi=150)

lines = [
    f"samples               : {len(rows)}",
    f"first x / last x      : {f17(X[0])} / {f17(X[-1])}",
    f"Delta+ min / max      : {f17(D.min())} / {f17(D.max())}",
    f"min r                 : {f17(R.min())}   q = {f17(Q.min())}",
    f"max r                 : {f17(R.max())}   q = {f17(Q.max())}",
    f"u / eps_mach          : {f17(U)} / {f17(EPS)}",
    f"all u < r <= eps      : {bool(np.all((R > U) & (R <= EPS)))}",
]
save_text("task2_3_spacing.txt", lines)
print("saved results/spacing.csv and plots/fig1, fig2")