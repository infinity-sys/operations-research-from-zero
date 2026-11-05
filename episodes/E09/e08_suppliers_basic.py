# E08 exercise: suppliers model in standard form, list every basic solution
from itertools import combinations
import numpy as np

# 3a + b - e1 = 15
# a + 2b - e2 = 10
# a + b + s3 = 12
# b + s4 = 8
names = ["a", "b", "e1", "e2", "s3", "s4"]
A = np.array([
    [3, 1, -1,  0, 0, 0],
    [1, 2,  0, -1, 0, 0],
    [1, 1,  0,  0, 1, 0],
    [0, 1,  0,  0, 0, 1],
], dtype=float)
b = np.array([15, 10, 12, 8], dtype=float)
c = np.array([6000, 5000, 0, 0, 0, 0], dtype=float)  # cost on a, b only

singular = infeasible = 0
feasible = []
for zero in combinations(range(6), 2):  # C(6,2)=15
    basic = [k for k in range(6) if k not in zero]
    B = A[:, basic]
    if abs(np.linalg.det(B)) < 1e-9:
        singular += 1
        continue
    x = np.zeros(6)
    x[basic] = np.linalg.solve(B, b)
    if np.all(x >= -1e-9):
        feasible.append((zero, x.round(6) + 0.0))
    else:
        infeasible += 1

print(f"choices 15: singular {singular}, infeasible {infeasible}, feasible {len(feasible)}")
for zero, x in sorted(feasible, key=lambda f: c @ f[1]):
    z = ", ".join(names[k] for k in zero)
    print(f"zeros {z:8} -> (a, b) = ({x[0]:g}, {x[1]:g})  cost = {c @ x:,.0f}")
