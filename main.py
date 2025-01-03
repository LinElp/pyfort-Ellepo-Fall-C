from epreuve_mathematiques import *
from epreuves_hasard import *
from epreuve_logique import *
from enigme_pere_fouras import *
from epreuve_finale import *
def jeu():
    print("🏰 Bienvenue dans le fort!")
    print("Votre mission est de former une équipe de 3 joueurs maximum.")
    print("Votre équipe devra réussir 3 épreuves pour obtenir 3 clés et enfin ouvrir la salle du trésor,")
    print("Bonne chance !")
    equipe = []
    nb_joueurs = 0
    print("Créer votre équipe de 3 joueurs")
    while nb_joueurs < 3:
        nom_joueur = input("Nom du joueur: ")
        equipe.append(nom_joueur)
        nb_joueurs += 1
    print("Votre équipe est prête!")
    cles_gagnees = 0
    while cles_gagnees < 3:
        print("Menu des épreuves:")
        print("1 - Mathématiques")
        print("2 - Hasard")
        print("3 - Logique")
        print("4 - Énigme du Père Fouras")
        choix_epreuve = int(input("Choisissez un chiffre entre 1 et 4 pour le type d'épreuve: "))

        if choix_epreuve not in ["1", "2", "3", "4"]:
            print("Veuillez entrer un nombre valide entre 1 et 4.")
            return

        choix_epreuve = int(choix_epreuve)

        # Gestion des épreuves
        if choix_epreuve == 1:
            print("Vous avez choisi une épreuve de Mathématiques !")
            if epreuve_math():
                cles_gagnees += 1
        elif choix_epreuve == 2:
            print("Vous avez choisi une épreuve de Hasard !")
            if epreuve_hasard():
                cles_gagnees += 1
        elif choix_epreuve == 3:
            print("Vous avez choisi une épreuve de Logique !")
            if jeu_tictactoe():
                cles_gagnees += 1
        elif choix_epreuve == 4:
            print("Vous avez choisi une énigme du Père Fouras !")
            if enigmes_pere_fouras():
                cles_gagnees += 1

        print(f"\n Clés obtenues : {cles_gagnees}/3\n")


if __name__ == "__main__":
    jeu()
