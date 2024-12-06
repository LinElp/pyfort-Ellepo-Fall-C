import random

def bonneteau():
    L=['A','B','C']
    print("Bienvenue au jeu de bonneteau")
    print("Vous avez droit à 2 essaies")
    print("Un clé est caché dans l")
    nb_tentatives=2
    tentative=0
    val_select=random.choice(L)
    while tentative<=nb_tentatives:
        choix_joueur=input("Choisissez un bonneteau: ")
        if choix_joueur in L:
            print("présent dans les bonneteaux")
            tentative += 1
            if choix_joueur==val_select:
                print("clé trouvé sous le bonneteau")
                return True
            else:
                print("clé pas trouvé")
                nb_tentatives=nb_tentatives-tentative
                print("il vous reste",nb_tentatives,"essaies")
        else:
            print("bonneteau inexistant:")
    print("Vous avez perdu,la clé se trouve sous le bonneteau",val_select)
    return False








