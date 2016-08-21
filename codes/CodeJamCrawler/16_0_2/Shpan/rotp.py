# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 18:40:40 2016

@author: WAM
"""

f = open("input.txt", "r")
lines=f.read().splitlines()
f.close

g = open("output.txt", "w")
numCases = int(lines[0])
for caseNum in range(1,numCases+1):
    line = lines[caseNum]
    prevc = line[0]
    if prevc == '-':
        topCake = 1
    else:
        topCake = 0
            
    numFlips = 0
    for c in line:
        if c != prevc:
            numFlips = numFlips + 1
        prevc = c
    numFlips = numFlips + (numFlips+topCake)%2
    g.write('Case #{}: {}\n'.format(str(caseNum),str(numFlips)))
    
g.close
