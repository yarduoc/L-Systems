import turtle

# def affiche(M):
#     for x in M:
#         if x=='F': turtle.forward(10)
#         if x == '+': turtle.left(90)
#         if x == '-': turtle.right(90)
# def cree(n,M):
#     for i in range (n):
#         C=''
#         for x in M:
#             if x =='F': C+= 'F+F-F-F+F'
#             else:C+=x
#         M=C
#     return M
# 
# 
# def depile(L):
#     for x in L:
#         if x=='F': turtle.backward(10)
#         if x == '+': turtle.right(30)
#         if x == '-': turtle.left(30)
#         if x =='[':break

# def affiche2(M):
#     k=0
#     while k<len(M):
#         if M[k]=='F': turtle.forward(10)
#         if M[k] == '+': turtle.left(30)
#         if M[k] == '-': turtle.right(30)
#         if M[k] == '[':
#             L=''
#             while M[k]!=']':
#                 L=M[k]+L
#                 if M[k]=='F': turtle.forward(10)
#                 if M[k] == '+': turtle.left(30)
#                 if M[k] == '-': turtle.right(30)
#                 k+=1
#             depile(L)
#         k+=1
#         
# def cree2(n,M):
#     for i in range (n):
#         C=''
#         for x in M:
#             if x =='F': C+= 'F[-F]F[+F][F]'
#             else:C+=x
#         M=C
#     return M
#                 
##
from turtle import *
def argument(M,indice):
    C=""
    a=1.0
    k=indice+2
    while k<len(M) and M[k]!=')' and M[k]!='(':
        if M[k]=='*':
            # print(C)
            a=a*float(C)
            C=""
        else:
            C+=M[k]
        k+=1
        # print(C)
    return a*float(C)
def cree3(n,M):
    for i in range (n):
        C=""
        j=0
        while j<len(M):
            if M[j] =='X':
                C+= "-(0.1)F("+str(argument(M,j))+")[+(0.5)X(0.4*"+str(argument(M,j))+")][-(0.5)X(0.4*"+str(argument(M,j))+")]X(0.8*"+str(argument(M,j))+")"
                while M[j]!=')':
                    j+=1
                j+=1
            else:
                C+=M[j]
                j+=1
        M=C
    return M

def L_sys(M,y):
    C=''
    k=y+1
    while k<len(M) and M[k]!=']':
        C+=M[k]
        k+=1
    return C
        

def L_system(graine):
        y=0
        while y<len(graine):
            if graine[y]=='F': forward(argument(graine,y))
            if graine[y]== '+': left(argument(graine,y))
            if graine[y]== '-': right(argument(graine,y))
            if graine[y]=='[':
                position=pos()
                angle=heading()
                while graine[y]!=']':
                    y+=1
                    if graine[y]=='F': forward(argument(graine,y))
                    if graine[y]== '+': left(argument(graine,y))
                    if graine[y]== '-': right(argument(graine,y))
                goto(position)
                settiltangle(angle)
            y+=1
        
        
                
                
                
            
            
