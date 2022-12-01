from joueur import *

class IA(Joueur):
    def __init__(self, argent_max, argent, pseudo):
        super().__init__(argent_max, argent, pseudo)

    def preparation(self):
        self.RafraichirBoutique()
        #IA Qui se créer son deck
        if self.argent >= self.boutique.prix_upgrade:
            self.UpBoutique #Bug possible: Si boutique LV MAX, message d'erreur, mais pas de plantage

        while self.argent >= carte.PRIX_CARTE and len(self.combatants) < 4:
            self.Acheter(1)
            self.PoserCarte(1)

        if len(self.combatants) == 4 and len(self.main.cartes) < 6 and self.argent >= 3: #Si a deja le max de carte et la thune, vend la plus vieille et en rachete et pose une
            self.VendreCarte(1) 
            self.Acheter(1)
            self.PoserCarte(1)

        if self.argent > 0:
            self.RafraichirBoutique()