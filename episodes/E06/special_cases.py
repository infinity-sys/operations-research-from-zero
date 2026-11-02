import pulp

def plan(profit, line=True, shop=4):
    m = pulp.LpProblem("alex", pulp.LpMaximize)
    x1 = m.add_variable("x1", lowBound=0)
    x2 = m.add_variable("x2", lowBound=0)
    m += profit[0] * x1 + profit[1] * x2
    if line:                                   # the only real capacity limit
        m += 2 * x1 + 2.5 * x2 <= 32
        m += 1.5 * x1 + x2 <= 44
        m += 25 * x1 + 20 * x2 <= 1200
    m += x1 <= 10
    m += x2 >= shop
    r = m.solve(pulp.COIN_CMD(msg=False))
    return r.status_str, x1.value(), x2.value(), pulp.value(m.objective)

st, a, b, z = plan((400, 500))                  # brittle profit drops to 400
print(f"case 1  brittle 400:  {st}  ({a:g}, {b:g})  Z = {z:g}")
print(f"        Z at (10, 4.8) = {400*10 + 500*4.8:g}  (a tie)")
print(f"case 2  no capacity:  {plan((450, 500), line=False)[0]}")
print(f"case 3  shop wants 14: {plan((450, 500), shop=14)[0]}")
