from enum import Enum
from carte import Carte

def UpdateTierList(): #Classe le catalogue dans les tiers lists
    for carte in catalogue:
        tiermob = carte.GetTier() #Recupère et stock le tier du mob
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

class Races(Enum):
    NONDEFINIS=0
    MONSTRES=1
    ANIMEAUX=2
    HUMAINS=3

idcartes = {
    "GEANT": 0, "MAGENOIR": 1, "GOBELIN": 2 ,"LOUP" : 3 , "FEUFOLLET" : 4 , "GARDE" : 5 ,
    "ASSASSIN" : 6 , "PRETRE" : 7 , "FANTOME" : 8 , "TORTUE" : 9 , "DRAGON" : 10 ,
    "HEROS" : 11 , "ROIDEMON" : 12, "VIRUS" : 13
    }

#Listes de cartes par tier

#id, nom, pv, atk, effet, race, tier
catalogue = [
Carte(0, "Geant", 2, 2, [True,False,False,False,False], 1, 1),
Carte(1, "Mage noir", 2, 5,[False,False,False,False,True], 3, 2), #cri de guerre
Carte(2, "Gobelin", 3, 2,[False,False,False,False,True], 1, 1), #cri de guerre
Carte(3, "Loup", 2, 3,[False,False,False,False,False], 2, 1),
Carte(4, "Feu follet", 4, 1,[False,False,False,False,False], 1, 1),
Carte(5, "Garde de la ville", 4, 3,[True,False,False,False,False], 3, 2),
Carte(6, "Assassin", 2, 1,[False,False,True,False,False], 3, 2),
Carte(7, "Haut prêtre", 5, 4,[False,True,False,False,False], 3, 3),
Carte(8, "Fantome", 4, 4,[False,False,False,True,False], 1, 3),
Carte(9, "Tortue géante", 7, 2,[True,False,False,False,True], 2, 3), #cri de guerre
Carte(10, "Dragon sauvage", 6, 7,[False,False,False,False,False], 1, 4),
Carte(11, "Héros", 7, 5,[False,True,False,False,True], 3, 4), #cri de guerre
Carte(12, "Roi démon", 8, 8,[True,False,False,False,True], 1, 4), #cri de guerre
Carte(13, "Virus", 1, 1,[False,True,True,True,False], 0, 4),
Carte(14, "Sanglier", 3, 5, [False,False,False,True,True], 2, 3) #cri de guerre
]
# Liste d'effet:
# [False, False, False, False, True]
# Provocation: non
# Bouclier divin: non
# Toxicité: non
# Furie des vents: non
# Cri de guerre: oui

liste_tier_1 = []
liste_tier_2 = []
liste_tier_3 = []
liste_tier_4 = []