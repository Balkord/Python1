"""
Voici comment votre programme doit se comporter :
1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"
2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l’unité demandée)
3 - Afficher la valeur convertie (et l'unité : cm ou pouces)
- fin du programme
"""

print("Ce programme vous permet d'effectuer des conversions d'unité")
print("1 - Pouces vers cm")
print("2 - cm vers pouces")

choice = input("Votre choix (1 ou 2) : ")
if choice == "1":
    valeur_str = input("Conversion pouces ver cm. Donnez la valeur en pouces : ")
    valeur_float = float(valeur_str)
    valeur_convertie = valeur_float * 2.54
    print("Valeur convertie en cm " + str(valeur_convertie) + " cm")
else:
    choice == "2:"
    valeur_str = input("Conversion cm ver pouces. Donnez la valeur en cm : ")
    valeur_float = float(valeur_str)
    valeur_convertie = valeur_float / 2.54
    print("Valeur convertie en cm " + str(valeur_convertie) + " pouces")




    