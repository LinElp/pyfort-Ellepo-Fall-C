import random

#Première épreuve mathématique
def Factorielle(n):
    """Calcule la factorielle de l'entier n (notée n!)."""
    if n == 0:      #Isolation du cas unique du 0
        return 1
    else:           #Calcule de la factorielle de n
        res = 1
        for i in range(1, n+1):
            res *= i
        return res

def epreuve_math_factorielle():
    """Fonction de l'épreuve"""
    n = random.randint(1, 10)       #Choix aléatoire de n
    print(f"Épreuve de Mathématiques: Calculer la factorielle de {n}")
    reponse_joueur = int(input("Votre réponse: ")) #Réponse du joueur


    bonne_reponse = Factorielle(n)          #Calcule de la factorielle du n choisi aléatoirement

    if reponse_joueur == bonne_reponse:     #Vérification de la réponse du joueur
        print("Correct! Vous gagnez une clé.")
    else:
        print(f"Incorrect! La bonne réponse est {bonne_reponse}")


#Seconde épreuve mathématique
def epreuve_roulette_mathematique():
    """fonction de l'épreuve qui consiste à génèrer cinq nombres
    aléatoires entre 1 et 20, puis choisit aléatoirement une opération parmi l'addition, la
    soustraction et la multiplication. """

    nombres = []    #Création de la liste des nombres aléatoires
    for i in range(5):
        nombre = random.randint(1, 20)
        nombres.append(nombre)
    operation = ['addition', 'soustraction', 'multiplication']  #Les différentes opérations qui seront choisis aléatoirement
    operation = random.choice(operation)

#Les différentes opérations
    if operation == 'addition':
         res = 0
         for nombre in nombres:
            res += nombre

    elif operation == 'soustraction':
        res = nombres[0]
        for i in range(1, 5):
            res -= nombres[i]

    elif operation == 'multiplication':
        res = 1
        for nombre in nombres:
            res *= nombre

    print(f"Nombres sir la roulette :{nombres}")
    print(f"Calculez le résultat en combinant ces nombres avec une {operation}")

    reponse_joueur = int(input("Votre réponse: "))  # Réponse du joueur

    bonne_reponse = res # implémentation de la bonne réponse

    if reponse_joueur == bonne_reponse:  # Vérification de la réponse du joueur
        print("Correct! Vous gagnez une clé.")
    else:
        print(f"Incorrect! La bonne réponse est {bonne_reponse}")


#Fonction epreuve_math()
def epreuve_math():
    """Pour la sélection aléatoire d'une épreuve mathematique"""
    epreuves = [epreuve_math_factorielle,epreuve_roulette_mathematique]
    epreuve = random.choice(epreuves)

    return epreuve()
