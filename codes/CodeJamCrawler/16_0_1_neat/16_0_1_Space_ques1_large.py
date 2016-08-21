# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 18:35:48 2016

@author: antariksh
"""

def splitnum(num):
    arr=[]
    while num:
        arr=arr+[num%10]
        num/=10
    return arr
    
def compute(num):
    arr=[1,1,1,1,1,1,1,1,1,1];
    i=1
    while(sum(arr)):
        num2=num*i
        lst=splitnum(num2)
        for j in range(len(lst)):
            arr[lst[j]]=0
        i=i+1
    return num2

T=int(raw_input())
for i in range(T):
    num=int(raw_input())
    if num==0:
        print "Case #%d: "%(i+1)+'INSOMNIA'
    else:
        num2=compute(num)
        print "Case #%d: "%(i+1)+str(num2)