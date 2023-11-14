class Chien:
    def parler(self):
        return "Waf waf!"

class Chat:
    def parler(self):
        return "Miaou !"

def faire_parler(animal):
    print(animal.parler())

chat = Chat()
chien = Chien()
faire_parler(chat)
faire_parler(chien)
