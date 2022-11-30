import pygame, sys, random
from pygame.locals import *

class Cartes(pygame.sprite.Sprite):
    def __init__(self,pvmax,atk,prix,effet,race,tier,position):
        super().__init__()
        self.image = pygame.image.load("sprites/e3.png") #A modifier au moment de l'interface graphique
        self.PVMAX=pvmax #PV max de base
        self.PV=pvmax #PV du personnage.
        self.ATK=atk #Attaque du perso
        self.PRIX=prix #Prix d'achat en or
        self.EFFET=effet #Effet particulier
        self.RACE=race #Race
        self.TIER=tier #Tier de la boutique dans lequel il est achetable
        self.POSITION=position #Position pour affichage: 0=dans la boutique, 1= en main, 2=sur le terrain

    def Attaque(self, adversaire): #Fait attaquer cette carte
        adversaire.PV-=self.ATK #L'adversaire prend les dégats
        self.PV-=adversaire.ATK #L'attaquant prend les dégats aussi

    def Meurt(self): #Fait mourir la carte (La retire du terain)
        if self.PV<1:
            #A faire
    
    def Vendre(self,main):
        main.OR+=1
        self.Meurt()

    def Poser(self):
        #A faire

class Main(pygame.sprite.Sprite):
    def __init__(self,cartesdispo,ormax,thune): # cartesdispo est une liste d'objets "Cartes",    
        super().__init__()
        self.image = pygame.image.load("sprites/e3.png")
        self.NBCARTES= len(cartesdispo)
        self.ORMAX = ormax #Or max possible d'avoir dans la main
        self.OR = thune #Or possédé
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
        