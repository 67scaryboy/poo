import Ccarte, Cboutique, Cmain

class Joueur:
    def __init__(self, p_cartesdispo, p_argentmax, p_argent, p_pseudo):
        self.__pvmax = 20
        self.__pv = self.__pvmax
        self.__main = Cmain.Main(p_cartesdispo)
        self.__argentmax = p_argentmax
        self.__argent = p_argent
        self.__pseudo = p_pseudo
        self.__boutique = Cboutique.Boutique()
        self.__combatants = []
