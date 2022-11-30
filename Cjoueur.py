import Ccarte, Cboutique, Cmain

class Joueur:
    def __init__(self, p_cartesdispo, p_argentmax, p_argent, p_pseudo):
        self.__pvmax = 20
        self.__pv = self.__pvmax
        self.__main = Cmain.Main(p_cartesdispo) #Main du joueur
        self.__argentmax = p_argentmax #Pièces max disponibles (dépassable, uniquement pour le compte des tours)
        self.__argent = p_argent #Pièces disponibles
        self.__pseudo = p_pseudo #Nom du joueur
        self.__boutique = Cboutique.Boutique() #Boutique (propre au joueur)
        self.__combatants = [] #Cartes posées

    def acheter(self, p_carte):
        cartesboutiques = Cboutique.Boutique.get_cartes(self.__boutique)
        if p_carte in cartesboutiques:
            if (self.__argent >= 3) and (Cmain.Main.get_nbcartes(self.__main) < Cmain.Main.get_nbcartesmax(self.__main)):
                self.__argent -= 3
                Cmain.Main.ajoutcarte(self.__main, p_carte)
            else:
                print("Opération impossible")