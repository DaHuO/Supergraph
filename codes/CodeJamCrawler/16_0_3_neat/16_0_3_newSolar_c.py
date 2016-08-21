#!/usr/bin/env python
"""
# Author: palayutm
# Created Time : Sat 09 Apr 2016 03:43:45 PM CST

# File Name: c.py
# Description:

"""
print ('Case #1:')
x = (1<<15) + 1
n = 50
while True:
    a = []
    flag = True
    for base in range (2, 11):
        if not flag:
            break
        num = int(bin(x)[2:], base=base)
        t = 2
        while True:
            if num % t == 0:
                a.append (t)
                break
            if t*t >= num:
                flag = False
                break
            t += 1
    if flag:
        st = bin(x)[2:]
        #xx = [int(st, i) for i in range (2, 11)]
        for i in a:
            st += ' ' + str(i)
        print (st)
        #print (xx)
        n -= 1
        if n == 0:
            break
    x += 2

