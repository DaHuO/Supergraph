#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 vivek <vivek@Vivek>
#
# Distributed under terms of the MIT license.


for tc in xrange(1,input()+1):
    s=raw_input()
    dic={}
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    cnt=[0]*10
    while 'Z' in dic and dic['Z']!=0:
        cnt[0]+=1
        for j in 'ZERO':
            dic[j]-=1
    while 'U' in dic and dic['U']!=0:
        cnt[4]+=1
        for j in 'FOUR':
            dic[j]-=1
    while 'F' in dic and dic['F']!=0:
        cnt[5]+=1
        for j in 'FIVE':
            dic[j]-=1
    while 'X' in dic and dic['X']!=0:
        cnt[6]+=1
        for j in 'SIX':
            dic[j]-=1
    while 'S' in dic and dic['S']!=0:
        cnt[7]+=1
        for j in 'SEVEN':
            dic[j]-=1
    while 'G' in dic and dic['G']!=0:
        cnt[8]+=1
        for j in 'EIGHT':
            dic[j]-=1
    while 'W' in dic and dic['W']!=0:
        cnt[2]+=1
        for j in 'TWO':
            dic[j]-=1
    while 'T' in dic and dic['T']!=0:
        cnt[3]+=1
        for j in 'THREE':
            dic[j]-=1
    while 'O' in dic and dic['O']!=0:
        cnt[1]+=1
        for j in 'ONE':
            dic[j]-=1
    while 'N' in dic and dic['N']!=0:
        cnt[9]+=1
        for j in 'NINE':
            dic[j]-=1
    s=''
    for i in range(10):
        for j in range(cnt[i]):
            s+=chr(ord('0')+i)
    print 'Case #%d: %s'%(tc,s)
    #02345678

