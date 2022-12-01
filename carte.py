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

    def Afficher(self):
        print(f"{self.__nom}\n PV: {self.__pv} / ATK: {self.__atk}\n")

    def GetTier(self):
        return self.__tier
    
    def GetEffet(self):
        return self.__effet
    
    def GetPvCombat(self):
        return self.__pv_combat

    def SetPvCombat(self, valeur):  
        self.__pv_combat = valeur
    
    def GetAtkCombat(self):
        return self.__atk_combat

    def Attaquer(self, adversaire): #Fait attaquer cette carte
        adversaire.SetPvCombat(advarsaire.GetPvCombat() - self.__atk_combat) #L'adversaire prend les dégats
        self.__pv_combat -= adversaire.GetAtkCombat() #L'attaquant prend les dégats aussi