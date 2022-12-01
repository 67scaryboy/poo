import carte
from copy import deepcopy

class Main:
    def __init__(self):
        self.__Cartes = []
        self.__NbCartes = 0
        self.__NbCartesMax = 6
    
    def Ajout_carte(self, carte):
        if self.__NbCartes < self.__NbCartesMax:
            self.__Cartes.append(deepcopy(carte))
            self.__NbCartes += 1
    
    def GetNbCartes(self):
        return self.__NbCartes
    
    def GetNbCartesmax(self):
        return self.__NbCartesMax

    def GetCartes(self):
        return self.__Cartes
    
    def GetCartesEnMain(self):
        return self.__Cartes

    def Afficher(self):
        for carte in self.__Cartes:
            carte.Afficher()