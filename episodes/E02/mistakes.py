# The five common modeling mistakes of E02, each run for real (wrong version first, then the fix).
import pandas as pd
import pulp

prod = pd.read_csv("products.csv", index_col="product_id").loc[["P1", "P2", "P3"]].to_dict("index")
need = pd.read_csv("shift_demand.csv", index_col="day")["min_packing_staff"].to_dict()
days = list(need)

def mix(sesame_line=1.5, low=0):
    """Nile Snacks, 3 products at the Cairo plant; sesame_line = line time per batch of sesame sticks."""
    m = pulp.LpProblem("mix", pulp.LpMaximize)
    x1, x2, x3 = (m.add_variable(n, lowBound=low) for n in ("chips", "date_bars", "sesame"))
    m += 300 * x1 + 400 * x2 + 320 * x3
    m += x1 + 2 * x2 + sesame_line * x3 <= 40          # line hours
    m += 2 * x1 + x2 + x3 <= 50                         # packing hours
    m += 40 * x1 + 30 * x2 + 35 * x3 <= 1600            # cartons
    m.solve(pulp.COIN_CMD(msg=False))
    return [v.value() for v in (x1, x2, x3)], pulp.value(m.objective)

def staff(at_least=True):
    m = pulp.LpProblem("staff", pulp.LpMinimize)
    x = {d: m.add_variable(d, lowBound=0) for d in days}
    m += pulp.lpSum(x.values())
    for k, d in enumerate(days):
        on_duty = pulp.lpSum(x[days[(k - j) % 7]] for j in range(5))
        m += (on_duty >= need[d]) if at_least else (on_duty <= need[d])
    m.solve(pulp.COIN_CMD(msg=False))
    return pulp.value(m.objective)

print("1 units, 90 minutes written as 90:", mix(sesame_line=90))
print("  right, 1.5 hours:", mix())
print("2 no x >= 0:", mix(low=None))
print("3 at least written as <=: staff", staff(at_least=False), "| right: staff", staff())
print("4 sum of daily needs:", sum(need.values()), "staff-days | people needed:", staff())
m = pulp.LpProblem("price", pulp.LpMaximize)
price, qty = m.add_variable("price", lowBound=0), m.add_variable("qty", lowBound=0)
try:
    m += price * qty                                    # revenue = price x quantity
except TypeError as e:
    print("5 price * qty:", "TypeError:", e)
