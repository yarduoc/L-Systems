ll = 3
lr = 5
ld = 4
d = 5
w = 40

def skip_dyck_croissant(mot,indice):
    compteur_dyck = 1
    for k in range(indice+1,len(mot)):
        
        if mot[k][0] == "[" or mot[k][0] == "]":
            compteur_dyck += (-1)**(mot[k][0] == "]")
        if compteur_dyck == 0:
            return k+1
            
    return "Impossible"

def regle_14(mot, indice):
    if indice == len(mot):
        return "Impossible"
    j = skip_dyck_croissant(mot,indice+1)
    return mot[j+2][0] == "D"
    
def regle_parasite(indice, mot, alphabet):
    lettre = mot[indice]
    x = lettre[0]
    if x == "A":
        n,m = lettre[1],lettre[2]
        if M.est_predecesseur(mot, indice, "F"):
            if m > 0:
                return [["A",n,m-1]]
            if n > 0 and m == 0:
                return [["F"],["A",n-1,d]]
            if n == 0 and m == 0:
                return [["L"],["&"],["["],["+"],["F"],["A",ll,d],["]"],["["],["-"],["F"],["A",lr,d],["]"],["^"],["^"],["["],["F"],["A",ld,d],["]"]]
        if M.est_predecesseur(mot, indice, "U"):
            return [["D"]]
    if x == "W":
        t = lettre[1]
        if t > 0:
            return [["W",t-1]]
        if t == 0:
            return [["U"]]
    if x == "F":
        if M.est_predecesseur(mot, indice, "U"):
            return [["F"],["U"]]
        if indice+1 < len(mot) and mot[indice+1][0] == "D":
            return [["D"],["F"]]
    if x == "U":
        return []
    if x == "+" and M.est_predecesseur(mot,indice,"UL"):
        return [["+"],["U"]]
    if x == "D":
        return []
    if x == "L" and indice+3 < len(mot) and mot[indice+3][0] == "D":
        return [["U"],["R"]]
    if x == "-" and M.est_predecesseur(mot,indice,"UR"):
        return [["-"],["U"]]
    if x == "R" and regle_14(mot,indice):
        return [["D"]]
    return [lettre]


def affichage(mot):
    pos = []
    for k in mot:
        if k[0] == "F":
            t.forward(10)
        elif k[0] =="[":
            pos.append((t.get_position(),t.get_orientation()))
        elif k[0] =="]":
            x=pos.pop()
            t.set_position(x[0])
            t.set_orientation(x[1])
        
        elif k[0] == "+":
            t.rotate_relative_Z(30)
        
        elif k[0] == "-":
            t.rotate_relative_Z(-30) 
    
        