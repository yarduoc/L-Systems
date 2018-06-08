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

import os
os.chdir("C:\\GitHub\\L-Systems\\src\\L_objets")
 
from morphisme import Morphisme



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
        


def regle(indice,mot,alphabet):
    lettre = mot[indice]
    x = lettre[0]
    if x == 'T' :
        t1,t2,t3 = lettre[1::]
        if t3 < l :
            return [['F', t1, t2*facteur_epaisseur],['T',t1,t2,t3+1]] #p1
        return [['['],['+',alpha1],['F',t1,t2],['A',d,t1,t2],[']'],['['],['+',alpha2],['&',alpha3],['F',t1,t2],['A',d,t1,t2],[']'],['['],['+',alpha2],['&',-alpha3],['F',t1,t2],['A',d,t1,t2],[']']] #p2
    if x == 'A' :
        p,taille,epaisseur = lettre[1::]
        if p < d: 
            return [['F', taille, epaisseur*facteur_epaisseur],['A',p+1,taille,epaisseur]] #p3
        return [['F', taille, epaisseur*facteur_epaisseur],['['],['^',randint(0,180)],['&',randint(0,5)],['F', taille, epaisseur*facteur_epaisseur],['&',randint(0,5)],['F', taille, epaisseur*facteur_epaisseur],['&',randint(-30,30)],['F', taille, epaisseur*facteur_epaisseur],['&',randint(0,5)],['F', taille, epaisseur*facteur_epaisseur],['&',randint(0,5)],['F', taille, epaisseur*facteur_epaisseur],['&',randint(0,5)],['F', taille, epaisseur*facteur_epaisseur],['&',randint(0,5)],['F', taille, epaisseur*facteur_epaisseur],['&',randint(0,5)],['F', taille, epaisseur*facteur_epaisseur],['&',randint(0,5)],['F', taille, epaisseur*facteur_epaisseur],['&',randint(0,5)],['F', taille, epaisseur*facteur_epaisseur],['A',0,taille,epaisseur],[']'],['A',0,taille,epaisseur]] #p4

    return [lettre]

alphabet = ['T','F','A','L']
l = 5
d = 3
y = 1
e = .1
facteur_epaisseur = .9
alpha1,alpha2,alpha3= 15,-24,30
from random import randint
graine = [['&',-90],['T',y, e, 0]]


def passer_branche(mot,i):
    j = i
    n = len(mot)-1
    
    compteur_dyck = 1
    
    while i < n  and (compteur_dyck != 0) :
        
        if mot[i][0] == '[' :
            
            compteur_dyck += 1
        if mot[i][0] == ']' :
            compteur_dyck -= 1
        
        
        i += 1
        
    return i

def affichage_standard( mot, angle = 5, ratio_d = 0.95, ratio_l = 8/12):
    mem = []
    i = 0
    while i < len(mot):
        char = mot[i][0]
        if char == "+":
            t.rotate_relative_Z(mot[i][1])
        elif char == "&":
            t.rotate_relative_Y(mot[i][1])
        elif char == "^":
            t.rotate_relative_X(mot[i][1])
        elif char == "[":
            mem.append((t.get_position(),t.get_orientation(),t.line_thickness))
        elif char == "]":
            position,orientation,epaisseur = mem.pop()
            t.set_position(position)
            t.set_orientation(orientation)
            t.set_thickness(epaisseur)
        elif char == "F":
            if t.forward(mot[i][1]) == "Erreur_collision":
                if i < len(mot) - 1:
                    
                    i = passer_branche(mot,i) -2
            else:
                t.forward(mot[i][1])
        t.set_thickness(t.line_thickness*ratio_d)
        i += 1



M = Morphisme(regle,alphabet)
L = L_systeme(M,graine,alphabet)

A = Interpretation_geometrique(affichage_standard,L)

A.tracer(4)


