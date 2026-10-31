import pandas as pd

DATA = "../../data/"

shops = pd.read_csv(DATA + "shops.csv")
wh = pd.read_csv(DATA + "warehouses.csv")

reg = shops.groupby("region")["weekly_demand_cartons"].sum()
t = reg.rename("demand").to_frame()
t["capacity"] = wh.set_index("region")["capacity_cartons_per_week"]
t["spare"] = t["capacity"] - t["demand"]
print(t)
print("total:", t["demand"].sum(), "of", t["capacity"].sum())

top = shops.loc[shops["weekly_demand_cartons"].idxmax()]
print("largest:", top["shop_id"], top["name"], top["weekly_demand_cartons"])
