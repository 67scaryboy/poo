import joueur

class Champ_de_bataille():
    def __init__(self, p_joueur, p_ia):
        self.__joueur = p_joueur
        self.__ia = p_ia
    
    def LancerCombat():
        teamJ = self.__joueur.GetCombatants()