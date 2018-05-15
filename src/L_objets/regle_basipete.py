alpha1 = 10
alpha2 = 32
sigma0 = 17
nu = 0.89
lbd = 0.7
vth = 5.0

alphabet = ['A','I','N']

graine = [['N',1],['I',0,2,0,1],['A']]




def skip_dyck(mot,indice):
    compteur_dyck = -1
    for k in range(indice-1,-1,-1):
        if compteur_dyck == 0:
            return k+1
        if mot[k][0] == "[" or mot[k][0] == "]":
            compteur_dyck += (-1)**(mot[k][0] == "]")
    return "Impossible"
    
def indice_predec(mot, indice):
    """ Renvoie l'indice du predecesseur d'un lettre dans un mot
            
        mot est une liste de listes
        indice est un entier (indice de la lettre à tester dans mot)
    """
        
    if indice == 0:
        return "Impossible"
    if mot[indice - 1][0] in alphabet:
        return indice - 1
    elif mot[indice - 1][0] == "]":
        j = skip_dyck(mot,indice - 1)
        if j == "Impossible" :
            return "Impossible"
        return indice_predec(mot, j)
    else:
        return indice_predec(mot, indice - 1)

def skip_dyck_croissant(mot,indice):
    compteur_dyck = 1
    for k in range(indice+1,len(mot)):
        
        if mot[k][0] == "[" or mot[k][0] == "]":
            compteur_dyck += (-1)**(mot[k][0] == "]")
        if compteur_dyck == 0:
            return k+1
            
    return "Impossible"
        
def indice_succ(mot,indice):
    if indice >= len(mot)-1:return 'Impossible'
    if mot[indice+1][0] in alphabet : return indice+1
    if mot[indice+1][0] != '[' and mot[indice+1][0] != ']' : return indice_succ(mot,indice+1)
    i = skip_dyck_croissant(mot,indice+1)
    if i == 'Impossible' :
        return i
    return indice_succ(mot,i)

        
        
def indice_fils(mot,indice):
    i1 = indice+1
    dyck = 1
    while mot[i1][0] != 'I' and dyck > 0 :
        i1 += 1
        if mot[i1][0] == "[" or mot[i1][0] == "]":
            dyck += (-1)**(mot[i1][0] == "]")
        
    i2 = i1 + 1
    dyck = 1
    while mot[i2][0] != 'I' and dyck > 0 :
        i2 += 1
        if mot[i2][0] == "[" or mot[i2][0] == "]":
            dyck += (-1)**(mot[i1][0] == "]")
    return i1,i2
        
        
            
def regle_basipete(indice,mot, alphabet):
    print(indice)
    lettre = mot[indice]
    x = lettre[0]
    if x == "I":
        
        [b,m,v,c] = lettre[1::]
        p = indice_predec(mot,indice)
        
        if p != 'Impossible' : 
            if mot[p][0] == 'N' :
                k = mot[p][1]
                if b == 0 and m == 2 : 
                    return [['I',b,1,sigma0 * 2**((k-1)*(nu**k)),c]] #p1
                    
            if mot[p][0] == 'I' :
                [bl,ml,vl,cl] = mot[p][1::]
                if ml == 1 and b == 1 :
                    return [['I',b,ml,vl - vl*(1-lbd)*((cl-c)/c),c]] #p3
                    
                if ml == 1 and b == 2 :
                    return [['I',b,ml,vl*(1-lbd)*(c/(cl-c)),c]] #p4
                    
        s = indice_succ(mot,indice)
        
        if s != 'Impossible' and m == 0 and mot[s][0] != 'A' : #-Si I n'est pas suivi d'un apex, alors il a 2 branches filles
            i1,i2 = indice_fils(mot,indice)
            [b1,m1,v1,c1] = mot[i1][1::]
            [b2,m2,v2,c2] = mot[i2][1::]
            if m1 == 2 and m2 == 2 :
                return [['I',b,2,v,c1+c2]] #p7
        if m == 1 :
            return [['I',b,0,v,c]] #p8
            
        if p != 'Impossible' : 
            if mot[p][0] == 'I' :
                [bl,ml,vl,cl] = mot[p][1::]
                if ml == 2 and m == 2 :
                    return [['I',b,0,v,c]] #p9
    if x == 'N' :
        
        k = lettre[1]
        s = indice_succ(mot,indice)
        
        if mot[s][0] != 'Impossible' : 
            if mot[s][0] == 'I' :
                [b,m,v,c] = mot[s][1::]
                if b == 0 and m == 2 :
                    return [['N',k+1]] #p2
    if x == 'A' :
        p = indice_predec(mot,indice)
        if p != 'Impossible':
            if mot[p][0] == 'I' :
                [b,m,v,c] = mot[p][1::]
                if m == 1 and v > vth :
                    return [["/",180],['['],["-",alpha2],["I",2,2,v*(1-lbd),1],["A"],[']'],['+',alpha1],['I',1,2,v*lbd,1],['A']] #p5
        s = indice_succ(mot,indice)
        if s != 'Impossible' :
            if mot[s][0] == 'I' :
                [b,m,v,c] = mot[s][1::]
                if m == 1 and v <= vth :
                    return [['I',b,2,v,c]] #p6
    return [lettre]