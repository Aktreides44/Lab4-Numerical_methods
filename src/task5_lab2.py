import math
from common import f17, save_text

# Lab 2 values, entered manually from my Lab 2 report (Table 1, Python, run under WSL)
n_stop = 94_906_266            # first index whose addition left the sum unchanged
s = 1.644934057834575          # stored sum after the last successful update
# Prediction: s is in [1, 2), so gap = 2^-52; the term should be just below half the gap

gap = math.nextafter(s, math.inf) - s
x = float(n_stop)
term = 1.0 / (x * x)               # same expression as in Lab 2
candidate = s + term

xp = float(n_stop - 1)             # the last term that was still added
term_prev = 1.0 / (xp * xp)

k_est = math.sqrt(2.0 / gap)       # solve 1/k^2 = gap/2
tail_lo = 1.0 / n_stop             # bounds on the remaining tail sum_{k>=n_stop} 1/k^2
tail_hi = 1.0 / (n_stop - 1)

lines = [
    "Source: Lab 2 report, Table 1 (Python), entered manually",
    f"n_stop              = {n_stop}",
    f"s                   = {f17(s)}   (hex {s.hex()})",
    f"gap above s         = {f17(gap)}   (= 2^-52: {gap == 2**-52})",
    f"term 1/n_stop^2     = {f17(term)}",
    f"term / gap          = {f17(term / gap)}",
    f"candidate == s      : {candidate == s}",
    f"previous term / gap = {f17(term_prev / gap)}   (index {n_stop - 1})",
    f"k_est = sqrt(2/gap) = {f17(k_est)}   (= 2^{math.log2(k_est)})",
    f"tail bounds         : {f17(tail_lo)} < R < {f17(tail_hi)}",
    f"tail / lost term    = {f17(tail_lo / term)}",
]
save_text("task5_lab2.txt", lines)