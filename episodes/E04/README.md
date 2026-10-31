# E04: Your OR Toolkit in Python: NumPy, pandas, PuLP, SciPy, OR-Tools and NetworkX

Video: VIDEO_LINK_PLACEHOLDER

This episode opens with the solution of the E03 exercise (the gift boxes: matrix form, slack, Gaussian elimination,
NumPy and PuLP), then sets up the six Python libraries of the course, loads the Nile Snacks data with pandas, solves
one model with three solvers (PuLP, SciPy, OR-Tools), shows two traps, and finds a shortest route with NetworkX.
The scripts read the CSV files in `../../data/`; run them from this folder.

- `check_setup.py`: prints the version of each library and whether the CBC solver is available.
- `gift_numpy.py`: the E03 exercise in NumPy. `A @ x` = [30, 50, 65, -15], slack `b - A @ x` = [0, 0, 0, 10],
  profit 145,000 EGP, `np.linalg.solve` on the three binding rows = [10, 15, 5], `matrix_rank` = 3.
- `gift_pulp.py`: the same model in PuLP 4: status Optimal, plan [10, 15, 5], profit 145,000 EGP (the optimum is unique).
- `nile_pandas.py`: `read_csv`, `shape`, renaming and picking columns, and `groupby`: weekly demand by region
  Alexandria 373, Cairo 707, Delta 308 cartons, 1,388 in total.
- `gift_scipy.py`: the gift boxes with `scipy.optimize.linprog` (HiGHS). linprog always minimizes, so the profit is
  negated: success True, plan [10, 15, 5], profit 145,000.
- `gift_ortools.py`: the gift boxes with OR-Tools (GLOP): OPTIMAL, plan [10, 15, 5], profit 145,000. The raw value
  of x1 prints as 9.999999999999996: floating-point noise, so round before you report.
- `nile_network.py`: a directed graph from `plant_warehouse.csv` and `warehouse_shop.csv` (29 nodes, 78 arcs).
  Routes from plant PL2 to shop S03: via W1 289.3 km, via W2 261.4 km, via W3 288.4 km; shortest: PL2 → W2 → S03.

## Install
    pip install numpy pandas scipy "pulp[cbc]" ortools networkx

PuLP 4 needs Python 3.12 or newer (`model.add_variable(...)`, `pulp.COIN_CMD(msg=False)`).

Tested with Python 3.13.5, NumPy 2.5.4, pandas 3.0.6, SciPy 1.18.1, PuLP 4.2.0, OR-Tools 9.15.6755, NetworkX 3.7.
