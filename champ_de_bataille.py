import joueur, carte

import random, math

class Champ_de_bataille():
    def __init__(self, joueur, ia):
        self.__joueur = joueur
        self.__ia = ia
    
    def LancerCombat(self):
        team_j = self.__joueur.GetCombatants()
        team_ia = self.__ia.GetCombatants()
        relais = random.randint(0,1)
        attaquant_j = 0
        attaquant_ia = 0
        while (len(team_j) > 0) and (len(team_ia) > 0):
            place = -1
            if relais == 1: #tour du joueur
                for i in range(0,len(team_ia)):
                    if team_ia[i].GetEffet()[0] == True: #si la carte a provocation
                        place = i #elle devient la cible prioritaire
                if place == -1: #si aucune carte n'a provocation
                    place = random.randint(0,len(team_ia) -1) #une carte est choisie aléatoirement
                
                team_j[attaquant_j].Attaquer(team_ia[place]) #la carte attaque     
                
                if team_j[attaquant_j].GetPvCombat() <= 0:
                    del team_j[attaquant_j] #enlever si elle est morte
               
                else:# gestion du windfurry ici-----------------------------------------------------------------------------
                    attaquant_j = attaquant_j + 1 % len(team_j) #selection du prochain attaquant allié
                if team_ia[place].GetPvCombat() <= 0:
                    del team_ia[place] #enlever la carte ennemi si elle est morte
                    
                    if place < attaquant_ia: #réajustement de l'attaquant enemi
                        attaquant_ia -= 1 
                    elif place == attaquant_ia:
                        if place >= len(team_ia):
                            attaquant_ia = 0
            
            else: #tour de l'ia
                for j in range(0,len(team_j)):
                    if team_j[j].GetEffet()[0] == True: #si la carte a provocation
                        place = j #elle devient la cible prioritaire
                if place == -1: #si aucune carte n'a provocation
                    place = random.randint(0,len(team_ia) -1) #une carte est choisie aléatoirement
                
                team_ia[attaquant_ia].Attaquer(team_j[place]) #la carte attaque     
                
                if team_ia[attaquant_ia].GetPvCombat() <= 0:
                    del team_ia[attaquant_ia] #enlever si elle est morte
               
                else:# gestion du windfurry ici-----------------------------------------------------------------------------
                    attaquant_ia = attaquant_ia + 1 % len(team_ia) #selection du prochain attaquant enemi
                if team_j[place].GetPvCombat() <= 0:
                    del team_j[place] #enlever la carte alliée si elle est morte
                    
                    if place < attaquant_j: #réajustement de l'attaquant allié
                        attaquant_j -= 1 
                    elif place == attaquant_j:
                        if place >= len(team_j):
                            attaquant_ia = 0
            relais = relais + 1 % 2 #Changement de joueur
            #Affichage zbeule, a faire propre
            print("\n---===[COMBAT]===---")
            print("Mobs coté IA:")
            for mobs in team_ia:
                mobs.Afficher()
            print("\nMobs coté joueur:")
            for mobs in team_j:
                mobs.Afficher()
        degats = 0
        if len(team_j) > 0: #victoire joueur
            for carte in team_j:
                degats += carte.GetAtkCombat()
            self.__ia.SetPV(self.__ia.GetPV() - degats)

        elif len(team_ia) > 0: #victoire IA
            for carte in team_ia:
                degats += carte.GetAtkCombat()
            self.__joueur.SetPV(self.__joueur.GetPV() - degats)
        else:
            pass #draw     