class Carte:

    valeurs = (None, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi", "As")
    couleurs = ("Coeur", "Carreau", "Trèfle", "Pique")

    def __init__(self, val, coul):
        if val < 2 or val > 14:
            print("ERREUR : La valeur de la carte est comprise entre 2 et 14")
            exit(1)
        if coul < 0 or coul > 3:
            print("ERREUR : La couleur doit être comprise entre 0 et 3")
            exit(1)
        self.__valeur = val
        self.__couleur = coul

    def __str__(self):
        return str(Carte.valeurs[self.__valeur]) + " de " + Carte.couleurs[self.__couleur]

    def afficherASCII(self):
        nom = str(Carte.valeurs[self.__valeur]) + " de " + Carte.couleurs[self.__couleur]
        taille = len(nom) + 2
        print("/", "-" * taille, "\\", sep="")
        print("|", nom, "|")
        print("\\", "-" * taille, "/", sep="")



    #Encapsulation :

    def __getValeur(self):
        #print("Passage en getValeur ...")
        return self.__valeur

    def __setValeur(self, val):
        print("Passage en setValeur ...")
        self.__valeur = val

    valeur = property(__getValeur, __setValeur)

    def __getCouleur(self):
        print("Passage en getCouleur ...")
        return self.__couleur

    def __setCouleur(self, coul):
        print("Passage en setCouleur ...")
        self.__couleur = coul

    couleur = property(__getCouleur, __setCouleur)
