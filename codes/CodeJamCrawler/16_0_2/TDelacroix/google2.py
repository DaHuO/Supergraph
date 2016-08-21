# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 11:51:15 2016

@author: thomas
"""


g = open('output2', 'w')

f = open('input2', 'r')

n=int(f.readline()[:-1])

pIn = []
for x in xrange(n):
    pIn +=[f.readline()[:-1]]

pOut = ''

def countMin(s):
    m=0
    i=0
    while i<len(s):
        if s[i]=='-':
            while s[i]=='-':
                i+=1
                if i==len(s):
                    break
            m+=1
        else:
            i+=1
    return m

pOut = ''

def function(pIn,pOut):
    for i in xrange(len(pIn)):
        m=countMin(pIn[i])
        if pIn[i][0]=='-':
            N=2*m-1
        else:
            N=2*m
        pOut += 'Case #'+str(i+1)+': '+str(N)+'\n'
    return pOut


out = function(pIn,pOut)


g.write(out)