import time
import os

def aff_msg(msg):
    """Affiche un message à l'écran assez longtemps pour le lire"""

    print(msg)
    time.sleep(1)

def Info():
    """Manuel utilisateur en jeu"""
    
    rouge = '\033[91m'
    vert = '\033[92m'
    jaune = '\033[93m'
    gris = '\033[0m'
    bleu = '\033[34m'
    violet = '\033[35m'

    print("\n" * 15)#Clear de l'écran sauvage, pratique si le clear suivant ne fonctionne pas
    os.system("cls||clear") #Efface le terminal
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
    print(f"    - Les {rouge}PV{gris} (points de vie) : Lorsqu’ils atteignent 0, la carte ne peut plus attaquer ou se faire attaquer.")
    print(f"    - L’{jaune}ATK{gris} (attaque) représentent les dégâts infligés aux cartes adverses et au personnage adverse en cas de victoire.")
    print("    - Les effets.")
    print("\n")
    print("Chaque carte peut posséder un ou plusieurs effets. Les effets existants sont :")
    print(f"    - {rouge}Provocation{gris} : Force les adversaire à attaquer en priorité cette carte. Si plusieurs cartes ont provocation, celle la plus à droite sur le terrain sera visée en priorité.")
    print(f"    - {jaune}Bouclier divin{gris} : La première fois que cette carte prend des dégâts pendant un combat, elle les ignore.")
    print(f"    - {vert}Toxicité{gris} : Si cette carte inflige des dégâts à un autre carte, la tue, peu importe le nombre de PV restant.")
    print(f"    - {bleu}Furie des vents{gris} : Attaque deux fois d’affilée, sauf en cas de mort.")
    print("    - Cri de guerre : Déclenche un effet lorsque posée sur le terrain par le joueur.")
    print(f"    - {violet}Représailles{gris} : Si cette carte se fait tuer par une carte avec Toxicité, la tue également.")
    print("\n")

def AfficherVainqueur(j1, ia1):
    os.system("cls||clear")
    if j1.pv > 0 and ia1.pv <= 0:
        print("             ╔════VAINQUEUR════════════════════════════════════════════╗ ")
        print("             ║Le Joueur gagne !                                        ║")
        print(f"             ║Il lui reste {j1.pv} PV                                       ║")
        print(f"             ║Sa boutique est tier {j1.boutique.tier} !                                 ║")
        print("             ╚═════════════════════════════════════════════════════════╝\n\n")
    elif j1.pv <= 0 and ia1.pv > 0:
        print("             ╔════VAINQUEUR════════════════════════════════════════════╗ ")
        print("             ║L'IA gagne !                                             ║")
        print(f"             ║Il lui reste {ia1.pv} PV                                       ║")
        print(f"             ║Sa boutique est tier {ia1.boutique.tier} !                                 ║")
        print("             ╚═════════════════════════════════════════════════════════╝\n\n")
    elif j1.pv <= 0 and ia1.pv <= 0:
        print("---=== DRAW ===---")