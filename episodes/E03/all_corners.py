import itertools
import numpy as np

A = np.array([[4, 2, 3], [2, 1, 3], [2, 0.5, 3], [2, -1, 0], [0, 0, 1]])
b = np.array([120, 80, 60, 0, 10])
c = np.array([900, 350, 800])
G = np.vstack([A, -np.eye(3)])           # add x >= 0 as -x <= 0
h = np.concatenate([b, np.zeros(3)])     # 8 borders in all

triples = list(itertools.combinations(range(8), 3))
singular, feasible, corners = 0, 0, set()
for rows in triples:
    B, r = G[list(rows)], h[list(rows)]
    if np.linalg.matrix_rank(B) < 3:     # not independent: no single point
        singular += 1
        continue
    x = np.linalg.solve(B, r)
    if np.all(G @ x <= h + 1e-9):        # inside every half-space
        feasible += 1
        corners.add(tuple(np.round(x, 6).tolist()))
best = max(corners, key=lambda p: c @ p)
outside = len(triples) - singular - feasible
print("systems:", len(triples), "| singular:", singular, "| outside:", outside)
print("feasible:", feasible, "| distinct corners:", len(corners))
print("best:", best, "| profit:", c @ best)
