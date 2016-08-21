#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 vivek <vivek@Vivek>
#
# Distributed under terms of the MIT license.

def getdiv(n):
    if n%2==0:
        return 2;
    lim = int(n**0.5)+1
    i=3
    while i<lim:
        if n%i==0:
            return i
        i+=2
    return n
for tc in range(1,1+input()):
    n,J=map(int,raw_input().split())
    l=1<<(n-1)
    r=1<<n
    done=0
    print 'Case #%d:'%(tc)
    for i in xrange(l,r):
        if i%2==0:
            continue
        res=[]
        x=bin(i)[2:]
        fl = True
        for j in range(2,11):
            y = int(x,j)
            z = getdiv(y)
            if z==y:
                fl = False
                break
            res.append(z)
        if fl:
            done+=1
            print x,
            for i in res:
                print i,
            print
        if done==J:
            break
