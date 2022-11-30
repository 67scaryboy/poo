class Cartes():
    def __init__(self,id_cartes):
        self.id=id_cartes
        self.pv= #PV du personnage.
        self.pv_combat=self.pv
        self.atk= #Attaque du perso
        self.atk_combat=self.atk
        self.prix= #Prix d'achat en or
        self.effet= #Effet particulier
        self.race= #Race
        self.tier= #Tier de la boutique dans lequel il est achetable

    def Attaquer(self, p_adversaire): #Fait attaquer cette carte
        p_adversaire.pv_combat-=self.atk_combat #L'adversaire prend les dégats
        self.pv_combat-=p_adversaire.atk_combat #L'attaquant prend les dégats aussi

    def Meurt(self): #Fait mourir la carte (La retire du terain)
        if self.PV<1:
            #A faire
    
    def Vendre(self,main):
        main.OR+=1
        self.Meurt()

    def Poser(self):
        #A faire