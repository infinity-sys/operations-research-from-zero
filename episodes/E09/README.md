# E09: The Simplex Method, Step by Step

Video: VIDEO_LINK_PLACEHOLDER (planned Wed 18 Nov 2026, 18:00 Cairo)

This episode opens with the solution of the E08 exercise (the suppliers model in standard form: fifteen
choices of two zeros, five feasible basic solutions, cheapest (4, 3) at 39,000 EGP), then walks the simplex
method by hand on a small Alexandria model without the shop floor: Tableau 0 at the origin, enter / leave /
pivot to (0, 12.8) then to (10, 4.8) with Z = 6,900. The same plan is checked in PuLP, and the final Z-row
is read as shadow prices for the manager.

- `e08_suppliers_basic.py`: E08 exercise. Standard form with 2 surplus and 2 slack; C(6, 2) = 15 choices:
  1 singular, 9 infeasible, 5 feasible. Costs: (4, 3) 39,000; (2.33, 8) 54,000; (10, 0) 60,000; (4, 8)
  64,000; (12, 0) 72,000. Matches the five corners of E06.
- `simplex_hand.py`: hand tableaux for Max 450x1 + 500x2, 2x1 + 2.5x2 ≤ 32, x1 ≤ 10. Tableau 0 (origin)
  → Tableau 1 (0, 12.8) Z = 6,400 → Tableau 2 (10, 4.8) Z = 6,900. Final Z-row: 200 under s1, 50 under s4.
- `simplex_pulp.py`: the same model in PuLP (COIN_CMD). Optimal, x1 = 10, x2 = 4.8, Z = 6,900; both slacks
  zero. Agrees with the final tableau.

## Install
    pip install numpy "pulp[cbc]"
