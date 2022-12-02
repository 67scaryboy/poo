import carte, random, catalogue

class Boutique:
    def __init__(self):
        self.__tier = 1 #le tier maximal des cartes dans la taverne
        self.__tier_max = 5 #le tier maximal de la boutique
        self.__prix_upgrade = 5 #le prix pour monter le niveau de la taverne
        self.__cartes = [] #les cartes disponibles à l'achat
        self.__prix_refresh = 1
    
    #Getteurs et setteurs-------------------------------------------------------------------------------

    def GetPrixRefresh(self):
        return self.__prix_refresh

    prix_refresh = property(GetPrixRefresh)

    def GetCartes(self):
        return self.__cartes
    
    def SetCartes(self, cartes):
        self.__cartes = cartes

    cartes = property(GetCartes, SetCartes)

    def GetPrixUpgrade(self):
        return self.__prix_upgrade

    def SetPrixUpgrade(self, prix):
        if prix > 0 and prix < 6:
            self.__prix_upgrade = prix
    
    prix_upgrade = property(GetPrixUpgrade, SetPrixUpgrade)

    def GetTier(self):
        return self.__tier

    def SetTier(self, nb):
        if nb > 1 and nb < self.tier_max:
            self.__tier = nb

    tier = property(GetTier, SetTier)

    def GetTierMax(self):
        return self.__tier_max

    tier_max = property(GetTierMax)

    #Méthodes------------------------------------------------------------------------------------------
    
    def DelCartes(self,numcarte): #Retire une carte de la boutique en fonction de sa position
        del self.__cartes[numcarte-1]

    def Rafraichir(self): #Changer les cartes proposées en boutique
        self.__cartes = []

        for i in range (5):
            #randomisation du tier de la carte à tirer
            temp = random.randint(0,self.__tier - 1)

            #choix aléatoire de la carte du tier donné
            self.__cartes.append(catalogue.liste_tiers[temp][random.randint(0,len(catalogue.liste_tiers[temp])-1)])
    
    def Ameliorer(self): #Fonction amélioration appelée par le joueur
        self.tier += 1
        self.prix_upgrade = 5