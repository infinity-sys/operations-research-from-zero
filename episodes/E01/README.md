# E01: What Is Operations Research? From Wartime Radar to Delivery Apps
Video: https://youtu.be/DVvRopAnH8E

The first model of the course: the Nile Snacks Cairo plant (a fictional company) makes chips (x) and
date bars (y), in batches per week.

    maximize   300x + 400y          (profit, EGP)
    subject to  x + 2y <= 40        (line hours)
               2x +  y <= 50        (packing hours)
                x, y >= 0

Best plan: x = 20, y = 10, profit 10,000 EGP a week.

- `nile_mix.py`: method 3, the model in Python with PuLP. Output: `Status: Optimal`, chips 20.0, date bars 10.0, profit 10000.0 EGP.
- `corners.py`: method 2, check the four corners O, A, B, C (plain Python, no library).
- `peek.py` / `peek.ipynb`: a first look at `shops.csv` with pandas (shape, first rows, demand by region). Put `shops.csv` (from `data/`) next to it, or read it online:
  `pd.read_csv("https://raw.githubusercontent.com/infinity-sys/operations-research-from-zero/main/data/shops.csv")`

## Install
    pip install "pulp[cbc]" pandas

This code uses **PuLP 4** (Python 3.12 or newer), with the free CBC solver from the `cbc` extra.
Many older tutorials use PuLP 3.x, where variables are written `pulp.LpVariable("chips", lowBound=0)` and the
solver `pulp.PULP_CBC_CMD(msg=False)`. In PuLP 4 they are `model.add_variable("chips", lowBound=0)` and
`pulp.COIN_CMD(msg=False)`. See https://www.coin-or.org/pulp/guides/how_to_migrate_to_v4.html

Tested with Python 3.13, PuLP 4.2.0, pandas 3.0.5.
