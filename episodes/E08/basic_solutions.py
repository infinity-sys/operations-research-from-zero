# Basic solutions of the Alexandria model in standard form:
# pick 2 of the 7 variables, set them to 0 (non-basic), solve the 5 equations for the other 5 (basic)
from itertools import combinations
import numpy as np

names = ["x1", "x2", "s1", "s2", "s3", "s4", "e5"]
A = np.array([[2, 2.5, 1, 0, 0, 0, 0], [1.5, 1, 0, 1, 0, 0, 0], [25, 20, 0, 0, 1, 0, 0],
              [1, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, -1]], dtype=float)
b = np.array([32, 44, 1200, 10, 4], dtype=float)
c = np.array([450, 500, 0, 0, 0, 0, 0])

singular, infeasible, feasible = 0, 0, []
for zero in combinations(range(7), 2):         # 21 ways to choose the 2 zeros
    basic = [k for k in range(7) if k not in zero]
    B = A[:, basic]
    if abs(np.linalg.det(B)) < 1e-9:            # no unique solution
        singular += 1
        continue
    x = np.zeros(7)
    x[basic] = np.linalg.solve(B, b)
    if np.all(x >= -1e-9):
        feasible.append((zero, x.round(6) + 0.0))
    else:
        infeasible += 1

print(f"choices 21: singular {singular}, infeasible {infeasible}, feasible {len(feasible)}")
for zero, x in sorted(feasible, key=lambda f: c @ f[1]):
    z = ", ".join(names[k] for k in zero)
    print(f"zeros {z:7} -> (x1, x2) = ({x[0]:g}, {x[1]:g})  Z = {c @ x:,.0f}")

# two of the infeasible ones, in full
for zero in [(0, 1), (2, 6)]:                   # zeros x1, x2  and  zeros s1, e5
    basic = [k for k in range(7) if k not in zero]
    x = np.zeros(7)
    x[basic] = np.linalg.solve(A[:, basic], b)
    print(" ".join(f"{n}={v:g}" for n, v in zip(names, x.round(2) + 0.0)))
