from joueur import *
from champ_de_bataille import *
from message import *
from ia import *
import catalogue, os

def Principal():
    #Initialise les joueurs
    j1 = Joueur(3, 3, "Joueur")
    ia1 = IA(3, 3, "IA")

    #initialise les listes de cartes
    catalogue.UpdateTierList()

    #Affrontement j1 contre ia
    terrain = Champ_de_bataille(j1,ia1)

    #initialise les boutiques
    j1.boutique.Rafraichir()
    ia1.boutique.Rafraichir()

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
    while j1.pv > 0 and ia1.pv > 0:
        """"" A déplacer après le combat
        if j1.argent_max < 10:
            j1.SetArgentMax(j1.argent_max+1)
        if ia.argent_max < 10:
            ia.SetArgentMax(ia.argent_max+1)
        j1.SetArgent(j1.argent_max)
        ia.SetArgent(ia.argent_max)
        """
        print("\n" * 100) #Clear de l'écran sauvage, pratique si le clear dessous marche pas
        os.system("cls||clear") #Efface le terminal

        j1.AffStats()
        ia1.AffStats()

        entree = input("b) Ouvrir la boutique\np) Poser des cartes\nv) Vendre\nc) Combatre\nq) Quitter\n--> ")

        if entree == 'b':
            j1.AffBoutique()
            j1.ActionBoutique()

        elif entree == 'p':
            j1.AffPoser()
            j1.ActionPoser()
            
        elif entree == 'c':
            ia1.preparation()

            #---- combat ----

            terrain.LancerCombat()

            #---- après le combat ----

            #mise à jour de l'argent
            terrain.MajArgent()

            #mise à jour du prix d'upgrade des boutiques
            terrain.MajBoutique()

            input("--------- appuyez pour passer ---------")

        elif entree == 'v':
            print ("Choisissez le numéro de la carte que vous souhaitez vendre, ou tapez autre chose pour quitter\n\n")
            print("Les cartes dans votre main:\n")
            j1.main.Afficher()
            print ("\nVos cartes sur le terrain:\n")
            for i in j1.combatants:
                i.Afficher()
            entree = input()
            if entree == "1" and len(j1.combatants) > 0:
                j1.VendreCarte(1)
            elif entree == "2" and len(j1.combatants) > 1:
                j1.VendreCarte(2)
            elif entree == "3" and len(j1.combatants) > 2:
                j1.VendreCarte(3)
            elif entree == "4" and len(j1.combatants) > 3:
                j1.VendreCarte(4)

        elif entree == 'q':
            return

Principal()