from joueur import *
from champ_de_bataille import *
import catalogue


def Principal():
    #Initialise les joueurs avec 1 d'or de plus que le max pour la première initialisation boutique
    j1 = Joueur(3, 10, "bob")
    ia = Joueur(3, 10, "IA")

    #initialise les listes de cartes
    catalogue.UpdateTierList()

    terrain = Champ_de_bataille(j1,ia)

    j1.RafraichirBoutique()
    ia.RafraichirBoutique()

    #affichage environnement j1
    j1.AffStats()
    j1.AffBoutique()

    #actions en jeu
    j1.Acheter(1)
    j1.Acheter(2)
    ia.Acheter(1)
    ia.Acheter(2)
    j1.PoserCarte(1)
    j1.PoserCarte(1)
    ia.PoserCarte(1)
    ia.PoserCarte(1)
    print("=============")

    ia.AffCombatants()

    j1.AffCombatants()

    terrain.LancerCombat()
"""
    print("_______________")
    j1.AffBoutique()

    j1.AffMain()

    j1.AffStats()
    """

Principal()