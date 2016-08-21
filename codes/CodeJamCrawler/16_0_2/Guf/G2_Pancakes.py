# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:28:50 2016

@author: zozo
"""

import numpy as np
import pandas as pd
import string

fname = 'B-large.in'
f = open(fname,'r')

nlines = f.readline().replace('\n','') #
inputs = []
for l in range(int(nlines)):
    inputs.append(f.readline().replace('\n',''))

f.close()


def flip(s):
    return s[::-1].translate(string.maketrans('+-','-+'))




def opflips(panc):
    op = 0
    while panc.replace('+','') != '':
        while panc[-1]=='+':
            panc = panc[:len(panc)-1]
        if panc == '':
            break
        else:
            k=0
            while panc[:k+1].replace('+','')=='':
                k+=1
            
            if k==0:
                panc = flip(panc)
            else :
                panc = flip(panc[:k]) + panc[k:]
            op+=1
    return op







  
fout = open('fout','w')     
k=0
for panc in inputs:
    k+=1    
    fout.write('Case #'+str(k)+': ' + str(opflips(panc))+'\n')
    
fout.close()