import os
os.chdir("C:\\GitHub\\L-Systems\\src\\L_objets")

from interpret_geometrique import Interpretation_geometrique



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
        angle = randint(1,10)
        return [['F', taille, epaisseur*facteur_epaisseur],['['],['^',randint(10,180)],['&',angle],['F', taille, epaisseur*facteur_epaisseur],['&',angle],['F', taille, epaisseur*facteur_epaisseur],['&',angle],['F', taille, epaisseur*facteur_epaisseur],['&',angle],['F', taille, epaisseur*facteur_epaisseur],['&',angle],['F', taille, epaisseur*facteur_epaisseur],['A',0,taille,epaisseur],[']'],['A',0,taille,epaisseur]] #p4

    return [lettre]
