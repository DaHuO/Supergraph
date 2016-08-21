#!/usr/bin/python
from math import sqrt

d = {}

def checkPrime(s, n):
    p = int(s, n)
    for i in xrange(int(sqrt(p))+2):
        if (i > 1) and (p % i) == 0:
            return i
    return 1


for i in range(pow(2,15)+1, pow(2,16), 2):
    s = bin(i)[2:]
    l = []
    ok = True
    for j in range(2,11):
        a = checkPrime(s, j)
        if a == 1:
            ok = False
            break
        l.append(a)
    if ok:
        d[s] = l
    if(len(d) >= 50):break

print 'Case #1'
for i in d:
    print i,
    for j in d[i]:
        print j,
    print
        