from joueur import *
from champ_de_bataille import *
from ia import *
import catalogue, os
from event import *

def Principal():
    #Initialise les joueurs
    j1 = Joueur(3, 3, "Joueur")
    ia1 = IA(3, 3, "IA")

    #initialise les listes de cartes
    catalogue.UpdateTierList()

    #Prépare l'affrontement de j1 contre ia
    terrain = Champ_de_bataille(j1,ia1)

    #initialise les boutiques
    j1.boutique.Rafraichir()
    ia1.boutique.Rafraichir()

    running = True
    #boucle principale de jeu
    while running:
        print("\n" * 100) #Clear de l'écran sauvage, pratique si le clear suivant ne fonctionne pas
        os.system("cls||clear") #Efface le terminal

        #affichage des statistiques des joueurs
        j1.AffStats()
        ia1.AffStats()

        #choix joueur
        entree = input("i) Afficher les informations\nb) Ouvrir la boutique\np) Poser des cartes\nv) Vendre\nc) Combatre\nq) Quitter\n--> ")
        continuer = EventHandler(entree, j1, ia1, terrain)

        running = j1.pv > 0 and ia1.pv > 0 and continuer

        AfficherVainqueur(j1, ia1)

Principal()