import carte, boutique, main

class Joueur:
    def __init__(self, argent_max, argent, pseudo):
        self.__pv_max = 20
        self.__pv = self.__pv_max
        self.__main = main.Main() #Main du joueur
        self.__argent_max = argent_max #Pièces max disponibles (dépassable, uniquement pour le compte des tours)
        self.__argent = argent #Pièces disponibles
        self.__pseudo = pseudo #Nom du joueur
        self.__boutique = boutique.Boutique() #Boutique (propre au joueur)
        self.__combatants = [] #Cartes posées

    #Geteurs et Seteurs---------------------------------------------------------------------

    def SetArgentMax(self, valeur):
        self.__argent_max = valeur
    
    def GetArgentMax(self):
        return self.__argent_max

    argent_max = property(GetArgentMax, SetArgentMax)

    def SetArgent(self, valeur):
        self.__argent = valeur

    def GetArgent(self):
        return self.__argent

    argent = property(GetArgent, SetArgent)

    def GetBoutique(self):
        return self.__boutique

    boutique = property(GetBoutique)

    def GetMain(self):
        return self.__main

    main = property(GetMain)
    
    def GetCombatants(self):
        return self.__combatants

    combatants = property(GetCombatants)
    
    def GetPV(self):
        return self.__pv
    
    def SetPV(self, nouveauxpv):
        self.__pv = nouveauxpv

    pv = property(GetPV, SetPV)

    #Méthodes---------------------------------------------------------------------------------------------------------

    def Acheter(self, numcarte):
        cartes_boutiques = self.__boutique.cartes
        if (self.__argent >= 3) and (main.Main.GetNbCartes(self.__main) < main.Main.GetNbCartesmax(self.__main)):
            self.__argent -= 3
            self.__main.Ajout_carte(cartes_boutiques[numcarte-1])
            self.__boutique.DelCartes(numcarte)
        else:
            print("Opération impossible")

    def UpBoutique(self):
        if self.__argent >= self.boutique.prix_upgrade and self.boutique.tier < self.boutique.tier_max:
            self.__argent -= self.boutique.prix_upgrade
            self.boutique.Ameliorer()
            self.__boutique.Rafraichir()
        else:
            print("Opération impossible")
            # Ajouter la fonction "afficher jeu"
    
    def RafraichirBoutique(self):
        if self.__argent > 0:
            self.__boutique.Rafraichir()
            self.__argent -= 1
        else:
            print("Opération impossible")
            # Ajouter la fonction "affichage jeu"
    
    def PoserCarte(self,numcarte):
        if numcarte > self.main.nb_cartes:
            print ("La carte que tu essaie de poser n'existe pas")
            exit(2)
        self.main.cartes[numcarte-1].CriDeGuerre(self) #lancer le cri de guerre 
        self.combatants.append(self.main.cartes[numcarte-1]) #Ajoute à la droite des éléments placés sur le terain la carte choisie
        del self.main.cartes[numcarte-1] #Retire la carte choisie de la main
    
    def VendreCarte(self, numcarte):
        if numcarte > len(self.combatants):
            print ("La carte que tu essaie de poser n'existe pas")
            exit(2)
        del self.combatants[numcarte - 1]
        self.argent = self.argent + 1

    def ActionBoutique(self):
        entree = input()

        #achat de carte avec son numéro
        try:
            nb = int(entree)
        except:
            if entree == "Rafraichir":
                self.RafraichirBoutique()
            elif entree == "Upgrade":
                self.UpBoutique()
        else:
            if nb in range (1, len(self.boutique.cartes) + 1):
                self.Acheter(nb)

    def ActionPoser(self):
        entree = input()

        try:
            nb = int(entree)
        except:
            pass
        else:
            self.PoserCarte(nb)
    
    #Méthodes liées à l'affichage---------------------------------------------------------------------------------------------

    def AffPoser(self):
        print ("Choisissez le numéro de la carte que vous souhaitez poser, ou tapez autre chose pour quitter\n\n")
        print("Les cartes dans votre main:\n")
        self.main.Afficher()
        print ("\nVos cartes sur le terrain:\n")
        for carte in self.combatants:
            carte.Afficher()

    def AffCombatants(self):
        print(f"    Combatants {self.__pseudo}:")
        print("    ", end="")
        for carte in self.__combatants:
            carte.Afficher()
        print('\n')

    def AffBoutique(self):
        print(f"    Boutique tier {self.boutique.tier} {self.__pseudo} ({self.boutique.prix_upgrade} pour upgrade)")
        print("    ", end="")
        for carte in self.__boutique.cartes:
            carte.Afficher()
        print('\n')
        print("Vous pouvez quitter la boutique en tappant 'Quitter', l'upgrade avec 'Upgrade', la rafraichir avec 'Rafraichir' ou acheter une carte en entrant son numéro")

    def AffMain(self):
        print(f"    Main {self.__pseudo}:")
        print("    ", end="")
        for carte in self.__main.cartes:
            carte.Afficher()
        print('\n')
    
    def AffStats(self):
        print(f"{self.__pseudo}({self.__pv}/{self.__pv_max}) argent:{self.__argent}/{self.__argent_max}\n")