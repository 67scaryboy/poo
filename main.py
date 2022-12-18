import carte
from copy import deepcopy

class Main:
    def __init__(self):
        self.__Cartes = []
        self.__NbCartesMax = 6
    
    #Geteurs et Seteurs-----------------------------------------------------------------------------
    
    def GetNbCartesmax(self):
        return self.__NbCartesMax

    nb_cartes_max = property(GetNbCartesmax)

    def GetCartes(self):
        return self.__Cartes
    
    cartes = property(GetCartes)

    #Méthodes----------------------------------------------------------------------------------------

    def Ajout_carte(self, carte):
        if len(self.cartes) < self.__NbCartesMax:
            self.__Cartes.append(deepcopy(carte)) #Ajout une copie de la carte (sinon c'est la vraie carte et on la modifie)