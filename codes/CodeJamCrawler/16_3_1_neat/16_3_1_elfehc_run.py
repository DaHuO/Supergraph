# script de.py

import  random, math
import numpy as np
from array import *
import random
from Fonctions import *

file= "donnees.txt"

#G = parsoneinteger(file)
G = parsonarrayinteger(file)
#G= parsonarraylonginteger(file)
#G=parsonarraystring(file)
#G=parsewords(file)
#G=parsewordsletterperletter(file)
    
Nb = len(G)

Letters =  [a for a in map(chr, range(65, 91))]

def calc(g):  # fonction principale: calcul pour une case de G
        Nbparts = len(g)
        gg = g
        res = []
        print(g, gg, Nbparts)
        while(max(gg)>0):
                m = max(gg)
                
                argmaxx=set()
                rang=-1
                while(rang < Nbparts-1):
                        rang =rang + 1
                        if gg[rang]==m:
                                argmaxx =argmaxx.union({rang})
                                
                AR= list(argmaxx)
                if len(AR)==1:
                        rang=AR[0]
                        gg[rang] = gg[rang]-1
                        res.append(Letters[rang])
                if len(AR)>1 and m>1:
                        rang0=AR[0]
                        rang1=AR[1]
                        gg[rang0] = gg[rang0]-1
                        gg[rang1] = gg[rang1]-1
                        res.append(Letters[rang0]+Letters[rang1])
                if len(AR)>1 and m==1:
                        if len(AR)%2 ==1:
                                rang0=AR[0]
                                gg[rang0] = gg[rang0]-1
                                res.append(Letters[rang0])
                        if len(AR)%2 ==0:
                                rang0=AR[0]
                                rang1=AR[1]
                                gg[rang0] = gg[rang0]-1
                                gg[rang1] = gg[rang1]-1
                                res.append(Letters[rang0]+Letters[rang1])
                        
        #return([2*g+1, 4*g*g+3*g])
        #print(res)
        
        return(res) # attention laisser les crochets !!

#for i in range(0,Nb):
#        calc(G[i])

printeverything([calc(G[i]) for i in range(0,Nb)])


#printarraynumbers([calc(G[i]) for i in range(0,Nb)])
#printarraystring([calc(G[i]) for i in range(0,Nb)])

