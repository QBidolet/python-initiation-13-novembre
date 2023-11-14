z = 3 + 4j

print(type(z))
print(z.real)
print(z.imag)

# Le module math ne fonctionne pas avec les nombres complexes.
# Utiliser cmath

import cmath
# Calculer l'angle d'un nombre complexe
print(cmath.phase(z))