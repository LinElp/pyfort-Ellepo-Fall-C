import json
import random
def charger_enigmes(fichier):
    with open("enigmes_PF.json", 'r',encoding='utf-8') as f:
        donnees=json.load(f)
    print(donnees)
    enigmes=[{"question":e["question"],"reponse":e["reponse"]} for e in donnees]
    return enigmes
def enigmes_pere_fouras():
    L=charger_enigmes("enigmes_PF.json")
    enigme=random.choice(L)
    print("Voici l'enigme choisi:",enigme)
    nbre_essai=3
    while nbre_essai>0:
        reponse=input("Entrer votre reponse:").lower
        if reponse==enigme["reponse"]:
            print("Bravo! Réponse correcte")
            return True
        else:
            nbre_essai-=1
            if nbre_essai>0:
                print(f"Il vous reste {nbre_essai},essais")
            else:
                print("Dommage! vous avez échoué")
                return False





