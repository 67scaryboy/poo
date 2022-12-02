from joueur import *
from champ_de_bataille import *
from message import *
from ia import *
import catalogue, os

def Info(): #Manuel utilisateur en jeu
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Manuel utilisateur du jeu\n\n")
    print("La boutique :")
    print("Tier : La boutique possède un tier, n’affichant ainsi que les monstres de tier égal ou inférieur à celui de la boutique. Il peut être augmenter en dépensant de l’or. Chaque tour, le prix d’amélioration est réduit de 1. Après amélioration, il est fixé à 5 or.")
    print("Sélection : La sélection disponible dans la boutique est aléatoire et composé de cartes de rang inférieur ou égal au rang de la boutique. Il y à maximum 5 cartes dans la boutique.")
    print("Rafraichir : Actualise la sélection de monstre présent dans la boutique, moyennant 1 or. Après une amélioration de la boutique, un rafraichissement est effectué gratuitement.")
    print("\n")
    print("La main : ")
    print("La main du joueur peut contenir au maximum 6 cartes. Au-delà, il n’est plus possible d’en acheter. Le seul moyen de se débarrasser d’une carte est de la poser sur le terrain.")
    print("\n")
    print("Poser :")
    print("Pose une carte de votre main à la droite du terrain.")
    print("\n")
    print("Vendre :")
    print("Vous ne pouvez vendre qu’une carte posée sur le terrain. Vous pouvez cependant choisir quelle carte vendre. La vente d’une carte rapporte 1 or au joueur.")
    print("\n")
    print("Le terrain :")
    print("Il contient les cartes posées par les deux joueurs. Cependant, les joueurs ne peuvent pas voir quelles sont les cartes adverses avant le début du combat. Les joueurs ne peuvent pas voir l’or adverse utilisé.")
    print("\n")
    print("Personnage :")
    print("Ils représentent les joueurs. Chaque personnage possèdent un nombre de point de vie. Le joueur perd la partie si les points de vie de son personnage atteignent 0.")
    print("\n")
    print("Combat :")
    print("Lance le combat contre l’adversaire. Lors d’un combat, le joueur attaquant en premier est choisi aléatoirement, de même que l’attaquant et l’attaquer (Sauf en présence de cartes avec l’attribut provocation). Une carte du premier joueur attaque, puis une carte du deuxième avant de recommencer jusqu’à ce que l’un  ou les deux joueurs n’ait(ent) plus de cartes sur le terrain. S’il reste des cartes dans le camp d’un joueur, l’autre encaissera des dégâts de personnage égaux à la somme de leurs tiers. Les cartes sur le terrain se gardent d’un combat à l’autre et regagnent tous leurs  PV avant le début.")
    print("\n")
    print("Les cartes et leurs effets :")
    print("Il existe dans le jeu une variété de cartes et d’effet associés. Chaque cartes possèdent des attributs qui sont communes aux autres cartes :")
    print("    - Les PV (points de vie) : Lorsqu’ils atteignent 0, la carte ne peut plus attaquer ou se faire attaquer.")
    print("    - L’ATK (attaque) représentent les dégâts infligés aux cartes adverses et au personnage adverse en cas de victoire.")
    print("    - Les effets.")
    print("\n")
    print("Chaque carte peut posséder un ou plusieurs effets. Les effets existants sont :")
    print("    - Provocation : Force les adversaire à attaquer en priorité cette carte. Si plusieurs cartes ont provocation, celle la plus à droite sur le terrain sera visée en priorité.")
    print("    - Bouclier divin : La première fois que cette carte prend des dégâts pendant un combat, elle les ignore.")
    print("    - Toxicité : Si cette carte inflige des dégâts à un autre carte, la tue, peu importe le nombre de PV restant.")
    print("    - Furie des vents : Attaque deux fois d’affilée, sauf en cas de mort.")
    print("    - Crie de guerre : Déclenche un effet lorsque posée sur le terrain par le joueur.")
    print("    - Représailles : Si cette carte se fait tuer par une carte avec Toxicité, la tue également.")
    print("\n")
    print("Chaque effet est indiqué en jeu grâce à un code couleur facilement reconnaissable :")
    print("    - Provocation : Le nom de la carte apparait en rouge.")
    print("    - Bouclier divin : Les parenthèses autour de la carte apparaissent en jaune.")
    print("    - Toxicité : L’attaque de la carte apparait en vert.")
    print("    - Furie des vents : Le mot ATK de la carte apparait en bleu.")
    print("    - Cri de guerre : Un symbole spécial apparait sur la carte (✜ ).")
    print("    - Représailles : Ajout d’un crâne précédant le nom (☠ ).")

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

    #boucle principale de jeu
    while j1.pv > 0 and ia1.pv > 0:
        print("\n" * 100) #Clear de l'écran sauvage, pratique si le clear suivant ne fonctionne pas
        os.system("cls||clear") #Efface le terminal

        #affichage des statistiques des joueurs
        j1.AffStats()
        ia1.AffStats()

        #infos joueur
        entree = input("b) Ouvrir la boutique\np) Poser des cartes\nv) Vendre\nc) Combatre\nq) Quitter\n--> ")

        if entree == 'b':
            j1.AffBoutique()
            j1.ActionBoutique()

        elif entree == 'p':
            j1.AffPoser()
            j1.ActionPoser()
            
        elif entree =='i':
            Info()
            input("--------- appuyez pour passer ---------")

        elif entree == 'c':
            ia1.Preparation()

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