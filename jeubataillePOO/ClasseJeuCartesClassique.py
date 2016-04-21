from ClasseJeuCartes import *
from ClasseCarte import *

class JeuCartesClassique(JeuCartes):
    def __init__(self):
        super().__init__()

    def initialiser(self):
        for coul in range(4):
            for val in range(2, 15):
                self.cartes.append(Carte(val, coul))
