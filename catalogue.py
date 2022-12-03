from enum import Enum
from carte import Carte

#Initialisation des liste différents tiers (pour la boutique)
liste_tier_1 = []
liste_tier_2 = []
liste_tier_3 = []
liste_tier_4 = []
liste_tiers = [liste_tier_1, liste_tier_2, liste_tier_3, liste_tier_4]

class Races(Enum):
    NONDEFINIS=0
    MONSTRES=1
    ANIMEAUX=2
    HUMAINS=3

idcartes = { #Pas utilisé pour le moment
    "GNOLL": 0, "MAGENOIR": 1, "GOBELIN": 2 ,"LOUP" : 3 , "FEUFOLLET" : 4 , "GARDE" : 5 ,
    "ASSASSIN" : 6 , "PRETRE" : 7 , "FANTOME" : 8 , "TORTUE" : 9 , "DRAGON" : 10 ,
    "HEROS" : 11 , "ROIDEMON" : 12, "VIRUS" : 13,  "SANGLIER" : 14, "SCORPION" : 15, 
    "T-REX" : 16, "PAYSAN" : 17, "METAMORPHE" : 18
    }

#Listes de cartes par tier
#id, nom, pv, atk, effet, race, tier
catalogue = [
Carte(0, "Gnoll", 2, 2, {'provocation': True, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': False, 'represailles':False}, 1, 1),
Carte(1, "Mage noir", 2, 5,{'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': True,'represailles':False }, 3, 2),
Carte(2, "Gobelin", 3, 2,{'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': True,'represailles':False}, 1, 1),
Carte(3, "Loup", 2, 3,{'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': True,'represailles':False}, 2, 1),
Carte(4, "Feu follet", 4, 1,{'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': False,'represailles':False}, 1, 1),
Carte(5, "Garde de la ville", 4, 3,{'provocation': True, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': False,'represailles':False}, 3, 2),
Carte(6, "Assassin", 2, 1,{'provocation': False, 'bouclier divin': False, 'toxicite': True, 'furie des vents': False, 'cri de guerre': False,'represailles':False}, 3, 2),
Carte(7, "Haut prêtre", 5, 4,{'provocation': False, 'bouclier divin': True, 'toxicite': False, 'furie des vents': False, 'cri de guerre': True,'represailles':False}, 3, 3),
Carte(8, "Fantome", 4, 4,{'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': True, 'cri de guerre': False,'represailles':False}, 1, 3),
Carte(9, "Tortue géante", 7, 2,{'provocation': True, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': True,'represailles':False}, 2, 3),
Carte(10, "Dragon sauvage", 6, 7,{'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': False,'represailles':False}, 1, 4),
Carte(11, "Héros", 7, 5,{'provocation': False, 'bouclier divin': True, 'toxicite': False, 'furie des vents': False, 'cri de guerre': True,'represailles':False}, 3, 4),
Carte(12, "Roi démon", 8, 8,{'provocation': True, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': True,'represailles':True}, 1, 4),
Carte(13, "Virus", 1, 1,{'provocation': False, 'bouclier divin': True, 'toxicite': True, 'furie des vents': True, 'cri de guerre': False,'represailles':False}, 0, 4),
Carte(14, "Sanglier", 3, 3, {'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': True, 'cri de guerre': True,'represailles':False}, 2, 3),
Carte(15, "Scorpion", 2, 1, {'provocation': False, 'bouclier divin': False, 'toxicite': True, 'furie des vents': False, 'cri de guerre': False,'represailles':True}, 2, 2),
Carte(16, "T-Rex", 10, 6, {'provocation': True, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': False,'represailles':False}, 2, 4),
Carte(17, "Paysan", 2, 1, {'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': True,'represailles':False}, 3, 1),
Carte(18, "Métamorphe", 1, 1, {'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': True,'represailles':False}, 0, 2),
Carte(19, "Mangouste", 2, 3, {'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': False,'represailles':True}, 2, 2)
]

def UpdateTierList(): #Classe le catalogue dans les tiers lists
    for carte in catalogue:
        try:
            liste_tiers[carte.tier - 1].append(carte)
        except:
            print ("La carte ", carte, " du catalogue appartient a un tier non définis (<1 ou >4)")
            exit(1)


# Affichage classe de liste de cartes

def VisualiserListe(cartes):
    rouge = '\033[91m' #codes couleurs
    vert = '\033[92m'
    jaune = '\033[93m'
    gris = '\033[0m'
    bleu = '\033[34m'
    violet = '\033[35m'
    n = 1
    for carte in cartes:
        name = carte.nom
        name = name[0:16:1]
        print(f"{n} ╔═{name:═<16}╗    ", end = '') #nom de la carte
        n +=1
    print('')
    for carte in cartes: # Affichage générique des effets de cartes stylés
        print("  ║                 ║    ", end ='')
    print('')
    for carte in cartes:
        if carte.effet['provocation']:
            print(f"  ║ {rouge}Provocation{gris}     ║    ",end='')
        else:
            print("  ║                 ║    ",end ='')
    print('')
    for carte in cartes:
        if carte.effet['toxicite']:
            print(f"  ║ {vert}Toxicitée{gris}       ║    ",end='')
        else:
            print("  ║                 ║    ",end ='')
    print('')
    for carte in cartes:
        if carte.effet['bouclier divin']:
            print(f"  ║ {jaune}Bouclier divin{gris}  ║    ",end='')
        else:
            print("  ║                 ║    ",end ='')
    print('')
    for carte in cartes:
        if carte.effet['furie des vents']:
            print(f"  ║ {bleu}Furie des vents{gris} ║    ",end='')
        else:
            print("  ║                 ║    ",end ='')
    print('')
    for carte in cartes:
        if carte.effet['represailles']:
            print(f"  ║ {violet}Représailles{gris}    ║    ",end='')
        else:
            print("  ║                 ║    ",end ='')
    print('')
    for carte in cartes:
        if carte.effet['cri de guerre']:
            print(f"  ║ Cri de guerre : ║    ",end='')
        else:
            print("  ║                 ║    ",end ='')
    print('')

    for carte in cartes: #Affichage générique des cris de guerre stylés des cartes
        if carte.id == 1: #Mage noir
            print("  ║ Humains +1 Atq  ║    ",end='')
        elif carte.id == 2: #Gobelin
            print("  ║ Joueur +1 Or    ║    ",end='')
        elif carte.id == 3: #Loup
            print("  ║ Bêtes +1 Atq    ║    ",end='')
        elif carte.id == 7: #Haut prêtre
            print("  ║ Humains +2 Pv   ║    ",end='')
        elif carte.id == 9: #Tortue Géante
            print("  ║ Tous +2 Pv      ║    ",end='')
        elif carte.id == 11: #Héros
            print("  ║ Hasard Bouclier ║    ",end='')
        elif carte.id == 12: #Roi démon
            print("  ║ Hasard Toxicité ║    ",end='')
        elif carte.id == 14: #Sanglier
            print("  ║ Invoque Sanglier║    ",end='')
        elif carte.id == 17: #Paysans
            print("  ║ Paysans +1/+1   ║    ",end='')
        elif carte.id == 18: #Métamorphe
            print("  ║ Copie gauche    ║    ",end='')
        else:
            print("  ║                 ║    ",end='')
    print('')
    for carte in cartes: #indicateur de la race et stats
        atk = jaune + str(carte.atk_combat) +gris
        pv =  rouge + str(carte.pv_combat) +gris
        if carte.race == 0:
            print(f"  ╚{atk:═<11}═════════════{pv:═>11}╝    ",end='')
        elif carte.race == 1:
            print(f"  ╚{atk:═<11}═══Monstre═══{pv:═>11}╝    ",end='')
        elif carte.race == 2:
            print(f"  ╚{atk:═<11}════Bêtes════{pv:═>11}╝    ",end='')
        elif carte.race == 3:
            print(f"  ╚{atk:═<11}═══Humains═══{pv:═>11}╝    ",end='')
    print('')


#Je garde au cas où
"""
def Visualiser(carte):
    rouge = '\033[91m' #codes couleurs
    vert = '\033[92m'
    jaune = '\033[93m'
    gris = '\033[0m'
    bleu = '\033[34m'
    violet = '\033[35m'

    name = carte.nom
    liste_effets = carte.effet
    atk = jaune + str(carte.atk_combat) + gris
    pv = rouge + str(carte.pv_combat) + gris

    print(f"╔═{name:═<16}╗")
    print("║                 ║")
    if liste_effets['provocation']:
        print(f"║ {rouge}Provocation{gris}     ║")
    else:
        print("║                 ║")

    if liste_effets['toxicite']:

        print(f"║ {vert}Toxicité{gris}        ║")
    else:
        print("║                 ║")

    if liste_effets['bouclier divin']:
        print(f"║ {jaune}Bouclier divin{gris}  ║")
    else:
        print("║                 ║")

    if liste_effets['furie des vents']:
        print(f"║ {bleu}Furie des vents{gris} ║")
    else:
        print("║                 ║")

    if liste_effets['represailles']:
        print(f"║ {violet}Représailles{gris}    ║")
    else:
        print("║                 ║")    

    if liste_effets['cri de guerre']:
        print("║ Cri de guerre : ║")
    else:
        print("║                 ║")

    if carte.id == 1: #Mage noir
        print("║ Humains +1 Atq  ║")
    elif carte.id == 2: #Gobelin
        print("║ Joueur +1 Or    ║")
    elif carte.id == 3: #Loup
        print("║ Bêtes +1 Atq    ║")
    elif carte.id == 7: #Haut prêtre
        print("║ Humains +2 Pv   ║")
    elif carte.id == 9: #Tortue Géante
        print("║ Tous +2 Pv      ║")
    elif carte.id == 11: #Héros
        print("║ Hazard Bouclier ║")
    elif carte.id == 12: #Roi démon
        print("║ Hazard Toxicité ║")
    elif carte.id == 14: #Sanglier
        print("║ Invoque Sanglier║")
    elif carte.id == 17: #Paysans
        print("║ Paysans +1/+1   ║")
    elif carte.id == 19:
        print("║ Copie gauche    ║")

    else:
        print("║                 ║")

    #Indicateur de la Race
    if carte.race == 0:
        print(f"╚{atk:═<11}═════════════{pv:═>11}╝")
    elif carte.race == 1:
        print(f"╚{atk:═<11}═══Monstre═══{pv:═>11}╝")
    elif carte.race == 2:
        print(f"╚{atk:═<11}════Bêtes════{pv:═>11}╝")
    elif carte.race == 3:
        print(f"╚{atk:═<11}═══Humains═══{pv:═>11}╝")
    """
    
        