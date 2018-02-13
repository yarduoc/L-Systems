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

    
