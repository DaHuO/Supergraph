# script de.py

import  random, math
import numpy as np
from array import *
import random
from Fonctions import *
#from parser import *
#from help import *


file= "donnees.txt"

#G = parsoneinteger(file)
#parsonarrayinteger()
#parsonarraylonginteger()
#parsonarraystring()
#G=parsewords(file)
G=parsewordsletterperletter(file)
    
Nb = len(G)

Tab=["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

ordre= [0,8,2,6,3,4,5,1,7,9]



def calc(g):  # fonction principale: calcul pour une case de G
        res = []
        gg= g
        C= Comptemultiplicite(gg)
        N = len(C)
        #print("C",C)
        for i in ordre:
                #print(i)
                
                toto = Tab[i]
                RES= [C[j][1] for j in range(0,N) if IN(C[j][0], toto)]
                if(len(RES)==0 or len(set(toto))>len(RES)):
                        m=0
                else:
                        m= min(RES)
                #print('essai',i, m, RES)
                
                #m=min(C[j][1] for j in range(0,N) if IN(C[j][0], toto))
                for j in range(0,m):
                        res.append(i)
                for j in range(0,N):
                        for l in toto:
                                if(C[j][0]==l):
                                        C[j][1]=C[j][1]-m
                
        res2=sort(res)
        word=''
        for i in range(0,len(res)):
                word=word+str(res2[i])
        print("WORD",word)
        return(word)

        #return([2*g+1, 4*g*g+3*g])


for i in range(0,Nb):
        print(calc(G[i]))

printeverything([calc(G[i]) for i in range(0,Nb)])


#printarraynumbers([calc(G[i]) for i in range(0,Nb)])
#printarraystring([calc(G[i]) for i in range(0,Nb)])

