from itertools import combinations
import numpy as np

# sesame, sugar (>= rows times -1), dock, supplier B, a >= 0, b >= 0
A = np.array([[-3, -1], [-1, -2], [1, 1], [0, 1], [-1, 0], [0, -1]], dtype=float)
b = np.array([-15, -10, 12, 8, 0, 0], dtype=float)
corners = {}
for i, j in combinations(range(len(A)), 2):
    if abs(np.linalg.det(A[[i, j]])) < 1e-9:
        continue
    p = np.linalg.solve(A[[i, j]], b[[i, j]])
    if np.all(A @ p <= b + 1e-9):
        corners[(round(p[0], 2) + 0.0, round(p[1], 2) + 0.0)] = 6000 * p[0] + 5000 * p[1]
for (a_, b_), z in sorted(corners.items(), key=lambda kv: kv[1]):
    print(f"({a_:g}, {b_:g})  cost = {z:,.0f}")
