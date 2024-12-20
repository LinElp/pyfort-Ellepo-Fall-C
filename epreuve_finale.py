import json
import random


def salle_De_Tresor(fichier):
    with open("indicesSales.json", 'r', encoding='utf-8') as f:
         jeu_tv= json.load(f)
         emission_cle=random.choice(list(jeu_tv.keys()))
         emission=jeu_tv[emission_cle]
         indices=emission['Indices']
         mot_code=emission['MOT_CODE']

