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
    # turtle.speed("fastest")
    # turtle.up
    # turtle.goto(-300,-300)
    # turtle.down
    for k in mot:
        if k=="F":
            t.forward(10)
        elif k=="+":
            t.rotate_Z(90)
        elif k=="-":
            t.rotate_Z(-90)

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
    # turtle.speed("fastest")
    for k in mot:
        if k=="F" or k=="G":
            t.forward(10)
        elif k=="+":
            t.rotate_Z(120)
        elif k=="-":
            t.rotate_Z(-120)

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
    # turtle.speed("fastest")
    for k in mot:
        if k=="f":
            t.forward(10)
        elif k=="-":
            t.rotate_Z(90)
        elif k=="+":
            t.rotate_Z(-90)

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
    # turtle.resetscreen()
    # turtle.speed("fastest")
    # t.rotate_Z(90)
    # turtle.penup()
    # turtle.goto(0,-300)
    # turtle.pendown()
    # turtle.tracer(0, 0)
    pos=[]
    for k in mot:
        if k=="F":
            t.forward(2)
        elif k=="-":
            t.rotate_Z(22.5)
        elif k=="+":
            t.rotate_Z(-22.5)
        elif k=="[":
            pos.append( (t.setposition(),t.heading()))
        elif k=="]":
            t.penup()
            x=pos.pop()
            t.goto(x[0])
            turtle.setheading(x[1])
            turtle.pendown()
    turtle.update()

affichage4(L_system( "X", regle4,8))

## L_system 3D

 def regle5(f):
     if f=="F":
         return "Y[++++++MF][-----NF][^^^^^OF][&&&&&PF]"
     elif f=="M":
         return "Z-M"
     elif f=="N":
         return "Z+N"
     elif f=="O":
         return "Z&O"
     elif f=="P":
         return "Z^P"
     elif f=="Y":
         return "Z-ZY+"
     elif f=="Z":
         return "ZZ"
 
 def affichage5(mot):
     turtle.resetscreen()
     turtle.speed("fastest")
     turtle.left(90)
     turtle.penup()
     turtle.goto(0,-300)
     turtle.pendown()
     turtle.tracer(0, 0)
     pos=[]
     for k in mot:
         if k=="F" or k=="M" or k=="N" or k=="O" or k=="P" or k=="Y" or k=="Z":
             t.forward(2)
         elif k=="-":
             t.rotate_Z(22.5)
         elif k=="+":
             t.rotate_Z(-22.5)
         elif k=="&":
             t.rotate_Y(22.5)
         elif k=="^":
             t.rotate_Y(-22.5)
         elif k=="/":
             t.rotate_Y(-22.5)
         elif k=="|":
             t.rotate_Z(180)
         elif k=="[":
             pos.append( (turtle.position(),turtle.heading()))
         elif k=="]":
             turtle.penup()
             x=pos.pop()
             turtle.goto(x[0])
             turtle.setheading(x[1])
             turtle.pendown()
     turtle.update()
