
class L_systeme :
    
    alphabet = []
    regle = None
    graine = ""
    langage = []
    
    def __init__(self,regle,graine,alphabet):
        self.regle = regle
        self.aphabet = alphabet
        self.graine = graine
        self.langage.append(graine)
        
    def appartiens_a_alphabet(self,caractere):
        return caractere in self.langage
    
    def etendre_langage(self):
        mot = self.langage[-1]
        sortie = ""
        for lettre in mot :
            sortie += regle(lettre)
            
        self.langage.append(sortie)
        
    def renvoyer_mot(self, n):
        if len(self.langage) == n :
            return self.langage[-1]
        self.etendre_langage()
        return self.renvoyer_mot(n)
        
        
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
        
