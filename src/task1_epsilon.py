import math
import sys
from common import f17, save_text, U

# Prediction: last_changed = 2^-52, first_unchanged = 2^-53
eps = 1.0
last_changed = None
while 1.0 + eps != 1.0:   # equality on purpose: did the stored value change?
    last_changed = eps
    eps = eps / 2.0
first_unchanged = eps

gap_above_1 = math.nextafter(1.0, math.inf) - 1.0

lines = [
    f"last_changed           = {f17(last_changed)}  = 2^{int(math.log2(last_changed))}",
    f"first_unchanged        = {f17(first_unchanged)}  = 2^{int(math.log2(first_unchanged))}",
    f"nextafter(1, inf) - 1  = {f17(gap_above_1)}",
    f"sys.float_info.epsilon = {f17(sys.float_info.epsilon)}",
    f"all three equal        : {last_changed == gap_above_1 == sys.float_info.epsilon}",
    f"unit roundoff u        = {f17(U)}",
    f"1 + 2^-53 == 1         : {1.0 + first_unchanged == 1.0}",
]
save_text("task1_epsilon.txt", lines)