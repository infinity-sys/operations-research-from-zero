import pulp
from scipy.optimize import linprog

c = [4000, 5000, 6000]
A = [[1, 1, 1], [2, 1, 3], [1, 3, 2], [0, -1, 0]]
b = [30, 60, 65, -5]          # cardboard: 50 -> 60

m = pulp.LpProblem("gift_boxes", pulp.LpMaximize)
x = [m.add_variable(n, lowBound=0) for n in ["s", "m", "l"]]
m += pulp.lpSum(c[j] * x[j] for j in range(3))
for i in range(4):
    m += pulp.lpSum(A[i][j] * x[j] for j in range(3)) <= b[i]
m.solve(pulp.COIN_CMD(msg=False))
print("PuLP :", [round(v.value(), 3) for v in x], pulp.value(m.objective))

res = linprog([-v for v in c], A_ub=A, b_ub=b, method="highs")
print("SciPy:", res.x.round(3), -res.fun)
print("more profit:", -res.fun - 145000)
