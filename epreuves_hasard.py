import random

#Second épreuve hasard
def jeu_lance_des():
    essais_max = 3

    for essai in range(1,4):
        print(f"\nEssai {essai}/{essais_max}")

        input("Appuyer sur Entrée pour lancer vos dés !")
        des_joueur = (random.randint(1,6),random.randint(1,6))
        print(f"Valeur obtenue par le joueur : {des_joueur}")

        if 6 in des_joueur:
            print("Félicitations ! Vous remportez la partie et Vous gagnez une clé !")
            return True

        des_maitre = (random.randint(1, 6), random.randint(1, 6))
        print(f"Valeur obtenue par le maître : {des_maitre}")

        if 6 in des_maitre :
            print(f"Le maître remporte la partie.")
            return False

        print("Aucun n'a obtenu 6. On passe au prochain essai !")

    print("\n Aucun joueur n'a obtenu 6 après les 3 essais. C'est un match nul !")
    return False

#Fonction epreuve_hasard()
def epreuve_hasard():
    """Pour la sélection aléatoire d'une épreuve hasard"""
    epreuves = [jeu_lance_des]
    epreuve = random.choice(epreuves)

    return epreuve()