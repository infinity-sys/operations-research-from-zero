from itertools import combinations
import numpy as np

# every constraint as a1*x1 + a2*x2 <= b  (a >= row is multiplied by -1)
rows = {"line":    ([2, 2.5], 32),   "packing": ([1.5, 1], 44),
        "cartons": ([25, 20], 1200), "peanuts": ([1, 0], 10),
        "shop":    ([0, -1], -4),    "x1 >= 0": ([-1, 0], 0),
        "x2 >= 0": ([0, -1], 0)}
A = np.array([a for a, b in rows.values()], dtype=float)
b = np.array([b for a, b in rows.values()], dtype=float)
c = np.array([450, 500])                       # profit per batch

found, parallel, outside = [], 0, 0
for i, j in combinations(range(len(b)), 2):    # 7 lines -> 21 pairs
    M = A[[i, j]]
    if abs(np.linalg.det(M)) < 1e-9:           # parallel: no crossing
        parallel += 1
        continue
    p = np.linalg.solve(M, b[[i, j]]).round(6) + 0.0
    if np.all(A @ p <= b + 1e-9):              # inside every half-plane?
        found.append(p)
    else:
        outside += 1

print(f"pairs 21: parallel {parallel}, outside {outside}, corners {len(found)}")
for p in sorted(found, key=lambda p: c @ p):
    print(f"({p[0]:g}, {p[1]:g})  Z = {c @ p:,.0f}")
