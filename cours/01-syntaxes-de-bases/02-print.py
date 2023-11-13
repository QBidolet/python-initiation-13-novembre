# Afficher "Hello World!"
print("Hello World!")

# Passer plusieurs arguments
print("Hello", "World!")

# Argument sep
print("Hello", "World!", sep="")

# Argument end
print("Hello World!", sep=" - ", end="\n\n")
print("Hello World!", sep=" - ", end="\n\n")

prenom = "Quentin"
nom = "BIDOLET"

# Façon 1
print("Je m'appelle " + prenom + " " + nom + ".")

# Facon 2 : pythonic : f-string
print(f"Je m'appelle {prenom} {nom}.", "Test", sep="", end="")