import sys

class Solution:

    def __init__(self):
        pass

    def evaluate(self):
        # NOTE: Nous supposons que la valeur de l'objectif doit être maximisée.
        #       Par défaut, nous retournons donc la plus petite valeur possible
        #       pour un nombre à virgule flottante.
        return sys.float_info.max * -1

    def validate(self):
        # NOTE: Pour l'instant, nous avons une solution vide que nous considérons
        #       considerons toujours non realisable.
        return False
