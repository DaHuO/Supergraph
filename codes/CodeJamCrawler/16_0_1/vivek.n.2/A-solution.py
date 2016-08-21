#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 vivek <vivek@Vivek>
#
# Distributed under terms of the MIT license.

for tc in range(1,input()+1):
    i=input()
    if i==0:
        print 'Case #%d: INSOMNIA'%(tc)
        continue

    x=set([])
    a=0
    while len(x)<10:
        a+=i
        t=a
        while t>0:
            y=t%10
            t/=10
            x.add(y)
    print 'Case #%d: %d'%(tc,a)
