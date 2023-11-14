nom = "BIDOLET"
prenom = "Michel"

# condition
if prenom == "Julien":
    print("Bonjour Julien.")
elif prenom == "Michel":
    print("Bonjour Michel.")
else:
    print("Bonjour inconnu.")

# while
i = 0
while i < 6:
    if i == 0:
        print(i)
    i += 1
    # i = i + 1 équivalent
    # i -= 1 inverse du +=
print("On n'est plus dans la boucle while.")

