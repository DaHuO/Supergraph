# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

index = ['A','B','C','D','E','F','G','H','I','G','K','L','M','N','O','P','Q',\
    'R','S','T','U','V','W','X','Y','Z']

def removeOne(P):
    maxItem = max(P)
    maxIndex = P.index(maxItem)
    newP = P[:]
    newP[maxIndex] = newP[maxIndex]-1
    return maxIndex, newP

def removeTwo(P):
    maxItem1 = max(P)
    maxIndex1 = P.index(maxItem1)
    newP = P[:]
    newP[maxIndex1] = newP[maxIndex1]-1
    maxItem2 = max(newP)
    maxIndex2 = newP.index(maxItem2)
    newP[maxIndex2] = newP[maxIndex2]-1
    return maxIndex1, maxIndex2, newP
    

def validRatio(P):
    left = sum(item for item in P)
    ratio = [item/left for item in P]
    return all(item <= 0.5 for item in ratio)


fout = open('A-small-attempt0.out', 'w')
with open('A-small-attempt0.in') as f:
#with open('test.txt') as f:
    nCases = int(f.readline())
    for case in range(nCases):
        N = (int)(f.readline())
        P = list(map(int,f.readline().split()))
        
        solution = []
        
        while any(item > 0 for item in P):
            ansOne, newP = removeOne(P)
            if validRatio(newP):
                P = newP
                solution.append(index[ansOne])
            else:
                ansTwo1, ansTwo2, newP = removeTwo(P)
                P = newP
                ans = index[ansTwo1]+index[ansTwo2]
                solution.append(ans)
        
        print('Case #'+str(case+1)+': '+' '.join(solution), file=fout)
        print('Case #'+str(case+1)+': '+' '.join(solution))

fout.flush()
fout.close()