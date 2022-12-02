import random
from copy import deepcopy

PRIX_CARTE = 3

class Carte():
    def __init__(self, id, nom, pv, atk, effet, race, tier):
        self.__id = id                    #id de la carte
        self.__nom = nom                  #nom de la carte
        self.__pv = pv                    #PV de base de la carte
        self.__pv_combat = self.__pv        #PV effectifs de la carte
        self.__atk = atk                  #Attaque du perso
        self.__atk_combat = self.__atk      #Attaque effective de la carte
        self.__effet = effet              #Effet particulier
        self.__race = race                #Race
        self.__tier = tier                #Tier de la boutique dans lequel il est achetable

    #Geteurs et Seteurs-----------------------------------------------------------------------

    def GetTier(self):
        return self.__tier

    tier = property(GetTier)
    
    def GetEffet(self):
        return self.__effet
    
    def SetEffet(self,name,valeur):
        self.__effet[name] = valeur

    effet = property(GetEffet, SetEffet)
    
    def GetPvCombat(self):
        return self.__pv_combat

    def SetPvCombat(self, valeur):  
        self.__pv_combat = valeur

    pv_combat = property(GetPvCombat, SetPvCombat)
    
    def GetAtkCombat(self):
        return self.__atk_combat
    
    def SetAtkCombat(self, valeur):
        self.__atk_combat = valeur

    atk_combat = property(GetAtkCombat, SetAtkCombat)
    
    def GetRace(self):
        return self.__race
    
    def SetRace(self, valeur):
        self.__race = valeur

    race = property(GetRace, SetRace)

    def GetId(self):
        return self.__id
    
    def SetId(self, valeur):
        self.__id = valeur
    
    id = property(GetId, SetId)

    def GetNom(self):
        return self.__nom
    
    def SetNom(self, valeur):
        self.__nom = valeur
    
    nom = property(GetNom, SetNom)

    #Méthodes------------------------------------------------------------------------------------------

    def Attaquer(self, adversaire): #Fait attaquer cette carte
        if self.__effet['bouclier divin'] == True: #si l'attaquant a bouclier divin
            self.__effet['bouclier divin'] = False #l'enlever
        else: #sinon
            if adversaire.effet['toxicite'] == True: #si la cible a toxicité
                self.__pv_combat = 0 #mourir
            else: #sinon
                self.__pv_combat -= adversaire.GetAtkCombat() #prendre des dégats
        if self.__pv_combat <= 0: # si la carte meurt
            if self.__effet['represailles'] and adversaire.effet['toxicite']: #que la carte avait représailles et est tuée par toxicité
                adversaire.pv_combat = 0 #tuer l'ennemi

        if adversaire.effet['bouclier divin'] == True: #si la cible a bouclier divin 
            adversaire.SetEffet(1,False) #l'enlever
        else: #sinon
            if self.__effet['toxicite'] == True: #si l'attaquant a toxicité
                adversaire.SetPvCombat(0)  #tuer la cible
            else: #sinon
                adversaire.SetPvCombat(adversaire.pv_combat - self.__atk_combat) #lui faire prendre des dégats
        if adversaire.pv_combat <= 0: # si l'ennemi meurt
            if adversaire.effet['represailles'] and self.__effet['toxicite']: #qu'il avait représailles et est tuée par toxicité
                self.__pv_combat = 0 #tuer l'ennemi
            
    
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
                        mob.atk_combat = mob.atk_combat + 2 #gagnent 2 point d'attaque

            elif self.__id == 7: #Haut prêtre
                for mob in combatants:
                    if mob.race == 3: #tous les autres humains de l'équipe de combat
                        mob.atk_combat = mob.pv_combat + 2 #gagnent 2 Pv

            elif self.__id == 9: #Tortue Géante
                for mob in combatants: #tous les autres combatants
                    mob.pv_combat = mob.pv_combat + 1 #gagnent 1 Pv
            
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
                    self.nom = combatants[n].nom + '(métamorphe)'
                    self.pv_combat = combatants[n].pv_combat #devient la copie conforme du serviteur à sa gauche 
    
    #Méthodes liées à l'affichage-------------------------------------------------------------------

    def Afficher(self):
        rouge = '\033[91m'
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
        if self.__effet['provocation']:
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