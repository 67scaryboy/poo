from message import *

def EventHandler(entree, j1, ia1, terrain):
    os.system("cls||clear")
    if entree == 'b': #Boutique
        j1.AffStats()
        ia1.AffStats()

        j1.AffBoutique()
        sortie = j1.ActionBoutique()
        if sortie != 'q':
            EventHandler(entree, j1, ia1, terrain)
    elif entree == 'p': #Poser
        j1.AffStats()
        ia1.AffStats()

        j1.AffPoser()
        sortie = j1.ActionPoser()
        if sortie != 'q':
            EventHandler(entree, j1, ia1, terrain)
    elif entree =='i': #Info
        Info()
        input("--------- appuyez pour passer ---------")

    elif entree == 'c': #Combat
        ia1.Preparation()

        #---- combat ----

        terrain.LancerCombat()

        #---- après le combat ----

        #mise à jour de l'argent
        terrain.MajArgent()

        #mise à jour du prix d'upgrade des boutiques
        terrain.MajBoutique()

        input("--------- appuyez pour passer ---------")

    elif entree == 'v': # Vendre
        j1.AffStats()
        ia1.AffStats()

        j1.AffVendre()
        sortie = j1.ActionVendre()
        if sortie != 'q':
            EventHandler(entree, j1, ia1, terrain)
    elif entree == 'q':
        return False
    
    return True