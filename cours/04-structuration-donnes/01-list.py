# Définir liste avec []
une_liste = []
print(type(une_liste))

une_liste = ["pomme", "banane", "kiwi"]
print(une_liste)

une_liste = ["pomme", 52, True, ["kiwi"]]

# Sélection par un indice
print(une_liste[0])

# Ajouter
une_liste.append("Hello")
print(une_liste)
une_liste.insert(0, -99)
print(une_liste)

# Supprimer
del une_liste[0] # del est un cas particulier
print(une_liste)
une_liste.remove("Hello")
print(une_liste)

print(len(une_liste))

# Trier
nombres = [5, 8, 4, 3, 1]
# Attention .sort() trie directement, pas de retour en arrière possible
# Reverse = True pour inversé l'ordre, donc ordre décroissant.
nombres.sort(reverse=True)
print(nombres)

# test d'appartenance
if 4 in nombres:
    print("4 est dans nombres")

# gestion en mémoire
a = [1, 2]
b = a
a[0] = 8
print(b)

# import copy
# b = copy.deepcopy(a)

# Présence de valeur
chats = ['titi', 'minou', 'minet']
if "minou" in chats:
    print("Le nom est présent.")
