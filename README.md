# Lab 4 – Floating-Point Representation (Python, binary64)

Numerical Methods · Akash

This lab measures the spacing between neighbouring binary64 numbers and uses it to explain why the
Basel sum in Lab 2 stopped changing at term 94,906,266.

## Environment
- Python 3.14.4
- NumPy 2.5.1
- Matplotlib 3.11.2
- Windows 11 (10.0.26200)
- binary64 confirmed: `sys.float_info.radix == 2` and `sys.float_info.mant_dig == 53`

## Folder structure
```
src/        Python scripts (one per task) + common.py (shared helpers)
results/    text outputs of each task, spacing.csv, summary.txt
plots/      the three required figures
report/     LaTeX source (main.tex) and the report PDF
```

## How to run
From the project folder:
```
pip install numpy matplotlib
python src/task0_setup.py
python src/task1_epsilon.py
python src/task2_3_spacing.py
python src/task4_powers.py
python src/task5_lab2.py
python src/task6_order.py
python src/task7_summary.py
```
Each script prints its results and saves them in `results/`. The figures are saved in `plots/`.
Requires Python 3.9 or newer (for `math.nextafter`).

## Outputs
- `results/spacing.csv` – x, successor, delta_plus, r, q for all 100 logarithmic samples (17 significant digits)
- `results/task*.txt` – results of each task
- `results/summary.txt` – all results in one file
- `plots/fig1_absolute_spacing.png` – absolute spacing across scales
- `plots/fig2_relative_spacing.png` – normalized relative spacing across scales
- `plots/fig3_boundary_spacing.png` – local spacing around powers of two

## Lab 2 data (entered manually)
Task 5 uses my saved Lab 2 Python results, entered by hand in `src/task5_lab2.py`:
- `n_stop = 94906266` (first attempted index whose addition left the sum unchanged)
- `s = 1.644934057834575` (hex `0x1.a51a65fe79dfep+0`)

Source: my Lab 2 report, Table 1 (Python). Lab 2 was run on Ubuntu (WSL). Both systems use IEEE 754
binary64, so the values can be compared directly.

## Deviations from the instructions
None. Figures 1 and 2 set their log-axis limits and ticks by hand, because Matplotlib's automatic
log ticks overflow near 1e308.
