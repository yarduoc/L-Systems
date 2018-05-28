

def affichage_standard( mot, angle = 5, ratio_d = 0.95, ratio_l = 8/12):
    mem = []
    i = 0
    while i < len(mot):
        char = mot[i][0]
        if char == "+":
            t.rotate_relative_Z(mot[i][1])
        elif char == "&":
            t.rotate_relative_Y(mot[i][1])
        elif char == "^":
            t.rotate_relative_X(mot[i][1])
        elif char == "[":
            mem.append((t.get_position(),t.get_orientation(),t.line_thickness))
        elif char == "]":
            position,orientation,epaisseur = mem.pop()
            t.set_position(position)
            t.set_orientation(orientation)
            t.set_thickness(epaisseur)
        elif char == "A":
            if t.forward(mot[i][1]) == "Erreur_collision":
                if i < len(mot) - 1:
                    
                    i = passer_branche(mot,i) -2
            else:
                t.forward(mot[i][1])
        t.set_thickness(t.line_thickness*ratio_d)
        i += 1
M = Morphisme(regle,alphabet)
L = L_systeme(M,graine,alphabet)
A = Interpretation_geometrique(affichage_standard,L)

A.tracer(4)

