class Carte():
    def __init__(self, id, nom, pv, atk, effet, race, tier):
        self.id = id                    #id de la carte
        self.nom = nom                  #nom de la carte
        self.pv = pv                    #PV de base de la carte
        self.pv_combat = self.pv        #PV effectifs de la carte
        self.atk = atk                  #Attaque du perso
        self.atk_combat = self.atk      #Attaque effective de la carte
        self.effet = effet              #Effet particulier
        self.race = race                #Race
        self.tier = tier                #Tier de la boutique dans lequel il est achetable

    def GetTier(self):
        return self.tier

    def Attaquer(self, adversaire): #Fait attaquer cette carte
        adversaire.pv_combat -= self.atk_combat #L'adversaire prend les dégats
        self.pv_combat -= adversaire.atk_combat #L'attaquant prend les dégats aussi

    def Meurt(self): #Fait mourir la carte (La retire du terain)
        if self.PV < 1:
            pass
    
    def Vendre(self,main):
        main.OR += 1
        self.Meurt()

    def Poser(self):
        pass