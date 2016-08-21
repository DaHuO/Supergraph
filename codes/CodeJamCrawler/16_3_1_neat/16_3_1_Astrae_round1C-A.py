# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 21:34:08 2015

@author: Fred
"""


alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def qualifA(L):
    
    resultat=[]
    # on va chercher le rang des 2 plus grands indices de L
    max1=0
    if L[1]>L[0]:
        max1=1
        max2=0
    else:
        max1=0
        max2=1
    # au début on met dans max1 le rang du plus grand nbr et dans max2 le 2ieme plus grand
    
    for k in range(2,len(L)):        
        if L[k]>L[max1]: # si au nouvel indice on a un rang plus grand que le max
            max2=max1
            max1=k
        elif L[k]>L[max2]: # au nouvel indice, on a qqchose de strict plus grand que l'avant dernier
            max2=k
    
#    print max1,max2
    
    
    # ensuite on commence par diminuer le rang du max jusqu'à ce qu'il vaille max2
    while L[max1]>L[max2]:
        L[max1]=L[max1]-1
        resultat=resultat+[alphabet[max1]]
    
    # ok donc la on se retrouve avec une liste où les 2 indices max à la fin sont égaux (et stric positifs)
    
    # on peut ensuite évacuer les petits partis 1 par 1
    
    for k in range(len(L)):
        if k!=max1:
            if k!=max2:
                # donc on a un "petit parti"
                for nbr in range(0,L[k]):
                    resultat=resultat+[alphabet[k]]
    
    # maintenant il ne reste plus que les 2 gros à évacuer qui sont à autant de personnes
    
    for k in range(0,L[max1]):
        resultat=resultat+[alphabet[max1]+alphabet[max2]]
    
    return resultat
                
        
        
#    max2=L[1]
    


            
    

            
                
              

def main(ifn='A-large.in',ofn='output.txt'):
    with open(ifn) as inf:   # ouvre l'input et le renomme en inf
        with open(ofn,'w') as ouf:  # crée l'output dans lequel on va écrire
            noc = int(inf.readline().strip())  # permet de lire la 1ere ligne
                                               # en général le nbr de cas
                                               # le .strip() permet de virer les espace
            

            
            
            for tnoc in range(noc):          # boucle en fonction du nbr de cas

                ouf.write("Case #%d: " %(tnoc+1))   # case dans laquelle on écrit en sortie
                n=int(inf.readline().strip().split(' ')[0])
                L=inf.readline().strip().split(' ')
#                print n
#                print L
                realL=[]
                for elt in L:
                    
                    realL=realL+[int(elt)]
                print realL
                resultat=qualifA(realL)
                print resultat
                mot=''
                for j in resultat:
                    mot=mot+j+' '

                        

                    

                ouf.write("%s\n" %mot)   # recopie le nombre puis saute une ligne                    
#                else:
#                    ouf.write("%d\n" %resultat)                 


       


