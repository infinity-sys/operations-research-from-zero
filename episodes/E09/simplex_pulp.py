import pulp
m = pulp.LpProblem("alex_simplex", pulp.LpMaximize)
x1 = m.add_variable("x1", lowBound=0)
x2 = m.add_variable("x2", lowBound=0)
m += 450 * x1 + 500 * x2
m += 2 * x1 + 2.5 * x2 <= 32, "line"
m += x1 <= 10, "peanuts"
r = m.solve(pulp.COIN_CMD(msg=False))
print(r.status_str, f"x1={x1.value():g}", f"x2={x2.value():g}", f"Z={pulp.value(m.objective):g}")
for c in m.constraints():
    print(f"slack {c.name:10}{abs(c.slack):g}")
