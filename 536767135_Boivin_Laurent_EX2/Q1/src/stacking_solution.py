from solution import Solution
from containers_problem import ContainersProblem

import sys
import math


class Stacking(Solution):

    def __init__(self,
                 solvedProblem = ContainersProblem()):
        super(Stacking, self).__init__()
        # Stocker une référence au problème pour la réutiliser facilement
        # plus tard:
        self.problem = solvedProblem
        
        # Une solution, pas necessairement realisable, est definie par un 
        # empillage (stacking) de conteneurs et par les positions des 
        # conteneurs.
        # L'empillage est simplement le nombre de conteneurs dans chaque
        # cellule de la grille
        # La solution complete contient aussi, pour chaque conteneur
        # positionne dans la grille, c'est a dire la paire de cellules 
        # qu'il couvre.
        
        # Ci-dessous, on indique le nombre de conteneurs dans chaque cellule
        # qui correspond au plan du bateau pour former l'empillage, au depart
        # il n'y a aucun conteneur, donc tout est a zero:
        self.stacking = [ [ 0 ] * solvedProblem._width 
                        for i in range(0, solvedProblem._height)]

        # Ci-dessous, la liste des cellules couvetes par chaque conteneur.
        # On a une paire de cellules par conteneur.
        # On rappelle que les cellules sont numerotees de 1 a 
        # hauteur * largeur.
        # C'est ce numero qui est utilise pour identifier les cellules 
        # couvertes dans la liste ci-dessous.
        # Au depart la liste est vide:
        self.containers = [ ]
        
        # Permet d'indiquer si la solution est prouvee realisable ou pas:
        self.proved_optimal = False

    def __str__(self):
        tmp_str = "\nEmpillage (compte par cellule):\n"
        max_nb_digits = 0
        for e in self.stacking:
            for f in e:
                nb_digits = 1
                if f > 0:
                    nb_digits = int(math.log10(f)) + 1
                if nb_digits > max_nb_digits:
                    max_nb_digits = nb_digits

        for e in self.stacking:
            for f in e:
                nb_digits = 1
                if f > 0:
                    nb_digits = int(math.log10(f)) + 1
                for i in range(0, max_nb_digits - nb_digits + 1):
                    tmp_str += " "
                tmp_str += str(f)
            tmp_str += "\n"
            
        tmp_str += "\nListe de conteneurs (cellules couvertes):\n"
        tmp_str += str(self.containers)
        return tmp_str

    def evaluate(self):
        if self.validate() is False:
            # Pour nous, une solution non réalisable aura une très petite
            # valeur de fonction objectif.
            # (rappel: nous maximisons l'objectif)
            return sys.float_info.max * -1

        obj_val = 0
        # NOTE: Non codee actuellement

        return obj_val

    def validate(self):
        # NOTE: Non codee actuellement

        return True
