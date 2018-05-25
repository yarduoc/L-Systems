def affichage(mot):
    pos = []
    i = 0
    while i < len(mot):
        k = mot[i]
        if k[0] == "I":
            if t.forward(10) == "Erreur collision":
                if i < len(mot) - 1 and mot[i+1][0] == "[":
                    i = A.L_system.morphism.skip_dyck_croissant(mot,i+1) - 1
            else:
                t.forward(10)
                
        elif k[0] =="[":
            pos.append((t.get_position(),t.get_orientation()))
        elif k[0] =="]":
            x=pos.pop()
            t.set_position(x[0])
            t.set_orientation(x[1])
        
        elif k[0] == "+":
            t.rotate_relative_Z(k[1])
        
        elif k[0] == "-":
            t.rotate_relative_Z(-k[1])
            
        elif k[0] == "/":
            t.rotate_relative_X(k[1])
            
        elif k[0] == "^":
            t.rotate_relative_Y(k[1])
        
        i += 1