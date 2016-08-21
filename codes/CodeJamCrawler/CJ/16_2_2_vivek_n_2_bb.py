#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 vivek <vivek@Vivek>
#
# Distributed under terms of the MIT license.

arr=[[],[],[]]
for i in range(10):
    arr[0].append(chr(ord('0')+i))
for i in range(10):
    for j in arr[0]:
        arr[1].append(chr(ord('0')+i)+j)
for i in range(10):
    for j in arr[1]:
        arr[2].append(chr(ord('0')+i)+j)

for tc in range(1,input()+1):
    a,b=raw_input().split(' ')
    l=len(a)
    la=[]
    lb=[]
    for i in arr[l-1]:
        fl=True
        for j in range(l):
            if a[j]!=i[j] and a[j]!='?':
                fl=False
        if fl:
            la.append(i)
    for i in arr[l-1]:
        fl=True
        for j in range(l):
            if b[j]!=i[j] and b[j]!='?':
                fl=False
        if fl:
            lb.append(i)
    diff=100000000
    da="10000"
    db="10000"
    for i in la:
        for j in lb:
            nd=abs(int(j)-int(i))
            if nd<diff:
                diff=nd
                da=i
                db=j
            elif nd==diff:
                if int(i)<int(da):
                    da=i
                elif int(i)==int(da) and int(j)<int(db):
                    db=i
    print 'Case #%d: %s %s'%(tc,da,db)
