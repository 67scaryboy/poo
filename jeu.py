from joueur import *
import catalogue

def Principal():
    j1 = Joueur(3, 3, "bob")
    j1.AffStats()

    catalogue.UpdateTierList() #initialise les listes de cartes
    j1.RafraichirBoutique()

    for carte in j1.GetBoutique().GetCartes():
        carte.Afficher()

Principal()