def do_nothing():
    pass


do_nothing()

# Paramètres par défaut
def somme(nombre_1=1, nombre_2=2):
    return nombre_1 + nombre_2

resultat = somme(1, 2)
print(resultat)

# Retour multiple
def get_items():
    # [...]
    return "item 1", "item 2"

# Paramètres positionnels
somme(2, 3)

# Paramètres nommés
somme(nombre_2=3, nombre_1=2)

# Paramètres positionnels + nommés
somme(2, nombre_2=3)

print("Hello", "World!", "!!", sep="_")
print(somme(nombre_2=5))

# numpy + pandas : combo statisticien