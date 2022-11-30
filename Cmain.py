import Ccarte

class Main:
    def __init__(self,p_cartesdispo): # cartesdispo est une liste d'objets "Cartes",
        self.__nbcartes = len(p_cartesdispo)
        self.__nbcartesmax = 6
        self.__cartesdispo = p_cartesdispo #Liste des cartes en main
    
    def ajoutcarte(self, p_carte):
        if self.__nbcartes < self.__nbcartesmax:
            self.__cartesdispo.append(p_carte)
    
    def get_nbcartes(self):
        return self.__nbcartes
    
    def get_nbcartesmax(self):
        return self.__nbcartesmax