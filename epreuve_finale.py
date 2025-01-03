import json
import random


def salle_De_Tresor():
    with open(r'C:/Users/ellep/OneDrive - Efrei/Bureau/Dépot_intermédiaire_ELLEPO_FALL/indicesSalle (1).json', 'r', encoding='utf-8') as f:
        jeu_tv = json.load(f)

    annee = random.choice(list(jeu_tv['Fort Boyard'].keys()))
    emission_cle = random.choice(list(jeu_tv['Fort Boyard'][annee].keys()))
    emission = jeu_tv['Fort Boyard'][annee][emission_cle]

    indices = emission['Indices']
    mot_code = emission['MOT-CODE']

    print("Indices :")
    i = 0
    while i < 3 and i < len(indices):
        print(f"- {indices[i]}")
        i += 1

    essais_restants = 3
    reponse_correcte = False

    while essais_restants > 0:
        reponse = input("Entrez le mot-code : ").upper()

        if reponse == mot_code:
            reponse_correcte = True
            break
        else:
            essais_restants -= 1
            if essais_restants > 0:
                print(f"Mauvaise réponse. Il vous reste {essais_restants} essai(s).")
                indice_supplementaire = 3 + (3 - essais_restants)
                if indice_supplementaire < len(indices):
                    print(f"Indice supplémentaire : {indices[indice_supplementaire]}")
            else:
                print(f"Dommage ! Le mot-code était : {mot_code}")

    if reponse_correcte:
        print("Bravo ! Vous avez trouvé le mot-code !")
    else:
        print("Échec ! Vous n'avez pas trouvé le mot-code.")

