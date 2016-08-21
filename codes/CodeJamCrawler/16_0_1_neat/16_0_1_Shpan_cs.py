# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 20:49:16 2016

@author: WAM
"""

f = open("input.txt", "r")
lines=f.read().splitlines()
f.close

g = open("output.txt", "w")
numCases = int(lines[0])
for caseNum in range(1,numCases+1):
    N = int(lines[caseNum])
    if N==0:
        g.write('Case #{}: {}\n'.format(str(caseNum),'INSOMNIA'))
    else:
        numberSeen = [False] * 10
        i=0
        while sum(numberSeen)<10:
            i=i+1
            num=N*i
            strNum=str(num)
            for c in strNum:
                cNum = int(c)
                numberSeen[cNum]=True
        

        g.write('Case #{}: {}\n'.format(str(caseNum),str(num)))
    
g.close
