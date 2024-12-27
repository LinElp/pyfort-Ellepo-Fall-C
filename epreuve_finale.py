import json
import random


def salle_De_Tresor():
    with open("indicesSales.json", 'r', encoding='utf-8') as f:
         jeu_tv= json.load(f)
         annee=random.choice(list(jeu_tv.keys()))
         emission_cle = random.choice(list(jeu_tv[annee].keys()))
         emission = jeu_tv[annee][emission_cle]
         indices = emission['Indices']
         mot_code = emission['MOT-CODE']
         print("Indices :")
         i = 0
         while i < 3 and i < len(indices):
              print(f"- {indices[i]}")
              i += 1
         essais_restants = 3
         reponse_correcte = False

         while essais_restants > 0 and not reponse_correcte:
              reponse = input("Entrez le mot-code : ").upper()

              if reponse == mot_code:
                   reponse_correcte = True
              else:
                   essais_restants -= 1
                   print(f"Mauvaise réponse. Il vous reste {essais_restants} essai(s).")
                   indice_supplementaire = 3 + (3 - essais_restants)
                   if essais_restants > 0 and indice_supplementaire < len(indices):
                        print(f"Indice supplémentaire : {indices[indice_supplementaire]}")
         if reponse_correcte:
              print("Bravo ! Vous avez trouvé le mot-code !")
         else:
              print(f"Dommage ! Le mot-code était : {mot_code}")
