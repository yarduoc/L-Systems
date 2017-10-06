import turtle
    
## L-systèmes

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

## L-systeme fractal

def regle(f):
    if f == "F":
        return "F+F-F-F+F"
    return f

def affichage(mot):
    turtle.speed("fastest")
    turtle.up
    turtle.goto(-300,-300)
    turtle.down
    for k in mot:
        if k=="F":
            turtle.forward(10)
        elif k=="+":
            turtle.left(90)
        elif k=="-":
            turtle.right(90)

a = L_system("F",regle,5)

affichage(a)

## Serpinski triangles

def regle2(f):
    if f=="F" :
        return "F-G+F+G-F"
    elif f =="G" :
        return "GG"
    else :
        return f

def affichage2(mot):
    turtle.speed("fastest")
    for k in mot:
        if k=="F" or k=="G":
            turtle.forward(10)
        elif k=="+":
            turtle.left(120)
        elif k=="-":
            turtle.right(120)

affichage2(L_system( "F-G-G", regle2,7))

##L Courbe du dragon


def regle3(f):
    if f=="x" :
        return "x+yf+"
    elif f =="y" :
        return "-fx-y"
    else :
        return f

def affichage3(mot):
    turtle.speed("fastest")
    for k in mot:
        if k=="f":
            turtle.forward(10)
        elif k=="-":
            turtle.left(90)
        elif k=="+":
            turtle.right(90)

affichage3(L_system( "fx", regle3,7))

## Plante fractale


def regle4(f):
    if f=="F" :
        return "FF"
    elif f=="X" :
        return "F-[[X]+X]+F[+FX]-X"
    else :
        return f

def affichage4(mot):
    turtle.resetscreen()
    turtle.speed("fastest")
    turtle.left(90)
    turtle.penup()
    turtle.goto(0,-300)
    turtle.pendown()
    turtle.tracer(0, 0)
    pos=[]
    for k in mot:
        if k=="F":
            turtle.forward(2)
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

affichage4(L_system( "X", regle4,8))
