# Gaussian elimination by hand, checked with exact fractions (no rounding).
from fractions import Fraction as F

def show(M, note):
    print(note)
    for r in M:
        print("  [" + "  ".join(f"{str(v):>5}" for v in r[:-1]) + " | " + f"{str(r[-1]):>5}" + " ]")

def op(M, i, j, m):          # R_i <- R_i - m * R_j
    M[i] = [a - m * b for a, b in zip(M[i], M[j])]
    show(M, f"R{i+1} <- R{i+1} - ({m}) R{j+1}")

# 2 x 2: corner B of E01 (x + 2y = 40, 2x + y = 50), Gauss-Jordan
M = [[F(1), F(2), F(40)], [F(2), F(1), F(50)]]
show(M, "start")
op(M, 1, 0, F(2))
M[1] = [v / F(-3) for v in M[1]]; show(M, "R2 <- R2 / (-3)")
op(M, 0, 1, F(2))

# 3 x 3: the binding constraints of the Damietta workshop (carpentry, wood, ratio)
M = [[F(4), F(2), F(3), F(120)], [F(2), F(1, 2), F(3), F(60)], [F(2), F(-1), F(0), F(0)]]
show(M, "start")
op(M, 1, 0, F(1, 2))
op(M, 2, 0, F(1, 2))
op(M, 2, 1, F(4))
x3 = M[2][3] / M[2][2]
x2 = (M[1][3] - M[1][2] * x3) / M[1][1]
x1 = (M[0][3] - M[0][1] * x2 - M[0][2] * x3) / M[0][0]
print("back substitution: x3 =", x3, " x2 =", x2, " x1 =", x1)
