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

    def GetBoutique(self):
        return self.__boutique
    
    def GetCombatants(self):
        return self.__combatants
    
    def GetPV(self):
        return self.__pv
    
    def SetPV(self, nouveauxpv):
        self.__pv = nouveauxpv

    def Acheter(self, carte):
        cartes_boutiques = boutique.Boutique.get_cartes(self.__boutique)
        if carte in cartes_boutiques:
            if (self.__argent >= 3) and (main.Main.get_nb_cartes(self.__main) < main.Main.get_nb_cartesmax(self.__main)):
                self.__argent -= 3
                main.Main.ajout_carte(self.__main, carte)
            else:
                print("Opération impossible")

    def AffStats(self):
        print(f"{self.__pseudo}: {self.__pv}/{self.__pv_max}     argent:{self.__argent}/{self.__argent_max}")

    def UpBoutique(self):
        if self.__boutique.__tier < 5 and self.__argent > self.__boutique.__prixupgrade:
            self.__argent-= self.__boutique.__prixupgrade
            self.__boutique.__tier +=1
            # Ajouter la fonction "afficher jeu"
    
    def RafraichirBoutique(self):
        if self.__argent > 1:
            self.__boutique.Rafraichir()
            self.__argent -= 1
            # Ajouter la fonction "affichage jeu"
    
    def PoserCarte(self,numcarte):
        if numcarte > self.__main.__nb_cartes:
            print ("La carte que tu essaie de poser n'existe pas")
            exit(2)
        self.__combatants.append(self.__main.__cartes_en_main[numcarte-1]) #Ajoute à la droite des éléments placés sur le terain la carte choisie
        del self.__main.__cartes_en_main[numcarte-1] #Retire la carte choisie de la main