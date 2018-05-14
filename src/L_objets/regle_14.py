def skip_dyck_croissant(mot,indice):
    compteur_dyck = 1
    for k in range(indice+1,len(mot)):
        
        if mot[k] == "[" or mot[k] == "]":
            compteur_dyck += (-1)**(mot[k] == "]")
        if compteur_dyck == 0:
            return k+1
            
    return "Impossible"

def regle_14(mot, indice):
    if indice == len(mot):
        return "Impossible"
    j = skip_dyck_croissant(mot,indice+1)
    return mot[j+2] == "D"