# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 19:07:28 2016

@author: Varun Joshi
"""

f=open("B-large.in","r")
T=int(f.readline())
c=1
while T>0:
    fl=0
    s=(f.readline()).strip()
    flag=0
    if len(s)==1:
        #print s
        if s[0]=='-':
            fl=1
        else:
            fl=0
        print "CASE #"+str(c)+": "+str(fl)
        c+=1
        T-=1
        continue
    
    
    if s[0]=='+':
        flag=1
    elif s[0]=='-' and s[1]=='+':
        flag=1
        fl=1
    i=1
    while i<len(s):
        if s[i]=='-':
            while i<len(s) and s[i]!='+':
                i+=1
            if flag==0:
                fl+=1
                flag=1
            else:
                fl+=2
        else:
            i+=1
    print "CASE #"+str(c)+": "+str(fl)
    c+=1
    T-=1
f.close()