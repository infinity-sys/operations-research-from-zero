import pandas as pd
import networkx as nx

DATA = "../../data/"

pw = pd.read_csv(DATA + "plant_warehouse.csv")
ws = pd.read_csv(DATA + "warehouse_shop.csv")

G = nx.DiGraph()
for r in pw.itertuples():
    G.add_edge(r.plant_id, r.warehouse_id, egp=r.cost_egp_per_carton, km=r.distance_km)
for r in ws.itertuples():
    G.add_edge(r.warehouse_id, r.shop_id, egp=r.cost_egp_per_carton, km=r.distance_km)

for p in nx.all_simple_paths(G, "PL2", "S03"):
    egp, km = nx.path_weight(G, p, "egp"), nx.path_weight(G, p, "km")
    print(" -> ".join(p), f"{egp:.1f} EGP  {km:.1f} km")
print("cheapest:", nx.shortest_path(G, "PL2", "S03", weight="egp"))
print("shortest:", nx.shortest_path(G, "PL2", "S03", weight="km"))
