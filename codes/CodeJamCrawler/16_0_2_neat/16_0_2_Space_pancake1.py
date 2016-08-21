# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 18:33:28 2016

@author: antariksh
Pancake problem

-group +'s and -'s
-if [0]='+' flip to '-'
-take right most '-' and flip till dat pos
"""
def flip(arr,pos,maxl):
    arr2=[]
    i=pos
    while i>=0:
        arr2+=[not(arr[i])]
        i=i-1
    i=pos+1
    while i<maxl:
        arr2+=[arr[i]]
        i=i+1
    return arr2
    
def posneg(arr,maxl):
    l=maxl
    i=l-1
    while arr[i]==True:
        i=i-1
    return i

def str2bool(strr):
    ch=strr[0]
    if ch=='-':
        bola=False
    else:
        bola=True
    arr=[bola]
    for i in range(1,len(strr)):
        if ch!=strr[i]:
            ch=strr[i]
            bola=not(bola)
            arr+=[bola]
    return arr

def compute(arr):
    ct=0
    l=len(arr)
    while sum(arr)<l:
        if arr[0]==True:
            arr[0]=False
        else:
            pos=posneg(arr,l)
            arr=flip(arr,pos,l)
        ct=ct+1
        #print arr        
    return ct

T=int(raw_input())
for i in range(T):
    strr=str(raw_input())
    # formatting string to bool and reducing
    arr=str2bool(strr)
    #print arr
    print "Case #%d: "%(i+1)+str(compute(arr))    