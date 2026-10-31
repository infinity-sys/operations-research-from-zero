from ortools.linear_solver import pywraplp

c = [4000, 5000, 6000]
A = [[1, 1, 1], [2, 1, 3], [1, 3, 2], [0, -1, 0]]
b = [30, 50, 65, -5]

s = pywraplp.Solver.CreateSolver("GLOP")     # Google's LP solver
x = [s.NumVar(0, s.infinity(), n) for n in ["small", "medium", "large"]]
for i in range(4):
    s.Add(sum(A[i][j] * x[j] for j in range(3)) <= b[i])
s.Maximize(sum(c[j] * x[j] for j in range(3)))

status = s.Solve()
print("status:", "OPTIMAL" if status == s.OPTIMAL else status)
print("raw x1:", x[0].solution_value())             # floating-point noise
print("plan  :", [round(v.solution_value(), 6) for v in x])
print("profit:", s.Objective().Value())
