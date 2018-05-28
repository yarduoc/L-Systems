import os
os.chdir("C:\\GitHub\\L-Systems\\src\\L_objets")

from interpret_geometrique import Interpretation_geometrique

alphabet = ['T','F','A','L']
l = 5
d = 3
y = 1
e = .1
facteur_epaisseur = .9
alpha1,alpha2,alpha3= 12,-24,30
from random import randint
graine = [['T',y, e, 0]]


def regle(indice,mot,alphabet):
    lettre = mot[indice]
    x = lettre[0]
    if x == 'T' :
        y,e,k = lettre[1::]
        if k < l :
            return [['F', y, e*facteur_epaisseur],['T',y,e,k+1]] #p1
        return [['['],['^',alpha1],['F',y,e],['A',d,y,e],[']'],['^',alpha2],['&',alpha3],['F',y,e],['A',d,y,e],[']'],['['],['^',alpha2],['&',-alpha3],['F',y,e],['A',d,y,e],[']']] #p2
    if x == 'A' :
        p,taille,epaisseur = lettre[1::]
        if p < d: 
            return [['F', y, e*facteur_epaisseur],['A',p+1,taille,epaisseur]] #p3
        return [['F', y, e*facteur_epaisseur],['['],['^',randint(-30,30)],['&',randint(-30,30)],['+',randint(-30,30)],['F', y, e*facteur_epaisseur],[']'],['A',0,taille,epaisseur]] #p4

    return [lettre]

M = Morphisme(regle,alphabet)
L = L_systeme(M,graine,alphabet)

A = Interpretation_geometrique(affichage_standard,L)

A.tracer(4)
