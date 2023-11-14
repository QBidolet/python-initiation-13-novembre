"""
Exercice 3 : Conversion
Vous devez écrire un programme qui demande à l'utilisateur
de saisir une vitesse en miles/heure
 et vous devez afficher cette vitesse en km/h et m/s
Vous devez également réinviter votre utilisateur à saisir une valeur une fois
la conversion terminé et boucler de cette façon
Indication pour la conversion : pour passer des miles/heure au mètre par seconde il faut diviser par 2.237
Indication pour la conversion : pour passer des miles/heure au km par heure il faut multiplier par 1.609
"""
continuer = "oui"
while continuer == "oui":
    # Saisie et conversion en float
    vitesse = input("Veuillez saisir une vitesse en miles/heure.\n")
    vitesse = float(vitesse)

    # Conversion en km/h et m/s
    vitesse_km_h = vitesse * 1.609
    vitesse_ms = vitesse / 2.237

    # Affichage
    print(f"Vitesse en km/h : {vitesse_km_h} km/h.")
    print(f"Vitesse en m/s : {vitesse_ms} m/s.")

    # Continuer ?
    continuer = input("Voulez-vous continuer ? [oui/non]")
    continuer = continuer.lower()