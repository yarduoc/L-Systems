import os
os.chdir("C:\\GitHub\\L-Systems\\src\\L_objets")
from l_system import *

class Interpretation_geometrique:
    
    """
        Cet objet s'occupe de l'interprétation géométrique des mots
        
        regle_affichage est une fonction qui transcrit chaque lettre en instruction de la turtle3D
        
        L_system est un L_système 
    """
    
    regle_affichage = None
    L_system = None
    
    def __init__(self , regle_affichage , L_system):
        self.regle_affichage = regle_affichage
        self.L_system = L_system
    
    
    def tracer(self,n):
        
        
        mot = self.L_system.renvoyer_mot(n)
        self.regle_affichage(mot)
