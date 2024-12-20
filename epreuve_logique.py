import random

symbole = random.choice(['X','O'])
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

#def tour_joueur(grille):

def tour_maitre(grille):
    ligne, colonne = coup_maitre(grille, symbole:'O')
    g