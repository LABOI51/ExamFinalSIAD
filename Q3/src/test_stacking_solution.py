import unittest
import sys

from containers_problem import ContainersProblem
from stacking_solution import Stacking


class TestStacking(unittest.TestCase):

    def setUp(self):
        """ Reinitialise automatiquement les donnees avant chaque test """
        # Le probleme suivant est realisable
        height = 5
        width = 6
        void_cells = [ 1, 4, 10, 22, 26, 29 ]

        self.inst1 = ContainersProblem(5,
                                       6,
                                       [ 1, 4, 10, 22, 26, 29 ])
 
        # La solution suivante est une solution optimale au probleme inst1
        # Sa valeur de fonction objectif est 11
        self.optimal_sol_inst1 = Stacking(self.inst1)
        self.optimal_sol_inst1.stacking =  \
            [ [ 0, 0, 1, 0, 1, 0 ] ,
              [ 1, 1, 1, 0, 1, 1 ] ,
              [ 1, 1, 1, 1, 1, 1 ] ,
              [ 1, 1, 1, 0, 1, 1 ] ,
              [ 1, 0, 1, 1, 0, 1 ] ]

        self.optimal_sol_inst1.containers = \
            [ [3, 9], [5, 11], [7, 8], [12, 18], [13, 14], [15, 16], [17, 23],
              [19, 25], [20, 21], [24, 30], [27, 28] ]
        self.obj_val_optimal_sol_inst1 = 11

        self.optimal_sol_inst1.proved_optimal = True

        # La solution suivante est une solution realisable, mais non optimale
        # au probleme inst1
        # Sa valeur de fonction objectif est 7
        self.feasible1_sol_inst1 = Stacking(self.inst1)
        self.feasible1_sol_inst1.stacking =  \
            [ [ 0, 1, 0, 0, 1, 0 ],
              [ 1, 1, 0, 0, 1, 0 ],
              [ 1, 0, 1, 0, 0, 0 ],
              [ 1, 0, 1, 0, 0, 1 ],
              [ 1, 0, 1, 1, 0, 1 ] ]
        self.feasible1_sol_inst1.containers = \
            [ [7, 13], [2, 8], [19, 25], [15, 21], [27, 28], [5, 11], [24, 30] ]
        self.obj_val_feasible1_sol_inst1 = 7

        # La solution suivante est une solution realisable, mais non optimale
        # au probleme inst1
        # Sa valeur de fonction objectif est 0
        self.feasible2_sol_inst1 = Stacking(self.inst1)
        self.feasible2_sol_inst1.stacking =  \
            [ [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ] ]
        self.feasible2_sol_inst1.containers = \
            [  ]
        self.obj_val_feasible2_sol_inst1 = 0

        # Voici une serie de solutions irrealisables au probleme inst1
        # Celles-ci sont irrealisables pour differentes raisons et devraient
        # toutes etre testees
        # Leur valeur de fonction objectif devrait etre un grand float
        # negatif 
        self.infeasible1_sol_inst1 = Stacking(self.inst1)
        self.infeasible1_sol_inst1.stacking = \
            [ [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 1, 0, 0, 0, 0 ],
              [ 0, 1, 0, 0, 0, 0 ] ]
        self.infeasible1_sol_inst1.containers = \
            [ [20, 26] ]
        self.obj_val_infeasible1_sol_inst1 = sys.float_info.max * -1

        self.infeasible2_sol_inst1 = Stacking(self.inst1)
        self.infeasible2_sol_inst1.stacking = \
            [ [ 0, 2, 1, 0, 0, 0 ],
              [ 0, 1, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ] ]
        self.infeasible2_sol_inst1.containers = \
            [ [2, 8], [2, 3] ]
        self.obj_val_infeasible2_sol_inst1 = sys.float_info.max * -1

        self.infeasible3_sol_inst1 = Stacking(self.inst1)
        self.infeasible3_sol_inst1.stacking = \
            [ [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 1 ] ]
        self.infeasible3_sol_inst1.containers = \
            [ [30, 31] ]
        self.obj_val_infeasible3_sol_inst1 = sys.float_info.max * -1

        self.infeasible4_sol_inst1 = Stacking(self.inst1)
        self.infeasible4_sol_inst1.stacking = \
            [ [ 0, 1, 0, 0, 0, 0 ],
              [ 0, 0, 1, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ] ]
        self.infeasible4_sol_inst1.containers = \
            [ [2, 9] ]
        self.obj_val_infeasible4_sol_inst1 = sys.float_info.max * -1

        self.infeasible5_sol_inst1 = Stacking(self.inst1)
        self.infeasible5_sol_inst1.stacking = \
            [ [ 0, 1, 1, 0, 0, 0 ],
              [ 0, 1, 1, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ],
              [ 0, 0, 0, 0, 0, 0 ] ]
        self.infeasible5_sol_inst1.containers = \
            [ [2, 3, 8, 9] ]
        self.obj_val_infeasible5_sol_inst1 = sys.float_info.max * -1

    def test_init(self):
        curr_stacking = Stacking(solvedProblem=self.inst1)

        # Initialement, tout est a 0 dans l'empillage de la solution:
        self.assertTrue(
            curr_stacking.stacking ==
            [ [ 0 ] * self.inst1._width 
            for i in range(0, self.inst1._height)]
        )

        # Initialement, la liste de conteneurs est vide
        self.assertTrue(
            len(curr_stacking.containers) == 0
        )

        # Initialement, proved_optimal est a false
        self.assertFalse(curr_stacking.proved_optimal)

        # Dans un objet Stacking, on conserve une
        # reference au probleme:
        self.assertTrue(curr_stacking.problem is self.inst1)

    # TODO Q3c Code des tests pour valider des solutions
    # RAPPEL: Doit utiliser la methode validate de la classe Stacking
    # DEBUT DU CODE ->
        

    # <- FIN DU CODE

    # TODO Q3d Code des tests de valeur de fonction objectifs
    # RAPPEL: Doit utiliser la methode evaluate de la classe Stacking
    # DEBUT DU CODE ->
    

    # <- FIN DU CODE
