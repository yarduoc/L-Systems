
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
        sortie = ""
        for lettre in mot :
            sortie += self.regle(lettre)
            
        self.langage.append(sortie)
        
    def renvoyer_mot(self, n):
        if len(self.langage) > n :
            return self.langage[n]
        self.etendre_langage()
        return self.renvoyer_mot(n)
    
    def predec(self,M,k):
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
    
class Affichage:
    
    regle_affichage = None
    L_system = None
    
    def __init__(self , regle_affichage , L_system):
        self.regle_affichage = regle_affichage
        self.L_system = L_system
    
    
    def afficher(self,n):
        
        
        mot = self.L_system.renvoyer_mot(n)
        self.regle_affichage(mot)
        
        

        
