from joueur import *
import catalogue

def principal():
    j1 = Joueur(3, 3, "bob")
    j1.aff_stats()

    catalogue.UpdateTierList() #initialise les listes de cartes
    j1.RafraichirBoutique()

    for carte in j1.GetBoutique().get_cartes():
        carte.afficher()

principal()