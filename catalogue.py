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