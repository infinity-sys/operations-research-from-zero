# Method 2: check every corner of the feasible region (Nile Snacks, E01)
corners = {"O": (0, 0), "A": (25, 0), "B": (20, 10), "C": (0, 20)}

for name, (x, y) in corners.items():
    line = x + 2 * y          # line hours used (max 40)
    packing = 2 * x + y       # packing hours used (max 50)
    profit = 300 * x + 400 * y
    ok = line <= 40 and packing <= 50
    print(name, (x, y), "line", line, "packing", packing, "profit", profit, "OK" if ok else "NOT allowed")
