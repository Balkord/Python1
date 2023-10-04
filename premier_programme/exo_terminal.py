"""
EXERCICE PYTHON
[Réivision jusqu'aux boucles]

> Dévlopper un mini-terminal tournant en boucle et gérant quelques commandes définies :
    - Votre programme invitera l'utilisateur à saisir une commande (comme la ligne commande windows, GNU/Linux, MacOS...)
    - Gérer le cas où un commande existe pas
    - Aucun module ne doit être importé

> Quatre commande à prevoir :
    - run (affiche 5 fois un point avec une pause entre chaque affichage de 1s)
    - name (modifie le nom du terminal, s'appellera "Défaut" de base)
    - help (affiche la liste des commandes + description brève)
    - quit (termine l'exécution du programme)

> Ce qui devra être affiché :
        [nom_terminal]> 
"""

import time
# Mettre en pause 1s -> time.sleep(1)

terminal_launched = True
terminal_name = "Défaut"
user_comand = ""
cpt = 0

while terminal_launched:
    user_comand = input(f"[{terminal_name}]> ")

    if user_comand == "run" :
        while cpt < 5:
            print(".")
            cpt += 1
            time.sleep(1)
        cpt = 0
    elif user_comand == "name" :
        terminal_name = input("Choisir nouveau nom de terminal : ")
    elif user_comand == "help":
        print("\
-------------------------------\n\
LISTE DES COMMANDES DISPONIBLES\n\
-------------------------------\n\
run   : Exécute la boucle 5 fois\n\
name  : Modifie le nom du terminal\n\
help  : Affiche la liste des commandes\n\
quit  : Quitte le terminal\n\
-------------------------------------------")
    elif user_comand == "quit" :
        terminal_launched = False
    else:
        print("Commande introuvable...")



