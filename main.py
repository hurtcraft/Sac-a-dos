from docplex.mp.model import Model

import csv

weights = []
values = []

with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        weights.append(int(row['weight']))
        values.append(int(row['value']))

mdl = Model(name="knapsack")
capacity = 5
x = mdl.binary_var_list(len(weights))
mdl.add_constraint(mdl.sum(x[i] * weights[i] for i in range(len(weights))) <= capacity)
mdl.maximize(mdl.sum(x[i] * values[i] for i in range(len(weights))))
solution = mdl.solve()

if solution:
    print("Pour une capacite de :",capacity)
    print("Valeur optimale :", solution.objective_value)
    print("Les Objets selectionnes :", [i for i in range(len(weights)) if x[i].solution_value > 0])
    
else:
    print("Pas de solution trouvée")
