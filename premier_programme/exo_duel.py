#coding:utf-8
"""
EXERCICE PYTHON #3
> Créer un programme simulant un combat qui respecte les contraintes suivantes :
    - Deux joueurs, auquels on demandera de choisir un pseudo
    - Les deux combattants démarrent avec 250 points de vie chacun
    - Le combat se déroule en 4 attaques (Joueur1, Joueur2, Joueur1 et enfin Joueur2)
    - Chaque attaque est une tentative (si elle réussit, le joueur infligera un nombre de dégâts entre 0 et 100 -
                                        si elle échoue, l'attaque est ratée, et c'est au tour de l'autre joueur)
    - À la fin du combat (les 4 attaques), on déclare le gagnant (celui à qui il reste le plus de points de vie)

> Indications :
    - Le déroulement du combat doit être logique et annoncé à l'utilisateur (affichez du texte, décrivez ce qu'il se passe)
    - Coder dans un premier temps uniquement avec des affichages/saisies, variables, opérations, conditions
    - Pour les plus avancés, vous pourrez optimiser ce code ensuite en l'adaptant avec vos connaissances (boucles, fonctions, classes, etc.)
"""

import random

titan1_name = " "
titan1_hp = 250

titan2_name = " "
titan2_hp = 250


random_attack = True # True = face / False = pile
random_damage = 0

titan1_name = input(" Joueur 1, choisissez un pseudo : ")
print(f"{titan1_name} est le joueur 1.")
 
titan2_name = input(" Joueur 2, choisissez un pseudo : ")
print(f"{titan2_name} est le joueur 2.")


print("\nLE COMBAT COMMENCE ! \n")

#-----------------------------------------------------------------------------------------------------------------------
# 1ère attaque
input()
print(f"{titan1_name}, à vous de commencer !")
print(f"{titan1_name} : {titan1_hp} PV / {titan2_name} : {titan2_hp} PV")
random_attack = random.randint(0, 1)
random_attack = bool(random_attack)

if random_attack:
    # Si l'attaque réussit
    random_damage = random.randint(0, 100)
    
    print(f"{titan2_name} subit une attaque de {titan1_name} qui lui inflige {random_damage} points de dégât.")
    titan2_hp -= random_damage    
else:
    # Si l'attaque échoue
    print(f"{titan1_name} rate son attque...")

#-----------------------------------------------------------------------------------------------------------------------
# 2ème attaque
input()
print(f"{titan2_name}, à vous de commencer !")
print(f"{titan1_name} : {titan1_hp} PV / {titan2_name} : {titan2_hp} PV")
random_attack = random.randint(0, 1)
random_attack = bool(random_attack)

if random_attack:
    # Si l'attaque réussit
    random_damage = random.randint(0, 100)
    print(f"{titan1_name} subit une attaque de {titan2_name} qui lui inflige {random_damage} points de dégât.")
    titan1_hp -= random_damage
else:
    # Si l'attaque échoue
    print(f"{titan2_name} rate son attque...")


#-----------------------------------------------------------------------------------------------------------------------
# 3ème attaque

input()
print(f"{titan1_name}, à vous de commencer !")
print(f"{titan1_name} : {titan1_hp} PV / {titan2_name} : {titan2_hp} PV")
random_attack = random.randint(0, 1)
random_attack = bool(random_attack)

if random_attack:
    # Si l'attaque réussit
    random_damage = random.randint(0, 100)
    
    print(f"{titan2_name} subit une attaque de {titan1_name} qui lui inflige {random_damage} points de dégât.")
    titan2_hp -= random_damage    
else:
    # Si l'attaque échoue
    print(f"{titan1_name} rate son attque...")


#-----------------------------------------------------------------------------------------------------------------------
# 4ème attaque
input()

print(f"{titan2_name}, à vous de commencer !")
print(f"{titan1_name} : {titan1_hp} PV / {titan2_name} : {titan2_hp} PV")
random_attack = random.randint(0, 1)
random_attack = bool(random_attack)

if random_attack:
    # Si l'attaque réussit
    random_damage = random.randint(0, 100)
    print(f"{titan1_name} subit une attaque de {titan2_name} qui lui inflige {random_damage} points de dégât.")
    titan1_hp -= random_damage
else:
    # Si l'attaque échoue
    print(f"{titan2_name} rate son attque...")


#-----------------------------------------------------------------------------------------------------------------------
# Résultat final
input()
print("\nFIN DU COMBAT !\n")
print(f"{titan1_name} : {titan1_hp} PV / {titan2_name} : {titan2_hp} PV")

if titan1_hp > titan2_hp:
    print(f"{titan1_name} remporte la victoire !!")
elif titan1_hp < titan2_hp:
    print(f"{titan2_name} remporte la victoire !!")
else:
    print("Match nul...")
