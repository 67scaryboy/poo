import random

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

    race = property(GetRace)

    #Méthodes------------------------------------------------------------------------------------------

    def Attaquer(self, adversaire): #Fait attaquer cette carte
        if self.__effet['bouclier divin'] == True: #si l'attaquant a bouclier divin
            self.__effet['bouclier divin'] = False #l'enlever
        else: #sinon
            if adversaire.effet['toxicite'] == True: #si la cible a toxicité
                self.__pv_combat = 0 #mourir
            else: #sinon
                self.__pv_combat -= adversaire.GetAtkCombat() #prendre des dégats
        
        if adversaire.effet['bouclier divin'] == True: #si la cible a bouclier divin
            adversaire.SetEffet(1,False) #l'enlever
        else: #sinon
            if self.__effet['toxicite'] == True: #si l'attaquant a toxicité
                adversaire.SetPvCombat(0)  #tuer la cible
            else: #sinon
                adversaire.SetPvCombat(adversaire.pv_combat - self.__atk_combat) #lui faire prendre des dégats
    
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
            
            elif self.__id == 17: #Paysan
                for mob in combatants:
                    if mob.race == 3: #tous les autres humains de l'équipe de combat
                        mob.atk_combat = mob.atk_combat + 1 #gagnent 1 point d'attaque
                        mob.pv_combat = mob.pv_combat + 1 # et un point de Pv
    
    #Méthodes liées à l'affichage-------------------------------------------------------------------

    def Afficher(self):
        print(f"({self.__nom} {self.__pv_combat}PV {self.__atk_combat}ATK) | ", end='')