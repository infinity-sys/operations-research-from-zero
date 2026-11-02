import pulp

def alexandria(shop=4, capacity=True):
    m = pulp.LpProblem("alex", pulp.LpMaximize)
    x1 = m.add_variable("x1", lowBound=0)
    x2 = m.add_variable("x2", lowBound=0)
    m += 450 * x1 + 500 * x2
    if capacity:
        m += 2 * x1 + 2.5 * x2 <= 32, "line"
    m += x1 <= 10, "peanuts"
    m += x2 >= shop, "shop"
    r = m.solve(pulp.COIN_CMD(msg=False))
    return r.status_str, x1.value(), x2.value(), pulp.value(m.objective)

for name, kw in [("normal", {}), ("shop 14", {"shop": 14}), ("no line", {"capacity": False})]:
    st, a, b, z = alexandria(**kw)
    print(f"{name:7} {st:10} ({a:g}, {b:g}) Z={z:g}")
