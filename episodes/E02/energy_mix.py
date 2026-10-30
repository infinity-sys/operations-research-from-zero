import pulp
# per 100 g: protein, fiber, sugar (g, rounded, illustrative); price in EGP per kg
food = {"dates": (2, 7, 66, 80), "peanuts": (26, 9, 5, 150), "oats": (14, 10, 1, 60)}

model = pulp.LpProblem("energy_mix", pulp.LpMinimize)
g = {f: model.add_variable(f, lowBound=0) for f in food}   # grams in one pack

def per_pack(k):   # grams of nutrient k in one pack: 0 protein, 1 fiber, 2 sugar
    return pulp.lpSum(food[f][k] / 100 * g[f] for f in g)

model += pulp.lpSum(food[f][3] / 1000 * g[f] for f in g), "cost"   # EGP per pack
model += pulp.lpSum(g.values()) == 100, "pack_100g"
model += per_pack(0) >= 14, "protein"
model += per_pack(1) >= 9, "fiber"
model += per_pack(2) <= 15, "sugar"
model += g["dates"] >= 0.20 * 100, "dates_at_least_20pct"
model += g["peanuts"] <= 0.30 * 100, "peanuts_at_most_30pct"

result = model.solve(pulp.COIN_CMD(msg=False))
print("Status:", result.status_str)
for f in g:
    print(f + ":", g[f].value(), "g")
print("Cost:", round(pulp.value(model.objective), 2), "EGP per pack")
print("Protein, fiber, sugar:", [round(pulp.value(per_pack(k)), 1) for k in range(3)])
