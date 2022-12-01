from joueur import *
from champ_de_bataille import *
import catalogue, os, time


def Principal():
    #Initialise les joueurs avec 1 d'or de plus que le max pour la première initialisation boutique
    j1 = Joueur(3, 4, "Joueur")
    ia = Joueur(3, 4, "IA")

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
    while j1.pv > 0 and ia.pv > 0:
        """"" A déplacer après le combat
        if j1.argent_max < 10:
            j1.SetArgentMax(j1.argent_max+1)
        if ia.argent_max < 10:
            ia.SetArgentMax(ia.argent_max+1)
        j1.SetArgent(j1.argent_max)
        ia.SetArgent(ia.argent_max)
        """
        os.system("cls||clear") #Effacte le terminal
        j1.AffStats()
        j1.main.Afficher()
        ia.AffStats()
        print("Ouvrez la boutique en tappant 'Boutique', ou preparez le combat en tappant 'Combat'")
        entree = input ()
        if entree == "Boutique":
            j1.AffBoutique()
            j1.ActionBoutique()

        elif entree == "Combat":
            print("Vous pouvez poser des cartes avec 'Poser' et démarrer le combat avec 'Combat'")
            entree = input()
            if entree == "Poser":
                j1.AffPoser()
                j1.ActionPoser()
                
            elif entree == "Combat":
                ia.RafraichirBoutique()
                #IA Qui se créer son deck
                if ia.GetArgent() >= ia.GetBoutique().prix_upgrade:
                    ia.UpBoutique() #Bug possible: Si boutique LV MAX, message d'erreur, mais pas de plantage
                while ia.main.nb_cartes < 6 and ia.argent >= 3 and len(ia.GetCombatants()) < 4:
                    print("Carte achetée et poser")
                    ia.Acheter(1)
                    ia.PoserCarte(1)
                """ MODIFIER ICI QUAN FONCTION VENTE
                if len(ia.GetCombatants()) == 4 and ia.GetMain().GetNbCartes() < 6 and ia.GetArgent() >= 3: #Si a deja le max de carte et la thune, vend la plus vieille et en rachete et pose une
                    ia. ####Ajouter la mathode de vente ici et vendre la 1er carte
                    ia.Acheter(1)
                    ia.PoserCarte(1)
                """
                terrain.LancerCombat()
                if j1.argent_max < 10:
                    j1.SetArgentMax(j1.argent_max+1)
                if ia.argent_max < 10:
                    ia.SetArgentMax(ia.argent_max+1)
                j1.SetArgent(j1.argent_max)
                ia.SetArgent(ia.argent_max)
                
        else:
            print ("Commande inconnue")
        time.sleep(1)

Principal()