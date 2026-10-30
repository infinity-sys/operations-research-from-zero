import pulp

marks = {"OR": 3, "Numerical": 2, "Probability": 2.5}   # expected marks per hour (your estimate)

model = pulp.LpProblem("study_plan", pulp.LpMaximize)
h = {s: model.add_variable(s, lowBound=5, upBound=15) for s in marks}   # hours this week
sleep = model.add_variable("sleep", lowBound=49)                          # 7 hours a night

model += pulp.lpSum(marks[s] * h[s] for s in h), "expected_marks"
model += pulp.lpSum(h.values()) + sleep <= 84, "free_hours"

result = model.solve(pulp.COIN_CMD(msg=False))
print("Status:", result.status_str)
print({s: h[s].value() for s in h}, "sleep:", sleep.value())
print("Expected marks:", pulp.value(model.objective))
