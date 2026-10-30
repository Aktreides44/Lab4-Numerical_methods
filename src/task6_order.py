
import math
from common import f17, save_text

a = 1e16
b = -1e16
c = 1.0
# Prediction: (a+b)+c = 1 (exact), a+(b+c) = 0 because c is lost in b+c

left = (a + b) + c
right = a + (b + c)

gap_b = math.nextafter(b, math.inf) - b      # spacing near 1e16
up_b = math.nextafter(b, math.inf)           # the float just above b


def loop_sum(values):
    """Explicit left-to-right sum, one addition at a time."""
    total = 0.0
    for v in values:
        total = total + v
    return total


lines = [
    f"a + b            = {f17(a + b)}",
    f"b + c            = {f17(b + c)}   (b + c == b: {(b + c) == b})",
    f"(a + b) + c      = {f17(left)}",
    f"a + (b + c)      = {f17(right)}",
    "exact result     = 1",
    f"gap near b       = {f17(gap_b)}   (c == gap/2: {c == gap_b / 2})",
    f"b       = {int(b)} = {int(b) // 2} x 2",
    f"b + gap = {int(up_b)} = {int(up_b) // 2} x 2",
]
for order in ([a, c, b], [a, b, c]):
    lines.append(f"order {order}: loop = {f17(loop_sum(order))}   fsum = {f17(math.fsum(order))}")

save_text("task6_order.txt", lines)