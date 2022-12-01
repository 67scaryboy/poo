import carte

class Main:
    def __init__(self):
        self.__cartes_en_main = []
        self.__nb_cartes = 0
        self.__nb_cartes_max = 6
    
    def Ajout_carte(self, carte):
        if self.__nb_cartes < self.__nb_cartes_max:
            self.__cartes_en_main.append(carte)
            self.__nb_cartes += 1
    
    def GetNbCartes(self):
        return self.__nb_cartes
    
    def GetNbCartesmax(self):
        return self.__nb_cartes_max

    def GetCartesEnMain(self):
        return self.__cartes_en_main