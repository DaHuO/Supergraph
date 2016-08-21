# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 17:34:17 2016

@author: Desmond
"""
import numpy as np

with open("B-large.in","r") as f:
    l=f.readlines()
    n=int(l[0])
    problems=list()
    for i in range(n):
        problems.append([True if s=="+" else False for s in l[i+1].strip()]) 

#def flip(vals):
#   return [not(v) for v in vals][-1::-1]

output=""
t=1
for p in problems:
    pn=len(p)

    v=0 if p[0] else 1
    firstTrue=0
    for i in range(pn):
        if p[i]: 
            firstTrue=i
            break
        firstTrue=pn
    if firstTrue<pn:
        for i in range(firstTrue,pn):
            if p[i-1] and not p[i]: v+=2
    
    output += "Case #%d: %d \n" % (t,v)
    t+=1
    
#print output
with open("output.txt", "w") as f:
    f.write(output)