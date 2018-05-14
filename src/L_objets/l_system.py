"""def regle(indice,mot,alphabet):
    lettre = mot[indice][0]
    if lettre == 'b' :
        if M.est_predecesseur(mot,indice,'a'):
            return [['c'],['b']]
        if M.est_predecesseur(mot,indice,'aab'):
            return [['c'],['c'],['c']]
        return [['a'],['a'],['a']]
    if lettre == 'a':
        return [['a'],['b']]
    return [mot[indice]]
    
M = Morphisme(regle,['a','b'])

L = L_systeme(M,[['a',0]],['a','b'])"""





class Morphisme:
    regle = None
    alphabet = None
    def __init__(self,regle,alphabet):
        self.regle = regle
        self.alphabet = alphabet
        
    def skip_dyck(self,mot,indice):
        compteur_dyck = -1
        for k in range(indice-1,-1,-1):
            if compteur_dyck == 0:
                return k+1
            if mot[k][0] == "[" or mot[k][0] == "]":
                compteur_dyck += (-1)**(mot[k][0] == "]")
        return "Impossible"
    
    def indice_predec(self, mot, indice):
        if indice == 0:
            return "Impossible"
        if mot[indice - 1][0] in self.alphabet:
            return indice - 1
        elif mot[indice - 1][0] == "]":
            j = self.skip_dyck(mot,indice - 1)
            if j == "impossible" :
                return "impossible"
            return self.indice_predec(mot, j)
        else:
            return self.indice_predec(mot, indice - 1)
            
            
    def est_predecesseur(self, mot,indice, motif):
        if motif == "" :
            return True
        
        nouvel_indice = self.indice_predec(mot,indice)
        
        if nouvel_indice == "Impossible" :
            return False
        if mot[nouvel_indice][0] != motif[-1] :
            return False
        return self.est_predecesseur(mot,nouvel_indice, motif[:-1:])
        
    def succ(self,mot,k,motif):
        pass
        
    def appliquer(self,mot):
        
        sortie = []
        for k in range(len(mot)):
            
            m = self.regle(k,mot,self.alphabet)
            
            sortie += m

        return sortie


class L_systeme :

    alphabet = []
    morphism = None
    graine = None
    langage = []
    
    def __init__(self,morphism,graine,alphabet):
        self.morphism = morphism
        self.alphabet = alphabet
        self.graine = graine
        self.langage.append(graine)
        
    def appartiens_a_alphabet(self,caractere):
        return caractere in self.langage
    
    def etendre_langage(self):
        mot = self.langage[-1]
        
        self.langage.append(self.morphism.appliquer(mot))
        
    def renvoyer_mot(self, n):
        
        if len(self.langage) > n :
            
            return self.langage[n]
            
        self.etendre_langage()
        return self.renvoyer_mot(n)
    

    
class Interpretation_geometrique:
    
    regle_affichage = None
    L_system = None
    
    def __init__(self , regle_affichage , L_system):
        self.regle_affichage = regle_affichage
        self.L_system = L_system
    
    
    def tracer(self,n):
        
        
        mot = self.L_system.renvoyer_mot(n)
        self.regle_affichage(mot)
