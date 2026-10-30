"""Nile Snacks: the running case of "Operations Research: From Zero to Hero" (Infinity Systems).

Nile Snacks is a FICTIONAL Egyptian snack-food company. Every number here is synthetic.
The files are generated once with a fixed seed (1947, the year of the simplex method)
and reused across the course. Re-running this script gives exactly the same files.

  products.csv           6 products: hours per batch on the production line and packing, profit
  plants.csv             2 plants (Cairo side and Alexandria side) with weekly hours and capacity
  warehouses.csv         3 warehouses (Cairo, Alexandria, Delta)
  shops.csv              24 shops in Cairo/Giza, Alexandria and the Delta, with weekly demand
  plant_warehouse.csv    shipping cost per carton, plant -> warehouse
  warehouse_shop.csv     distance and delivery cost per carton, warehouse -> shop
  vans.csv               8 delivery vans: base warehouse, capacity, cost per km
  shift_demand.csv       packing staff needed per day at the Cairo plant (staff scheduling)

Distances are straight-line (haversine) distances x 1.25, an estimate, not real road data.
Usage: python3 make_nile_snacks.py     -> writes the CSV files next to this script
Needs: numpy, pandas
"""
import math
import os

import numpy as np
import pandas as pd

SEED = 1947
rng = np.random.default_rng(SEED)
OUT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- products (hand-set, used in E01 and E05)
products = pd.DataFrame([
    ["P1", "Crunchy Chips", 1.0, 2.0, 300, 40],
    ["P2", "Date Bars", 2.0, 1.0, 400, 30],
    ["P3", "Sesame Sticks", 1.5, 1.0, 320, 35],
    ["P4", "Peanut Brittle", 2.0, 1.5, 450, 25],
    ["P5", "Lentil Crackers", 1.0, 1.0, 250, 40],
    ["P6", "Halawa Bites", 2.5, 1.0, 500, 20],
], columns=["product_id", "name", "line_hours_per_batch", "packing_hours_per_batch",
            "profit_egp_per_batch", "cartons_per_batch"])

# ---------------------------------------------------------------- plants
plants = pd.DataFrame([
    ["PL1", "Cairo plant", "10th of Ramadan City", 30.296, 31.745, 40, 50, 1600],
    ["PL2", "Alexandria plant", "New Borg El Arab", 30.866, 29.576, 32, 44, 1200],
], columns=["plant_id", "name", "location", "lat", "lon", "line_hours_per_week",
            "packing_hours_per_week", "capacity_cartons_per_week"])

# ---------------------------------------------------------------- warehouses
warehouses = pd.DataFrame([
    ["W1", "Cairo warehouse", "Obour City", "Cairo", 30.228, 31.478, 1500, 1.5],
    ["W2", "Alexandria warehouse", "Amreya", "Alexandria", 31.020, 29.800, 1000, 1.2],
    ["W3", "Delta warehouse", "Tanta", "Delta", 30.790, 31.000, 900, 1.0],
], columns=["warehouse_id", "name", "location", "region", "lat", "lon",
            "capacity_cartons_per_week", "handling_egp_per_carton"])

# ---------------------------------------------------------------- shops (area centres + small seeded jitter)
areas = [
    ("Cairo", "Nasr City", 30.056, 31.330), ("Cairo", "Heliopolis", 30.090, 31.322),
    ("Cairo", "Maadi", 29.960, 31.257), ("Cairo", "Downtown", 30.045, 31.240),
    ("Cairo", "Shubra", 30.100, 31.245), ("Cairo", "New Cairo", 30.030, 31.470),
    ("Cairo", "Dokki", 30.038, 31.212), ("Cairo", "Mohandessin", 30.056, 31.200),
    ("Cairo", "6th of October", 29.960, 30.930), ("Cairo", "Helwan", 29.850, 31.334),
    ("Alexandria", "Smouha", 31.215, 29.945), ("Alexandria", "Sidi Gaber", 31.220, 29.942),
    ("Alexandria", "Miami", 31.268, 30.005), ("Alexandria", "Mansheya", 31.200, 29.885),
    ("Alexandria", "Agami", 31.100, 29.760), ("Alexandria", "Sporting", 31.212, 29.930),
    ("Alexandria", "Montaza", 31.285, 30.015),
    ("Delta", "Tanta", 30.786, 31.000), ("Delta", "Mansoura", 31.040, 31.378),
    ("Delta", "Zagazig", 30.587, 31.502), ("Delta", "Damanhour", 31.034, 30.468),
    ("Delta", "Kafr El Sheikh", 31.111, 30.940), ("Delta", "Banha", 30.466, 31.185),
    ("Delta", "Shibin El Kom", 30.552, 31.009),
]
base = {"Cairo": 70, "Alexandria": 55, "Delta": 45}
rows = []
for k, (region, area, lat, lon) in enumerate(areas, 1):
    jlat, jlon = rng.normal(0, 0.004, 2)
    demand = int(round(base[region] + rng.normal(0, 9)))
    rows.append([f"S{k:02d}", f"{area} shop", area, region, round(lat + jlat, 4), round(lon + jlon, 4), demand])
shops = pd.DataFrame(rows, columns=["shop_id", "name", "area", "region", "lat", "lon", "weekly_demand_cartons"])


def km(a_lat, a_lon, b_lat, b_lon):
    """Estimated road distance: haversine distance x 1.25, rounded to 0.1 km."""
    p1, p2 = math.radians(a_lat), math.radians(b_lat)
    dp, dl = p2 - p1, math.radians(b_lon - a_lon)
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return round(2 * 6371 * math.asin(math.sqrt(h)) * 1.25, 1)


# ---------------------------------------------------------------- shipping plant -> warehouse (trucks)
pw = []
for _, p in plants.iterrows():
    for _, w in warehouses.iterrows():
        d = km(p.lat, p.lon, w.lat, w.lon)
        pw.append([p.plant_id, w.warehouse_id, d, round(2.0 + 0.06 * d, 1)])
plant_wh = pd.DataFrame(pw, columns=["plant_id", "warehouse_id", "distance_km", "cost_egp_per_carton"])

# ---------------------------------------------------------------- delivery warehouse -> shop (vans)
ws = []
for _, w in warehouses.iterrows():
    for _, s in shops.iterrows():
        d = km(w.lat, w.lon, s.lat, s.lon)
        ws.append([w.warehouse_id, s.shop_id, d, round(1.0 + 0.12 * d, 1)])
wh_shop = pd.DataFrame(ws, columns=["warehouse_id", "shop_id", "distance_km", "cost_egp_per_carton"])

# ---------------------------------------------------------------- vans
vans = []
home = ["W1", "W1", "W1", "W2", "W2", "W2", "W3", "W3"]
for k, w in enumerate(home, 1):
    cap = int(rng.choice([120, 150, 180]))
    vans.append([f"V{k}", w, cap, round(float(rng.uniform(3.2, 4.2)), 2), 8])
vans = pd.DataFrame(vans, columns=["van_id", "warehouse_id", "capacity_cartons", "cost_egp_per_km", "shift_hours"])

# ---------------------------------------------------------------- packing staff needed per day (Cairo plant)
days = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]
need = [int(x) for x in np.clip(np.round(rng.normal(14, 3, 7)), 8, 20)]
need[-1] = min(need[-1], 9)  # Friday is a short day
shift = pd.DataFrame({"plant_id": "PL1", "day": days, "min_packing_staff": need})

for name, df in [("products", products), ("plants", plants), ("warehouses", warehouses), ("shops", shops),
                 ("plant_warehouse", plant_wh), ("warehouse_shop", wh_shop), ("vans", vans),
                 ("shift_demand", shift)]:
    df.to_csv(os.path.join(OUT, name + ".csv"), index=False)
    print(f"{name}.csv: {len(df)} rows")
