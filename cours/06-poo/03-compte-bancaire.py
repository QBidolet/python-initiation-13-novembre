# Classe compte bancaire:
# nom et solde en attribut
# ajouter et retirer en méthode

class CompteBancaire:
    def __init__(self, nom="DUPONT", solde=1000):
        self.nom = nom
        self.solde = solde

    def deposer(self, somme):
        if somme > 0:
            self.solde += somme

    def retirer(self, somme):
        if somme > 0:
            self.solde -= somme

compte_bancaire = CompteBancaire()
compte_bancaire.deposer(-1000)
print(compte_bancaire.solde)