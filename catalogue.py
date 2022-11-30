from enum import Enum
from carte import Carte

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

print(catalogue[Nom.GEANT.value].nom)

# Liste d'effet:
# [False, False, False, False, True]
# Provocation: non
# Bouclier divin: non
# Toxicité: non
# Furie des vents: non
# Cri de guerre: oui
