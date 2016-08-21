#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 vivek <vivek@Vivek>
#
# Distributed under terms of the MIT license.

f=open('pre')
x=f.readlines()
for i in range(len(x)):
    x[i]=map(int,x[i].strip('\n').split())

for i in range(1,input()+1):
    n=input()
    bff=map(int,raw_input().split())
    lis=[m for m in range(n)]
    res=0
    done = False
    for k in x:
        flag=True
        j=len(k)
        if j<=res or j>n or max(k)>=n:
            continue
        for l in range(j):
            #print k[(l+1)%j],k[l],k[(l-1+j)%j]
            if not(lis[k[(l+1)%j]]==bff[lis[k[l]]]-1 or lis[k[(l-1+j)%j]]==bff[lis[k[l]]]-1):
                flag = False
                break
        if flag:
            res=max(res,j)
    print "Case #%d:"%(i),res
            



