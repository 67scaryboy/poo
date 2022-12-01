import carte, random, catalogue

class Boutique:
    def __init__(self):
        self.__tier = 2 #le tiers maximal des cartes dans la taverne
        self.__prix_upgrade = 5 #le prix pour monter le niveau de la taverne
        self.__cartes = [] #les cartes disponibles à l'achat
    
    #Getteurs et setteurs-------------------------------------------------------------------------------

    def GetCartes(self):
        return self.__cartes
    
    def SetCartes(self, cartes):
        self.__cartes = cartes

    #Méthodes------------------------------------------------------------------------------------------
    
    def GetPrixUpgrade(self):
        return self.__prix_upgrade
    
    def SetPrixUpgrade(self,prix):
        if prix > 0:
            self.__prix_upgrade = prix
    
    def DelCartes(self,numcarte): #Retire une carte de la boutique en fonction de sa position
        del self.__cartes[numcarte-1]

    def Rafraichir(self): #Changer les cartes proposées en boutique
        self.__cartes = []

        for i in range (0,5,1):
            #randomisation du tier de la carte à tirer
            temp = random.randint(0,self.__tier - 1)
            
            #choix aléatoire de la carte du tier donné
            self.__cartes.append(catalogue.liste_tiers[temp][random.randint(0,len(catalogue.liste_tiers[temp])-1)])
    
    def Ameliorer(self):
        if self.__tier < 4:
            self.__tier += 1
            self.__prix_upgrade = 5
        #retirer l'argent du joueur