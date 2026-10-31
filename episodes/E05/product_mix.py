import pandas as pd
import pulp

DATA = "../../data/"
P = pd.read_csv(DATA + "products.csv").set_index("product_id")
plant = pd.read_csv(DATA + "plants.csv").set_index("plant_id").loc["PL1"]

m = pulp.LpProblem("product_mix", pulp.LpMaximize)
x = {j: m.add_variable(f"x_{j}", lowBound=0) for j in P.index}

def use(col):                 # sum over j of a_j * x_j
    return pulp.lpSum(float(P.at[j, col]) * x[j] for j in P.index)

m += use("profit_egp_per_batch")
m += use("line_hours_per_batch") <= float(plant["line_hours_per_week"])
m += use("packing_hours_per_batch") <= float(plant["packing_hours_per_week"])
m += use("cartons_per_batch") <= float(plant["capacity_cartons_per_week"])

r = m.solve(pulp.COIN_CMD(msg=False))
print("status:", r.status_str)
for j in P.index:
    print(f"{j} {P.at[j, 'name']:16}{x[j].value():6.1f}")
print("profit:", pulp.value(m.objective), "EGP a week")
