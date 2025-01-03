import random

def afficher_grille(grille):
    for i in range(3):
        if i > 0:
            print("---------")
        print('|'.join(grille[i]))

def verifier_victoire(grille, symbole):
    for i in range(3):
        if grille[i][0] == symbole and grille[i][1] == symbole and grille[i][2] == symbole:
            return True

    for j in range(3):
        if grille[0][j] == symbole and grille[1][j] == symbole and grille[2][j] == symbole:
            return True

    if grille[0][0] == symbole and grille[1][1] == symbole and grille[2][2] == symbole:
        return True
    if grille[0][2] == symbole and grille[1][1] == symbole and grille[2][0] == symbole:
        return True
    return False

def coup_maitre(grille, symbole):
    adversaire = 'X' if symbole == 'O' else 'O'

    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = symbole
                if verifier_victoire(grille, symbole):
                    grille[i][j] = " "
                    return (i, j)
                grille[i][j] = adversaire
                if verifier_victoire(grille, adversaire):
                    grille[i][j] = " "
                    return (i, j)
                grille[i][j] = " "

    choix = [(i, j) for i in range(3) for j in range(3) if grille[i][j] == " "]
    return random.choice(choix) if choix else None

def tour_joueur(grille):
    valide = False
    while not valide:
        entree = input("Joueur X, c'est à vous. Où voulez-vous placer votre symbole ? Entrez sous forme 'ligne,colonne': ")
        coordonnees = entree.split(',')
        if len(coordonnees) == 2 and coordonnees[0].isdigit() and coordonnees[1].isdigit():
            ligne, colonne = int(coordonnees[0]) - 1, int(coordonnees[1]) - 1
            if 0 <= ligne < 3 and 0 <= colonne < 3:
                if grille[ligne][colonne] == " ":
                    grille[ligne][colonne] = 'X'
                    valide = True
                else:
                    print("Cette case est déjà prise. Veuillez choisir une autre case.")
            else:
                print("Les coordonnées doivent être entre 1 et 3 pour chaque axe.")
        else:
            print("Entrée invalide. Assurez-vous de séparer les chiffres par une virgule et d'utiliser des nombres valides.")

def tour_maitre(grille):
    coup = coup_maitre(grille, symbole='O')
    if coup:
        ligne, colonne = coup
        grille[ligne][colonne] = 'O'
        print("Tour du maître du jeu (O)...")

def grille_complete(grille):
    for ligne in grille :
        for case in ligne :
            if case == ' ':
                return False
    return True

def verifier_resultat(grille):
    if verifier_victoire(grille, 'X'):
        print("Le joueur X a gagné !")
        return True
    if verifier_victoire(grille, 'O'):
        print("Le maître du jeu O a gagné !")
        return True
    if grille_complete(grille):
        print("Match nul !")
        return True
    return False

def initialiser_grille():
    grille = []

    for _ in range(3):
        ligne = []
        for _ in range(3):
            ligne.append(" ")
        grille.append(ligne)

    return grille


def jeu_tictactoe():
    grille = initialiser_grille()
    afficher_grille(grille)

    while True:
        tour_joueur(grille)
        afficher_grille(grille)
        if verifier_resultat(grille):
            break

        if not grille_complete(grille):
            tour_maitre(grille)
            afficher_grille(grille)
            if verifier_resultat(grille):
                break
        else:
            print("Match nul !")
            break


if __name__ == "__main__":
    jeu_tictactoe()