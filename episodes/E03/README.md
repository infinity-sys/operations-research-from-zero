# E03: The Math You Need: Matrices, Linear Systems and Inequalities

Video: https://youtu.be/yGutz7jXnKk

Every linear program fits in one line: maximize cᵀx subject to Ax ≤ b, x ≥ 0. This episode writes the E02 exercise
(the Damietta furniture workshop) in matrix form, multiplies a matrix by a vector by hand, solves linear systems by
Gauss–Jordan and Gaussian elimination, shows why the best corner of an LP is the solution of its binding constraints,
and checks everything with NumPy. No data files are needed for this episode.

- `workshop.py`: the solution of the E02 exercise, built straight from the matrix form (lists `c`, `A`, `b`) and
  solved with PuLP. Output: 12 tables, 24 chairs, 8 bookshelves, 25,600 EGP a week (the optimum is unique).
  Binding: carpentry (120 of 120 h), wood (60 of 60 m²) and the 2-chairs rule; finishing uses 72 of 80 h, the market 8 of 10.
- `gauss_by_hand.py`: the two board calculations, step by step with exact fractions (no rounding):
  Gauss–Jordan on x + 2y = 40, 2x + y = 50 (x = 20, y = 10, corner B of E01), and Gaussian elimination with back
  substitution on the 3 × 3 system of the workshop's binding constraints (x1 = 12, x2 = 24, x3 = 8).
- `matrix_tools.py`: NumPy checks. `A @ x` = [120, 72, 60, 0, 8] (what the plan uses), the slack `b - A @ x`
  = [0, 8, 0, 0, 2], the profit `c @ x` = 25600, `np.linalg.solve` on the binding rows = [12, 24, 8],
  and `np.linalg.matrix_rank`: 3 for the binding rows, 2 for carpentry, finishing and market (not independent).
- `all_corners.py`: brute force. The workshop has 8 borders (5 constraints and 3 sign rows); every choice of 3 gives a
  system, 56 in all: 10 are singular (rank below 3), 34 give points outside the region, 12 land on it, and they make
  8 distinct corners. The best is (12, 24, 8) with 25,600 EGP, the same as PuLP.

For vectors and dot products in data science, see Data Science E09 in the Data Science playlist.

## Install
    pip install numpy "pulp[cbc]"

`workshop.py` uses **PuLP 4** (Python 3.12 or newer): `model.add_variable(...)`, `pulp.COIN_CMD(msg=False)`, and the
status read from the value returned by `solve()`. Tip: PuLP 4.2 did not accept a numpy integer on the right of `<=`
in our tests (`TypeError`), so convert values with `float()` (or pandas rows with `.to_dict()`) before building constraints.

Tested with Python 3.13, PuLP 4.2.0, NumPy 2.5.3.
