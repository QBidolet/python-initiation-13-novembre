"""
Un programme qui demande à l'utilisateur de saisir
des noms de chats et le programme se stop une fois que
l'utilisateur décide d'arrêter la saisie.
Le programme doit nous retourner la liste des chats dans
l'ordre de saisie.
Bonus : ne pas pouvoir saisir deux fois le même nom
et afficher le numéro du chat à saisir
( exemple : saisir chat numéro 1 etc ... )
"""

chats = []
reponse = ""
mots_stop = ["exit", "stop", "quitter", "quit"]
while reponse.lower() not in mots_stop:
    reponse = input("Entrez un nom de chat.\n")
    if reponse.lower() not in mots_stop and reponse.strip() != "":
        nom_chat = reponse.strip().capitalize()
        if reponse not in chats:
            chats.append(nom_chat)
        else:
            print("Vous avez déjà saisi ce nom de chat.")

for indice, chat in enumerate(chats):
    print(f"Le chat n°{indice + 1 } s'appelle {chat}.")









