from joueur import *

class IA(Joueur):
    def __init__(self, argent_max, argent, pseudo):
        super().__init__(argent_max, argent, pseudo)

    def IndexMeilleurTier(self): #Fonction servant a l'ia a trouver la meilleure carte a acheter
        res = 0

        if self.boutique.cartes:
            meilleur_tier = self.boutique.cartes[0].tier #Compare les tiers de chaque carte de la boutique

            if meilleur_tier == self.boutique.tier:#meilleur tier possible trouvé
                return res

            for i in range(1, len(self.boutique.cartes)):
                if self.boutique.cartes[i].tier > meilleur_tier:
                    meilleur_tier = self.boutique.cartes[i].tier
                    res = i

                    if meilleur_tier == self.boutique.tier: #meilleur tier possible trouvé
                        return res
        else:
            print("La fonction ne doit pas être appelée: la boutique est vide")
        
        return res

    def AcheterMeilleursTiers(self): # Fonction permettant à l'ia d'acheter la meilleure carte possible
        while self.argent >= self.boutique.prix_refresh:
            if self.boutique.cartes:
                i_meil_tier = self.IndexMeilleurTier()

                if self.boutique.cartes[i_meil_tier].tier == self.boutique.tier: #meilleur tier trouvé dans la boutique
                    if self.argent >= carte.PRIX_CARTE: #assez d'argent pour acheter
                        self.Acheter(i_meil_tier + 1)
                        self.DeployerCarte()
                    else:
                        return #attend le tour suivant pour acheter par manque d'argent
                else:
                    self.RafraichirBoutique()
            else:
                self.RafraichirBoutique()
    
    def DeployerCarte(self): #Fonction si le board est plein, pour remplacer les plus vieille carte (a améliorer pour rendre l'ia plus forte en changeant les cartes de plus bas tier)
        if len(self.combatants) == 4:
            self.VendreCarte(1)
        
        self.PoserCarte(1)
            

    def Preparation(self):
        #IA upgrade la boutique s'il peut aussi acheter le même tour
        if self.argent >= self.boutique.prix_upgrade + carte.PRIX_CARTE and self.boutique.tier < self.boutique.tier_max:
            self.argent -= self.boutique.prix_upgrade
            self.boutique.Ameliorer()
            self.boutique.Rafraichir()

        self.AcheterMeilleursTiers()

        # while self.argent >= carte.PRIX_CARTE and len(self.combatants) < 4:
        #     self.Acheter(1)
        #     self.PoserCarte(1)

        # while len(self.combatants) == 4 and len(self.main.cartes) < 6 and self.argent >= carte.PRIX_CARTE: #Si a deja le max de carte et la thune, vend la plus vieille et en rachete et pose une
        #     self.VendreCarte(1) 
        #     self.Acheter(1)
        #     self.PoserCarte(1)

        # if self.argent > 0:
        #     self.RafraichirBoutique()