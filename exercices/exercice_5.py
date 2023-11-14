"""
Exercice 5 : Recherche de Sous-Chaîne
Développer une fonction trouver_sous_chaine
qui recherche une sous-chaîne dans une chaîne donnée
et retourne l'index de début de cette sous-chaîne ou -1
si elle n'est pas trouvée.
"""
def trouver_sous_chaine(phrase, sous_chaine):
    position = phrase.find(sous_chaine)
    return position

phrase = input("Veuillez entrer la phrase.\n")
sous_chaine = input("Veuillez entrer sous chaine à rechercher.\n")
position = trouver_sous_chaine(phrase, sous_chaine)
print(position)
