## Plante_2D 
## Regle : F[[-X][+X]]F[+FX]-X

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

def regle(f):
    if f=="X":
        return "F[[-X][+X]]F[+FX]-X"
    elif f=="F":
        return "FF"
    else:
        return f

def affichage(mot):
    turtle.resetscreen()
    turtle.speed("fastest")
    turtle.left(90)
    turtle.penup()
    turtle.goto(0,-300)
    turtle.pendown()
    turtle.tracer(0, 0)
    pos=[]
    for k in mot:
        if k=="F" or k=="G":
            turtle.forward(5)
        elif k=="-":
            turtle.left(22.5)
        elif k=="+":
            turtle.right(22.5)
        elif k=="[":
            pos.append( (turtle.position(),turtle.heading()))
        elif k=="]":
            turtle.penup()
            x=pos.pop()
            turtle.goto(x[0])
            turtle.setheading(x[1])
            turtle.pendown()
    turtle.update()

affichage(L_system( "X", regle,7))