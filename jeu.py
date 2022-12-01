from joueur import *
from champ_de_bataille import *
import catalogue, os, time


def Principal():
    #Initialise les joueurs avec 1 d'or de plus que le max pour la première initialisation boutique
    j1 = Joueur(2, 2, "Joueur")
    ia = Joueur(2, 2, "IA")

    #initialise les listes de cartes
    catalogue.UpdateTierList()

    terrain = Champ_de_bataille(j1,ia)

    j1.RafraichirBoutique()
    ia.RafraichirBoutique()
    """
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

    j1.AffStats()
    ia.AffStats()
    """

    #Prototype de code:
    while j1.GetPV() > 0 and ia.GetPV() > 0:
        if j1.GetArgentMax() < 10:
            j1.SetArgentMax(j1.GetArgentMax()+1)
        if ia.GetArgentMax() < 10:
            ia.SetArgentMax(ia.GetArgentMax()+1)
        j1.SetArgent(j1.GetArgentMax())
        ia.SetArgent(ia.GetArgentMax())
        os.system("cls") #Effacte le terminal
        j1.AffStats()
        ia.AffStats()
        print("Ouvrez la boutique en tappant 'Boutique', ou preparez le combat en tappant 'Combat'")
        entree = input ()
        if entree == "Boutique":
            print ("a")
            exit()
        elif entree == "Combat":
            print("b")
            exit()
        else:
            print ("Commande inconnue")
        time.sleep(1)

Principal()