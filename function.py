import random

def bonneteau():
    L=['A','B','C']
    print("Bienvenue au jeu de bonneteau")
    print("Vous avez droit à 2 essaies")
    print("Un clé est caché dans l")
    nb_tentaives=2
    tentative=0
    val_select=random.choice(L)
    while tentative<nb_tentaives:
        choix_joueur=input("Choisissez un bonnetau: ")
        if choix_joueur==val_select:
            tentative+=1







