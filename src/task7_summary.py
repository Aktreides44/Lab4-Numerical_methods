from common import RESULTS, save_text

parts = [
    ("ENVIRONMENT", "task0_environment.txt"),
    ("TASK 1 - EPSILON", "task1_epsilon.txt"),
    ("TASKS 2-3 - SPACING", "task2_3_spacing.txt"),
    ("TASK 4 - POWERS OF TWO", "task4_powers.txt"),
    ("TASK 5 - LAB 2 CONNECTION", "task5_lab2.txt"),
    ("TASK 6 - ADDITION ORDER", "task6_order.txt"),
]
lines = []
for title, fname in parts:
    lines.append(f"===== {title} =====")
    lines += (RESULTS / fname).read_text(encoding="utf-8").splitlines()
    lines.append("")
save_text("summary.txt", lines)