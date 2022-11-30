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
            print ("La carte ", i, " du catalogue appartient a un tier non définis (<1 ou >4)")
            exit(1)

class Nom(Enum):
    GEANT = 0
    MAGE_NOIR = 1
    GOBELIN = 2

#Listes de cartes par tier

#id, nom, pv, atk, effet, race, tier
catalogue = [
Carte(0, "Geant", 3, 3, [True,False,False,False,False], 1, 1),
Carte(1, "Mage noir", 5, 3,[False,False,False,False,True], 1, 1),
Carte(2, "Gobelin", 2, 4,[False,False,False,False,True], 1, 2)
]

liste_tier_1 = []
liste_tier_2 = []
liste_tier_3 = []
liste_tier_4 = []

# Liste d'effet:
# [False, False, False, False, True]
# Provocation: non
# Bouclier divin: non
# Toxicité: non
# Furie des vents: non
# Cri de guerre: oui