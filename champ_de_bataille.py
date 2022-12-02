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
                degats += carte.tier

            self.__ia.pv -= degats

        elif len(team_ia) > 0: #victoire IA
            for carte in team_ia:
                degats += carte.tier

            self.__joueur.pv -= degats
        else:
            pass #draw

    def LancerAttaque(self, j_atk, j_deff, team_atk, team_def, deuxieme_att, tour_du_joueur):
        place = -1
        for i in range(0,len(team_def)):
            if team_def[i].effet['provocation'] == True: # la carte a provocation
                place = i #elle devient la cible prioritaire

        if place == -1: #si aucune carte n'a provocation
                place = random.randint(0,len(team_def) -1) #une carte est choisie aléatoirement

        team_atk[j_atk.num_attaquant].Attaquer(team_def[place]) #la carte attaque
        
        if team_def[place].pv_combat <= 0:
            del team_def[place] #enlever la carte ennemi si elle est morte

            if place < j_deff.num_attaquant: #réajustement de l'attaquant enemi
                j_deff.num_attaquant -= 1 
            elif place == j_deff.num_attaquant:
                if place >= len(team_def):
                    j_deff.num_attaquant = 0

        if team_atk[j_atk.num_attaquant].pv_combat <= 0:
            del team_atk[j_atk.num_attaquant] #enlever si elle est morte
            if team_atk:
                j_atk.num_attaquant %= len(team_atk)
            
            deuxieme_att = 0
        
        else:# gestion du windfurry ici-----------------------------------------------------------------------------
            if (team_atk[j_atk.num_attaquant].effet['furie des vents'] == True) and (deuxieme_att == 0): #si la carte a furie des vents et attaqué une seule fois
                tour_du_joueur = (tour_du_joueur + 1) % 2 #empecher le changement de joueur
                deuxieme_att = 1 #et empecher une troisième attaque
            else:    
                j_atk.num_attaquant = (j_atk.num_attaquant + 1) % len(team_atk) #selection du prochain attaquant allié

        return (deuxieme_att, tour_du_joueur)

    def LancerCombat(self):
        team_j = copy.deepcopy(self.__joueur.combatants)
        team_ia = copy.deepcopy(self.__ia.combatants)

        tour_du_joueur = random.randint(0,1)

        deuxieme_att = 0 #pour gerer la furie des vents

        print("---===  [EQUIPES]  ===---")
        self.AffCombat(team_j, team_ia)

        while (team_j and team_ia):

            print("---===  [COMBAT]  ===---")
            self.AffCombat(team_j, team_ia)

            if tour_du_joueur:
                deuxieme_att, tour_du_joueur = self.LancerAttaque(self.__joueur, self.__ia, team_j, team_ia, deuxieme_att, tour_du_joueur)

            else: #tour de l'ia
                deuxieme_att, tour_du_joueur = self.LancerAttaque(self.__ia, self.__joueur, team_ia, team_j, deuxieme_att, tour_du_joueur)

            tour_du_joueur = (tour_du_joueur + 1) % 2 #Changement de joueur
            
            print("---===  [RESULTAT]  ===---")
            self.AffCombat(team_j, team_ia)

        self.DegatsPerdant(team_j, team_ia)