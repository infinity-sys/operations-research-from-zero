import pulp

names = ["tables", "chairs", "bookshelves"]
c = [900, 350, 800]               # profit per item, EGP
A = [[4, 2, 3],                   # carpentry hours
     [2, 1, 3],                   # finishing hours
     [2, 0.5, 3],                 # wood, m2
     [2, -1, 0],                  # 2 chairs per table: 2x1 - x2 <= 0
     [0, 0, 1]]                   # market: at most 10 bookshelves
b = [120, 80, 60, 0, 10]
rows = ["carpentry", "finishing", "wood", "ratio", "market"]

model = pulp.LpProblem("damietta", pulp.LpMaximize)
x = [model.add_variable(n, lowBound=0) for n in names]
model += pulp.lpSum(c[j] * x[j] for j in range(3)), "profit"
for i in range(5):
    model += pulp.lpSum(A[i][j] * x[j] for j in range(3)) <= b[i], rows[i]

result = model.solve(pulp.COIN_CMD(msg=False))
print("Status:", result.status_str)
print("Plan:", [v.value() for v in x], "Profit:", pulp.value(model.objective))
for i in range(5):
    used = sum(A[i][j] * x[j].value() for j in range(3))
    tag = "binding" if abs(used - b[i]) < 1e-6 else ""
    print(f"{rows[i]:<10} {used:6.1f} of {b[i]:>3}", tag)
