# E07: Solving Linear Programs in Python with PuLP

Video: https://youtu.be/AQJxYNmDLPI (premieres Wed 11 Nov 2026, 18:00 Cairo)

This episode opens with the solution of the E06 exercise (the sesame and sugar suppliers, solved by picture and in
PuLP), then builds the full PuLP workflow: a model built from the data files with named constraints, the status
checked before anything else, a clear report of the plan and the slack of every constraint, whole batches with
integer variables, and what-if questions solved in a loop.
The scripts that read data use the CSV files in `../../data/`; run them from this folder.

- `e06_corners.py`: E06 exercise, the five corners and their costs: (4, 3) 39,000 EGP; (2.33, 8) 54,000;
  (10, 0) 60,000; (4, 8) 64,000; (12, 0) 72,000.
- `e06_suppliers.py`: the same model in PuLP: Optimal, a = 4, b = 3, 39,000 EGP. Slack: sesame 0, sugar 0,
  dock 5, supplier B 5. Bonus: with a truck from A at 12,000 or 15,000 the plan stays (4, 3); at 16,000 it moves
  to (2.33, 8).
- `cairo_report.py`: the Cairo plant (PL1), six products, at least 2 batches each, built from products.csv and
  plants.csv; writes `cairo.lp`. Optimal, 10,190 EGP a week: 17 batches of chips, 7 of lentil crackers, 2 of the
  rest. Line 40/40 and packing 50/50 binding; cartons 1,180 of 1,600 (420 spare).
- `check_status.py`: Optimal (10, 4.8) 6,900; with a shop order of 14 the status is Infeasible but values are
  still printed; without the line constraint, Unbounded.
- `whole_batches.py`: continuous 6,900; rounded down (10, 4) 6,500; integer (6, 8) 6,700.
- `what_if.py`: Alexandria line hours 32, 33, 34, 36, 40 give 6,900, 7,100, 7,300, 7,700, 8,500 EGP:
  +200 EGP per extra hour while the same corner stays best.

## Install
    pip install pandas numpy "pulp[cbc]"
