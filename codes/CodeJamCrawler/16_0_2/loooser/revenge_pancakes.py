#!usr/bin/env python
from __future__ import print_function
from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *

def main():
    cases=int(raw_input())
    for i in xrange(cases):
        pattern=raw_input()
        pattern=map(lambda x: 0 if x== '+' else 1, pattern)
        l=len(pattern)
        count=0
        while 1 in pattern:
            if l > 0:
                if pattern[l-1]==1:
                    pattern=flip(pattern,l-1)
                    count+=1
                l-=1
        print("Case #",i+1,":"," ",count,sep="")

def flip(a,index):
    rev=list()
    it=0
    for i in xrange(index,-1,-1):
        a[i],a[it]=a[it],a[i]
        it+=1
    for i in xrange(index,-1,-1):
        if(a[i]==0):
            a[i]=1
        else:
            a[i]=0
    return a

if __name__=='__main__':
	main()