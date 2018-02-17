def L_system ( graine, regle_evolution, profondeur):
    
    mot = graine
    
    def evolution( mot, regle_evolution):
        sortie = ""
        for k in range(len(mot)):
            sortie += regle_evolution(mot,k)
        return sortie
        
    for _ in range(profondeur):
        mot = evolution( mot, regle_evolution)
    
    return mot
        
        
def regle_context(M,k):
        if M[k] == "0":
            if predec(M,k) == "0" and succ(M,k) == "0":
                return "0" 
            if predec(M,k) == "1" and succ(M,k) == "0":
                return "1F1"
            if predec(M,k) == "0" and succ(M,k) == "1":
                return "1[-F1F1]" 
        elif M[k] == "1":
            if predec(M,k) == "0" and succ(M,k) == "0":
                return "1" 
            if predec(M,k) == "0" and succ(M,k) == "1":
                return "1" 
            if predec(M,k) == "1" and succ(M,k) == "0":
                return "1" 
            if predec(M,k) == "1" and succ(M,k) == "1":
                return "0"
        elif M[k] == "+":
            return "-"
        elif M[k] =="-":
            return "+"
        else: return M[k]


def predec(M,k):
    if k == 0 :
        return 'no'
    else:
        dick = 0
        i = k
        
        while (M[i] == '[' or M[i] == "F" or M[i] == ']' or dick != 0  or i==k):
            i -= 1
            if M[i] == ']' :
                dick += 1
            if M[i] == '[' :
                dick -= 1

            print(i,M[i],dick)
        if i == -1 :
            return 'no'
        return M[i]
            
            
def succ(M,k):
    if k == len(M)-1 :
        return 'no'
    else:
        dick = 0
        i = k
        
        while (M[i] == '[' or M[i] == ']' or M[i] == "F" or dick != 0  or i==k):
            i += 1
            if M[i] == ']' :
                dick += 1
            if M[i] == '[' :
                dick -= 1

            print(i,M[i],dick)
        if i == len(M) :
            return 'no'
        return M[i]