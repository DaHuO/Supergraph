from __future__ import division

import os
import os.path, time
import itertools
import numpy as np



#fo=open("test.txt")
#fw=open("test_out.txt","w")
#fo=open("A-small-attempt0.in")
#fw=open("A-small-attempt0.out","w")
fo=open("A-large.in")
fw=open("A-large.out","w")
a=0

def del_el(L,R):
        for i in range(0,len(R)):
                L.remove(R[i])
        return L
                        

def find_el(L):
        Arr=[]
        Drop=""
        for i in range(0,len(L)):
                if L[i]=="Z":
                        Arr.append('0')
                        Drop=Drop+"ZERO"
                elif L[i]=="W":
                        Arr.append('2')
                        Drop=Drop+"TWO"
                elif L[i]=="U":
                        Arr.append('4')
                        Drop=Drop+"FOUR"
                elif L[i]=="X":
                        Arr.append('6')
                        Drop=Drop+"SIX"
                elif L[i]=="G":
                        Arr.append('8')
                        Drop=Drop+"EIGHT"
        P1=del_el(L,Drop)
        Drop=""
        for i in range(0,len(P1)):
                if P1[i]=="O":
                        Arr.append('1')
                        Drop=Drop+"ONE"
                elif P1[i]=="R":
                        Arr.append('3')
                        Drop=Drop+"THREE"
                elif P1[i]=="F":
                        Arr.append('5')
                        Drop=Drop+"FIVE"
                elif P1[i]=="S":
                        Arr.append('7')
                        Drop=Drop+"SEVEN"
        
        P2=del_el(P1,Drop)
        Drop=""
        for i in range(0,len(P2)):
                if P2[i]=="I":
                        Arr.append('9')
                        Drop=Drop+"NINE"
        
        return(''.join(sorted(Arr)))
                



n=int(fo.readline())
for k in range(0,n):
        print "Case #"+ str(k+1)+": "
        #converts line to array of floats
        Probline=fo.readline().strip("\n")
       
     
        
        ans=find_el(list(Probline))
                        
        
       
        
        fw.write("Case #"+ str(k+1)+": ")
        fw.write(ans+"\n")         
fw.close()        
        
                





