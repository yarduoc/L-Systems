## Turtle 3D by Yarduoc
#import bpy
from numpy import *

##

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
    
    """
        Cette classe permet de créer un morphisme de mot, à partir d'une règle de dérivation de chaque lettre et d'un alphabet
        
        regle est une fonction
        alphabet est une liste de caractères
    """
    
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
    
    def skip_dyck_croissant(self,mot,indice):
        compteur_dyck = 1
        for k in range(indice+1,len(mot)):
            
            if mot[k][0] == "[" or mot[k][0] == "]":
                compteur_dyck += (-1)**(mot[k][0] == "]")
            if compteur_dyck == 0:
                return k+1
                
        return "Impossible"
    
    def indice_predec(self, mot, indice):
        """ Renvoie l'indice du predecesseur d'un lettre dans un mot
            
            mot est une liste de listes
            indice est un entier (indice de la lettre à tester dans mot)
        """
        
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
        
        """ Renvoie un booléen qui vérifie si un motif donné est prédecesseur d'une lettre 
            dans un mot
            
            mot est une liste de lettres (une lettre étant une liste de caractère et de paramètres)
            indice est un entier (indice de la lettre à tester dans mot)
            motif est une liste de lettres
        """
        
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
        
        """ Applique la règle de dérivation sur un mot
        """
        sortie = []
        for k in range(len(mot)):
            
            m = self.regle(k,mot,self.alphabet)
            
            sortie += m

        return sortie


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
        
        return caractere in self.langage
    
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
##

def passer_branche(mot,i):
    j = i
    n = len(mot)-1
    est_sur_branche_principale = True
    compteur_dyck = 0
    while est_sur_branche_principale or compteur_dyck != 0 :
        if mot[i][0] == '[' :
            
            compteur_dyck += 1
        if mot[i][0] == ']' :
            compteur_dyck -= 1
        
        if compteur_dyck != 0 :
            est_sur_branche_principale = False
        
        i += 1
    return i
    
def affichage_standard( mot, angle = 5, ratio_d = 0.95, ratio_l = 8/12):
    mem = []
    i = 0
    while i < len(mot):
        char = mot[i][0]
        if char == "+":
            t.rotate_relative_Z(angle)
        elif char == "-":
            t.rotate_relative_Z(-angle)
        elif char == "&":
            t.rotate_relative_Y(angle)
        elif char == "^":
            t.rotate_relative_Y(-angle)
        elif char == "/":
            t.rotate_relative_X(-angle)
        elif char == "\\":
            t.rotate_relative_X(angle)
        elif char == "|":
            t.rotate_relative_Z(180)
        elif char == "[":
            mem.append((t.get_position(),t.get_orientation(),t.line_thickness))
        elif char == "]":
            position,orientation,epaisseur = mem.pop()
            t.set_position(position)
            t.set_orientation(orientation)
            t.set_thickness(epaisseur)
        else:
            if t.forward(10) == "Erreur_collision":
                if i < len(mot) - 1 and mot[i+1][0] == "[":
                    
                    i = passer_branche(mot,i)
            else:
                t.forward(10)
        t.set_thickness(t.line_thickness*ratio_d)
        i += 1

    #t.blender_print(5)
        
            

def regle_evolution_3d(indice, mot,  alphabet = ["F","M","N","O","P","Y","Z"]):
    k = mot[indice][0]
    if k == "F":
        return [["Y"],["["],["+"],["+"],["+"],["+"],["+"],["+"],["M"],["F"],["]"],["["],["-"],["-"],["-"],["-"],["-"],["N"],["F"],["]"],["["],["^"],["^"],["^"],["^"],["^"],["O"],["F"],["]"],["["],["&"],["&"],["&"],["&"],["&"],["P"],["F"],["]"]]
    elif k == "M":
        return [["Z"],["-"],["M"]]
    elif k == "N":
        return [["Z"],["+"],["N"]]
    elif k == "O":
        return [["Z"],["&"],["O"]]
    elif k == "P":
        return [["Z"],["^"],["P"]]
    elif k == "Y":
        return [["Z"],["-"],["Z"],["Y"],["+"]]
    elif k == "Z":
        return [["Z"],["Z"]]
    else :
        return [k]

M = Morphisme(regle_evolution_3d,["F","M","N","O","P","Y","Z"])
L = L_systeme(M,["F"],["F","M","N","O","P","Y","Z"])
A = Interpretation_geometrique(affichage_standard,L)

A.tracer(3)
