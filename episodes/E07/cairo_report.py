import pandas as pd
import pulp

DATA = "../../data/"
P = pd.read_csv(DATA + "products.csv").set_index("product_id")
plant = pd.read_csv(DATA + "plants.csv").set_index("plant_id").loc["PL1"]

m = pulp.LpProblem("cairo", pulp.LpMaximize)
x = {j: m.add_variable(f"x_{j}", lowBound=2) for j in P.index}   # at least 2 of each

def use(col):
    return pulp.lpSum(float(P.at[j, col]) * x[j] for j in P.index)

m += use("profit_egp_per_batch")
m += use("line_hours_per_batch") <= float(plant.line_hours_per_week), "line"
m += use("packing_hours_per_batch") <= float(plant.packing_hours_per_week), "packing"
m += use("cartons_per_batch") <= float(plant.capacity_cartons_per_week), "cartons"
m.writeLP("cairo.lp")

r = m.solve(pulp.COIN_CMD(msg=False))
if r.status_str != "Optimal":
    raise SystemExit("no plan: " + r.status_str)
print("status:", r.status_str, "  profit:", round(pulp.value(m.objective), 1), "EGP")
for j in P.index:
    print(f"{P.at[j, 'name']:16}{x[j].value():6.2f}")
for c in m.constraints():
    used = c.value() - c.constant
    print(f"{c.name:8} used {used:7.1f} of {-c.constant:6.0f}  slack {abs(c.slack):6.1f}")
