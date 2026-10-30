# Nile Snacks: the course's running case

**Nile Snacks is a FICTIONAL Egyptian snack-food company.** It does not exist, and every number in these
files is synthetic. It is the running case of **Operations Research: From Zero to Hero** (Infinity Systems):
the same company comes back in the product-mix, transportation, assignment, network, routing,
scheduling, inventory and capstone episodes.

The files are generated once by `make_nile_snacks.py` (numpy + pandas, fixed seed `1947`, the year of the
simplex method). Re-running the script gives exactly the same files.

Load a file online (Colab):
`pd.read_csv("https://raw.githubusercontent.com/infinity-sys/operations-research-from-zero/main/data/shops.csv")`
or, after downloading it, `pd.read_csv("shops.csv")`.

## The company in one picture
2 plants make 6 products, trucks take cartons to 3 warehouses, and 8 vans deliver them to 24 shops in
Cairo/Giza, Alexandria and the Delta (1,388 cartons a week in total).

## Files
| file | rows | what it holds |
|---|---|---|
| `products.csv` | 6 | `product_id`, `name`, `line_hours_per_batch`, `packing_hours_per_batch`, `profit_egp_per_batch`, `cartons_per_batch` |
| `plants.csv` | 2 | `plant_id`, `name`, `location`, `lat`, `lon`, `line_hours_per_week`, `packing_hours_per_week`, `capacity_cartons_per_week` |
| `warehouses.csv` | 3 | `warehouse_id`, `name`, `location`, `region`, `lat`, `lon`, `capacity_cartons_per_week`, `handling_egp_per_carton` |
| `shops.csv` | 24 | `shop_id`, `name`, `area`, `region` (Cairo, Alexandria, Delta), `lat`, `lon`, `weekly_demand_cartons` |
| `plant_warehouse.csv` | 6 | `plant_id`, `warehouse_id`, `distance_km`, `cost_egp_per_carton` (trucks) |
| `warehouse_shop.csv` | 72 | `warehouse_id`, `shop_id`, `distance_km`, `cost_egp_per_carton` (vans) |
| `vans.csv` | 8 | `van_id`, `warehouse_id` (home base), `capacity_cartons`, `cost_egp_per_km`, `shift_hours` |
| `shift_demand.csv` | 7 | `plant_id`, `day` (Sat to Fri), `min_packing_staff` at the Cairo plant |

## Notes
- Products, plants and warehouses are hand-set; shop positions (small jitter around real area centres),
  shop demand, vans and staff needs come from the seeded random generator.
- `distance_km` is the straight-line (haversine) distance x 1.25: an estimate, not real road data.
  Costs: trucks 2 + 0.06 EGP per carton-km, vans 1 + 0.12 EGP per carton-km.
- Weekly demand: Cairo 707, Alexandria 373, Delta 308 cartons (total 1,388).
- E01 uses the Cairo plant (40 line hours and 50 packing hours a week) with its first two products,
  Crunchy Chips (1 h line, 2 h packing, 300 EGP per batch) and Date Bars (2 h, 1 h, 400 EGP).
  Best weekly plan: 20 batches of chips and 10 of date bars, 10,000 EGP.
