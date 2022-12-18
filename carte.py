import random
from copy import deepcopy

PRIX_CARTE = 3
"""prix d'une carte dans la boutique"""

class Carte():
    def __init__(self, id, nom, pv, atk, effet, race, tier):
        """constructeur de la classe Carte"""

        self.__id = id                    #id de la carte
        self.__nom = nom                  #nom de la carte
        self.__pv = pv                    #PV de base de la carte
        self.__pv_combat = self.__pv      #PV effectifs de la carte
        self.__atk = atk                  #Attaque de la carte
        self.__atk_combat = self.__atk    #Attaque effective de la carte
        self.__effet = effet              #Effet de la carte
        self.__race = race                #Race de la carte
        self.__tier = tier                #Tier de la carte

    #Geteurs et Seteurs-----------------------------------------------------------------------

    def GetTier(self):
        """getter de __tier"""

        return self.__tier

    tier = property(GetTier)
    
    def GetEffet(self):
        """getter de __effet"""

        return self.__effet
    
    def SetEffet(self,name,valeur):
        """setter de __effet"""

        self.__effet[name] = valeur

    effet = property(GetEffet, SetEffet)
    
    def GetPvCombat(self):
        """getter de __pv_combat"""

        return self.__pv_combat

    def SetPvCombat(self, valeur):
        """setter de __pv_combat"""

        self.__pv_combat = valeur

    pv_combat = property(GetPvCombat, SetPvCombat)
    
    def GetAtkCombat(self):
        """getter de __atk_combat"""

        return self.__atk_combat
    
    def SetAtkCombat(self, valeur):
        """setter de __atk_combat"""

        self.__atk_combat = valeur

    atk_combat = property(GetAtkCombat, SetAtkCombat)
    
    def GetRace(self):
        """getter de __race"""

        return self.__race
    
    def SetRace(self, valeur):
        """setter de __race"""

        self.__race = valeur

    race = property(GetRace, SetRace)

    def GetId(self):
        """getter de __id"""

        return self.__id
    
    def SetId(self, valeur):
        """setter de __id"""

        self.__id = valeur
    
    id = property(GetId, SetId)

    def GetNom(self):
        """getter de __nom"""

        return self.__nom
    
    def SetNom(self, valeur):
        """setter de __nom"""

        self.__nom = valeur
    
    nom = property(GetNom, SetNom)

    #Méthodes------------------------------------------------------------------------------------------

    def GestionAttaque(self, attaquant, cible):
        """Gestion des effets et PV lors d'une attaque"""

        if attaquant.__effet['bouclier divin'] == True: #si l'attaquant a bouclier divin
            attaquant.SetEffet(1,False) #l'enlever

        else:
            if cible.__effet['toxicite'] == True: #si la cible a toxicité
                attaquant.__pv_combat = 0 #mourir
            else:
                attaquant.pv_combat -= cible.atk_combat #prendre des dégats

            if attaquant.__pv_combat <= 0: # si la carte meurt
                if attaquant.__effet['represailles'] and cible.effet['toxicite']: #si la carte a représailles et est tuée par toxicité
                    cible.pv_combat = 0 #tuer la cible

    def Attaquer(self, adversaire):
        """Fait attaquer la carte en gérant les PV et effets"""

        #gestion de l'attaquant
        self.GestionAttaque(self, adversaire)

        #gestion de l'adversaire
        self.GestionAttaque(adversaire, self)
            
    
    def CriDeGuerre(self,joueur):
        combatants = joueur.combatants
        if self.__effet['cri de guerre'] == True: #si la carte a un cri de guerre
            if self.__id == 1: #Mage noir
                for mob in combatants:
                    if mob.race == 3: #tous les autres humains de l'équipe de combat
                        mob.atk_combat = mob.atk_combat + 1 #gagnent 1 point d'attaque

            elif self.__id == 2: #Gobelin
                joueur.argent = joueur.argent +1 #le joueur gagne une pièce
            
            elif self.__id == 3: #Loup
                for mob in combatants:
                    if mob.race == 2: #tous les autres bêtes de l'équipe de combat
                        mob.atk_combat = mob.atk_combat + 1 #gagnent 1 point d'attaque

            elif self.__id == 7: #Haut prêtre
                for mob in combatants:
                    if mob.race == 3: #tous les autres humains de l'équipe de combat
                        mob.pv_combat = mob.pv_combat + 2 #gagnent 2 Pv

            elif self.__id == 9: #Tortue Géante
                for mob in combatants: #tous les autres combatants
                    mob.pv_combat = mob.pv_combat + 2 #gagnent 2 Pv
            
            elif self.__id == 11: #Heros
                if len(combatants) > 0:
                    n = random.randint(0,len(combatants)-1)
                    combatants[n].__effet['bouclier divin'] = True #donne bouclier divin à un random
            
            elif self.__id == 12: #Roi Démon
                if len(combatants) > 0:
                    n = random.randint(0,len(combatants)-1)
                    combatants[n].__effet['toxicite'] = True #donne toxicité à un random
            
            elif self.__id == 14: #Sanglier
                if len(combatants) < 3:
                    combatants.append(deepcopy(self)) #invoque un autre sanglier
            
            elif self.__id == 17: #Paysan
                for mob in combatants:
                    if mob.id == 17: #tous les paysans de l'équipe de combat
                        mob.atk_combat = mob.atk_combat + 1 #gagnent 1 point d'attaque
                        mob.pv_combat = mob.pv_combat + 1 # et un point de Pv
            
            elif self.__id == 18: #Métamorphe
                if len(combatants) > 0: #si il y a d'autres serviteurs
                    n = len(combatants) - 1
                    liste_effets = combatants[n].GetEffet()
                    self.atk_combat  = combatants[n].atk_combat
                    self.SetEffet('provocation', liste_effets['provocation'])
                    self.SetEffet('bouclier divin', liste_effets['bouclier divin'])
                    self.SetEffet('toxicite', liste_effets['toxicite'])
                    self.SetEffet('furie des vents', liste_effets['furie des vents'])
                    self.SetEffet('represailles', liste_effets['represailles'])
                    self.race = combatants[n].race
                    self.id = combatants[n].id
                    self.nom = combatants[n].nom
                    if '(métamorphe)' not in self.nom:#empècher les (métamorhe)(métamorphe)
                        self.nom += '(métamorphe)'
                    self.pv_combat = combatants[n].pv_combat #devient la copie conforme du serviteur à sa gauche 
    
    #Méthodes liées à l'affichage-------------------------------------------------------------------

    def Afficher(self):
        rouge = '\033[91m' #codes couleurs
        vert = '\033[92m'
        jaune = '\033[93m'
        gris = '\033[0m'
        bleu = '\033[34m'
        violet = '\033[35m'
        provoc = gris
        shield = gris
        toxi = gris
        fury = gris
        cdg = ''
        repre = ''
        if self.__effet['provocation']: #application des codes couleurs en fonction  des effets des cartes 
            provoc = rouge
        if self.__effet['bouclier divin']:
            shield = jaune
        if self.__effet['toxicite']:
            toxi = vert
        if self.__effet['furie des vents']:
            fury = bleu
        if self.__effet['cri de guerre']:
            cdg = '✜'
        if self.__effet['represailles']:
            repre = '☠'

        print(f"{shield}({violet}{repre} {gris}{provoc}{self.__nom}{gris}{cdg} {self.__pv_combat}PV {toxi}{self.__atk_combat}{gris}{fury}ATK{gris}{shield}){gris} | ", end='')