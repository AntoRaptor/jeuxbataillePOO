from ClasseCarte import *
from ClasseJeuCartes import *
from ClasseJeuCartesClassique import * 
from ClasseJoueur import *
from ClassePartieBataille import *

 
#c1 = Carte(5, 3)
#c1.afficherASCII()

#c2 = Carte(13, 1)
#c2.afficherASCII()
#print(c1)
 
#j = JeuCartes()
#j.mélanger()



#j = JeuCartesClassique()
#j.mélanger()
#for k in range(52):
#    print(j.tirer())
#print(j.tirer())
#carte = Carte(2, 3)
#olivier = Joueur("Fontaine", "olivier")
#print(olivier)
#print(olivier.getVictoires())
#olivier.ajouterCarte(carte)
#print(olivier)

joueur1 = Joueur("Fontaine", "Antonin")
jeu = PartieBataille(joueur1)
jeu.démarrerPartie()