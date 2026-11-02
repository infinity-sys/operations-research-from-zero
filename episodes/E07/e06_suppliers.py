import pulp

def solve(cost_a=6000):
    m = pulp.LpProblem("sesame_sugar", pulp.LpMinimize)
    a = m.add_variable("a", lowBound=0)        # trucks from supplier A a month
    b = m.add_variable("b", lowBound=0)        # trucks from supplier B a month
    m += cost_a * a + 5000 * b
    m += 3 * a + 1 * b >= 15, "sesame"
    m += 1 * a + 2 * b >= 10, "sugar"
    m += a + b <= 12, "dock"
    m += b <= 8, "supplier_B"
    r = m.solve(pulp.COIN_CMD(msg=False))
    return m, r.status_str, a.value(), b.value(), pulp.value(m.objective)

m, st, a, b, z = solve()
print(f"{st}  a={a:g}  b={b:g}  cost={z:,.0f}")
for c in m.constraints():
    print(f"slack {c.name:11}{abs(c.slack):5.1f}")
for ca in (12000, 15000, 16000):
    _, _, a, b, z = solve(ca)
    print(f"A at {ca}: a={a:.2f} b={b:g} {z:,.0f}")
