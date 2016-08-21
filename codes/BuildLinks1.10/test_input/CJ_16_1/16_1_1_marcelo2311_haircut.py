'''
Created on 15 de abr. de 2016

@author: Marcelo
'''
from math import floor

def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())
import sys


def getString(S):
    
    prev = []

    for s in S:
    
        if (len(prev) == 0):
            prev.append(s)    
            continue
  
        fut = prev

        for p in range(len(prev) ):

            prev[p] = prev[p] + s
        
            prev.append(s+prev[p][:-1])
            #print prev
            #print fut[p], p
        
    return  prev
        
    
    

_T = readint()
for t in range(1, _T+1):
    S = raw_input()

    st = getString(S)
   
    #print max(st)
    
   
    
    print 'Case #%i:'%(t), max(st)