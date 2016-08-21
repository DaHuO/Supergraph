#! /usr/bin/env python

from pyprimes import factorise
from pyprimes import isprime

fname = 'C-small'

fin = open(fname+'.in', 'r')
fout = open(fname+'.out', 'w')

def fact(x):
    f = []
    for i in range(2, 11):
        n = int(bin(x)[2:], i)
        if isprime(n):
            return None
        f.append(next(factorise(n))[0])
    return f

def solve(N, J):
    r = []
    for x in range(2 ** (N - 1) + 1, 2 ** N, 2):
        f = fact(x)
        if f is not None:
            r.append([bin(x)[2:]] + list(map(str, f)))
            if len(r) == J:
                return r

T = int(fin.readline())
for i in range(1, T+1):
    fout.write("Case #"+str(i)+":\n")
    N, J = map(int, fin.readline().strip().split())
    x = solve(N, J)
    for a in x:
        fout.write(' '.join(a)+"\n")
fout.close()
fin.close()
