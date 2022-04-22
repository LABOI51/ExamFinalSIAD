from problem import Problem
from numbers import Number

import copy


class ContainersProblem(Problem):

    def __init__(self,
                 height = 0,
                 width = 0,
                 list_void_cells = []):

        super(ContainersProblem, self).__init__()

        # Le plan d'un bateau est defini par une grille de cellules de 1 unite
        # par 1 unite.
        # Les parametres du problemes sont:
        #  - hauteur et largeur
        #  - liste de cellules occupees: un conteneur ne peut pas etre 
        #    superpose sur les cellules de cette liste.
        # La numerotation des celulles est a partir de 1, de gauche a droite,
        # de haut en bas. Exemple, pour une grille 3 par 4, nous avons la 
        # numerotation suivante:
        #  1  2  3  4
        #  5  6  7  8
        #  9 10 11 12
        # Si la liste de cellules occupees contient 6 et 11 alors les cellules
        # 6 et 11 ci-dessus ne peuvent pas contenir de conteneur.

        if type(height) is not int:
            raise TypeError('La hauteur de la grille n\'est pas de type int.')
        if type(width) is not int:
            raise TypeError('La largeur de la grille n\'est pas de type int.')
        if type(list_void_cells) is not list:
            raise TypeError(
                'La liste n\'est pas de type list.')
            for e in list_void_cells:
                if type(e) is not int:
                    raise TypeError(
                        'Tous les éléments de list_pos_occ ' +
                        'doivent être de type int'
                        )

        self._height = height
        self._width = width
        self._void_cells = copy.deepcopy(list_void_cells)

        if not self.is_instance_correct():
            raise ValueError(
                'L\'instance est incorrecte.' +
                ' Vérifiez que les données sont entrées correctement')


    def __str__(self):
        tmp_str = ('Liste des cellules occupées: ' +
                   str(self._void_cells) +
                   '\nHauteur: ' +
                   str(self._height) +
                   '\nLargeur: ' +
                   str(self._width))

        return str(tmp_str)


    def is_instance_correct(self):
        """Retourne vrai si les donnees semblent correctes."""

        for e in self._void_cells:
            if e <= 0:
                return False
            if e > self._height * self._width:
                return False
        
        return True
        
