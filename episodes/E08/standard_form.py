# The Alexandria model (E05, E06) in standard form: every inequality becomes an equation
# x1, x2 = batches of brittle, halawa;  s1..s4 = slack (unused capacity);  e5 = surplus (above the order)
import numpy as np

names = ["x1", "x2", "s1", "s2", "s3", "s4", "e5"]
A = np.array([[2,   2.5, 1, 0, 0, 0,  0],     # line:     2x1 + 2.5x2 + s1      = 32
              [1.5, 1,   0, 1, 0, 0,  0],     # packing:  1.5x1 + x2 + s2       = 44
              [25,  20,  0, 0, 1, 0,  0],     # cartons:  25x1 + 20x2 + s3      = 1200
              [1,   0,   0, 0, 0, 1,  0],     # peanuts:  x1 + s4               = 10
              [0,   1,   0, 0, 0, 0, -1]])    # shop:     x2 - e5               = 4
b = np.array([32, 44, 1200, 10, 4])
print("A is", A.shape, ": 5 equations, 7 variables")

x1, x2 = 10, 4.8                              # the best plan from E06
rest = b - A[:, :2] @ [x1, x2]                # what the extra variables must be
x = np.array([x1, x2, rest[0], rest[1], rest[2], rest[3], -rest[4]])
for n, v in zip(names, x):
    print(f"{n} = {v:g}")
print("A @ x == b:", np.allclose(A @ x, b))
