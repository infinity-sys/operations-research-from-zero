import numpy as np

A = np.array([[4, 2, 3], [2, 1, 3], [2, 0.5, 3], [2, -1, 0], [0, 0, 1]])
b = np.array([120, 80, 60, 0, 10])
c = np.array([900, 350, 800])
x = np.array([12, 24, 8])          # the plan from PuLP

print("A @ x   =", A @ x)          # what the plan uses, row by row
print("b - A@x =", b - A @ x)      # slack: 0 means binding
print("profit  =", c @ x)

rows = [0, 2, 3]                   # carpentry, wood, ratio
B = A[rows]
print("solve   =", np.linalg.solve(B, b[rows]))
print("rank(B) =", np.linalg.matrix_rank(B))
print("rank(carpentry, finishing, market) =", np.linalg.matrix_rank(A[[0, 1, 4]]))
