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

    #Méthodes------------------------------------------------------------------------------------------

    def Attaquer(self, adversaire): #Fait attaquer cette carte
        if self.__effet[1] == True: #si l'attaquant a bouclier divin
            self.__effet[1] = False #l'enlever
        else: #sinon
            if adversaire.GetEffet()[2] == True: #si la cible a toxicité
                self.__pv_combat = 0 #mourir
            else: #sinon
                self.__pv_combat -= adversaire.GetAtkCombat() #prendre des dégats
        
        if adversaire.GetEffet()[1] == True: #si la cible a bouclier divin
            adversaire.SetEffet(1,False) #l'enlever
        else: #sinon
            if self.__effet[2] == True: #si l'attaquant a toxicité
                adversaire.SetPvCombat(0)  #tuer la cible
            else: #sinon
                adversaire.SetPvCombat(adversaire.GetPvCombat() - self.__atk_combat) #lui faire prendre des dégats
    
    #Méthodes liées à l'affichage-------------------------------------------------------------------

    def Afficher(self):
        print(f"({self.__nom} {self.__pv_combat}PV {self.__atk_combat}ATK) | ", end='')   