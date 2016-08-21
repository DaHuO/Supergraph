#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 vivek <vivek@Vivek>
#
# Distributed under terms of the MIT license.

for i in range(1,input()+1):
    n=input()
    lis=[]
    cnt=[0]*2501
    res=[]
    for j in range(2*n-1):
        lis.append(map(int,raw_input().split()))
    for j in range(2*n-1):
        for k in range(n):
            cnt[lis[j][k]]+=1
    for j in range(1,2501):
        if cnt[j]%2==1:
            res.append(j)
    res.sort()
    print "Case #%d:"%(i),
    for j in res:
        print j,
    print
