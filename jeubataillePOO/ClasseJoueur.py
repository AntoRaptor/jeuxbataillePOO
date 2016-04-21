from ClassePaquet import *

class Joueur:
    def __init__(self, nom, prénom):
        self.__nom = nom
        self.__prénom = prénom
        self.__victoires = 0
        self.__défaites = 0
        self.__paquet = Paquet()

    def getNom(self):
        return self.__nom
    nom = property(getNom)

    def getPrénom(self):
        return self.__prénom
    prénom = property(getPrénom)

    def getVictoires(self):
        return self.__victoires
    def setVictoires(self, n):
        self.__victoires = n
    victoires = property(getVictoires, setVictoires)

    def getDéfaites(self):
        return self.__défaites
    def setDéfaites(self, n):
        self.__défaites = n 
    défaites  = property(getDéfaites, setDéfaites)

    def getPaquet(self):
        return self.__paquet
    paquet = property(getPaquet)

    def tirerCarte(self):
        return self.paquet.tirer()

    def ajouterCarte(self, carte):
        self.paquet.ajouter(carte)

    def __str__(self):
        return "{0} {1}\n Palmarès : {2} victoire(s) et {3} défaite(s)\n {4}".format(self.nom, self.prénom, self.victoires, self.défaites, str(self.paquet))
