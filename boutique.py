import carte, random, catalogue

class Boutique:
    def __init__(self):
        self.__tier = 1 #le tier maximal des cartes dans la taverne
        self.__tier_max = 5 #le tier maximal de la boutique
        self.__prix_upgrade = 5 #le prix pour monter le niveau de la taverne
        self.__cartes = [] #les cartes disponibles à l'achat
        self.__prix_refresh = 1
    
    #Getteurs et setteurs-------------------------------------------------------------------------------

    def GetPrixRefresh(self):
        return self.__prix_refresh

    prix_refresh = property(GetPrixRefresh)

    def GetCartes(self):
        return self.__cartes
    
    def SetCartes(self, cartes):
        self.__cartes = cartes

    cartes = property(GetCartes, SetCartes)

    def GetPrixUpgrade(self):
        return self.__prix_upgrade

    def SetPrixUpgrade(self, prix):
        if prix > 0 and prix < 6:
            self.__prix_upgrade = prix
    
    prix_upgrade = property(GetPrixUpgrade, SetPrixUpgrade)

    def GetTier(self):
        return self.__tier

    def SetTier(self, nb):
        if nb > 1 and nb < self.tier_max:
            self.__tier = nb

    tier = property(GetTier, SetTier)

    def GetTierMax(self):
        return self.__tier_max

    tier_max = property(GetTierMax)

    #Méthodes------------------------------------------------------------------------------------------
    
    def DelCartes(self,numcarte): #Retire une carte de la boutique en fonction de sa position
        del self.__cartes[numcarte-1]

    def Rafraichir(self): #Changer les cartes proposées en boutique
        self.__cartes = []

        for i in range (5):
            #randomisation du tier de la carte à tirer
            temp = random.randint(0,self.__tier - 1)

            #choix aléatoire de la carte du tier donné
            self.__cartes.append(catalogue.liste_tiers[temp][random.randint(0,len(catalogue.liste_tiers[temp])-1)])
    
    def Ameliorer(self): #Fonction amélioration appelée par le joueur
        self.tier += 1
        self.prix_upgrade = 5
    
    #Méthodes Liées à l'Affichage------------------------------------------------------------------------------------------

    def VisualiserBoutique(self):
        rouge = '\033[91m' #codes couleurs
        vert = '\033[92m'
        jaune = '\033[93m'
        gris = '\033[0m'
        bleu = '\033[34m'
        violet = '\033[35m'

        n = 1
        for carte in self.__cartes:
            name = carte.nom
            print(f"{n} ╔═{name:═<16}╗    ", end = '') #nom de la carte
            n +=1
        print('')
        for carte in self.__cartes:
            print("  ║                 ║    ", end ='')
        print('')
        for carte in self.__cartes:
            if carte.effet['provocation']:
                print(f"  ║ {rouge}Provocation{gris}     ║    ",end='')
            else:
                print("  ║                 ║    ",end ='')
        print('')
        for carte in self.__cartes:
            if carte.effet['toxicite']:
                print(f"  ║ {vert}Toxicitée{gris}       ║    ",end='')
            else:
                print("  ║                 ║    ",end ='')
        print('')
        for carte in self.__cartes:
            if carte.effet['bouclier divin']:
                print(f"  ║ {jaune}Bouclier divin{gris}  ║    ",end='')
            else:
                print("  ║                 ║    ",end ='')
        print('')
        for carte in self.__cartes:
            if carte.effet['furie des vents']:
                print(f"  ║ {bleu}Furie des vents{gris} ║    ",end='')
            else:
                print("  ║                 ║    ",end ='')
        print('')
        for carte in self.__cartes:
            if carte.effet['represailles']:
                print(f"  ║ {violet}Représailles{gris}    ║    ",end='')
            else:
                print("  ║                 ║    ",end ='')
        print('')
        for carte in self.__cartes:
            if carte.effet['cri de guerre']:
                print(f"  ║ Cri de guerre : ║    ",end='')
            else:
                print("  ║                 ║    ",end ='')
        print('')

        for carte in self.__cartes:
            if carte.id == 1: #Mage noir
                print("  ║ Humains +1 Atq  ║    ",end='')
            elif carte.id == 2: #Gobelin
              print("  ║ Joueur +1 Or    ║    ",end='')
            elif carte.id == 3: #Loup
              print("  ║ Bêtes +1 Atq    ║    ",end='')
            elif carte.id == 7: #Haut prêtre
                print("  ║ Humains +2 Pv   ║    ",end='')
            elif carte.id == 9: #Tortue Géante
                print("  ║ Tous +2 Pv      ║    ",end='')
            elif carte.id == 11: #Héros
                print("  ║ Hazard Bouclier ║    ",end='')
            elif carte.id == 12: #Roi démon
                print("  ║ Hazard Toxicité ║    ",end='')
            elif carte.id == 14: #Sanglier
                print("  ║ Invoque Sanglier║    ",enf='')
            elif carte.id == 17: #Paysans
                print("  ║ Paysans +1/+1   ║    ",end='')
            elif carte.id == 19: #Métamorphe
                print("  ║ Copie gauche    ║    ",end='')

            else:
                print("  ║                 ║    ",end='')
        print('')
        for carte in self.__cartes: #indicateur de la race et stats
            atk = jaune + str(carte.atk_combat) +gris
            pv =  rouge + str(carte.pv_combat) +gris
            if carte.race == 0:
                print(f"  ╚{atk:═<11}═════════════{pv:═>11}╝    ",end='')
            elif carte.race == 1:
                print(f"  ╚{atk:═<11}═══Monstre═══{pv:═>11}╝    ",end='')
            elif carte.race == 2:
                print(f"  ╚{atk:═<11}════Bêtes════{pv:═>11}╝    ",end='')
            elif carte.race == 3:
                print(f"  ╚{atk:═<11}═══Humains═══{pv:═>11}╝    ",end='')
        print('')