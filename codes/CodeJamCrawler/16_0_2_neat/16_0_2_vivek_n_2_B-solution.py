#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 vivek <vivek@Vivek>
#
# Distributed under terms of the MIT license.

for tc in range(1,input()+1):
    s=list(raw_input())
    l=len(s)
    completed = True
    op = 0
    for i in s:
        if i=='-':
            completed = False
    while not completed:
        front = 0
        while front<l and s[front]=='+':
            s[front]=='-'
            front+=1
        if front!=0:
            op+=1
        end = l-1
        while end>=0 and s[end]=='+':
            end-=1
        if end<0:
            completed = True
            break
        while front<end:
            if s[front]=='+':
                s[front]='-'
            else:
                s[front]='+'
            if s[end]=='+':
                s[end]='-'
            else:
                s[end]='+'
            s[front],s[end]=s[end],s[front]
            front+=1
            end-=1
        if front == end:
            if s[front]=='+':
                s[front]='-'
            else:
                s[front]='+'
        op+=1
        newfl=True
        for i in s:
            if i=='-':
                newfl = False
        completed = newfl
    print 'Case #%d: %d'%(tc,op)
