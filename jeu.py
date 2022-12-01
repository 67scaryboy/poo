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
            print("Vous pouvez quitter la boutique en tappant 'Quitter', la rafraichir avec 'Rafraichir' ou acheter une carte en entrant son numéro")
            entree = input()

            #achat de carte avec son numéro
            if int(entree) in range (1, len(j1.boutique.cartes) +1):
                j1.Acheter(int(entree))

            elif entree == "Rafraichir":
                j1.RafraichirBoutique()

        elif entree == "Combat":
            print("Vous pouvez poser des cartes avec 'Poser' et démarrer le combat avec 'Combat'")
            entree = input()
            if entree == "Poser":
                print ("Choisissez le numéro de la carte que vous souhaitez poser, ou tappez autre chose pour quitter\n\n")
                print("Les cartes dans votre main:\n")
                j1.main.Afficher()
                print ("\nVos cartes sur le terrain:\n")
                for i in j1.combatants:
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
                #IA Qui se créer son deck
                while ia.main.nb_cartes < 6 and ia.argent > 3:
                    ia.Acheter(1)
                while len(ia.combatants) < 4 and ia.main.nb_cartes > 0:
                    ia.Poser(1)
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