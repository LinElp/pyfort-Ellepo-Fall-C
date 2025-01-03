
# 🏰 Fort Boyard Simulator


Le projet "Fort Boyard Simulator" demande de développer un simulateur inspiré du jeu télévisé, avec des épreuves interactives en Python. 

 **Présentation Générale :**  
   - **Titre :** Fort Boyard Simulator.  
   - **Contributeurs :** Les membres de votre binôme et leurs rôles.  
   - **Description :** Simulation de Fort Boyard avec des épreuves variées et une salle du trésor.  
   - **Fonctionnalités principales :** Constitution d'équipe, épreuves (mathématiques, hasard, logique, énigmes), collecte de clés et accès à la salle du trésor.  
   - **Technologies utilisées :** Python, JSON, bibliothèque random.  

 **Installation :**  
   - Clonage du dépôt Git.  
   - Configuration des dépendances et environnement.  


 **Utilisation :**  
   - Toutes les fonctionnalités :

| Fonctionnalité                    | Description                                                   |
|------------------------------------|---------------------------------------------------------------|
| 🎯 Constitution d'équipe          | Ajouter jusqu'à 3 joueurs à l'équipe.                         |
|  Épreuves mathématiques         | Résoudre des calculs et des équations (Factorielle, Nombres Premiers,Roulette Mathématique)                  |
| ➗ Épreuve de la Factorielle       | Calculer la factorielle d'un nombre donné.                    |
| 🔢 Épreuve des Nombres Premiers   | Identifier les nombres premiers le plus proche.               |
| 🎰 Épreuve de la Roulette Mathématique | Résoudre une épreuve en lien avec la roulette mathématique.  |
|  Jeux de hasard                 | Jouer au bonneteau ou au lancer de dés.( Bonneteau, Lancer de dés)                     |
| 🎩 Bonneteau                      | Le joueur doit deviner sous quel bonneteau (A, B ou C) se cache la clé. |
| 🎲 Lancer de dés                  | Le joueur et le maître du jeu lancent chacun deux dés. Le premier à obtenir un 6 remporte la partie, avec un maximum de trois essais.  |
|  Épreuves logiques              | Résoudre un jeu de logique ( Le Morpion (Tic-Tac-Toe) )            |
| ❌ Le Morpion (Tic-Tac-Toe)       | Jouer au jeu du morpion contre le maître du jeu.|
| 🔍 Enigme du Père Fouras          | Résoudre une énigme du Père Fouras.        |
| 🏁 Épreuve finale                 | dernière étape du jeu, où les joueurs doivent deviner un mot-code pour accéder àla salle du trésor.      |


 
 **Documentation technique :**  

Détails des algorithmes et fonctions implémentées pour chaque épreuve:

 **jeu()**
   - **Description :** Fonction principale qui gère le déroulement du jeu. Elle permet de créer une équipe, choisir des épreuves et déterminer les clés obtenues en fonction des réussites.
   
 **bonneteau()**
   - **Description :** Jeu de bonneteau où un joueur doit deviner sous quel bonneteau se cache la clé. Il dispose de 2 essais pour trouver la bonne réponse.

 **jeu_lance_des()**
   - **Description :** Jeu de dés où le joueur et le maître lancent chacun deux dés. Le joueur gagne si l’un des dés montre un "6". Il dispose de 3 essais pour réussir.

 **epreuve_hasard()**
   - **Description :** Sélection aléatoire d'une épreuve de hasard parmi plusieurs options disponibles (bonneteau ou jeu de lancer de dés).

 **salle_De_Tresor()**
   - **Description :** Une fois que toutes les clés sont gagnées, cette fonction permet de résoudre l'énigme finale du Père Fouras, avec des indices et un mot-code à deviner.

 **Factorielle(n)**
   - **Description :** Calcule la factorielle de l'entier donné, c'est-à-dire le produit des entiers de 1 à n.

 **epreuve_math_factorielle()**
   - **Description :** Épreuve mathématique où le joueur doit calculer la factorielle d'un nombre choisi aléatoirement et comparer sa réponse avec la bonne réponse.

 **epreuve_roulette_mathematique()**
   - **Description :** Épreuve mathématique où 5 nombres sont générés aléatoirement et une opération (addition, soustraction ou multiplication) est effectuée sur ces nombres. Le joueur doit deviner le résultat.

 **est_premier(n)**
   - **Description :** Vérifie si un nombre est premier (c’est-à-dire divisible uniquement par 1 et lui-même).

 **premier_plus_proche(n)**
   - **Description :** Trouve le nombre premier le plus proche d’un nombre donné.

 **epreuve_math_premier()**
   - **Description :** Épreuve mathématique où le joueur doit trouver le nombre premier le plus proche d'un nombre choisi aléatoirement.

 **epreuve_math()**
   - **Description :** Sélection aléatoire d'une épreuve mathématique parmi celles disponibles (factorielle, roulette mathématique ou premier).

 **afficher_grille(grille)**
   - **Description :** Affiche la grille du jeu de Tic-Tac-Toe dans un format lisible.

 **verifier_victoire(grille, symbole)**
   - **Description :** Vérifie si un joueur (ou le maître) a gagné en alignant 3 de ses symboles (X ou O) sur la grille.

 **coup_maitre(grille, symbole)**
   - **Description :** Calcule et place un coup pour le maître du jeu (symbole "O"). Le maître tente de bloquer ou de gagner.

 **tour_joueur(grille)**
   - **Description :** Permet au joueur "X" de jouer. Il entre les coordonnées pour placer son symbole "X" sur la grille.

 **tour_maitre(grille)**
   - **Description :** Permet au maître du jeu de jouer. Il place un "O" sur la grille en fonction de l’état du jeu.

 **grille_complete(grille)**
   - **Description :** Vérifie si la grille de Tic-Tac-Toe est complètement remplie, c’est-à-dire si toutes les cases sont occupées.

 **verifier_resultat(grille)**
   - **Description :** Vérifie si le jeu de Tic-Tac-Toe a un gagnant ou si c’est un match nul.

 **initialiser_grille()**
   - **Description :** Initialise la grille de Tic-Tac-Toe avec 3 lignes et 3 colonnes, toutes vides (représentées par des espaces).

 **jeu_tictactoe()**
   - **Description :** Fonction principale du jeu Tic-Tac-Toe. Elle gère les tours des joueurs et du maître, l'affichage de la grille, et la vérification du résultat.

 **charger_enigmes(fichier)**
   - **Description :** Charge les énigmes du fichier JSON spécifié et les retourne sous forme de liste d'énigmes.

 **enigmes_pere_fouras()**
   - **Description :** Permet de poser une énigme au joueur. Celui-ci a 3 essais pour répondre correctement au mot-code. Si la réponse est correcte, il gagne la clé.

 Remarques :
- Les jeux de hasard comme **bonneteau** et **jeu_lance_des** ajoutent un aspect d'incertitude et de chance.
- Les épreuves mathématiques et de logique testent les compétences du joueur en calcul et en résolution de problèmes.
- Le jeu de **Tic-Tac-Toe** et l'**énigme du Père Fouras** ajoutent des éléments de stratégie et de réflexion pour gagner les clés.


 **Journal de Bord :**  
  


 **Tests et validation :** 
 
   - Epreuve mathématiques:
    
   ![image](https://github.com/user-attachments/assets/1272889d-7285-4ac4-af58-7d6c32864ebf) 
   ![image](https://github.com/user-attachments/assets/8a834f84-c3ba-4292-93d5-782bbaf18b77)
   ![image](https://github.com/user-attachments/assets/7fdc1165-b504-495e-a361-3de8898c7e7b) 
   ![image](https://github.com/user-attachments/assets/f87779d7-c0cc-4fa0-a4c5-4fa8da814595)
   
   - Epreuve hasard:

   ![image](https://github.com/user-attachments/assets/7d22d630-2e48-4e3b-96bd-f8639809d78c) 
   ![image](https://github.com/user-attachments/assets/bcdd95f3-aefc-4923-a5d8-e8ec03551a79)
   ![image](https://github.com/user-attachments/assets/b792aef2-d3e7-4d47-bfe0-005779848add)

   - Epreuve logique:
     
   ![image](https://github.com/user-attachments/assets/d476baad-df77-4756-80c9-371fe3070f63) ![image](https://github.com/user-attachments/assets/54b3cf88-ba8a-4e14-8486-b48c2586a2b8) 
   ![image](https://github.com/user-attachments/assets/eae6a268-a51a-46ed-8692-3ef74538ff03) ![image](https://github.com/user-attachments/assets/3ccddc1c-9e87-48bf-80a0-d053919d9eee)

   - Enigme du père Fouras :

   ![image](https://github.com/user-attachments/assets/8d6cf9c2-a7e9-401f-9450-f57b7696866e)

   - Epreuve finale :

   ![image](https://github.com/user-attachments/assets/8ac791d0-e7d0-4af9-93b8-05f84822a318)

   - Main :

   ![image](https://github.com/user-attachments/assets/402d9a90-9c1d-4a61-a2b8-e1c1cd3c823c) ![image](https://github.com/user-attachments/assets/61348fd2-11cd-496e-b553-dae9ded1e903)






   

   








