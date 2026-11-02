import pulp

def profit(hours):
    m = pulp.LpProblem("alex", pulp.LpMaximize)
    x1 = m.add_variable("x1", lowBound=0)
    x2 = m.add_variable("x2", lowBound=0)
    m += 450 * x1 + 500 * x2
    m += 2 * x1 + 2.5 * x2 <= hours, "line"
    m += x1 <= 10, "peanuts"
    m += x2 >= 4, "shop"
    m.solve(pulp.COIN_CMD(msg=False))
    return pulp.value(m.objective)

before = profit(32)
for h in (32, 33, 34, 36, 40):
    z = profit(h)
    print(f"line hours {h}:  Z = {z:7.0f}  (+{z - before:.0f})")
