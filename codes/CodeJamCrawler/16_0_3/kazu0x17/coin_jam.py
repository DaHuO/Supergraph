#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def toBinary(val):
    s = ""
    while(val > 0):
        if val & 1:s = s + "1"
        else:s = s + "0"
        val /= 2
    s = s[::-1]
    return s

def ChangeBase(val, base):
    length = len(val)
    res = 0;
    for i in xrange(length):
        res *= base;
        if val[i] == '1':
            res += 1;
    return res

    
t = raw_input()
n, line = map(int, raw_input().split(' '))
cnt = 0
n -= 1
val = (1<<n)
print "Case #1: "
for i in xrange(20000):
    i += 1
    if cnt == line: break
    s = toBinary(val + i)
    if s[len(s) - 1] != '1': continue
    ans = []
    for j in xrange(2, 11):
        after = ChangeBase(s, j)
        k = 2
        is_prime = True
        
        while k*k <= after:
            if after%k == 0:
                is_prime = False
                ans.append(k)
                break
            k += 1
        if is_prime:
            break
        
        if j == 10:
            print s, ans[0], ans[1], ans[2], ans[3], ans[4], ans[5], ans[6], ans[7], ans[8]
            cnt += 1
