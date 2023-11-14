"""
Exercice 4 : Inversion de Chaîne
Écrire une fonction inverser_chaine qui
prend une chaîne de caractères en entrée et retourne la chaîne inversée.
"""


def inverser_chaine(chaine):
    chaine_inversee = chaine[::-1]
    return chaine_inversee


chaine = input("Ecrivez votre chaine à inverser.\n")
chaine_inversee = inverser_chaine(chaine)
print(chaine_inversee)
