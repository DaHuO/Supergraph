#!/bin/python
import math

T = int(raw_input())
N, J = raw_input().split()
N, J = int(N), int(J)

print 'Case #1:'
for i in xrange(2**(N-1)+1, 2**N,2):
    r = []
    i = str(bin(i))[2:]
    for b in range(2, 11):
        n = int(i,b)
        for d in xrange(2, 10): #int(math.sqrt(n))):
            if n % d == 0:
                r.append(str(d))
                break
    if len(r) == 9:
        print "%s " % i + ' '.join(r)
        J -= 1
    if J == 0: break
