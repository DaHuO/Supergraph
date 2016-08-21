# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:37:18 2016

@author: zozo
"""
import string
import pandas as pd
import numpy as np

fname = 'A-large.in'
f = open(fname,'r')

nlines = f.readline().replace('\n','') #
inputs = []
for l in range(int(nlines)):
    nparties = f.readline().replace('\n','')
    inputs.append(f.readline().replace('\n',''))

f.close()

outstr = ''

indices = range(len(numb))


for k in range(len(inputs)):
    outstr +='Case #'+ str(k+1) + ': '
    numb = np.array([int(x) for x in inputs[k].split(' ')])
    names = np.array(list(string.ascii_uppercase)[:len(numb)])
    
    
    while numb.sum()>1:
        numbsorted =  np.sort(numb)[::-1]
        
        if numb.sum()==3 and numbsorted[0]==numbsorted[1]:
            order = numb.argsort()[::-1][:1]
            numb[order[0]]=numb[order[0]]-1
            outstr+= names[order[0]]*1 + ' '
        else:
            if numbsorted[0]==numbsorted[1]:
                order = numb.argsort()[::-1][:2]
                for i in range(len(order)):
                    outstr+= names[order[i]]
                    numb[order[i]]=numb[order[i]]-1
                outstr+=' '
            else:
                order = numb.argsort()[::-1][:1]
                outstr+= names[order[0]]*2 + ' '
                numb[order[0]]=numb[order[0]]-2
        
    if numb.sum()==1:
        order = numb.argsort()[::-1][:1]
        outstr+= names[order[0]]*1

    outstr +='\n'
    





fout = open(fname + '.sub','w')
fout.writelines(outstr)
fout.close()