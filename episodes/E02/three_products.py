import pandas as pd
import pulp

PLANT = "PL1"   # Cairo plant; try "PL2" (Alexandria): same model, new data
prod = pd.read_csv("products.csv", index_col="product_id").head(3).to_dict("index")
plant = pd.read_csv("plants.csv", index_col="plant_id").loc[PLANT].to_dict()

model = pulp.LpProblem("three_products", pulp.LpMaximize)
x = {p: model.add_variable(p, lowBound=0) for p in prod}   # batches per week

def use(col):   # sum over the products of (data in column col) * x
    return pulp.lpSum(prod[p][col] * x[p] for p in x)

model += use("profit_egp_per_batch"), "profit"
model += use("line_hours_per_batch") <= plant["line_hours_per_week"], "line"
model += use("packing_hours_per_batch") <= plant["packing_hours_per_week"], "packing"
model += use("cartons_per_batch") <= plant["capacity_cartons_per_week"], "cartons"

result = model.solve(pulp.COIN_CMD(msg=False))
print("Status:", result.status_str)
for p in x:
    print(f"{prod[p]['name']}: {x[p].value()} batches")
print("Profit:", pulp.value(model.objective), "EGP")
print("Cartons used:", pulp.value(use("cartons_per_batch")))
