import pandas as pd

DATA = "../../data/"
products = pd.read_csv(DATA + "products.csv")
shops = pd.read_csv(DATA + "shops.csv")

print(products.shape, "rows x columns")
p = products.rename(columns={"profit_egp_per_batch": "profit"})
print(p[["name", "profit"]].to_string(index=False))

print("demand by region:")
print(shops.groupby("region").weekly_demand_cartons.sum().to_string())
print("total:", shops.weekly_demand_cartons.sum(), "cartons a week")
