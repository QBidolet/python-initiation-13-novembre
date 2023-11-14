"""
A partir de cette liste
["Jean", "Maximilien", "Brigitte", "Sonia"]
Coder un programme permettant de séparer
les prénoms, c'est-à-dire une liste avec ceux
ayant moins de 6 caractères (6 inclus)
et ceux ayant plus de 6 caractères.
"""
prenoms = ["Jean", "Maximilien", "Brigitte", "Sonia"]
prenoms_plus_6_lettres = []
prenoms_moins_6_lettres = []

for prenom in prenoms:
    if len(prenom) <= 6:
        prenoms_moins_6_lettres.append(prenom)
    else:
        prenoms_plus_6_lettres.append(prenom)

prenoms_plus_6_lettres.sort()
prenoms_moins_6_lettres.sort()
print(f"Prénom de moins de 6 lettres : {prenoms_moins_6_lettres}")
print(f"Prénom de plus de 6 lettres : {prenoms_plus_6_lettres}")
