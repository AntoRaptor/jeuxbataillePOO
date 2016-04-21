# on utilise la librairie graphique tkinter

from tkinter import *
from test import *

# zone de déclaration de fonctions

truc = c1

def convertir():
    """
        cette fonction convertit un nombre décimal entier en séquence
        binaire de 0 et de 1, puis affiche le résultat;
        si les données entrées ne sont pas correctes, le résultat
        affichera 'error';
    """
    # on récupère les données saisies par l'utilisateur
    sequence = entree.get()

    # on essaie de faire la conversion en séquence binaire
    try:
        # conversion d'un entier en séquence binaire
        résultat = bin(int(sequence))
    # si une erreur survient
    except:

        # on affiche 'error' à la place

        résultat = 'error'
    # end try

    # affichage du résultat
    cvarRésultat.set(test)

# end def

# programme principal (GUI - interface graphique utilisateur)

# on crée une fenêtre principale
fenêtre = Tk()

# on ajoute des composants graphiques

# étiquette texte à afficher
Label(fenêtre, text="Veuillez saisir un entier décimal, SVP :").pack(pady=5, padx=10)

# zone de texte pour la saisie des données entrées par l'utilisateur
entree = Entry(fenêtre)
entree.pack(padx=10)

# on va utiliser une variable de contrôle pour afficher un résultat
# variable selon les calculs de conversion que l'on va effectuer
# ultérieurement
cvarRésultat = StringVar()
# on rattache cette variable de contrôle à une étiquette texte afin
# de pouvoir afficher ses données en sortie visuelle
Label(fenêtre, textvariable=cvarRésultat).pack(pady=5, padx=10)

# il ne nous reste plus qu'à utiliser un bouton cliquable pour
# déclencher l'opération de conversion du nombre en séquence binaire
# de 0 et de 1
Button(fenêtre, text="Convertir", command=convertir).pack(side=LEFT, pady=10, padx=30)

# ainsi qu'un bouton cliquable pour quitter notre application
Button(fenêtre, text="Quitter", command=fenêtre.destroy).pack(side=RIGHT, pady=10, padx=10)

# pour finir, on lance l'application graphique en entrant dans la
# boucle événementielle principale
fenêtre.mainloop()
