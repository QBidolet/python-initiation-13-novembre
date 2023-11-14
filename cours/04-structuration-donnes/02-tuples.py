# Un tuple est une liste immuable.
mon_tuple = (1, 2)
print(type(mon_tuple))
mon_tuple = (1,)
print(type(mon_tuple))

# unpacking
a, b = (1, 2)
print(a, b)

# Retour d'une fonction
def ma_func():
    return 5, 2

a, b = ma_func()
print(a, b)
