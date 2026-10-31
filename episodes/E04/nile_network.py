import pandas as pd
import networkx as nx

DATA = "../../data/"
pw = pd.read_csv(DATA + "plant_warehouse.csv")
ws = pd.read_csv(DATA + "warehouse_shop.csv")

G = nx.DiGraph()                     # one-way arcs: plant -> warehouse -> shop
for r in pw.itertuples():
    G.add_edge(r.plant_id, r.warehouse_id, km=r.distance_km)
for r in ws.itertuples():
    G.add_edge(r.warehouse_id, r.shop_id, km=r.distance_km)

print(G.number_of_nodes(), "nodes,", G.number_of_edges(), "arcs")
for p in nx.all_simple_paths(G, "PL2", "S03"):
    print(p, round(nx.path_weight(G, p, "km"), 1), "km")
best = nx.shortest_path(G, "PL2", "S03", weight="km")
print("shortest:", best)
