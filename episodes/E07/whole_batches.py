import pulp

def alexandria(cat):
    m = pulp.LpProblem("alex", pulp.LpMaximize)
    x1 = m.add_variable("x1", lowBound=0, cat=cat)
    x2 = m.add_variable("x2", lowBound=0, cat=cat)
    m += 450 * x1 + 500 * x2
    m += 2 * x1 + 2.5 * x2 <= 32, "line"
    m += x1 <= 10, "peanuts"
    m += x2 >= 4, "shop"
    m.solve(pulp.COIN_CMD(msg=False))
    return x1.value(), x2.value(), pulp.value(m.objective)

a, b, z = alexandria("Continuous")
print(f"continuous   x1={a:g}  x2={b:g}  Z={z:g}")
print(f"rounded down x1={int(a)}  x2={int(b)}  Z={450*int(a) + 500*int(b)}")
a, b, z = alexandria("Integer")
print(f"integer      x1={a:g}  x2={b:g}  Z={z:g}")
