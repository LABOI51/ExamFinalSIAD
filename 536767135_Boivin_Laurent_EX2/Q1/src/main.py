import os

from containers_problem import ContainersProblem
from stacking_solution import Stacking
from containers_problem_solver import ContainersProblemSolver

print("Une instance du probleme")
print("========================")
height = 5
width = 6
void_cells = [ 1, 4, 10, 22, 26, 29 ]

my_problem = ContainersProblem(height,
                               width,
                               void_cells)


# Affichage de l'instance:
print(my_problem)


print("\n" +
      "Exemple de solution realisable (pas necessairement optimale) pour " +
      "le cas stocke dans my_problem")
print("------------------------------------------------------------------" +
      "-----------------------------")
print("D'autres conteneurs peuvent entrer, donc pas optimal.")

my_sol_ex_feasible = Stacking(my_problem)
my_sol_ex_feasible.stacking = [ [ 0, 1, 0, 0, 1, 0 ],
                                [ 1, 1, 0, 0, 1, 0 ],
                                [ 1, 0, 1, 0, 0, 0 ],
                                [ 1, 0, 1, 0, 0, 1 ],
                                [ 1, 0, 1, 1, 0, 1 ] ]
my_sol_ex_feasible.containers = [ [7, 13],
                                  [2, 8],
                                  [19, 25],
                                  [15, 21],
                                  [27, 28],
                                  [5, 11],
                                  [24, 30] ]

print(my_sol_ex_feasible)


print("\n" +
      "Exemple de solution non-realisable pour le cas stocke dans " +
      "my_problem")
print("-----------------------------------------------------------" +
      "----------")
print("On couvre une position occupée.")
my_sol_ex_infeasible1 = Stacking(my_problem)
my_sol_ex_infeasible1.stacking = [ [ 0, 0, 0, 0, 0, 0 ],
                                   [ 0, 0, 0, 0, 0, 0 ],
                                   [ 0, 0, 0, 0, 0, 0 ],
                                   [ 0, 1, 0, 0, 0, 0 ],
                                   [ 0, 1, 0, 0, 0, 0 ] ]
my_sol_ex_infeasible1.containers = [ [20, 26] ]

print(my_sol_ex_infeasible1)


print("\n" +
      "Exemple de solution non-realisable pour le cas stocke dans " +
      "my_problem")
print("-----------------------------------------------------------" +
      "----------")
print("Deux conteneurs sont superposés.")
my_sol_ex_infeasible2 = Stacking(my_problem)
my_sol_ex_infeasible2.stacking = [ [ 0, 2, 1, 0, 0, 0 ],
                                   [ 0, 1, 0, 0, 0, 0 ],
                                   [ 0, 0, 0, 0, 0, 0 ],
                                   [ 0, 0, 0, 0, 0, 0 ],
                                   [ 0, 0, 0, 0, 0, 0 ] ]
my_sol_ex_infeasible2.containers = [ [2, 8],
                                     [2, 3] ]

print(my_sol_ex_infeasible2)


print("\n" +
      "Exemple de solution non-realisable pour le cas stocke dans " +
      "my_problem")
print("-----------------------------------------------------------" +
      "----------")
print("Un conteneur depasse de la grille")
my_sol_ex_infeasible3 = Stacking(my_problem)
my_sol_ex_infeasible3.stacking = [ [ 0, 0, 0, 0, 0, 0 ],
                                   [ 0, 0, 0, 0, 0, 0 ],
                                   [ 0, 0, 0, 0, 0, 0 ],
                                   [ 0, 0, 0, 0, 0, 0 ],
                                   [ 0, 0, 0, 0, 0, 1 ] ]
my_sol_ex_infeasible3.containers = [ [30, 31] ]

print(my_sol_ex_infeasible3)


print("\n" +
      "Exemple de solution non-realisable pour le cas stocke dans " +
      "my_problem")
print("-----------------------------------------------------------" +
      "----------")
print("Un conteneur n'est pas sur les cellules adjacentes: en croix, pas de diagonale")
my_sol_ex_infeasible4 = Stacking(my_problem)
my_sol_ex_infeasible4.stacking = [ [ 0, 1, 0, 0, 0, 0 ],
                                   [ 0, 0, 1, 0, 0, 0 ],
                                   [ 0, 0, 0, 0, 0, 0 ],
                                   [ 0, 0, 0, 0, 0, 0 ],
                                   [ 0, 0, 0, 0, 0, 0 ] ]
my_sol_ex_infeasible4.containers = [ [2, 9] ]

print(my_sol_ex_infeasible4)


print("\n" +
      "Exemple de solution non-realisable pour le cas stocke dans " +
      "my_problem")
print("-----------------------------------------------------------" +
      "----------")
print("Tous les conteneurs sont de taille 2.")
my_sol_ex_infeasible5 = Stacking(my_problem)
my_sol_ex_infeasible5.stacking = [ [ 0, 1, 1, 0, 0, 0 ],
                                   [ 0, 1, 1, 0, 0, 0 ],
                                   [ 0, 0, 0, 0, 0, 0 ],
                                   [ 0, 0, 0, 0, 0, 0 ],
                                   [ 0, 0, 0, 0, 0, 0 ] ]
my_sol_ex_infeasible5.containers = [ [2, 3, 8, 9] ]

print(my_sol_ex_infeasible5)

# Resolution
print("\n" +
      "Résolution de l'instance my_problem")
print("===================================")
my_solution = ContainersProblemSolver().solve(my_problem)

# Affichage de la solution
print("\n" +
      "Solution retournee")
print("------------------")
print(my_solution)
