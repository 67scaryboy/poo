import pygame, sys, random
from pygame.locals import *

class Cartes(pygame.sprite.Sprite):
    def __init__(self,p_pvmax,p_atk,p_prix,p_effet,p_race,p_tier,p_position):
        super().__init__()
        self.image = pygame.image.load("sprites/e3.png") #A modifier au moment de l'interface graphique
        self.PVMAX=p_pvmax #PV max de base
        self.PV=p_pvmax #PV du personnage.
        self.ATK=p_atk #Attaque du perso
        self.PRIX=p_prix #Prix d'achat en or
        self.EFFET=p_effet #Effet particulier
        self.RACE=p_race #Race
        self.TIER=p_tier #Tier de la boutique dans lequel il est achetable
        self.POSITION=p_position #Position pour affichage: 0=dans la boutique, 1= en main, 2=sur le terrain

    def Attaque(self, p_adversaire): #Fait attaquer cette carte
        p_adversaire.PV-=self.ATK #L'adversaire prend les dégats
        self.PV-=p_adversaire.ATK #L'attaquant prend les dégats aussi

    def Meurt(self): #Fait mourir la carte (La retire du terain)
        if self.PV<1:
            #A faire
    
    def Vendre(self,main):
        main.OR+=1
        self.Meurt()

    def Poser(self):
        #A faire

class Main:
    def __init__(self,cartesdispo,ormax,thune): # cartesdispo est une liste d'objets "Cartes",
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

class Boutique:
    def __init__(self):
        