import joueur

import random

class Champ_de_bataille():
    def __init__(self, joueur, ia):
        self.__joueur = p_joueur
        self.__ia = p_ia
    
    def LancerCombat():
        team_j = self.__joueur.GetCombatants()
        team_ia = self.__ia.GetCombatants()
        first = random.randint(0,1)
        while (len(team_j) > 0) and (len(team_ia) > 0):
            if first == 1: #le joueur commence
                pass
        if len(team_j) > 0:
            pass #victoire joueur
        elif len(team_ia) > 0:
            pass #victoire ia
        else:
            pass #draw     