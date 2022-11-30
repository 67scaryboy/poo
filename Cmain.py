import Ccarte

class Main:
    def __init__(self,p_cartesdispo,p_argentmax,p_argent): # cartesdispo est une liste d'objets "Cartes",
        self.__nbcartes= len(p_cartesdispo)
        self.__argentmax = p_argentmax #Or max possible d'avoir dans la main
        self.__argent = p_argent #Or possédé
        self.__cartesdispo = p_cartesdispo #Liste d'objet "cartes"