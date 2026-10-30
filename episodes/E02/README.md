# E02: Thinking Like a Modeler: Decisions, Objectives and Constraints

Video: https://youtu.be/xeC5g9LnYm0

Every formulation answers three questions: what can I decide (decision variables, with names and units),
what do I want (the objective), and what limits me (constraints: resources, demand, logic, non-negativity).
This episode builds three classic formulations line by line and solves each one with PuLP.
Nile Snacks is a FICTIONAL company with synthetic data (see `data/`).

- `study_plan.py`: the solution of the E01 exercise, a study plan as a model (hours on OR, Numerical and
  Probability, plus sleep). Output: OR 15 h, Numerical 5 h, Probability 15 h, sleep exactly 49 h, 92.5 expected marks.
  The bounds `lowBound=5, upBound=15` are the "between 5 and 15 hours" constraints.
- `three_products.py`: formulation 1, a product mix. The Cairo plant with the first three products of
  `products.csv` and three resources from `plants.csv` (line hours, packing hours, carton capacity).
  Output: 17.5 batches of chips, 0 date bars, 15 of sesame sticks, 10,050 EGP a week, 1,225 cartons used.
  Change `PLANT = "PL1"` to `"PL2"` for the Alexandria plant: 17 chips, 10 sesame sticks, 8,300 EGP.
- `energy_mix.py`: formulation 2, a blend. The cheapest 100 g pack of dates, peanuts and oats with at least
  14 g protein, 9 g fiber, at most 15 g sugar, at least 20% dates and at most 30% peanuts (nutrition values
  rounded, for illustration). Output: 20 g dates, 20 g peanuts, 60 g oats, 8.2 EGP a pack.
- `packing_staff.py`: formulation 3, staffing. Packers work 5 days in a row, then 2 days off; the minimum
  packers per day come from `shift_demand.csv`. Output: 19 packers (4 start on Sunday, 5 on Tuesday,
  5 on Wednesday, 5 on Friday).
- `mistakes.py`: the five common modeling mistakes, each run for real: mixing units (minutes as hours),
  forgetting non-negativity (date bars = -30), a constraint the wrong way round (0 staff), counting twice
  (83 staff-days are not 83 people), and a non-linear term (PuLP refuses `price * qty`).

Put `products.csv`, `plants.csv` and `shift_demand.csv` (from `data/`) next to the scripts, or read them online, e.g.
`pd.read_csv("https://raw.githubusercontent.com/infinity-sys/operations-research-from-zero/main/data/products.csv", index_col="product_id")`

## Install
    pip install "pulp[cbc]" pandas

This code uses **PuLP 4** (Python 3.12 or newer): `model.add_variable(...)`, `pulp.COIN_CMD(msg=False)`, and the
status read from the value returned by `solve()`. Tip: PuLP 4.2 did not accept a numpy integer on the right of
`<=` in our tests (`TypeError`), so the scripts turn pandas rows into plain Python values with `.to_dict()`.

Tested with Python 3.13, PuLP 4.2.0, pandas 3.0.5.
