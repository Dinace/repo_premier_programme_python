"""
Premier programme python
Formation
Apprendre la programmation en python

"""

nom = input("Quel est ton nom ? ")

age = (input("Quel est votre age ? "))


try:
    age_prochain = int(age) + 1
except ValueError:
    print("Erreur, vous devez rentrer un nombre pour l'âge")
else:
    print("Vous vous appelez " + nom)

    print("Vous vous appelez " + nom + "," + "vous avez " + str(int(age)) + " ans")

    print("L'an prochain, vous aurez " + str(age_prochain) + " ans")




"""
Cet exercice consiste à trouver le prochain nombre
A partir d'un nombre arbotrairement choisi
"""

nbre_initiale = input("Quel est le premier nombre ? ")
prochain_nbre = int(nbre_initiale) + 1

print(f"La lettre que vous aavez choisie est : {nbre_initiale} La lettre suivante sera :   {prochain_nbre}")

