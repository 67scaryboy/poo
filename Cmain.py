import Ccarte

class Main:
    def __init__(self,p_cartesdispo): # cartesdispo est une liste d'objets "Cartes",
        self.__nbcartes= len(p_cartesdispo)
        self.__cartesdispo = p_cartesdispo #Liste des cartes en main