from epreuve_mathematiques import *
from epreuves_hasard import *
from epreuve_logique import *
from enigme_pere_fouras import *
from epreuve_finale import *
def jeu():
    print("Bienvenue dans le fort!")
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
        choix_epreuve = int(input("Choisissez un chiffre entre & et 4 pour le type d'épreuve: "))


