#Cour de python GRAVEN youtube

# VARIABLE --------------------------------------------------------------------------------------------------------

"""
def main():
   #recolter une premiere note
   note1 = int(input("Entrer la premiere note"))
    #recolter une seconde note
   note2 = int(input("Entrer la deuxieme note"))
   #recolter la troisieme note
   note3 = int(input("Entrer la derniere note"))
   #calculer la moyenne
   result = (note1 + note2 + note3) / 3
   # afficher le resultat
   print("La moyenne de l'élève est de " + str(result))

if __name__ == '__main__':
    main()

     
# recolter une valeur porte monnaie
wallet = int(input("Entrer le nombre d'€ que vous possedez"))
print("Vous avez actuellement", wallet, "euros")
 
# creer un produit qui aura pour valeur 50
produit = 50
print("Le Produit vaut ", produit, "euros")
 
# enleve au "wallet" le prix du produit
wallet = wallet - produit
# ou wallet -= produit
 
# afficher la nouvelle valeur
print("Produit acheté !")
print("Il ne vous reste plus que", wallet, "euros")


# LES CONDITIONS --------------------------------------------------------------------------------------------------------

# exemple : Systeme de verification de mot de passe
password = input("Entrée votre mot de passe ")
password_length = len(password)

#Verifier si le mot de passe est inferieur à 8 caracteres
if password_length <= 8:
    print("Mot de passe trop court ! ")
elif password_length > 8 and password_length < 12:
    print("Mot de passe moyen !")
else:
    print("Mot de passe parfait ! ")

print(password_length)


#Place de cinema 

age = int(input("Entrée votre age "))

if age < 18:
    prix_total = 7
else:
    prix_total = 12
    
popcorn = input("Voulez-vous du popcorn ? (Oui, Non)")

if popcorn == "oui":
    prix_total += 5


print(" Vous devez", prix_total, "€")


# LES LISTE --------------------------------------------------------------------------------------------------------

from random import shuffle
 
# Générateur de phrases
# demander en console une chaine de la forme "mot1/mot2/mot3/mot4"
chained_words = input("Entrer une chaine de la forme mot1/mot2/mot3/mot4")
 
# transformer cette chaine en liste
words = chained_words.split("/")
 
# la melanger
shuffle(words)
 
# recuperer le nombre d'elements
words_len = len(words)
 
# si le nombre d'élements de cette liste est inferieur à 10
if words_len < 10:
  # afficher les deux premiers mots
  print(words[0], words[1])
  
# si le nombre d'éements est superieur ou égal à 10
else:
  # afficher les 3 derniers
  print(words[words_len - 1], words[words_len - 2], words[words_len - 3])


# LES BOUCLES --------------------------------------------------------------------------------------------------------

from random import randint
 
# choisir un nombre aleatoire entre 1 et 1000
just_price = randint(1, 1000)  
 
# statut du jeu (activé/désactivé)
running = True
 
# tant que le jeu est en cours d'éxécution
while running:
         
    # demander à l'utilisateur d'entrer un prix dans la console
    user_price = int(input("Entrer un prix"))
 
    # si le prix est le meme que le juste prix
    if user_price == just_price:
     print("Trouvé !")
     # fin du jeu
     running = False
 
    # si le prix de l'utilisateur est supérieur au prix à trouver
    elif user_price > just_price:
     print("C'est moins")
       
    # si le prix de l'utilisateur est inférieur au prix à trouver
    elif user_price < just_price:
     print("C'est plus")
 
# fin du jeu après la boucle
print("Fin du jeu !")


# LES FONCTIONS --------------------------------------------------------------------------------------------------------

def max():
    valeur1 = input("Entrée la premiere valeur : ")
    valeur2 = input("Entrée la deuxieme valeur : ")
    if valeur1 != valeur2:
        if valeur1 > valeur2:
            print("La valeur la plus haute est ", valeur1)
        else:
            print("La valeur la plus haute est : ", valeur2)
    else:
        print("La valeur est la même")

max()


def get_vowels_numbers(word):
    nb_vowels = 0

    for letter in word:
        if letter in ['a','e','i','o','u','y']:
            nb_vowels +=1
    return nb_vowels

word = input("Entrée un mot : ")
vowels_count = get_vowels_numbers(word)
print("Il y a", vowels_count, "voyelles dans le mot ", word)

"""

class Player:

    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        print("Bienvenue au joueur", pseudo, " / Points de vie : ", health," / Attaque : ", attack)

    def get_pseudo(self):
        return self.pseudo
    
    def get_health(self):
        return self.health
    
    def get_attack(self):
        return self.attack
    
    def damage(self, damage):
        self.health -= damage

    def attack_player(self, target_player):
        target_player.damage(self.attack)
        

player1 = Player("Graven", 20, 3)
player2 = Player("BoB", 20, 5)

player1.attack_player(player2)
print(player1.get_pseudo(), "Attaque", player2.get_pseudo())
print("Bienvenue au joueur", player1.get_pseudo(), " / Points de vie : ", player1.get_health()," / Attaque : ", player1.get_attack())
print("Bienvenue au joueur", player2.get_pseudo(), " / Points de vie : ", player2.get_health()," / Attaque : ", player2.get_attack())