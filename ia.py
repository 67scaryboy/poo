from joueur import *

class IA(Joueur):#IA est une classe fille de Joueur
    def __init__(self, argent_max, argent, pseudo):
        super().__init__(argent_max, argent, pseudo)

    #Méthodes suplémentaires propres à la classe IA--------------------------------------------------------------------------

    def IndexMeilleurTier(self): 
        """
        Fonction servant à l'ia pour trouver la meilleure carte à acheter
        
        Returns:
            res (int): Index de la meilleure carte dans la boutique
        """

        res = 0 #index de la carte du plus haut tier dans la boutique

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

    @staticmethod
    def IndexPireTier(cartes): 
        """
        Fonction servant à l'ia pour trouver la pire carte dans une liste
        
        Returns:
            res (int): Index de la pire carte dans la liste
        """

        res = 0 #index de la carte du plus bas tier dans la liste

        if cartes:
            pire_tier = cartes[0].tier #Compare les tiers de chaque carte de la boutique

            for i in range(1, len(cartes)):
                if cartes[i].tier < pire_tier:
                    pire_tier = cartes[i].tier
                    res = i

        return res

    def AcheterMeilleursTiers(self): 
        """Fonction permettant à l'ia d'acheter la meilleure carte possible dans la boutique"""

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
    
    def DeployerCarte(self):
        """Fonction pour remplacer les cartes de plus faible tier si le board est plein"""

        if len(self.combattants) == 4:
            self.VendreCarte(self.IndexPireTier(self.combattants))
        
        self.PoserCarte(1)
            

    def Preparation(self):
        """l'IA upgrade la boutique si elle peut aussi acheter le même tour"""

        if self.argent >= self.boutique.prix_upgrade + carte.PRIX_CARTE and self.boutique.tier < self.boutique.tier_max:
            self.argent -= self.boutique.prix_upgrade
            self.boutique.Ameliorer()
            self.boutique.Rafraichir()

        self.AcheterMeilleursTiers()