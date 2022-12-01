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
    
    def GetEffet(self):
        return self.__effet
    
    def SetEffet(self,num,valeur):
        self.__effet[num] = valeur
    
    def GetPvCombat(self):
        return self.__pv_combat

    def SetPvCombat(self, valeur):  
        self.__pv_combat = valeur
    
    def GetAtkCombat(self):
        return self.__atk_combat
    
    def SetAtkCombat(self, valeur):
        self.__atk_combat = valeur
    
    def GetRace(self):
        return self.__race

    #Méthodes------------------------------------------------------------------------------------------

    def Attaquer(self, adversaire): #Fait attaquer cette carte
        if self.__effet['bouclier divin'] == True: #si l'attaquant a bouclier divin
            self.__effet['bouclier divin'] = False #l'enlever
        else: #sinon
            if adversaire.GetEffet()['toxicite'] == True: #si la cible a toxicité
                self.__pv_combat = 0 #mourir
            else: #sinon
                self.__pv_combat -= adversaire.GetAtkCombat() #prendre des dégats
        
        if adversaire.GetEffet()['bouclier divin'] == True: #si la cible a bouclier divin
            adversaire.SetEffet(1,False) #l'enlever
        else: #sinon
            if self.__effet['toxicite'] == True: #si l'attaquant a toxicité
                adversaire.SetPvCombat(0)  #tuer la cible
            else: #sinon
                adversaire.SetPvCombat(adversaire.GetPvCombat() - self.__atk_combat) #lui faire prendre des dégats
    
    def CriDeGuerre(self,joueur):
        if self.__effet['cri de guerre'] == True: #si la carte a un cri de guerre
            if self.__id == 1: #Mage noir
                for mobs in joueur.GetCombatants():
                    if mobs.GetRace() == 3: #tous les autres humains de l'équipe de combat
                        mobs.SetAtkCombat(mobs.GetAtkCombat() + 1) #gagnent 1 point d'attaque

            elif self.__id == 2: #Gobelin
                joueur.SetArgent(joueur.GetArgent() +1) #le joueur gagne une pièce--------------------------------------------à corriger

            elif self.__id == 9: #Tortue Géante
                for mobs in joueur.GetCombatants(): #tous les autres combatants
                    mobs.SetPvCombat(mobs.GetPvCombat() + 1) #gagnent 1 Pv

        else: #sinon
            pass #rien
    
    #Méthodes liées à l'affichage-------------------------------------------------------------------

    def Afficher(self):
        print(f"({self.__nom} {self.__pv_combat}PV {self.__atk_combat}ATK) | ", end='')   