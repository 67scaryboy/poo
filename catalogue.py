from enum import Enum
from carte import Carte

class Races(Enum):
    NONDEFINIS=0
    MONSTRES=1
    ANIMEAUX=2
    HUMAINS=3

def UpdateTierList(): #Classe le catalogue dans les tiers lists
    for carte in catalogue:
        tiermob = carte.tier #Recupère et stock le tier du mob
        if tiermob == 1: #Verifie le tier du mob
            liste_tier_1.append(carte) #Ajoute la mob a la liste correspondante a son tier
        elif tiermob == 2:
            liste_tier_2.append(carte)
        elif tiermob == 3:
            liste_tier_3.append(carte)
        elif tiermob == 4:
            liste_tier_4.append(carte)
        else: #En cas d'erreur (tier pas dans l'interval [1,4])
            print ("La carte ", carte, " du catalogue appartient a un tier non définis (<1 ou >4)")
            exit(1)

idcartes = {
    "GEANT": 0, "MAGENOIR": 1, "GOBELIN": 2 ,"LOUP" : 3 , "FEUFOLLET" : 4 , "GARDE" : 5 ,
    "ASSASSIN" : 6 , "PRETRE" : 7 , "FANTOME" : 8 , "TORTUE" : 9 , "DRAGON" : 10 ,
    "HEROS" : 11 , "ROIDEMON" : 12, "VIRUS" : 13
    }

#Listes de cartes par tier

#id, nom, pv, atk, effet, race, tier
catalogue = [
Carte(0, "Geant", 2, 2, {'provocation': True, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': False}, 1, 1),
Carte(1, "Mage noir", 2, 5,{'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': True}, 3, 2),
Carte(2, "Gobelin", 3, 2,{'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': True}, 1, 1),
Carte(3, "Loup", 2, 3,{'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': True}, 2, 1),
Carte(4, "Feu follet", 4, 1,{'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': False}, 1, 1),
Carte(5, "Garde de la ville", 4, 3,{'provocation': True, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': False}, 3, 2),
Carte(6, "Assassin", 2, 1,{'provocation': False, 'bouclier divin': False, 'toxicite': True, 'furie des vents': False, 'cri de guerre': False}, 3, 2),
Carte(7, "Haut prêtre", 5, 4,{'provocation': False, 'bouclier divin': True, 'toxicite': False, 'furie des vents': False, 'cri de guerre': False}, 3, 3),
Carte(8, "Fantome", 4, 4,{'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': True, 'cri de guerre': False}, 1, 3),
Carte(9, "Tortue géante", 7, 2,{'provocation': True, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': True}, 2, 3),
Carte(10, "Dragon sauvage", 6, 7,{'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': False}, 1, 4),
Carte(11, "Héros", 7, 5,{'provocation': False, 'bouclier divin': True, 'toxicite': False, 'furie des vents': False, 'cri de guerre': True}, 3, 4),
Carte(12, "Roi démon", 8, 8,{'provocation': True, 'bouclier divin': False, 'toxicite': False, 'furie des vents': False, 'cri de guerre': True}, 1, 4),
Carte(13, "Virus", 1, 1,{'provocation': False, 'bouclier divin': True, 'toxicite': True, 'furie des vents': True, 'cri de guerre': False}, 0, 4),
Carte(14, "Sanglier", 3, 5, {'provocation': False, 'bouclier divin': False, 'toxicite': False, 'furie des vents': True, 'cri de guerre': True}, 2, 3)
]

# Liste d'effet:
# [False, False, False, False, True]
# Provocation: non
# Bouclier divin: non
# toxicite: non
# Furie des vents: non
# cri de guerre: oui

liste_tier_1 = []
liste_tier_2 = []
liste_tier_3 = []
liste_tier_4 = []
liste_tiers = [liste_tier_1, liste_tier_2, liste_tier_3, liste_tier_4]