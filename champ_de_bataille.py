import joueur, carte, copy
import random, math
from catalogue import *

class Champ_de_bataille():
    def __init__(self, joueur, ia):
        self.__joueur = joueur
        self.__ia = ia
    
    #Méthodes-----------------------------------------------------------------------------------------

    def MajBoutique(self):
        if self.__joueur.boutique.prix_upgrade > 1:
            self.__joueur.boutique.prix_upgrade -= 1
        if self.__ia.boutique.prix_upgrade > 1:
            self.__ia.boutique.prix_upgrade -= 1

    def MajArgent(self):
        if self.__joueur.argent_max < 10:
            self.__joueur.argent_max = self.__joueur.argent_max + 1
        if self.__ia.argent_max < 10:
            self.__ia.argent_max = self.__ia.argent_max + 1

        self.__joueur.argent = self.__joueur.argent_max
        self.__ia.argent = self.__ia.argent_max

    def AffCombat(self, team_j, team_ia):   
        print("Mobs coté joueur:")
        for mobs in team_j:
            mobs.Afficher()
        print("\n")
        print("Mobs coté IA:")
        for mobs in team_ia:
            mobs.Afficher()
        print("\n")

    def DegatsPerdant(self, team_j, team_ia):
        degats = 0
        
        if len(team_j) > 0: #victoire joueur
            for carte in team_j:
                degats += carte.atk_combat

            self.__ia.pv -= degats

        elif len(team_ia) > 0: #victoire IA
            for carte in team_ia:
                degats += carte.atk_combat

            self.__joueur.pv -= degats
        else:
            pass #draw

    def LancerCombat(self):
        team_j = copy.deepcopy(self.__joueur.combatants)
        team_ia = copy.deepcopy(self.__ia.combatants)

        tour_du_joueur = random.randint(0,1)

        attaquant_j = 0
        attaquant_ia = 0

        nb_atq = 0 #pour gerer la furie des vents

        while (team_j and team_ia):
            place = -1

            print("---===  [COMBAT]  ===---")
            self.AffCombat(team_j, team_ia)

            if tour_du_joueur:

                for i in range(0,len(team_ia)):
                    if team_ia[i].effet['provocation'] == True: # la carte a provocation
                        place = i #elle devient la cible prioritaire

                if place == -1: #si aucune carte n'a provocation
                    place = random.randint(0,len(team_ia) -1) #une carte est choisie aléatoirement
                
                team_j[attaquant_j].Attaquer(team_ia[place]) #la carte attaque     
                
                if team_j[attaquant_j].pv_combat <= 0:
                    del team_j[attaquant_j] #enlever si elle est morte
                    nb_atq = 0
               
                else:# gestion du windfurry ici-----------------------------------------------------------------------------
                    if (team_j[attaquant_j].effet['furie des vents'] == True) and (nb_atq == 0): #si la carte a furie des vents et attaqué une seule fois
                        tour_du_joueur = tour_du_joueur + 1 % 2 #empecher le changement de joueur
                        nb_atq = 1 #et empecher une troisième attaque
                    else:    
                        attaquant_j = attaquant_j + 1 % len(team_j) #selection du prochain attaquant allié
                
                if team_ia[place].pv_combat <= 0:
                    del team_ia[place] #enlever la carte ennemi si elle est morte

                    if place < attaquant_ia: #réajustement de l'attaquant enemi
                        attaquant_ia -= 1 
                    elif place == attaquant_ia:
                        if place >= len(team_ia):
                            attaquant_ia = 0
            
            else: #tour de l'ia
                for j in range(0,len(team_j)):
                    if team_j[j].effet['provocation'] == True: #si la carte a provocation
                        place = j #elle devient la cible prioritaire
                if place == -1: #si aucune carte n'a provocation
                    place = random.randint(0,len(team_j) -1) #une carte est choisie aléatoirement
                
                team_ia[attaquant_ia].Attaquer(team_j[place]) #la carte attaque     
                
                if team_ia[attaquant_ia].pv_combat <= 0:
                    del team_ia[attaquant_ia] #enlever si elle est morte
                    nb_atq = 0
                    
                else:# gestion du windfurry ici-----------------------------------------------------------------------------
                    if (team_ia[attaquant_ia].effet['furie des vents'] == True) and (nb_atq == 0): #si l'ennemi a furie des vent et attaqué une seule fois
                        tour_du_joueur = tour_du_joueur + 1 % 2 #empecher le changement de joueur
                        nb_atq = 1 #et empecher une troisième attaque
                    else:    
                        attaquant_ia = attaquant_ia + 1 % len(team_ia) #selection du prochain attaquant ennemi
                        nb_atk = 0
                
                if team_j[place].pv_combat <= 0:
                    del team_j[place] #enlever la carte alliée si elle est morte
                    
                    if place < attaquant_j: #réajustement de l'attaquant allié
                        attaquant_j -= 1 
                    elif place == attaquant_j:
                        if place >= len(team_j):
                            attaquant_ia = 0

            tour_du_joueur = tour_du_joueur + 1 % 2 #Changement de joueur
            
            print("---===  [RESULTAT]  ===---")
            self.AffCombat(team_j, team_ia)

        self.DegatsPerdant(team_j, team_ia)