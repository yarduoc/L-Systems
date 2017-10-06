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
    if f=="X" :
        return "F[-X][X]F[-X]+FX"
    elif f =="F" :
        return "FF"
    else :
        return f

def affichage4(mot):
    turtle.resetscreen()
    turtle.speed("fastest")
    turtle.left(60)
    pos=[]
    for k in mot:
        if k=="F":
            turtle.forward(3)
        elif k=="-":
            turtle.left(25)
        elif k=="+":
            turtle.right(25)
        elif k=="[":
            pos.append( turtle.position())
        elif k=="]":
            turtle.penup()
            turtle.goto(pos.pop())
            turtle.pendown()

affichage4(L_system( "X", regle4,6))
