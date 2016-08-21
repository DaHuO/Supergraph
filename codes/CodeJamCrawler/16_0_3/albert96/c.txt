# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 22:46:56 2016

@author: shak
"""
#16
#50
#32
#500
n = 32
m = 500
L = []
for mask in range(2**(n-2)):
    v = mask*2+1+(2**(n-1))
    fl = 0
    U = []
    for b in range(2,11):
        val = 0
        for i in range(n):
            if (2**i)&v!=0:
                val = val+(b**i)
        e = 1
        for u in range(2,val):
            if u > 10000:
                break
            if u*u > val:
                break
            if val%u==0:
                e = u
                break
        if e==1:
            fl = 1
            break
        U.append(e)
        if b==10:
            U.insert(0,val)
    if fl==0:
        L.append(U)
    if len(L)==m:
        break
import csv
with open("output1.txt", 'w') as f:
   writer = csv.writer(f, delimiter=' ')
   writer.writerows(L)
    

        
    