import Ccarte

class Main:
    def __init__(self,cartesdispo,ormax,thune): # cartesdispo est une liste d'objets "Cartes",
        self.NBCARTES= len(cartesdispo)
        self.ORMAX = ormax #Or max possible d'avoir dans la main
        self.OR = thune #Or possédé
        self.CARTESDISPO = cartesdispo #Liste d'objet "cartes"