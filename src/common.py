import math
from pathlib import Path

# Folders (work no matter where you run the script from)
ROOT = Path(__file__).resolve().parent.parent
RESULTS = ROOT / "results"
PLOTS = ROOT / "plots"
RESULTS.mkdir(exist_ok=True)
PLOTS.mkdir(exist_ok=True)

# Machine epsilon (definition 1 in the handout) and unit roundoff
EPS = math.nextafter(1.0, math.inf) - 1.0
U = EPS / 2


def f17(x):
    """Format a float with 17 significant digits."""
    return format(x, ".17g")


def save_text(name, lines):
    """Print lines and also save them to results/<name>.txt."""
    text = "\n".join(lines)
    print(text)
    (RESULTS / name).write_text(text + "\n", encoding="utf-8")