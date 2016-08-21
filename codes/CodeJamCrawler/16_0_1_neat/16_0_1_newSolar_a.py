#!/usr/bin/env python
"""
# Author: palayutm
# Created Time : Sat 09 Apr 2016 03:01:36 PM CST

# File Name: a.py
# Description:

"""
T = int(input ())
for cas in range (T):
    n = int(input ())
    se = set()
    if n == 0:
        print ('Case #%i: INSOMNIA' % (cas+1))
    else:
        cnt = 0
        while True:
            cnt += n
            for x in str(cnt):
                se.add (x)
            if len (se) == 10:
                print ('Case #%i: %i' % (cas+1, cnt))
                break



