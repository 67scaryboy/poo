from message import *

def EventHandler(entree, j1, ia1, terrain):
    if entree == 'b': #Boutique
        j1.AffBoutique()
        j1.ActionBoutique()

    elif entree == 'p': #Poser
        j1.AffPoser()
        j1.ActionPoser()
        
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
        j1.AffVendre()
        j1.ActionVendre()

    elif entree == 'q':
        return False
    
    return True