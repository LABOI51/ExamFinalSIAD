from base_solver import BaseSolver
from containers_problem import ContainersProblem
from stacking_solution import Stacking

import numpy as np
import datetime
import copy

import enum
import os
import minizinc as mzn


class ContainersProblemSolver(BaseSolver):

    def __init__(self):
        super(ContainersProblemSolver, self).__init__()

    def solve(self, prob=None):
        super(ContainersProblemSolver, self)._prepare()

        if type(prob) is not ContainersProblem:
            raise TypeError('Le type du problème est invalide.')

        curr_stacking = Stacking(prob)

        # TODO Q1a Inserer le code pour instancier le probleme a l'aide
        # de MiniZinc ici
        # DEBUT DU CODE ->
        #Code optionnel pour trouver l'éxecutable de Minizinc: (nécessaire pour moi car minizinc n'est pas ajouté au PATH python)

        driver = mzn.find_driver(
            'C:/Users/Laurent/Documents/Uni/SessionHiver2022/SIAD/MiniZinc/minizinc')
        print(driver)
        #Trouver le solveur à partir de son nom
        solver = mzn.Solver.lookup("coin-bc")

        #Charger le modele
        model_path = os.path.normpath("./Q1/src/minizinc_models/containers.mzn")
        problem = mzn.Model(model_path)
        instance = mzn.Instance(solver, problem)
        instance["HEIGHT"] = prob._height
        instance["WIDTH"] = prob._width
        instance["Void_Nodes"] = prob._void_cells
        # <- FIN DU CODE

        # TODO Q1b Inserer le code pour resoudre le probleme a l'aide
        # de MiniZinc ici
        # DEBUT DU CODE ->
        result = instance.solve(timeout=self.max_time_sec)
        # <- FIN DU CODE

        # TODO Q1c Inserer le code pour extraire les donnees du modele resolu
        # par MiniZinc et placer celles-ci dans curr_empillage ici.
        # Attention, il y a plusieurs indices en commentaire et il faut bien 
        # les lire.
        # INDICES:
        # - Pour vous assurer que la solution est realisable avant 
        #   l'extraction, vous devez verifier que la solution est au moins 
        #   realisable. Ceci peut etre fait utiliser en verifiant si le status
        #   du resultat, disons result.status, correspond a 
        #   mzn.Status.SATISFIED ou mzn.Status.OPTIOMAL_SOLUTION.
        # - mzn.Status.OPTIOMAL_SOLUTION peut aussi etre utilise pour mettre
        #   a jour le "flag" qui indique si oui ou non la solution est prouvee
        #   optimale.
        # - Pour ce probleme, la sortie du code MiniZinc a la console, nous 
        #   aidera grandement a extraire la solution.
        #   Le code suivant vous permettra d'obtenir une liste de paires de
        #   cellules couvertes par chacun des conteneurs a partir de 
        #   l'affichage console de MiniZinc:
        #   paires_str = [ s.split(" ") 
        #                  for s in result.solution._output_item[0:-1].split("|")
        #                ]
        #   paires = [ [ int(s) 
        #                for s in p
        #              ] 
        #              for p in paires_str
        #            ]
        # - Les cellules sont numerotees de 1..(hauteur * largeur). 
        #   Pour trouver la position de la cellule C dans une grille
        #   ou la numerotation des lignes et des colonnes debutes
        #   a 0, utilisez le calcul suivant en Python:
        #     i = int((C - 1) / largeur_de_la_grille) 
        #     j = (C - 1) % largeur_de_la_grille
        #   avec i le numero de ligne, j le numero de colonne,
        #   int l'arrondi a l'entier inferieur et % le reste de la
        #   la division entiere.
        #   Par exemple, voici la position de la cellule numero 8
        #   dans une grille 4 par 3:
        #      0 1 2
        #    0 . . .
        #    1 . . .
        #    2 . 8 .
        #    3 . . . 
        # DEBUT DU CODE ->
        #Vérification que le problème est réalisable et/ou optimal
        if result.status == mzn.Status.SATISFIED:
            if result.status == mzn.Status.OPTIMAL_SOLUTION:
                curr_stacking.proved_optimal = True

            #Liste de paires de cellules couvertes
            paires_str = [s.split(" ")
            for s in result.solution._output_item[0:-1].split("|")
                          ]
            curr_stacking.containers = [ [ int(s)
                for s in p
                       ]
                       for p in paires_str
                       ]

            #Itérer sur les cellules:
            for paire in paires_str:
                for position in range(2):
                    cell = paire[position]
                    i = int((cell - 1) / prob._width)
                    j = (cell - 1) % prob._width
                    curr_stacking.stacking[i][j] += 1

        # <- FIN DU CODE

        super(ContainersProblemSolver, self)._terminate()

        # Retourner une solution
        return curr_stacking
