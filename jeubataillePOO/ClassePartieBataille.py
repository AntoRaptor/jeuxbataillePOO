from ClasseJoueur import *
from ClasseJeuCartesClassique import *



class PartieBataille: 

    

    def __init__(self, joueur):
        self.__joueur = joueur
        self.__ordinateur = Joueur("9000", "HAL")
        self.__jeu = JeuCartesClassique()


    def démarrerPartie(self):
        self.__mélanger()
        self.__distribuer()

        nombredetours = 0
        poursuivre = True
        nombredebataille = 0
         
        while poursuivre:
            poursuivre = self.__main()
            nombredetours += 1
            if self.__bataille == True:
                nombredebataille +=1
        #print("Partie achevée en {0} tours".format(nombredetours))
        print("Partie achevée en {0} tours, dont {1} bataille(s)".format(nombredetours, nombredebataille))

    def __mélanger(self):
        self.__jeu.mélanger()

    def __distribuer(self):
        for i in range(len(self.__jeu.cartes)):
            carte = self.__jeu.tirer()
            if i % 2 == 0:
                self.__joueur.ajouterCarte(carte)
            else:
                self.__ordinateur.ajouterCarte(carte)


    def __main(self, reste=[]):

        #input()

        
        carte_joueur = self.__joueur.tirerCarte()
        carte_ordinateur = self.__ordinateur.tirerCarte()

        if carte_joueur is None:
            self.finPartie(self.__joueur, self.__ordinateur)
            return False
        elif carte_ordinateur is None:
            self.finPartie(self.__ordinateur, self.__joueur)
            return False

        print("Main :")
        print("    -{0} {1} : {2}".format(self.__joueur.prénom, self.__joueur.nom, str(carte_joueur)))
        print("    -{0} {1} : {2}".format(self.__ordinateur.prénom, self.__ordinateur.nom, str(carte_ordinateur)))

        if carte_joueur.valeur == carte_ordinateur.valeur:
            reste.append(carte_joueur)
            reste.append(carte_ordinateur)
            
            return self.__bataille(reste)
        elif carte_joueur.valeur > carte_ordinateur.valeur:
            self.__joueur.ajouterCarte(carte_joueur)
            self.__joueur.ajouterCarte(carte_ordinateur)
            print("    {0} {1} gagne la main !".format(self.__joueur.prénom, self.__joueur.nom))
        else:
            self.__ordinateur.ajouterCarte(carte_ordinateur)
            self.__ordinateur.ajouterCarte(carte_joueur)
            print("    {0} {1} gagne la main !".format(self.__ordinateur.prénom, self.__ordinateur.nom))

        return True

    def __bataille(self, reste):
        print("!! BATAILLE !!")
        #nombredebataille += 1
        return self.__main(reste)

    def finPartie(self, perdant, gagnant):
        perdant.défaites += 1
        gagnant.victoires += 1
        print("{0} {1} a gagné !".format(gagnant.prénom, gagnant.nom))
        #print("Partie achevée en {0}".format(nombredetours))
