# Simplex by hand on Alexandria (no shop order): Max 450 x1 + 500 x2
# 2 x1 + 2.5 x2 + s1 = 32
# x1           + s4 = 10
# Start at origin (feasible). Print each tableau after a real pivot.
import numpy as np

# Columns: x1, x2, s1, s4 | RHS ; last row is -Z coefficients (we maximize)
# Representation: rows for basic vars + Z-row; track basis names

def show(title, basis, T):
    cols = ["x1", "x2", "s1", "s4", "RHS"]
    print(title)
    print("basis", " ".join(f"{c:>8}" for c in cols))
    for name, row in zip(basis + ["Z"], T):
        print(f"{name:5}", " ".join(f"{v:8.4g}" for v in row))
    print()

# Initial tableau
# s1:  2, 2.5, 1, 0 | 32
# s4:  1, 0,   0, 1 | 10
# Z:  -450,-500,0,0 | 0
basis = ["s1", "s4"]
T = np.array([
    [2, 2.5, 1, 0, 32],
    [1, 0,   0, 1, 10],
    [-450, -500, 0, 0, 0],
], dtype=float)
show("Tableau 0 (origin)", basis, T)

def pivot(T, basis, row, col, enter):
    piv = T[row, col]
    T[row] = T[row] / piv
    for r in range(len(T)):
        if r == row:
            continue
        T[r] = T[r] - T[r, col] * T[row]
    basis[row] = enter
    return T, basis

# Enter x2 (most negative Z = -500), leave s1 (min ratio 32/2.5=12.8; s4 coeff 0)
T, basis = pivot(T, basis, 0, 1, "x2")
show("Tableau 1 (after enter x2, leave s1)", basis, T)
x1, x2 = (T[basis.index("x1"), -1] if "x1" in basis else 0), (T[basis.index("x2"), -1] if "x2" in basis else 0)
print(f"current: x1={0 if 'x1' not in basis else T[basis.index('x1'),-1]:g}, x2={T[basis.index('x2'),-1]:g}, Z={T[-1,-1]:g}")
print()

# Enter x1 (Z has -50), ratios: row x2: 12.8/0.8=16, row s4: 10/1=10 → leave s4
T, basis = pivot(T, basis, 1, 0, "x1")
show("Tableau 2 (optimal)", basis, T)
print(f"optimal: x1={T[basis.index('x1'),-1]:g}, x2={T[basis.index('x2'),-1]:g}, Z={T[-1,-1]:g}")
# reduced costs (negated of Z row for nonbasic)
print("Z-row (reduced costs of nonbasics s1,s4):", T[-1, 2], T[-1, 3], "both ≥ 0 → stop")
