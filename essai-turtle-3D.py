def L_system ( graine, regle_evolution, profondeur):
    
    mot = graine
    
    def evolution( mot, regle_evolution):
        sortie = ""
        for k in mot:
            sortie += regle_evolution( k)
        return sortie
    
    for _ in range(profondeur):
        mot = evolution( mot, regle_evolution)
    
    return mot



def regle3(f):
    if f=="x" :
        return "x+yf+"
    elif f =="y" :
        return "-fx-y"
    else :
        return f

def affichage3(mot):
    # turtle.speed("fastest")
    for k in mot:
        if k=="f":
            t.forward(10)
        elif k=="-":
            t.rotate_Z(90)
        elif k=="+":
            t.rotate_Z(-90)

# affichage3(L_system( "fx", regle3,7))