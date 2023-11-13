# Noms des variables utilisent le snake_case
# C'est à dire, tout en minuscule séparé par un underscore entre les mots.
# Tout l'alphabet, SAUF caractères spéciaux et accent : é ! @ , etc.
# Un nom de variable ne doit pas commencer par un chiffre.

# nom de variables valides
# a
# a_1
# a1
# _abc

# nom de variables invalides
# 1a
# a@
# for etc. tous les mots réservés

ma_boite = 42
ma_boite_2 = ma_boite
print(id(42))
print(id(ma_boite))
print(id(ma_boite_2))
ma_boite = 12
print(id(12), id(ma_boite), id(ma_boite_2))