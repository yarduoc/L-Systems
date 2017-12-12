#import turtle3D
    
## L-système

def L_system ( graine, regle_evolution, ordre):
    mot = graine
    def evolution( mot, regle_evolution):
        sortie = ""
        for k in mot:
            sortie += regle_evolution( k)
        return sortie
    for _ in range(ordre):
        mot = evolution( mot, regle_evolution)
    return mot
    
    
def affichage_standard( mot, angle, ratio_d, ratio_l):
    t = turtle3D((0,0,0),(0,0,1))
    mem = []
    for char in mot :
        if char == "+":
            t.rotate_relative_Z(angle)
        elif char == "-":
            t.rotate_relative_Z(-angle)
        elif char == "&":
            t.rotate_relative_Y(angle)
        elif char == "^":
            t.rotate_relative_Y(-angle)
        elif char == "/":
            t.rotate_relative_X(-angle)
        elif char == "\\":
            t.rotate_relative_X(angle)
        elif char == "|":
            t.rotate_relative_Z(180)
        elif char == "[":
            mem.append((t.get_position(),t.get_orientation(),t.line_thickness))
            print(mem)
        elif char == "]":
            position,orientation,epaisseur = mem.pop()
            t.set_position(position)
            t.set_orientation(orientation)
            t.set_thickness(epaisseur)
        else:
            t.forward(10)
        t.set_thickness(t.line_thickness*ratio_d)

    #t.blender_print(5)
        
            

def regle_evolution_3d( mot):
    sortie = ""
    for k in mot:
        if k == "F":
            sortie += "Y[++++++MF][-----NF][^^^^^OF][&&&&&PF]"
        elif k == "M":
            sortie += "Z-M"
        elif k == "N":
            sortie += "Z+N"
        elif k == "O":
            sortie += "Z&O"
        elif k == "P":
            sortie += "Z^P"
        elif k == "Y":
            sortie += "Z-ZY+"
        elif k == "Z":
            sortie += "ZZ"
        else :
            sortie += k
    return sortie
        
        
mot = L_system("F",regle_evolution_3d,3)
affichage_standard(mot,56,0.95,1)