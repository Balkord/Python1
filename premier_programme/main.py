
def demander_nom():
    nom_str = ""
    while nom_str == "":
        nom_str = input(" entrée votre nom svp :")
    return nom_str


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " entrée votre age svp :")
        try: 
            age_int = int(age_str)
        except:
            print("ERREUR: vous devez entrer un nombre pour l'age")
    return  age_int

def afficher_information_personne(nom, age, taille):
    print()
    print("Bonjour je m'aplle " + nom + " et j'ai " + str(age) + " ans")
    print("l'année prochaine vous aurez " + str(age + 1) + " ans")

    if age == 17:
        print("Vous êtes presque majeur")
    elif 12 <= age < 18:
        print("Vous êtes adolescent")
    elif age == 1 or age == 2:
        print("Vous êtes un bébé")
    elif age == 18:
        print("Tout juste majeur : félécitation")
    elif age > 60:
        print("Vous êtes sénior")
    elif age < 10:
        print("Vous êtes un enfant")
    elif age > 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")

    #afficher la taille
    if not taille ==0:
        print("Votre taille : " + str(taille) + "m")

# demander nom                                                             
# nom1 = demander_nom()
# nom2 = demander_nom()


#demander l'age
#age1 = demander_age(nom1)
# age2 = demander_age(nom2)
#affichage 

# afficher_information_personne(nom1, age1)
# afficher_information_personne(nom2, age2)

NB_PERSONNES = 1

#la boucle for
for i in range(0, NB_PERSONNES):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    afficher_information_personne(nom, age) 