#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 vivek <vivek@Vivek>
#
# Distributed under terms of the MIT license.

from itertools import combinations as comb
for tc in range(1,input()+1):
    n=input()
    l=[]
    res=0
    for i in range(n):
        l.append(raw_input().split())
    for m in range(1,1<<n):
        a={}
        b={}
        c=[0 for i in range(n)]
        k=m
        cnt=0
        for j in range(n):
            if k%2==1:
                cnt+=1
                c[j]=1
                if l[j][0] in a:
                    a[l[j][0]]+=1
                else:
                    a[l[j][0]]=1
                if l[j][1] in b:
                    b[l[j][1]]+=1
                else:
                    b[l[j][1]]=1
            k>>=1
        flag=True
        for k in range(n):
            if c[k]==1 and (a[l[k][0]]!=1 and b[l[k][1]]!=1):
                flag=False

        if flag:
            nflag=True
            for j in range(n):
                if c[j]==0:
                    if l[j][0] not in a or l[j][1] not in b:
                        nflag=False
                        break
            if nflag:
                res=max(res,n-cnt)
    print "Case #%d: %d"%(tc,res)
