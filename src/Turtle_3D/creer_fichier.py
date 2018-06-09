os.chdir("C:\\GitHub\\L-Systems\\Environment-sensitive")
list = t.stored_lines
fichier = open("fichier_coordonees_arbre_avec_vent6.txt",'w')
fichier.write('['+'\n')
for ligne in list:
    fichier.write(str(ligne)+','+'\n')

fichier.write(']'+'\n')
fichier.close()