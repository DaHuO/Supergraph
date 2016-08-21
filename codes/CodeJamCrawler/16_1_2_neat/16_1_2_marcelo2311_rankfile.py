'''
Created on 15 de abr. de 2016

@author: Marcelo
'''
from math import floor

def readint(): return int(raw_input())
def readarray(f): return map(f, raw_input().split())
import sys


_T = readint()
for t in range(1, _T+1):
    S = readint()
    A = []
    
    for s in range(S*2-1):
        A = A + raw_input().split(" ")
    
    l = A
   
    uset=  set([int(x) for x in l if l.count(x)%2 > 0])
    
    unsorted = list(uset)
    
    
    print 'Case #%i:'%(t), sorted(unsorted)