import pulp

model = pulp.LpProblem("nile_snacks_mix", pulp.LpMaximize)

x = model.add_variable("chips", lowBound=0)       # batches per week
y = model.add_variable("date_bars", lowBound=0)   # batches per week

model += 300 * x + 400 * y, "profit"              # objective (EGP)
model += x + 2 * y <= 40, "line_hours"            # constraint 1
model += 2 * x + y <= 50, "packing_hours"         # constraint 2

result = model.solve(pulp.COIN_CMD(msg=False))

print("Status:", result.status_str)
print("Chips:", x.value(), "batches")
print("Date bars:", y.value(), "batches")
print("Profit:", pulp.value(model.objective), "EGP")
