#!/usr/bin/env python2
from sympy import *

def check(s):
    if s[0] != '1' or s[-1] != '1':
        return False
    for i in range(2,11):
        num = int(b,i)
        if isprime(num):
            return False
    return True

N = 16
J = 50

ans = []
for v in range(1<<N):
    b = bin(v)[2:].rjust(N,'0') 
    if check(b):
        ans.append(v)
    if len(ans) == J:
        break

print 'Case #1:'
for v in ans:
    b = bin(v)[2:].rjust(N,'0')
    s = [b]
    for i in range(2,11):
        num = int(b, i)
        s.append(str(factorint(num).items()[0][0]))
    print ' '.join(s)
