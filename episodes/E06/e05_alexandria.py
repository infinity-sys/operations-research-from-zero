import pandas as pd
import pulp

DATA = "../../data/"
P = pd.read_csv(DATA + "products.csv").set_index("product_id")
pl = pd.read_csv(DATA + "plants.csv").set_index("plant_id").loc["PL2"]
b, h = P.loc["P4"], P.loc["P6"]          # peanut brittle, halawa bites

m = pulp.LpProblem("alexandria", pulp.LpMaximize)
x1 = m.add_variable("x1", lowBound=0)    # batches of brittle a week
x2 = m.add_variable("x2", lowBound=0)    # batches of halawa a week

m += float(b.profit_egp_per_batch) * x1 + float(h.profit_egp_per_batch) * x2
m += (float(b.line_hours_per_batch) * x1 + float(h.line_hours_per_batch) * x2
      <= float(pl.line_hours_per_week), "line")
m += (float(b.packing_hours_per_batch) * x1 + float(h.packing_hours_per_batch) * x2
      <= float(pl.packing_hours_per_week), "packing")
m += (float(b.cartons_per_batch) * x1 + float(h.cartons_per_batch) * x2
      <= float(pl.capacity_cartons_per_week), "cartons")
m += x1 <= 10, "peanuts"
m += x2 >= 4, "shop"

r = m.solve(pulp.COIN_CMD(msg=False))
print("status:", r.status_str)
print("brittle x1 =", x1.value(), " halawa x2 =", x2.value())
print("profit:", pulp.value(m.objective), "EGP a week")
for c in m.constraints():
    print(f"slack {c.name:8}{abs(c.slack):8.1f}")
