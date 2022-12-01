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

<<<<<<< HEAD
    def afficher(self):
        print(f"{self.__nom}\n PV: {self.__pv} / ATK: {self.__atk}\n")

=======
>>>>>>> c86c691b9b2df5376462e295f9e8bf68525a17bb
    def GetTier(self):
        return self.__tier
    
    def GetPvCombat(self):
        return self.__pv_combat

    def SetPvCombat(self, valeur):  
        self.__pv_combat = valeur
    
    def GetAtkCombat(self):
        return self.__atk_combat
    
    def Afficher(self):
        print(f"{self.__nom}({self.__pv}): {self.__atk}\n")

    def Attaquer(self, adversaire): #Fait attaquer cette carte
        adversaire.__pv_combat -= self.__atk_combat #L'adversaire prend les dégats
        self.__pv_combat -= adversaire.__atk_combat #L'attaquant prend les dégats aussi

    def Meurt(self): #Fait mourir la carte (La retire du terain)
        if self.__pv < 1:
            pass