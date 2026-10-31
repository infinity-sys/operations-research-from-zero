import numpy as np

A = np.array([[1, 1, 1], [2, 1, 3], [1, 3, 2], [0, -1, 0]])
b = np.array([30, 50, 65, -5])     # the shop order x2 >= 5, times -1
c = np.array([4000, 5000, 6000])
x = np.array([10, 15, 5])          # the plan to test

print("A @ x   =", A @ x)          # what the plan uses
print("b - A@x =", b - A @ x)      # slack: 0 means binding
print("profit  =", c @ x)

B = A[:3]                          # the three binding rows
print("solve   =", np.linalg.solve(B, b[:3]))
print("rank(B) =", np.linalg.matrix_rank(B))
