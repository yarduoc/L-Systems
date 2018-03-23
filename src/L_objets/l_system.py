class Morphisme:
    regle = None
    
    def __init__(self,regle):
        self.regle = regle
        
    def predec(self,mot,k,motif):
        if k == 0:
            return None
        if M[k-1] in self.alphabet:
            return k-1
        if M[k-1] not in ["[","]"]:
            return self.predec(mot,k-1)
        j = k-1
        while M[j] != "[" or M[j-1] not in self.alphabet:
            j -= 1
            if j == 0:
                return None
        if M[j-1] in self.alphabet:
            return j-1
        return self.predec(mot,j-1)
        
    def succ(self,mot,k,motif):
        pass
        
    def appliquer(self,mot):
        
        sortie = []
        for k in range(len(mot)):
            m = self.regle(mot,k,self.predec,self.succ)
            sortie.append(m)
        return sortie
        

class L_systeme :

    alphabet = []
    regle = None
    graine = ""
    langage = []
    
    def __init__(self,regle,graine,alphabet):
        self.regle = regle
        self.alphabet = alphabet
        self.graine = graine
        self.langage.append(graine)
        
    def appartiens_a_alphabet(self,caractere):
        return caractere in self.langage
    
    def etendre_langage(self):
        mot = self.langage[-1]
        
        self.langage.append(regle.appliquer(mot))
        
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
        
        

        
        
