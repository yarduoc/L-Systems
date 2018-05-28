alphabet = ['T','F','A','L']
l = 5
d = 3
t = 1
e = .1
facteur_epaisseur = .9
alpha1,alpha2,alpha3= 12,-24,30
from random import randint
graine = [['T',t, e, 0]]


def regle(indice,mot,alphabet):
    lettre = mot[indice]
    x = lettre[0]
    if x == 'T' :
        t,e,k = lettre[1::]
        if k < l :
            return [['T',t,e,k+1],['F', t, e*facteur_epaisseur]] #p1
        return [['['],['^',alpha1],['F',t,e],['A',d,t,e],[']'],['^',alpha2],['&',alpha3],['F',t,e],['A',d,t,e],[']'],['['],['^',alpha2],['&',-alpha3],['F',t,e],['A',d,t,e],[']']] #p2
    if x == 'A' :
        p,taille,epaisseur = lettre[1::]
        if p < d: 
            return [['A',p+1,taille,epaisseur],['F', t, e*facteur_epaisseur]] #p3
        return [['F', t, e*facteur_epaisseur],['['],['^',randint(-30,30)],['&',randint(-30,30)],['+',randint(-30,30)],[']']] #p4
    
    
    return lettre

