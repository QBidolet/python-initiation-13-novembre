# Boucle for
# A préférer lorsqu'on a une boucle prévisible.
ma_liste = [1, 2, 3, 4]
for element in ma_liste:
    print(element)

print("#" * 25)

# Utiliser range pour itérer un certain nombre de fois.
for i in range(6):
    print(i)

print("#" * 25)

# range(debut, fin, pas)
for i in range(1, 6, 2):
    print(i)

# enumerate
fruits = ["pomme", "banane", "kiwi"]
for indice, fruit in enumerate(fruits):
    # print(f"{indice} - {fruit}")
    print(f"Fruit n°{indice + 1} : {fruit}")
