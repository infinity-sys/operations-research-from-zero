# E05: Formulating Linear Programs: Product Mix and Classic Patterns

Video: https://youtu.be/Z-OBZtKwww4 (premieres Wed 4 Nov 2026, 18:00 Cairo)

This episode opens with the solution of the E04 exercise (pandas, NetworkX, PuLP and SciPy), then formulates
linear programs at scale: sets, parameters, variables and the model written with sums. Three formulations on the
Nile Snacks data, each solved in PuLP 4: the product mix, two plants with a two-index variable, and a four-week
plan with a stock balance and make-or-buy. Then three mistakes, run for real.
The scripts read the CSV files in `../../data/`; run them from this folder.

- `e04_regions.py`: E04 part 1. Weekly demand vs warehouse capacity: Alexandria 373 of 1,000 (627 spare),
  Cairo 707 of 1,500 (793), Delta 308 of 900 (592); 1,388 of 3,400 in total. Largest order: S05 Shubra shop, 88.
- `e04_cheapest.py`: E04 part 2. PL2 → S03 via W1 23.1 EGP a carton (289.3 km), via W2 32.4 EGP (261.4 km),
  via W3 27.4 EGP (288.4 km). Cheapest: via W1; shortest: via W2.
- `e04_cardboard.py`: E04 part 3. Gift boxes with 60 cardboard rolls: PuLP and SciPy agree on
  (6.667, 11.667, 11.667) and 155,000 EGP, 10,000 EGP more than with 50 rolls.
- `product_mix.py`: six products at the Cairo plant: 10 batches of chips + 30 of lentil crackers, 10,500 EGP a week
  (line, packing and cartons all used up; the optimum is unique).
- `two_plants.py`: x[j, k] for 6 products × 2 plants, capacity per plant, shop demand 1,388 cartons, at least
  2 batches of every product: 17,116.36 EGP a week. There are several best plans with this profit; the solver prints one.
- `ramadan_plan.py`: date bars over 4 weeks (demand 18, 24, 34, 40; make ≤ 25 a week at 2,000 EGP, buy at 2,600,
  store at 150 a week): make 25 every week, stock 7 and 8, buy 1 and 15: 243,850 EGP (unique).
- `mistakes.py`: the variety rule per plant instead of in total (16,701.82 vs 17,116.36 EGP); the balance without last
  week's stock (246,400 vs 243,850 EGP); a numpy integer on the right-hand side of a PuLP constraint (TypeError, fixed
  with `float()`).

## Install
    pip install pandas scipy "pulp[cbc]" networkx

Tested with Python 3.13.5, pandas 3.0.6, SciPy 1.18.1, PuLP 4.2.0, NetworkX 3.7.
