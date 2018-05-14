##Import

from numpy import *

##Plan

class Plan:
    
    matrice_sysp = matrix([[] , [] , []])
    matrice_solp = matrix([[] , [] , []])
    
    
    def __init__(self , vecteur1 , vecteur2 , point):
        a , b , c = vecteur1
        d , e , f = vecteur2 
        p1 , p2 , p3 = point
        self.matrice_sysp = matrix([[a,d,0],[b,e,0],[c,f,0]])
        self.matrice_solp = matrix([[-p1],[-p2],[-p3]])

##Droite

class Droite:
    
    matrice_sysd = matrix([[] , [] , []])
    matrice_sold = matrix([[] , [] , []])
    
    def __init__(self , vecteur_dir , point):
        a , b , c = vecteur_dir
        p1 , p2 , p3 = point
        self.matrice_sysd = matrix([[0,0,-a],[0,0,-b],[0,0,-c]])
        self.matrice_sold = matrix([[p1],[p2],[p3]])

##Système d'équations

class Systeme:
    
    matrice_sys = matrix([[] , [] , []])
    matrice_sol = matrix([[] , [] , []])
    
    def __init__(self , Plan , Droite):
        self.matrice_sys = Plan.matrice_sysp + Droite.matrice_sysd
        self.matrice_sol = Plan.matrice_solp + Droite.matrice_sold
    
    def resolution(self):
        if linalg.det(self.matrice_sys) != 0:
            A = linalg.solve(self.matrice_sys , self.matrice_sol)
            return dot(P.matrice_sysp,A) - P.matrice_solp
        else:
            return "Pas de solution"