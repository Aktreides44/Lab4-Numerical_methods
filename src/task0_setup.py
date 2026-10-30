import sys
import platform
import numpy as np
import matplotlib
from common import save_text

lines = [
    f"Python     : {sys.version.split()[0]}",
    f"NumPy      : {np.__version__}",
    f"Matplotlib : {matplotlib.__version__}",
    f"OS         : {platform.platform()}",
    f"radix      : {sys.float_info.radix}",
    f"mant_dig   : {sys.float_info.mant_dig}",
]
ok = sys.float_info.radix == 2 and sys.float_info.mant_dig == 53
lines.append("binary64 confirmed" if ok else "WARNING: not binary64!")
save_text("task0_environment.txt", lines)