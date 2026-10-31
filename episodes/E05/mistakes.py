# Three formulation mistakes, run for real (E05)
import pandas as pd
import pulp

DATA = "../../data/"
P = pd.read_csv(DATA + "products.csv").set_index("product_id")
K = pd.read_csv(DATA + "plants.csv").set_index("plant_id")
cols = [("line_hours_per_batch", "line_hours_per_week"),
        ("packing_hours_per_batch", "packing_hours_per_week"),
        ("cartons_per_batch", "capacity_cartons_per_week")]

# 1. The variety rule with the index in the wrong place
demand_c = float(pd.read_csv(DATA + "shops.csv")["weekly_demand_cartons"].sum())
for where in ("per plant", "in total"):
    m = pulp.LpProblem("two_plants", pulp.LpMaximize)
    x = {(j, k): m.add_variable(f"x_{j}_{k}", lowBound=0) for j in P.index for k in K.index}
    use = lambda c, k: pulp.lpSum(float(P.at[j, c]) * x[j, k] for j in P.index)
    m += pulp.lpSum(use("profit_egp_per_batch", k) for k in K.index)
    for k in K.index:
        for a, b in cols:
            m += use(a, k) <= float(K.at[k, b])
    m += pulp.lpSum(use("cartons_per_batch", k) for k in K.index) <= demand_c
    for j in P.index:
        if where == "per plant":
            for k in K.index:
                m += x[j, k] >= 2
        else:
            m += pulp.lpSum(x[j, k] for k in K.index) >= 2
    m.solve(pulp.COIN_CMD(msg=False))
    print("1", where, ":", round(pulp.value(m.objective), 2))

# 2. Ramadan plan without the stock carried from last week
demand = {1: 18, 2: 24, 3: 34, 4: 40}
for carry in (False, True):
    m = pulp.LpProblem("ramadan", pulp.LpMinimize)
    xm = {t: m.add_variable(f"make_{t}", lowBound=0, upBound=25) for t in demand}
    y = {t: m.add_variable(f"buy_{t}", lowBound=0) for t in demand}
    s = {t: m.add_variable(f"stock_{t}", lowBound=0) for t in demand}
    m += pulp.lpSum(2000 * xm[t] + 2600 * y[t] + 150 * s[t] for t in demand)
    for t in demand:
        before = s[t - 1] if (carry and t > 1) else 0
        m += before + xm[t] + y[t] - demand[t] == s[t]
    m.solve(pulp.COIN_CMD(msg=False))
    print("2 carry" if carry else "2 no carry", [round(xm[t].value()) for t in demand],
          [round(y[t].value()) for t in demand], pulp.value(m.objective))

# 3. A numpy number on the right-hand side
m = pulp.LpProblem("t", pulp.LpMaximize)
z = m.add_variable("z", lowBound=0)
lim = K.at["PL1", "line_hours_per_week"]
print("3 type    :", type(lim).__name__)
try:
    m += z <= lim
    print("3 ok")
except TypeError as e:
    print("3 TypeError:", e)
m += z <= float(lim)
print("3 float() : ok")
