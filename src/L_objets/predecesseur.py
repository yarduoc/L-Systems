def skip_dyck(mot,indice):
    compteur_dyck = -1
    for k in range(indice-1,-1,-1):
        if compteur_dyck == 0:
            return k+1
        if mot[k] == "[" or mot[k] == "]":
            compteur_dyck += (-1)**(mot[k] == "]")
    return "Impossible"

def predecesseur(mot, indice, alphabet):
    if indice == 0:
        return "Impossible"
    if mot[indice - 1] in alphabet:
        return indice - 1
    elif mot[indice - 1] == "]":
        j = skip_dyck(mot,indice - 1)
        return predecesseur(mot, j, alphabet)
    else:
        return predecesseur(mot, indice - 1, alphabet)