import turtle

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
    
        p,s = predec(M,k,1), succ(M,k)
        
        if M[k] == "0":
            
            if p == "0" and s == "0":
                return "0" 
            elif p == "1" and s == "0":
                return "0"
            elif p == "0" and s == "1":
                return "1[-F1F1]"
            elif p == "1" and s == "1":
                return "1F1"
            else: return "0"
        elif M[k] == "1":
            if p == "0" and s == "0":
                return "1" 
            elif p == "0" and s == "1":
                return "1" 
            elif p == "1" and s == "0":
                return "1" 
            elif p == "1" and s == "1":
                return "0"
            else: return "1"
        elif M[k] == "+":
            return "-"
        elif M[k] =="-":
            return "+"
        else: return M[k]


def predec(M,k,l):
    mot = ''
    i = k
    for _ in range(l):
        p = predec_aux(M,i)
        print(i,mot,p)
        if p == 'no':
            return 'no'
        mot += M[p]
        i = p
    return mot[::-1]

def predec_aux(M,k):
    if k == 0 :
        return 'no'
    else:
        dyck = 0
        i = k -1
        
        while (M[i] !="0" and M[i] != "1") or  dyck != 0 :
            if M[i] == ']' :
                dyck += 1
            elif M[i] == '[' :
                dyck -= 1
            i-=1
            if i == -1 :
                return 'no'
        if i == -1 :
            return 'no'
        return i
            
            
def succ(M,k):
    if k == len(M)-1 :
        return 'no'
    else:
        dick = 0
        i = k + 1
        
        while (M[i] !="0" and M[i] != "1") or dick != 0 :
            i += 1
            if i == len(M):
                return "no"
            if M[i] == ']' :
                dick += 1
            if M[i] == '[' :
                dick -= 1

            # print(i,M[i],dick)
        if i == len(M) :
            return 'no'
        return M[i]
        
def affichage(mot):
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
            turtle.forward(20)
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
