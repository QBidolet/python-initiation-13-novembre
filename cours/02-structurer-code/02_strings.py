une_phrase = "J'ai 20 ans."

# Echapper un caractère avec \
une_phrase = 'J\'ai 20 ans'

# Retour à la ligne, tabulation ...
print("\n")
print("\t")

# Combiner chaine de caractère et variables
# concaténation : +
# ou f-string
print(une_phrase + " et je suis heureux.")
print(f'{une_phrase} et je suis heureux.')

# Duplication
print("#" * 25)

# Extraction de chaine avec [ start : end]
alphabet = "abcdefghijklm"

# Extraire un caractère à un indice donné
print(alphabet[0])

# Extraire une sous-chaine
print(alphabet[2:5])

# Tout sélectionner
print(alphabet[:])

# Sélectionner du début jusqu'à l'indice 6 non inclus.
print(alphabet[:6])
# Commencer par l'indice 2 jusqu'à la fin
print(alphabet[2:])

# Extraire les caractères de deux en deux, c'est à dire on extrait une lettre sur deux.
print(alphabet[::2])

# Je veux extraire la chaine début jusqu'à l'avant dernière lettre
print(alphabet[:-1])

print('#')

# Parcours inversé
print(alphabet[::-1])

print('#')
# Quelques méthodes utiles
# Attention à bien sauvegarder la valeur
majuscule = alphabet.upper()
miniscule = majuscule.lower()
print(miniscule)

phrase = "Python est intéressant."
# Remplacer toutes les occurrences dans une chaine de caractère
remplace = phrase.replace("intéressant", "génial")
print(remplace)

# Recherche dans une chaine
position = phrase.find("est")

print(position)  # Retourne -1 si introuvable.

# Count : Compte le nombre d'occurrence
print(phrase.count("e"))

# Longueur d'une chaine de caractère
print(len(phrase))