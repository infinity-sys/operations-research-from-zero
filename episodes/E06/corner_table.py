# check every corner against every constraint (left-hand side used)
corners = {"A": (0, 4), "B": (10, 4), "C": (10, 4.8), "D": (0, 12.8)}
for n, (x1, x2) in corners.items():
    line, pack, cart = 2*x1 + 2.5*x2, 1.5*x1 + x2, 25*x1 + 20*x2
    print(f"{n} ({x1:g}, {x2:g}) line {line:g} packing {pack:g} "
          f"cartons {cart:g} Z {450*x1 + 500*x2:g}")
