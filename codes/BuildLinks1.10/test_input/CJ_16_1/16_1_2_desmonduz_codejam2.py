# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 02:35:54 2016

@author: Desmond
"""

import numpy as np
from collections import defaultdict

with open("B-large.in","r") as f:
    l=f.readlines()
    k=int(l[0])
    problems=list()
    i=1
    while i<len(l):
        n=int(l[i])
        endN=2*n-1
        problems.append((n, map(lambda x: map(int, x.strip().split()), l[i+1:i+1+endN])))
        i=i+1+endN

output=""
for i, p in enumerate(problems):
    countNums=defaultdict(int)
    for v in p[1]:
        for t in v:
            countNums[t]+=1
    
    numsOut=[]
    for k in countNums:
        if countNums[k] % 2==1:
            numsOut.append(k)
    sol=" ".join([str(s) for s in sorted(numsOut)])
    output += "Case #%d: %s\n" % (i+1,sol)
print output

with open("output4.txt", "w") as f:
    f.write(output)