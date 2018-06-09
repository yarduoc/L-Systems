import os
os.chdir("C:\\GitHub\\L-Systems\\src\\L_objets")
from morphisme import *



class L_systeme :
    
    """ 
        Cette classe permet de créer des L_systèmes
        
        alphabet est une liste de caractères
        morphism est de la classe Morphisme
        graine est une liste de lettre (une lettre étant une liste de caractère et de paramètres)
        langage est une liste de mots
    """
    
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
        
        """
            Vérifie qu'un caractère appartient à l'alphabet
        """
        
        return (caractere in self.langage)
    
    def etendre_langage(self):
        
        """
            Ajoute au langage l'image de son dernier mot par le morphisme
        """
        
        mot = self.langage[-1]
        
        self.langage.append(self.morphism.appliquer(mot))
        
    def renvoyer_mot(self, n):
        
        """
            Renvoie le mot issu de n itérations du morphisme sur la graine
            
            n est un entier
        """
        
        if len(self.langage) > n :
            
            return self.langage[n]
            
        self.etendre_langage()
        return self.renvoyer_mot(n)