from solution import Solution

import time


class BaseSolver:

    def __init__(self,
                 max_time_sec=0, verbose=1):
        # Un temps maximal de 0 seconde indique qu'il n'y a pas de limite
        # de temps
        self.max_time_sec = max_time_sec
        # Pour contrôler le chronomètre:
        self._last_run_start = 0
        self._last_run_end = 0
        # Niveau de détails pour la sortie console.
        # Interprétation:
        #  0: Aucune sortie
        #  1: Sortie minimale
        #  2: Sortie détaillée
        #  >2: Niveau déboggage
        self.verbose = verbose

    def _prepare(self):
        # Initialiser tous les attributs pour l'exécution
        self._last_run_sec = 0
        # Démarrer le chronomètre
        self._last_run_start = time.time()

    def _continue(self):
        elapsed_time = time.time() - self._last_run_start
        if elapsed_time <= self.max_time_sec:
            return True
        return False

    def _terminate(self):
        # Arrêter le chronomètre et calculer le temps utilisé
        self._last_run_end = time.time()
        self._last_run_sec = self._last_run_end - self._last_run_start

    def solve(self, prob=None):
        # Préparer l'exécution
        self._prepare()

        # Boucle d'exécution
        # NOTE: Ce code, dans une classe derivee, est replace par la resolution 
        #       du probleme qui peut etre une boucle ou pas
        while(self._continue()):
            pass

        # Finaliser l'exécution
        self._terminate()

        # Retourner une solution
        # NOTE: Serait a mettre a jour dans une classe derivee pour retourner
        #       la meilleure solution courante.
        return Solution()
