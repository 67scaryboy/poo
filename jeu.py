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
    while j1.GetPV() > 0 and ia.GetPV() > 0:
        """"" A déplacer après le combat
        if j1.GetArgentMax() < 10:
            j1.SetArgentMax(j1.GetArgentMax()+1)
        if ia.GetArgentMax() < 10:
            ia.SetArgentMax(ia.GetArgentMax()+1)
        j1.SetArgent(j1.GetArgentMax())
        ia.SetArgent(ia.GetArgentMax())
        """
        os.system("cls||clear") #Effacte le terminal
        j1.AffStats()
        j1.GetMain().Afficher()
        ia.AffStats()
        print("Ouvrez la boutique en tappant 'Boutique', ou preparez le combat en tappant 'Combat'")
        entree = input ()
        if entree == "Boutique":
            j1.AffBoutique()
            print("Vous pouvez quitter la boutique en tappant 'Quitter', la rafraichir avec 'Rafraichir' ou acheter une carte en entrant son numéro")
            entree = input()
            if entree == "1":
                j1.Acheter(1)
            elif entree == "2":
                j1.Acheter(2)
            elif entree == "3":
                j1.Acheter(3)
            elif entree =="4":
                j1.Acheter(4)
            elif entree == "5":
                j1.Acheter(5)
            elif entree == "Rafraichir":
                j1.RafraichirBoutique()
        elif entree == "Combat":
            print("Vous pouvez poser des cartes avec 'Poser' et démarrer le combat avec 'Combat'")
            entree = input()
            if entree == "Poser":
                print ("Choisissez le numéro de la carte que vous souhaitez poser, ou tappez autre chose pour quitter\n\n")
                print("Les cartes dans votre main:\n")
                j1.GetMain().Afficher()
                print ("\nVos cartes sur le terrain:\n")
                for i in j1.GetCombatants():
                    i.Afficher()
                entree = input()
                if entree == "1":
                    j1.PoserCarte(1)
                elif entree == "2":
                    j1.PoserCarte(2)
                elif entree == "3":
                    j1.PoserCarte(3)
                elif entree == "4":
                    j1.PoserCarte(4)
                elif entree == "5":
                    j1.PoserCarte(5)
                elif entree == "6":
                    j1.PoserCarte(6)
            elif entree == "Combat":
                ia.RafraichirBoutique()
                #IA Qui se créer son deck
                if ia.GetArgent() >= ia.GetBoutique().GetPrixUpgrade():
                    ia.UpBoutique() #Bug possible: Si boutique LV MAX, message d'erreur, mais pas de plantage
                while ia.GetMain().GetNbCartes() < 6 and ia.GetArgent() >= 3 and len(ia.GetCombatants()) < 4:
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
                if j1.GetArgentMax() < 10:
                    j1.SetArgentMax(j1.GetArgentMax()+1)
                if ia.GetArgentMax() < 10:
                    ia.SetArgentMax(ia.GetArgentMax()+1)
                j1.SetArgent(j1.GetArgentMax())
                ia.SetArgent(ia.GetArgentMax())
                
        else:
            print ("Commande inconnue")
        time.sleep(1)

Principal()