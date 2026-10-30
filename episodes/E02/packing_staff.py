import pandas as pd
import pulp

need = pd.read_csv("shift_demand.csv", index_col="day")["min_packing_staff"].to_dict()
days = list(need)   # Sat, Sun, Mon, Tue, Wed, Thu, Fri

model = pulp.LpProblem("packing_staff", pulp.LpMinimize)
x = {d: model.add_variable("start_" + d, lowBound=0) for d in days}   # start day d

model += pulp.lpSum(x.values()), "staff"   # each person is counted once
duty = {}
for k, d in enumerate(days):   # on duty on day d: started 0 to 4 days before
    duty[d] = pulp.lpSum(x[days[(k - j) % 7]] for j in range(5))
    model += duty[d] >= need[d], "cover_" + d

result = model.solve(pulp.COIN_CMD(msg=False))
print("Status:", result.status_str)
for d in days:
    print(d, "start", x[d].value(), "| on duty", duty[d].value(), "| need", need[d])
print("Staff:", pulp.value(model.objective))
