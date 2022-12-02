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

    #Prototype de code:
    while j1.pv > 0 and ia1.pv > 0:
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
            j1.AffVendre()
            j1.ActionVendre()

        elif entree == 'q':
            return
    os.system("cls||clear")
    if j1.pv > 0:
        print("             ╔════VAINQUEUR════════════════════════════════════════════╗ ")
        print("             ║Le Joueur gagne !                                        ║")
        print(f"             ║Il lui reste {j1.pv} PV                                       ║")
        print(f"             ║Sa boutique est tier {j1.boutique.tier} !                                 ║")
        print("             ╚═════════════════════════════════════════════════════════╝\n\n")
    else:
        print("             ╔════VAINQUEUR════════════════════════════════════════════╗ ")
        print("             ║L'IA gagne !                                             ║")
        print(f"             ║Il lui reste {ia1.pv} PV                                       ║")
        print(f"             ║Sa boutique est tier {ia1.boutique.tier} !                                 ║")
        print("             ╚═════════════════════════════════════════════════════════╝\n\n")


Principal()