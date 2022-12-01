import joueur

import random

class Champ_de_bataille():
    def __init__(self, joueur, ia):
        self.__joueur = joueur
        self.__ia = ia
    
    def LancerCombat(self):
        team_j = self.__joueur.GetCombatants()
        team_ia = self.__ia.GetCombatants()
        place_provoc_j = []
        place_provoc_ia
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