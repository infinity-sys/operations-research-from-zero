# E06: The Graphical Method: Solving a Linear Program by Picture

Video: (link added after upload; premieres Sat 7 Nov 2026, 18:00 Cairo)

This episode opens with the solution of the E05 exercise (the Alexandria plant, formulated and solved in PuLP, with
the slack of every constraint), then solves the same two-variable linear program by picture: every constraint as a
line, the feasible region, its corners, the best corner found two ways, binding constraints, every corner found by
code, and three special cases run for real.
The scripts that read data use the CSV files in `../../data/`; run them from this folder.

- `e05_alexandria.py`: E05 exercise. Brittle (P4) and halawa bites (P6) at PL2: x1 = 10, x2 = 4.8,
  6,900 EGP a week. Slack: line 0, packing 24.2, cartons 854, peanuts 0, shop 0.8.
- `corner_table.py`: the four corners checked against every constraint: A (0, 4) 2,000 EGP; B (10, 4) 6,500;
  C (10, 4.8) 6,900 (line hours exactly 32); D (0, 12.8) 6,400. Packing never above 19.8 of 44, cartons never
  above 346 of 1,200: both redundant.
- `corners.py`: 7 boundaries, 21 pairs (itertools.combinations + numpy.linalg.solve): 2 parallel, 15 outside the
  region, 4 corners; the best is (10, 4.8), 6,900 EGP.
- `special_cases.py`: brittle at 400 EGP gives a tie (6,400 at D and at C); without the capacity rows the problem is
  unbounded; a shop order of 14 makes it infeasible.

## Install
    pip install pandas numpy "pulp[cbc]"
