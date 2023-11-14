class Voiture:
    # Etape 1 : Créer le constructeur
    def __init__(self, couleur="Rouge", marque="Tesla"):
        self.couleur = couleur
        self.marque = marque

    def repeindre(self, couleur):
        self.couleur = couleur

    # méthode "magique" ou spéciale
    def __str__(self):
        return (f"Je suis une voiture de couleur {self.couleur} "
                f"et de marque {self.marque}")

voiture = Voiture()
voiture_2 = Voiture("Verte", "Mercedes")
print(voiture.couleur, voiture.marque)
print(voiture_2.couleur, voiture_2.marque)
voiture.repeindre("Blanche")
print(voiture.couleur)
print(voiture)


# intropection
print(type(voiture))
print(isinstance(voiture, Voiture))
print(dir(voiture))
print(getattr(voiture, "marque"))
print(hasattr(voiture, "couleur"))