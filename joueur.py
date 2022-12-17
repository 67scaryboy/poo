import carte, boutique, main, catalogue
from time import sleep
from message import *

class Joueur:
    def __init__(self, argent_max, argent, pseudo):
        self._pv_max = 20
        self._pv = self._pv_max
        self._main = main.Main() #Main du joueur
        self._argent_max = argent_max #Pièces max disponibles (dépassable, uniquement pour le compte des tours)
        self._argent = argent #Pièces disponibles
        self._pseudo = pseudo #Nom du joueur
        self._boutique = boutique.Boutique() #Boutique (propre au joueur)
        self._combatants = [] #Cartes posées
        self._num_attaquant = 0 #Index du combatant en train d'attaquer (utile pour le combat)

    #Geteurs et Seteurs---------------------------------------------------------------------

    def SetNumAttaquant(self, valeur):
        self._num_attaquant = valeur
    
    def GetNumAttaquant(self):
        return self._num_attaquant

    num_attaquant = property(GetNumAttaquant, SetNumAttaquant)

    def SetArgentMax(self, valeur):
        self._argent_max = valeur
    
    def GetArgentMax(self):
        return self._argent_max

    argent_max = property(GetArgentMax, SetArgentMax)

    def SetArgent(self, valeur):
        self._argent = valeur

    def GetArgent(self):
        return self._argent

    argent = property(GetArgent, SetArgent)

    def GetBoutique(self):
        return self._boutique

    boutique = property(GetBoutique)

    def GetMain(self):
        return self._main

    main = property(GetMain)
    
    def GetCombatants(self):
        return self._combatants

    combatants = property(GetCombatants)
    
    def GetPV(self):
        return self._pv
    
    def SetPV(self, nouveaux_pv):
        self._pv = nouveaux_pv

    pv = property(GetPV, SetPV)

    def GetPVMax(self):
        return self._pv_max

    def SetPVMax(self, nouveaux_pv_max):
        self._pv_max = nouveaux_pv_max

    pv_max = property(GetPVMax, SetPVMax)

    def GetPseudo(self):
        return self._pseudo

    pseudo = property(GetPseudo)

    #Méthodes---------------------------------------------------------------------------------------------------------

    def Acheter(self, numcarte): #Acheter une carte
        cartes_boutiques = self.boutique.cartes
        if (self.argent >= 3) and (len(self.main.cartes) < self.main.nb_cartes_max): #Si assez d'argent et de la place en main
            self.argent -= 3
            self.main.Ajout_carte(cartes_boutiques[numcarte-1])
            self.boutique.DelCartes(numcarte)

        elif (len(self.main.cartes) == self.main.nb_cartes_max):
            aff_msg("Opération impossible, main pleine (6 cartes maximum !")
            sleep(1) #voir un input

        elif (self.argent <= 3):
            aff_msg("Opération impossible, argent insuffisant (3 pour un achat !)")
            sleep(1) #meme chose

    def UpBoutique(self): #Amélioration de la boutique
        if self.argent >= self.boutique.prix_upgrade and self.boutique.tier < self.boutique.tier_max - 1:
            self.argent -= self.boutique.prix_upgrade
            self.boutique.Ameliorer()
            self.boutique.Rafraichir()
        else:
            aff_msg("Opération impossible")
    
    def RafraichirBoutique(self):  #Rafraichissement de la boutique
        if self.argent > 0:
            self.boutique.Rafraichir()
            self.argent -= 1
        else:
            aff_msg("Opération impossible")

    
    def PoserCarte(self,numcarte): #PAsser une carte de la main aux combattant
        if numcarte > len(self.main.cartes) or numcarte <= 0:
            aff_msg ("La carte que tu essaie de poser n'existe pas")

        elif len(self.combatants) == 4:
            aff_msg("Opération impossible, nombre maximum de sbire atteint (4 max !)")
        
        else:
            self.main.cartes[numcarte-1].CriDeGuerre(self) #lancer le cri de guerre 
            self.combatants.append(self.main.cartes[numcarte-1]) #Ajoute à la droite des éléments placés sur le terain la carte choisie
            del self.main.cartes[numcarte-1] #Retire la carte choisie de la main
    
    def VendreCarte(self, numcarte): #Vendre une carte depuis le terrain
        if numcarte > len(self.combatants):
            aff_msg ("La carte que tu essaie de poser n'existe pas")
            sleep(1)
            exit(2)
        del self.combatants[numcarte - 1]
        self.argent = self.argent + 1

    def ActionBoutique(self): 
        entree = input()

        #achat de carte avec son numéro
        try:
            nb = int(entree)
        except:
            if entree == 'r':
                self.RafraichirBoutique()
            elif entree == 'u':
                self.UpBoutique()
        else:
            if nb in range (1, len(self.boutique.cartes) + 1):
                self.Acheter(nb)
        return entree

    def ActionPoser(self):
        entree = input()

        try:
            nb = int(entree)
        except:
            pass
        else:
            self.PoserCarte(nb)
        return entree

    def ActionVendre(self):
        entree = input()

        try:
            nb = int(entree)
        except:
            pass
        else:
            if nb > 0 and len(self.combatants) > nb - 1:
                self.VendreCarte(nb)
        return entree
    
    #Méthodes liées à l'affichage---------------------------------------------------------------------------------------------

    def AffPoser(self):
        print ("Choisissez le numéro de la carte que vous souhaitez poser, ou tapez autre chose pour quitter\n\n")

        print("Les cartes dans votre main:\n")
        catalogue.VisualiserListe(self.main.cartes)

        print ("\nVos cartes sur le terrain:\n")
        catalogue.VisualiserListe(self.combatants)
            

    def AffCombatants(self): #Fonction affichage combatants
        print(f"    Combatants {self.pseudo}:")
        catalogue.VisualiserListe(self.combatants)

    def AffBoutique(self): #Fonction affichage boutique
        print(f"    Boutique tier {self.boutique.tier} {self.pseudo} ({self.boutique.prix_upgrade} pour upgrade)")
        print('')
        catalogue.VisualiserListe(self.boutique.cartes)
        print('')
        print("Vous pouvez quitter la boutique en tappant 'q', l'upgrade avec 'u', la rafraichir avec 'r' ou acheter une carte en entrant son numéro")
        
    
    def AffMain(self): #Fonction affichage main
        print(f"    Main {self.pseudo}:")
        print("    ", end="")
        catalogue.VisualiserListe(self.main.cartes)
        print('\n')

    def AffVendre(self): #Fonction affichage menu vente
        print ("Choisissez le numéro de la carte que vous souhaitez vendre, ou tapez autre chose pour quitter\n\n")
        print("Les cartes dans votre main:\n")
        catalogue.VisualiserListe(self.main.cartes)
        print ("\nVos cartes sur le terrain:\n")
        catalogue.VisualiserListe(self.combatants)
    
    def AffStats(self): #Fonction affichage stats personnages
        print(f"{self.pseudo}({self.pv}/{self.pv_max}) argent:{self.argent}/{self.argent_max}\n")