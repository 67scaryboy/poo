import carte, random, catalogue

class Boutique:
    def __init__(self):
        """constructeur de la classe Boutique"""

        self.__tier = 1 #le tier maximal des cartes dans la taverne
        self.__tier_max = 5 #le tier maximal de la boutique
        self.__prix_upgrade = 5 #le prix pour monter le niveau de la taverne
        self.__cartes = [] #les cartes disponibles à l'achat
        self.__prix_refresh = 1 #le prix pour rafraichir les cartes de la boutique
    
    #Getters et setters-------------------------------------------------------------------------------

    def GetPrixRefresh(self):
        """getter de __prix_refresh"""

        return self.__prix_refresh

    prix_refresh = property(GetPrixRefresh)

    def GetCartes(self):
        """getter de __cartes"""

        return self.__cartes
    
    def SetCartes(self, cartes):
        """setter de __cartes"""

        self.__cartes = cartes

    cartes = property(GetCartes, SetCartes)

    def GetPrixUpgrade(self):
        """getter de __prix_upgrade"""

        return self.__prix_upgrade

    def SetPrixUpgrade(self, prix):
        """setter de __prix_upgrade"""

        if prix > 0 and prix < 6:
            self.__prix_upgrade = prix
    
    prix_upgrade = property(GetPrixUpgrade, SetPrixUpgrade)

    def GetTier(self):
        """getter de __tier"""

        return self.__tier

    def SetTier(self, nb):
        """setter de __tier"""

        if nb > 1 and nb < self.tier_max:
            self.__tier = nb

    tier = property(GetTier, SetTier)

    def GetTierMax(self):
        """getter de __tier_max"""

        return self.__tier_max

    tier_max = property(GetTierMax)

    #Méthodes------------------------------------------------------------------------------------------
    
    def DelCartes(self, numcarte):
        """Retire une carte de la boutique en fonction de sa position (commence a 1)"""

        del self.__cartes[numcarte-1]

    def Rafraichir(self):
        """Change les cartes proposées en boutique et la remplie"""

        self.__cartes = []

        for i in range (5):
            #tier aléatoire parmis les tiers disponibles
            randtier = random.randint(0,self.__tier - 1)

            #choix aléatoire d'une carte du tier donné
            self.__cartes.append(catalogue.liste_tiers[randtier][random.randint(0,len(catalogue.liste_tiers[randtier])-1)])
    
    def Ameliorer(self):
        """Amélioration de la boutique et réinitialisation de son prix"""

        self.tier += 1
        self.prix_upgrade = 5