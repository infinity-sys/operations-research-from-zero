# E08: Standard Form, Slack, Surplus and Basic Solutions

Video: https://youtu.be/EfAXWJ8xQLY (premieres Sat 14 Nov 2026, 18:00 Cairo)

This episode opens with the solution of the E07 exercise (the Cairo plant with whole batches in PuLP), then rewrites
the Alexandria model in standard form: every constraint an equation, every variable at least zero, with slack
variables for less-than constraints and a surplus variable for the shop's minimum. It then lists every basic
solution and shows that the basic feasible ones are exactly the corners of the graphical method.
The scripts that read data use the CSV files in `../../data/`; run them from this folder.

- `e07_cairo_whole.py`: E07 exercise. Cairo plant, six products, whole batches, at least 2 each, date bars at
  least 6. Optimal, 9,640 EGP a week: 14 chips, 6 date bars, 2 of the rest. Slack: line 0 and date bars 0
  (binding), packing 7, cartons 620. Bonus: 41 line hours gives 9,940, so one more line hour is worth 300 EGP.
- `standard_form.py`: the Alexandria model as A x = b, 5 equations and 7 variables. At (10, 4.8): s1 = 0,
  s2 = 24.2, s3 = 854, s4 = 0, e5 = 0.8; A x = b is True.
- `basic_solutions.py`: all 21 ways to pick 2 non-basic variables: 2 singular, 15 infeasible, 4 feasible:
  (0, 4) 2,000; (0, 12.8) 6,400; (10, 4) 6,500; (10, 4.8) 6,900 EGP.

## Install
    pip install pandas numpy "pulp[cbc]"
