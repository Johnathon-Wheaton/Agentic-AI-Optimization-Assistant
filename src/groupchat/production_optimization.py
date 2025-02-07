# filename: production_optimization.py

import pandas as pd
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpStatus, value, PULP_CBC_CMD

# Input parameters
products = ['A', 'B', 'C']
production_requirements = {
    'A': {'Mat1': 2, 'Mat2': 3, 'ProdTime': 2, 'Cost': 50},
    'B': {'Mat1': 4, 'Mat2': 1, 'ProdTime': 3, 'Cost': 80},
    'C': {'Mat1': 1, 'Mat2': 2, 'ProdTime': 1.5, 'Cost': 40},
}

demands = {
    1: {'A': 100, 'B': 150, 'C': 200},
    2: {'A': 120, 'B': 130, 'C': 180},
    3: {'A': 140, 'B': 140, 'C': 160},
    4: {'A': 130, 'B': 160, 'C': 150},
}

# Storage costs per product
storage_costs = {
    'A': 10,  # Cost for storing Product A
    'B': 12,  # Cost for storing Product B
    'C': 8    # Cost for storing Product C
}

# Create the problem
problem = LpProblem("Production_Optimization", LpMinimize)

# Decision variables
P = LpVariable.dicts("Production", ((t, p) for t in range(1, 5) for p in products), lowBound=0)  # Production quantities
S = LpVariable.dicts("Storage", ((t, p) for t in range(1, 5) for p in products), lowBound=0)  # Storage quantities

# Objective function including storage costs
problem += lpSum(production_requirements[p]['Cost'] * P[(t, p)] for t in range(1, 5) for p in products) + \
            lpSum(storage_costs[p] * S[(t, p)] for t in range(1, 5) for p in products)

# Constraints
for t in range(1, 5):
    for p in products:
        if t == 1:
            problem += S[(t, p)] == P[(t, p)] - demands[t][p]
        else:
            problem += S[(t, p)] == S[(t - 1, p)] + P[(t, p)] - demands[t][p]

        # Ensure non-negative storage
        problem += S[(t, p)] >= 0

# Solve the problem without time limit / optimality gap (commented out options)
problem.solve(PULP_CBC_CMD(msg=1))  # msg=1 to enable output messages during solving

# Collecting results
results = {
    'Decision Variable': [],
    'Value': []
}
for t in range(1, 5):
    for p in products:
        results['Decision Variable'].append(f"P_{t}{p}")
        results['Value'].append(value(P[(t, p)]))
        results['Decision Variable'].append(f"S_{t}{p}")
        results['Value'].append(value(S[(t, p)]))

# Save results to an Excel file
results_df = pd.DataFrame(results)
results_df.to_excel('output.xlsx', index=False)

# Print the status of the solution
print(f"Status: {LpStatus[problem.status]}")