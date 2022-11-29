import pygame, sys, random
from pygame.locals import *

class Cartes(pygame.sprite.Sprite):
    def __init__(self): #Ajouter les paramètres ici. Plusieurs init possible -> Constructeur
        super().__init__()
        self.image = pygame.image.load("sprites/e3.png") #A modifier au moment de l'interface graphique
        self.PV=0 #PV du personnage. Pas maxé, on peut les monter au besoin (soins, boost ...)
        self.ATK=0 #Attaque du perso
        self.PRIX=0 #Prix d'achat en or
        self.EFFET=0 #Effet particulier
        self.RACE=0 #Race
        self.TIER=0 #Tier de la boutique dans lequel il est achetable
        self.POSITION=0 #Position pour affichage: 0=dans la boutique, 1= en main, 2=sur le terrain

    def Attaque(self, adversaire): #Fait attaquer cette carte
        adversaire.PV-=self.ATK #L'adversaire prend les dégats
        self.PV-=adversaire.ATK #L'attaquant prend les dégats aussi

    def Meurt(self) #Fait mourir la carte (La retire du terain)
        if self.PV<1:
            #A faire
    
    def Vendre(self,main):
        main.OR+=1
        self.Meurt()

    def Poser(self):
        #A faire

class Main(pygame.sprite.Sprite):
    def __init__(self,cartesdispo,ormax,or): # cartesdispo est une liste d'objets "Cartes",    
        super().__init__()
        self.image = pygame.image.load("sprites/e3.png")
        self.NBCARTES= len(cartesdispo)
        self.ORMAX = ormax #Or max possible d'avoir dans la main
        self.OR = or #Or possédé
        self.CARTESDISPO = cartesdispo #Liste d'objet "cartes"

class Terrain(pygame.sprite.Sprite):
    def __init__(self,cartesposesp1,cartesposesp2):
        super().__init__()
        self.image = pygame.image.load("sprites/e3.png")
        self.MOBP1= cartesposesp1 #Liste de carte
        self.MOBP2 = cartesposesp2 #Liste de carte
        self.NBMOBP1 = len(cartesposesp1)
        self.NBMOBP2 = len(cartesposesp2)

    def TourSuivant():
        #A faire

class Boutique(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        