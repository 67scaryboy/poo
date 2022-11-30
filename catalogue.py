""" A virer dès que plus besoin pour exemple
from enum import Enum

class Enom(Enum):
    GEANT = "Géant"
    MAGE_NOIR = "Mage noir"
    GOBLIN = "Goblin"

class Eatk(Enum):
    GEANT = 3
    MAGE_NOIR = 5
    GOBLIN = 2

class Evie(Enum):
    GEANT = 3
    MAGE_NOIR = 3
    GOBLIN = 2

class Eprix(Enum):
    GEANT = 3
    MAGE_NOIR = 4
    GOBLIN = 2

class Eeffet(Enum):
    GEANT = 3
    MAGE_NOIR = 3
    GOBLIN = 2
"""

# [Nom,Attaque,Vie,Liste d'effet,race,tier]
Cartes= [
    ["Geant",3,3,[True,False,False,False,False],1,1],
    ["Mage noir",5,3,[False,False,False,False,True],1,2]
]
# Liste d'effet:
# [False, False, False, False, True]
# Provocation: non
# Bouclier divin: non
# Toxicité: non
# Furie des vents: non
# Cri de guerre: oui
