import random


def afficher_grille(grille):
    for i in range(3):
        if i > 0:
            print("---------")
        print('|'.join(grille[i]))



def verifier_victoire(grille,symbole):
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

def coup_maitre(grille,symbole):
    if symbole == 'O':
        adversaire = 'X'
    else:
        adversaire = 'O'

    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = symbole
                if verifier_victoire(grille,symbole):
                    return(i,j)
                grille[i][j] = adversaire
                if verifier_victoire(grille,adversaire):
                    grille[i][j] = " "
                    return (i,j)
                grille[i][j] = " "

    choix = []
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                choix.append((i, j))
    if choix :
        return random.choice(choix)
    else:
        return None
def tour_joueur(grille):
    valide = False
    while not valide:
        ligne, colonne = int(input("Joueur X, c'est à vous. Où voulez-vous placer votre symbole ? ").split(','))
        if grille[ligne - 1][colonne - 1] == " ":
            grille[ligne - 1][colonne - 1] = 'X'
            valide = True
        else:
            print("Cette case est déjà prise. Veuillez choisir une autre case.")
    if ValueError or IndexError:
        print("Entrée invalide. Veuillez entrer les coordonnées sous forme (ligne,colonne).")


def tour_maitre(grille):
    ligne, colonne = coup_maitre(grille, symbole='O')
    grille[ligne][colonne] = 'O'
    print("Tour du maître du jeu (O)...")

def grille_complete(grille):
    for ligne in grille:
        for case in ligne:
            if case == ' ':
                return False
    return True

def verifier_resultat(grille):
    if verifier_victoire(grille, 'X') or verifier_victoire(grille, 'O'):
        return True
    if grille_complete(grille):
        print("Match nul !")
        return True
    return False

def initialiser_grille():
    grille = []
    for _ in range(3):
        ligne = [" " for _ in range(3)]
        grille.append(ligne)
    return grille

def jeu_tictactoe():
    grille = initialiser_grille()
    afficher_grille(grille)
    continuer = True

    while True:
        tour_joueur(grille)
        afficher_grille(grille)
        if verifier_resultat(grille):
            print("Le joueur X a gagné !")
            return

        if not grille_complete(grille):
            tour_maitre(grille)
            afficher_grille(grille)
            if verifier_resultat(grille):
                print("Le maître du jeur O a gagné !")
                return
        else:
            print ("Match nul !")
            return

