# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 18:26:47 2016

@author: Varun Joshi
"""

f=open("A-large.in","r")
T=int(f.readline())
c=1
while T>0:
    n=int(f.readline())
    if n==0:
        print "CASE #"+str(c)+": INSOMNIA"
        T-=1
        c+=1
        continue
    arr=[0,1,2,3,4,5,6,7,8,9]
    i=1
    while len(arr)!=0 and i<100:
        t1=n*i
        t=t1
        while t!=0:
            r=t%10
            t/=10
            if r in arr:
                arr.remove(r)
        i+=1
    if(i!=100):
        print "CASE #"+str(c)+": "+str(t1)
    else:
        print "CASE #"+str(c)+": INSOMNIA"   
    c+=1
    T-=1