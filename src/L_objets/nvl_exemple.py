graine = [("F",1,1),("-",120),("F",1,1),("-",120),("F",1,1)]

def regle(lettre):
    if lettre[0] == "F":
        lit = ("F",lettre[1]/3,lettre[2])
        plus = ("+",60)
        moins = ("-",120)
        return [lit,plus,lit,moins,lit,plus,lit]
    return [lettre]

##

from turtle import *
from math import exp

r1,r2,alpha1,alpha2,phi1,phi2,w0,q,e,min,n = [.75,.77,35,-35,0,0,30,.50,.40,0,10]

graine = [("A",100,w0)]

def regle(lettre):
    if lettre[0] == "A"and lettre[1] >= min :
        A,s,w = lettre
        branche_gauche = [("["),("+",alpha1),("/",phi1),("A",s*r1,w*q*exp(e)),("]")]
        branche_droite = [("["),("+",alpha2),("/",phi2),("A",s*r2,w*(1-q)*exp(e)),("]")]
        return [("F",s,w)] + branche_gauche + branche_droite
    return [lettre]



