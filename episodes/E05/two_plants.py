import pandas as pd
import pulp

DATA = "../../data/"
P = pd.read_csv(DATA + "products.csv").set_index("product_id")
K = pd.read_csv(DATA + "plants.csv").set_index("plant_id")
demand = pd.read_csv(DATA + "shops.csv")["weekly_demand_cartons"].sum()

m = pulp.LpProblem("two_plants", pulp.LpMaximize)
x = {(j, k): m.add_variable(f"x_{j}_{k}", lowBound=0)
     for j in P.index for k in K.index}

def use(col, k):              # sum over j of a_j * x_jk, at plant k
    return pulp.lpSum(float(P.at[j, col]) * x[j, k] for j in P.index)

m += pulp.lpSum(use("profit_egp_per_batch", k) for k in K.index)
for k in K.index:                          # one row per plant
    m += use("line_hours_per_batch", k) <= float(K.at[k, "line_hours_per_week"])
    m += use("packing_hours_per_batch", k) <= float(K.at[k, "packing_hours_per_week"])
    m += use("cartons_per_batch", k) <= float(K.at[k, "capacity_cartons_per_week"])
m += pulp.lpSum(use("cartons_per_batch", k) for k in K.index) <= float(demand)
for j in P.index:                          # every product: >= 2 batches
    m += pulp.lpSum(x[j, k] for k in K.index) >= 2

r = m.solve(pulp.COIN_CMD(msg=False))
print("status:", r.status_str, "| demand:", demand, "cartons")
for (j, k), v in x.items():
    if v.value() > 1e-6:
        print(f"{j} at {k}: {v.value():7.3f} batches")
print("profit:", round(pulp.value(m.objective), 2), "EGP a week")
