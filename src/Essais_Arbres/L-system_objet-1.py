class Noeud:
    
    nom = ""
    parent = None
    enfants = []
    info = ""
    
    def __init__(self , nom , parent , info):
        self.nom = nom
        self.parent = parent
        self.info = info
        self.enfants = []
        parent.enfants.append(self)
    
    
class Arbre:
    
    L_system = None
    mot = ""
    Noeuds = []
    
    def __init__(self , L_system , mot):
        self.mot = mot
        self.Noeuds.append(Noeud(mot[0],None,""))
        for i in range(1,len(mot)):
            self.Noeuds.append(Noeud(mot[i],predec(mot,i,L_system),""))

class Affichage:
    
    regle_affichage = None
    L_system = None
    
    def __init__(self , regle_affichage , L_system):
        self.regle_affichage = regle_affichage
        self.L_system = L_system
    
    
    def afficher(self,n):
        t = turlte3D
        graine = self.L_system.graine
        mot = self.L_sysem.renvoie_mot(n)
        self.regle_affichage(graine , mot , n)
        
    