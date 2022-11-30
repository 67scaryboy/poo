import carte

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
        listecartes = [] #choisir aléatoirement les cartes des tiers
        self.__cartes = listecartes
    
    def améliorer(self):
        if tier < 5:
            self.__tier +=1
        #retirer l'argent du joueur