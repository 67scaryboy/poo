import Ccarte, random, catalogue

class Boutique:
    def __init__(self):
        self.__tier = 1 #le tiers maximal des cartes dans la taverne
        self.__prixupgrade = 5 #le prix pour monter le niveau de la taverne
        self.__cartes = [] #les cartes disponibles à l'achat
    
    def get_cartes(self):
        return self.__cartes
    
    def set_cartes(self, p_cartes):
        self.__cartes = p_cartes

    def raffraichir(self):
        self.__cartes = []
        for i in range (0,5,1):
            if self.__tier == 1:
                self.__cartes.append(catalogue.liste_tier_1[random.randint(0,len(catalogue.liste_tier_1))])
            elif self.__tier == 2:
                if random.randint(0,1) == 0:
                    self.__cartes.append(catalogue.liste_tier_1[random.randint(0,len(catalogue.liste_tier_1))])
                else:
                    self.__cartes.append(catalogue.liste_tier_2[random.randint(0,len(catalogue.liste_tier_2))])
            elif self.__tier == 3:
                temp=random.randint(0,2)
                if temp == 0:
                    self.__cartes.append(catalogue.liste_tier_1[random.randint(0,len(catalogue.liste_tier_1))])
                elif temp == 1 :
                    self.__cartes.append(catalogue.liste_tier_2[random.randint(0,len(catalogue.liste_tier_2))])
                else:
                    self.__cartes.append(catalogue.liste_tier_3[random.randint(0,len(catalogue.liste_tier_3))])
            elif self.__tier == 4:
                temp=random.randint(0,3)
                if temp == 0:
                    self.__cartes.append(catalogue.liste_tier_1[random.randint(0,len(catalogue.liste_tier_1))])
                elif temp == 1 :
                    self.__cartes.append(catalogue.liste_tier_2[random.randint(0,len(catalogue.liste_tier_2))])
                elif temp == 2:
                    self.__cartes.append(catalogue.liste_tier_3[random.randint(0,len(catalogue.liste_tier_3))])
                else: 
                    self.__cartes.append(catalogue.liste_tier_4[random.randint(0,len(catalogue.liste_tier_4))])


        listecartes = [] #choisir aléatoirement les cartes des tiers
        self.__cartes = listecartes
    
    def améliorer(self):
        if tier < 5:
            self.__tier +=1
        #retirer l'argent du joueur