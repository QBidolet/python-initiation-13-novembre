"""
Exercice 2 : Calculatrice
Écrire un programme qui demande deux nombres
à l'utilisateur puis effectue et affiche l'addition,
la soustraction, la multiplication, et la division de ces nombres.
Exemple :
Entrez le premier nombre. 1
Entrez le deuxième nombre. 1
1 + 1 = 2
1 - 1 = 0
1 * 1 = 1
1 / 1 = 1
"""

nombre_1 = float(input("Entrez le premier nombre\n"))
nombre_2 = float(input("Entrez le deuxième nombre\n"))

print(f"{nombre_1} + {nombre_2} = {nombre_1 + nombre_2}")
print(f"{nombre_1} - {nombre_2} = {nombre_1 - nombre_2}")
print(f"{nombre_1} * {nombre_2} = {nombre_1 * nombre_2}")
print(f"{nombre_1} / {nombre_2} = {nombre_1 / nombre_2}")