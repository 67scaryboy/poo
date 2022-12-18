import joueur, carte, copy
import random, math
from catalogue import *

class Champ_de_bataille():
    """Classe représentant le champ de bataille (board)"""

    def __init__(self, joueur, ia):
        """constructeur du de la classe Champ_de_bataille"""

        self.__joueur = joueur #le joueur humain
        self.__ia = ia #le joueur IA
    
    #Méthodes-----------------------------------------------------------------------------------------

    def MajBoutique(self):
        """met les boutiques à jour pour les débuts de tour"""

        if self.__joueur.boutique.prix_upgrade > 1:
            self.__joueur.boutique.prix_upgrade -= 1

        if self.__ia.boutique.prix_upgrade > 1:
            self.__ia.boutique.prix_upgrade -= 1

    def MajArgent(self):
        """met l'argent des joueurs à jour pour les débuts de tour"""

        if self.__joueur.argent_max < 10:
            self.__joueur.argent_max = self.__joueur.argent_max + 1

        if self.__ia.argent_max < 10:
            self.__ia.argent_max = self.__ia.argent_max + 1

        self.__joueur.argent = self.__joueur.argent_max
        self.__ia.argent = self.__ia.argent_max

    def DegatsPerdant(self, team_j, team_ia):
        """applique les dommages aux joueurs en fin de tour"""

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

    def LancerAttaque(self, j_atk, j_def, team_atk, team_def, deuxieme_att, tour_humain):
        """
        Attaque complète d'une carte
        
        Args:
            j_atk (Joueur): le joueur qui attaque
            j_def (Joueur): le joueur ciblé par l'attaque
            team_atk (list[Carte]): liste des cartes combattantes alliées
            team_def (list[Carte]): liste des cartes combattantes ennemies
            deuxieme_att (boolean): indique s'il s'agit d'une deuxième attaque de la même carte
            tour_humain (boolean): indique s'il s'agit du tour de l'humain

        Returns:
            deuxieme_att (boolean): indique s'il la carte doit réattaquer
            tour_humain (boolean): indique si le tour de l'humain vient de s'achever
        """

        place = -1 #place du combattant parmis deffenseurs

        for i in range(len(team_def)):
            if team_def[i].effet['provocation'] == True: # la carte a provocation
                place = i #elle devient la cible prioritaire

        if place == -1: #si aucune carte n'a provocation
                place = random.randint(0,len(team_def) -1) #une carte est choisie aléatoirement

        if tour_humain == False:
            print(f"{team_atk[j_atk.num_attaquant].nom} ennemi attaque {team_def[place].nom} allié")
        else:
            print(f"{team_atk[j_atk.num_attaquant].nom} allié attaque {team_def[place].nom} ennemi")

        team_atk[j_atk.num_attaquant].Attaquer(team_def[place]) #la carte attaque
        
        #enlever la carte ennemi si elle est morte
        if team_def[place].pv_combat <= 0:
            del team_def[place]

            #réajustement de la carte combattante ennemi
            if place < j_def.num_attaquant:
                j_def.num_attaquant -= 1 
            elif place == j_def.num_attaquant:
                if place >= len(team_def):
                    j_def.num_attaquant = 0

        #enlever la carte alliée si elle est morte
        if team_atk[j_atk.num_attaquant].pv_combat <= 0:
            del team_atk[j_atk.num_attaquant]

            #réajustement de la carte combattante allié
            if team_atk:
                j_atk.num_attaquant %= len(team_atk)
            
            deuxieme_att = False
        
        else:# gestion du windfurry ici
            if (team_atk[j_atk.num_attaquant].effet['furie des vents'] == True) and (deuxieme_att == False): #si la carte a furie des vents et attaqué une seule fois
                tour_humain = not tour_humain #empêche le changement de joueur
                deuxieme_att = True #empêche une troisième attaque
            else:
                j_atk.num_attaquant = (j_atk.num_attaquant + 1) % len(team_atk) #selection du prochain attaquant allié

        return (deuxieme_att, tour_humain)

    def LancerCombat(self):
        """Fais combattre les joueurs sur un champ de bataille"""

        #copie des liste de cartes combattantes pour ne pas les modifier entre deux combats
        team_j = copy.deepcopy(self.__joueur.combattants)
        team_ia = copy.deepcopy(self.__ia.combattants)

        #détermine si l'humain commence à attaquer
        tour_humain = random.choice([True, False])

        #gère la furie des vents (deuxième attaque d'une même carte)
        deuxieme_att = False

        print("---===  [EQUIPES]  ===---")
        self.AffCombat(team_j, team_ia)

        #affrontement des cartes combattantes joueurs
        while (team_j and team_ia):

            if tour_humain:
                deuxieme_att, tour_humain = self.LancerAttaque(self.__joueur, self.__ia, team_j, team_ia, deuxieme_att, tour_humain)

            else: #tour de l'ia
                deuxieme_att, tour_humain = self.LancerAttaque(self.__ia, self.__joueur, team_ia, team_j, deuxieme_att, tour_humain)

            tour_humain = not tour_humain #Changement de joueur
            
            print("---===  [RESULTAT]  ===---")
            self.AffCombat(team_j, team_ia)
        
        #application des dégats au perdant
        self.DegatsPerdant(team_j, team_ia)
    
    #Méthodes liées à l'affichage--------------------------------------------------------------------------------

    def AffCombat(self, team_j, team_ia):
        """Affiche la liste des combattants vivants des joueurs"""

        print("Mobs coté joueur:")
        VisualiserListe(team_j)
        print("\n")

        print("Mobs coté IA:")
        VisualiserListe(team_ia)
        print("\n")