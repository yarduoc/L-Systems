list = t.stored_lines
fichier = open("ichier_coordonees_arbre.txt",'w')
fichier.write('['+'\n')
for ligne in list:
    fichier.write(str(ligne)+','+'\n')

fichier.write(']'+'\n')
#fichier.close()