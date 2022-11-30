import carte

class Main:
    def __init__(self):
        self.__nb_cartes = 0
        self.__nb_cartes_max = 6
        self.__cartes_dispo = []
    
    def ajout_carte(self, carte):
        if self.__nb_cartes < self.__nb_cartes_max:
            self.__cartes_dispo.append(carte)
            self.__nb_cartes += 1
    
    def get_nb_cartes(self):
        return self.__nb_cartes
    
    def get_nb_cartesmax(self):
        return self.__nb_cartes_max