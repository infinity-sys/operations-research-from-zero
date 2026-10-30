# %%
import pandas as pd
shops = pd.read_csv("shops.csv")
shops.shape
# %%
shops.head()
# %%
shops.groupby("region")["weekly_demand_cartons"].sum()
