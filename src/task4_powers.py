import math
import numpy as np
import matplotlib.pyplot as plt
from common import f17, save_text, EPS, PLOTS

# Prediction: at x = 2^e the gap below is 2^(e-53) and the gap above is 2^(e-52), so the ratio is 2

lines = [f"{'x':>4} {'Delta-':>24} {'Delta+':>24} {'ratio':>6}  {'neg check':>9}  {'up-gap at -x':>24}"]
for x in [1.0, 2.0, 4.0, 8.0]:
    dm = x - math.nextafter(x, -math.inf)          # gap below x
    dp = math.nextafter(x, math.inf) - x           # gap above x
    neg_check = ((-x) - math.nextafter(-x, -math.inf)) == dp   # down from -x == up from x?
    up_at_neg = math.nextafter(-x, math.inf) - (-x)            # up from -x (towards 0)
    lines.append(f"{x:4g} {f17(dm):>24} {f17(dp):>24} {dp/dm:6g}  {str(neg_check):>9}  {f17(up_at_neg):>24}")

# Local plot on [0.5, 4] with the exact powers of two included
loc = np.unique(np.concatenate([np.linspace(0.5, 4.0, 200), [0.5, 1.0, 2.0, 4.0]]))
gap = np.array([math.nextafter(float(v), math.inf) - float(v) for v in loc])
lines.append(f"local samples after removing duplicates: {len(loc)}")

fig, ax = plt.subplots(figsize=(6.5, 4.2))
ax.plot(loc, gap / EPS, "o", ms=3)                 # markers only, no connecting line
for b in [1, 2, 4]:
    ax.axvline(b, color="grey", lw=0.6, ls=":")
ax.set_xlabel("x")
ax.set_ylabel(r"Upward spacing $\Delta^+(x)\,/\,\epsilon_{mach}$")
ax.set_title("Upward spacing on [0.5, 4] (linear axes)")
ax.grid(True, alpha=0.4)
fig.tight_layout(); fig.savefig(PLOTS / "fig3_boundary_spacing.png", dpi=150)

save_text("task4_powers.txt", lines)
print("saved plots/fig3_boundary_spacing.png")