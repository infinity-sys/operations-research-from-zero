from scipy.optimize import linprog

c = [4000, 5000, 6000]
A = [[1, 1, 1], [2, 1, 3], [1, 3, 2], [0, -1, 0]]
b = [30, 50, 65, -5]

# linprog always MINIMIZES: minimize -profit to maximize profit
res = linprog([-v for v in c], A_ub=A, b_ub=b,
              bounds=[(0, None)] * 3, method="highs")

print("success:", res.success)
print("plan  :", res.x)
print("profit:", -res.fun)
