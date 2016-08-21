# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:28:50 2016

@author: zozo
"""

import numpy as np
import pandas as pd

fname = 'A-large.in'
f = open(fname,'r')

nlines = f.readline().replace('\n','') #
inputs = []
for l in range(int(nlines)):
    inputs.append(int(f.readline().replace('\n','')))

f.close()



def SheepC(N):
    digits = set()
    stop=False
    i=1
    while stop==False:
        D=i*N
        for c in str(D):
            digits.add(c)
        if len(digits)==10:
            stop=True
            return str(D)
        else:
            i+=1
            if i>9999: 
                return 'INSOMNIA'
                break
  
fout = open('fout','w')     
k=0
for N in inputs:
    k+=1    
    fout.write('Case #'+str(k)+': ' + SheepC(N)+'\n')
    
fout.close()