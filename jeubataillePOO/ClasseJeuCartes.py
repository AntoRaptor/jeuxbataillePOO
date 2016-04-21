from ClasseCarte import *
import random


class JeuCartes:

    def __init__(self, vide=False):
        if self.__class__ is JeuCartes:
            raise Exception("Creation interdite")
        else: 
            self.__cartes = []
            self.initialiser()

    def __str__(self):
        cartes_du_jeu = ""
        for carte in self.cartes:
            if cartes_du_jeu == "":
                cartes_du_jeu = str(carte)
            else:
                cartes_du_jeu += ", " + str(carte)
        return cartes_du_jeu

    def mélanger(self):
        random.shuffle(self.cartes)

    def tirer(self):
        try:
            return self.cartes.pop(0)
        except IndexError as erreur:
            print("Il n'y a plus de cartes dans le jeu !")
            return None

    def __getcartes(self):
        return self.__cartes

    def __setcartes(self, carte):

        if len(self.__cartes) > 52:
            raise Exception("Jeu complet")
        self.__cartes.append(carte)
    cartes = property(__getcartes, __setcartes)

    def initialiser(self):
        pass
