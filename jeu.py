from joueur import *
from champ_de_bataille import *
import catalogue


def Principal():
    j1 = Joueur(3, 4, "bob") #Initialise le joueur avec 1 d'or de plus que le max pour la première initialisation boutique
    ia = Joueur(3, 4, "IA") #Pareil, mais avec l'ia
    terrain = Champ_de_bataille(j1,ia)

    catalogue.UpdateTierList() #initialise les listes de cartes
    j1.RafraichirBoutique()
    ia.RafraichirBoutique()
    j1.AffStats()

    for carte in j1.GetBoutique().GetCartes():
        carte.Afficher()
    j1.Acheter(1)
    ia.Acheter(1)
    j1.PoserCarte(1)
    ia.PoserCarte(1)
    print(j1.GetCombatants()[0])
    print(ia.GetCombatants()[0])
    terrain.LancerCombat()
"""
    print("_______________")
    for carte in j1.GetBoutique().GetCartes():
        carte.Afficher()
    print("_______________")
    j1.GetMain().GetCartesEnMain()[0].Afficher()
    print("____________")
    j1.AffStats()
    """

Principal()