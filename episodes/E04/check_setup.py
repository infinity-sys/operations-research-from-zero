import sys, numpy, pandas, scipy, pulp, networkx, ortools

print("Python  ", sys.version.split()[0])
print("NumPy   ", numpy.__version__)
print("pandas  ", pandas.__version__)
print("SciPy   ", scipy.__version__)
print("PuLP    ", pulp.__version__)
print("OR-Tools", ortools.__version__)
print("NetworkX", networkx.__version__)
print("CBC     ", "ok" if pulp.COIN_CMD().available() else "missing")
