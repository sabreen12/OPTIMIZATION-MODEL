import pulp

model = pulp.LpProblem("ProductionPlanning", pulp.LpMaximize)

A = pulp.LpVariable('A_units', lowBound=0)
B = pulp.LpVariable('B_units', lowBound=0)

model += 20 * A + 30 * B

model += 2 * A + 4 * B <= 100
model += 3 * A + 2 * B <= 90

model.solve()

print("Status:", pulp.LpStatus[model.status])
print("A Units:", A.varValue)
print("B Units:", B.varValue)
print("Maximum Profit:", pulp.value(model.objective))