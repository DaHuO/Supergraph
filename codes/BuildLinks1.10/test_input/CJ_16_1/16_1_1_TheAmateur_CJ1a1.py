# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 17:57:33 2016

@author: Varun Joshi
"""

f=open("A-large (1).in","r")
T=int(f.readline())
c=1

while T>0:
    n=(f.readline().strip())
    #print n
    res=n[0]
    for i in n[1:]:
        if ord(i)<ord(res[0]):
            res+=i
        else:
            res=i+res
    print "CASE #"+str(c)+": "+res
    c+=1
    T-=1