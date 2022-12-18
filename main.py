import carte
from copy import deepcopy

class Main:
    def __init__(self):
        self.__Cartes = []      #Liste des cartes dans la main
        self.__NbCartesMax = 6  #Nombre maximum possible de cartes dans la main
    
    #Geteurs et Seteurs-----------------------------------------------------------------------------
    
    def GetNbCartesmax(self):
        """Getter de __NbCartesMax"""

        return self.__NbCartesMax

    nb_cartes_max = property(GetNbCartesmax)

    def GetCartes(self):
        """Getter de __Cartes"""

        return self.__Cartes
    
    cartes = property(GetCartes)

    #Méthodes----------------------------------------------------------------------------------------

    def Ajout_carte(self, carte):
        """Ajout d"une carte à la main"""

        if len(self.cartes) < self.__NbCartesMax:
            self.__Cartes.append(deepcopy(carte)) #On la copie pour ne pas modifier la vraie entre les combats