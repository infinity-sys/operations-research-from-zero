import pulp

c = [4000, 5000, 6000]
A = [[1, 1, 1], [2, 1, 3], [1, 3, 2], [0, -1, 0]]
b = [30, 50, 65, -5]

m = pulp.LpProblem("gift_boxes", pulp.LpMaximize)
x = [m.add_variable(n, lowBound=0) for n in ["small", "medium", "large"]]
m += pulp.lpSum(c[j] * x[j] for j in range(3))
for i in range(4):
    m += pulp.lpSum(A[i][j] * x[j] for j in range(3)) <= b[i]

r = m.solve(pulp.COIN_CMD(msg=False))
print("status:", r.status_str)
print("plan  :", [v.value() for v in x])
print("profit:", pulp.value(m.objective))
