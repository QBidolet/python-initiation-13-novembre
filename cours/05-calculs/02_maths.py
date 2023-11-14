import math

x = 16
racine_carree = math.sqrt(x)
print(racine_carree)

# Arrondi
x = 0.999
# arrondi = math.floor(x)
# arrondi = math.ceil(x)
arrondi = round(x)
print(arrondi)

# angle
angle = math.pi / 4
sin_value = math.sin(angle)
cosinus_value = math.cos(angle)
tan_value = math.tan(angle)

print(angle, sin_value, cosinus_value, tan_value)

# numpy
# Pourquoi utiliser numpy ?
# On peut avoir des outils supplémentaires, comme obtenir moyenne/médianne etc.
# Manipulation de tableau de nombre / matrices
# Obtenir min du tableau, moyenne etc.