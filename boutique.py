import carte, random, catalogue

class Boutique:
    def __init__(self):
        self.__tier = 4 #le tiers maximal des cartes dans la taverne
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
            if self.__tier == 1:
                self.__cartes.append(catalogue.liste_tier_1[random.randint(0,len(catalogue.liste_tier_1)-1)])
            elif self.__tier == 2:
                if random.randint(0,1) == 0:
                    self.__cartes.append(catalogue.liste_tier_1[random.randint(0,len(catalogue.liste_tier_1)-1)])
                else:
                    self.__cartes.append(catalogue.liste_tier_2[random.randint(0,len(catalogue.liste_tier_2)-1)])
            elif self.__tier == 3:
                temp=random.randint(0,2)
                if temp == 0:
                    self.__cartes.append(catalogue.liste_tier_1[random.randint(0,len(catalogue.liste_tier_1)-1)])
                elif temp == 1 :
                    self.__cartes.append(catalogue.liste_tier_2[random.randint(0,len(catalogue.liste_tier_2)-1)])
                else:
                    self.__cartes.append(catalogue.liste_tier_3[random.randint(0,len(catalogue.liste_tier_3)-1)])
            elif self.__tier == 4:
                temp=random.randint(0,3)
                if temp == 0:
                    self.__cartes.append(catalogue.liste_tier_1[random.randint(0,len(catalogue.liste_tier_1)-1)])
                elif temp == 1 :
                    self.__cartes.append(catalogue.liste_tier_2[random.randint(0,len(catalogue.liste_tier_2)-1)])
                elif temp == 2:
                    self.__cartes.append(catalogue.liste_tier_3[random.randint(0,len(catalogue.liste_tier_3)-1)])
                else: 
                    self.__cartes.append(catalogue.liste_tier_4[random.randint(0,len(catalogue.liste_tier_4)-1)])
    
    def Ameliorer(self):
        if self.__tier < 4:
            self.__tier += 1
            self.__prix_upgrade = 5
        #retirer l'argent du joueur