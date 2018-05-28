class Morphisme:
    
    """
        Cette classe permet de créer un morphisme de mot, à partir d'une règle de dérivation de chaque lettre et d'un alphabet
        
        regle est une fonction
        alphabet est une liste de caractères
    """
    
    regle = None
    alphabet = None
    def __init__(self,regle,alphabet):
        self.regle = regle
        self.alphabet = alphabet
        
    def skip_dyck(self,mot,indice):
        compteur_dyck = -1
        for k in range(indice-1,-1,-1):
            if compteur_dyck == 0:
                return k+1
            if mot[k][0] == "[" or mot[k][0] == "]":
                compteur_dyck += (-1)**(mot[k][0] == "]")
        return "Impossible"
    
    def skip_dyck_croissant(self,mot,indice):
        compteur_dyck = 1
        for k in range(indice+1,len(mot)):
            
            if mot[k][0] == "[" or mot[k][0] == "]":
                compteur_dyck += (-1)**(mot[k][0] == "]")
            if compteur_dyck == 0:
                return k+1
                
        return "Impossible"
    
    def indice_predec(self, mot, indice):
        """ Renvoie l'indice du predecesseur d'un lettre dans un mot
            
            mot est une liste de listes
            indice est un entier (indice de la lettre à tester dans mot)
        """
        
        if indice == 0:
            return "Impossible"
        if mot[indice - 1][0] in self.alphabet:
            return indice - 1
        elif mot[indice - 1][0] == "]":
            j = self.skip_dyck(mot,indice - 1)
            if j == "impossible" :
                return "impossible"
            return self.indice_predec(mot, j)
        else:
            return self.indice_predec(mot, indice - 1)
            
            
    def est_predecesseur(self, mot,indice, motif):
        
        """ Renvoie un booléen qui vérifie si un motif donné est prédecesseur d'une lettre 
            dans un mot
            
            mot est une liste de lettres (une lettre étant une liste de caractère et de paramètres)
            indice est un entier (indice de la lettre à tester dans mot)
            motif est une liste de lettres
        """
        
        if motif == "" :
            return True
        
        nouvel_indice = self.indice_predec(mot,indice)
        
        if nouvel_indice == "Impossible" :
            return False
        if mot[nouvel_indice][0] != motif[-1] :
            return False
        return self.est_predecesseur(mot,nouvel_indice, motif[:-1:])
        
    def succ(self,mot,k,motif):
        pass
        
    def appliquer(self,mot):
        
        """ Applique la règle de dérivation sur un mot
        """
        sortie = []
        for k in range(len(mot)):
            
            m = self.regle(k,mot,self.alphabet)
            
            sortie += m

        return sortie