# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:20:33 2016

@author: thomas
"""

g = open('output1', 'w')

f = open('input1', 'r')

n=int(f.readline()[:-1])

pIn = []
for x in xrange(n):
    pIn +=[int(f.readline()[:-1])]

pOut = ''

def function(pIn,pOut):
    for i in xrange(len(pIn)):
        if pIn[i]==0:
            pOut += 'Case #'+str(i+1)+': '+'INSOMNIA'+'\n'
        else:
            D=[0,0,0,0,0,0,0,0,0,0]
            s=0
            while D <> [1,1,1,1,1,1,1,1,1,1]:
                s+=1
                Nxs=[int(j) for j in str(pIn[i]*s)]
                for k in xrange(len(Nxs)):
                    D[Nxs[k]] = 1
            pOut += 'Case #'+str(i+1)+': '+ str(pIn[i]*s)+'\n'
    return pOut


out = function(pIn,pOut)



g.write(out)

