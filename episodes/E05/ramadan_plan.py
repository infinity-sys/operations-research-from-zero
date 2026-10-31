import pulp

weeks  = [1, 2, 3, 4]
demand = {1: 18, 2: 24, 3: 34, 4: 40}   # batches of date bars
cap = 25                                # own line, batches a week
make, buy, store = 2000, 2600, 150      # EGP per batch (store: per week)

m = pulp.LpProblem("ramadan", pulp.LpMinimize)
x = {t: m.add_variable(f"make_{t}", lowBound=0, upBound=cap) for t in weeks}
y = {t: m.add_variable(f"buy_{t}", lowBound=0) for t in weeks}
s = {t: m.add_variable(f"stock_{t}", lowBound=0) for t in weeks}

m += pulp.lpSum(make * x[t] + buy * y[t] + store * s[t] for t in weeks)
for t in weeks:                         # stock balance, s_0 = 0
    before = s[t - 1] if t > 1 else 0
    m += before + x[t] + y[t] - demand[t] == s[t]

r = m.solve(pulp.COIN_CMD(msg=False))
print("status:", r.status_str)
print("week  make  buy  stock")
for t in weeks:
    print(f"{t:4}{x[t].value():6.0f}{y[t].value():5.0f}{s[t].value():7.0f}")
print("cost:", pulp.value(m.objective), "EGP")
