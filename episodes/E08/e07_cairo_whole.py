import pandas as pd
import pulp

DATA = "../../data/"
P = pd.read_csv(DATA + "products.csv").set_index("product_id")
plant = pd.read_csv(DATA + "plants.csv").set_index("plant_id").loc["PL1"]

def solve(line=None, cat="Integer"):
    m = pulp.LpProblem("cairo_whole", pulp.LpMaximize)
    x = {j: m.add_variable(f"x_{j}", lowBound=2, cat=cat) for j in P.index}
    use = lambda col: pulp.lpSum(float(P.at[j, col]) * x[j] for j in P.index)
    m += use("profit_egp_per_batch")
    m += use("line_hours_per_batch") <= (line or float(plant.line_hours_per_week)), "line"
    m += use("packing_hours_per_batch") <= float(plant.packing_hours_per_week), "packing"
    m += use("cartons_per_batch") <= float(plant.capacity_cartons_per_week), "cartons"
    m += x["P2"] >= 6, "date_bars"
    r = m.solve(pulp.COIN_CMD(msg=False))
    return m, r.status_str, x

m, st, x = solve()
print("status:", st, " profit:", pulp.value(m.objective))
print("  ".join(f"{P.at[j, 'name'].split()[0]} {x[j].value():g}" for j in P.index))
for c in m.constraints():
    print(f"{c.name:10} slack {abs(c.slack):6.1f}")
m2, st2, _ = solve(line=41)
print("line 41:", st2, pulp.value(m2.objective))
m3, st3, _ = solve(cat="Continuous")
print("continuous:", st3, round(pulp.value(m3.objective), 2))
