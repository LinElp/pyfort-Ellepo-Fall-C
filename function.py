import random
"""def est_premier(n):
    nb_premier=False
    if n<=1:
        return nb_premier
    for i in range(2,n):
        if n%i==0:
            nb_premier=False
    return nb_premier
def premier_plus_proche(n):
    while not est_premier(n):
        n=n+1
    return n

def epreuve_math_premier():
    n = random.randint(10, 20)
    print("Saisir le nombre de premier le plus proche de {}".format(n))
    reponse = input("Entrer votre réponse: ")
    if premier_plus_proche(n) == reponse:
        return True
    else:
        return False


epreuve_math_premier()"""

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







