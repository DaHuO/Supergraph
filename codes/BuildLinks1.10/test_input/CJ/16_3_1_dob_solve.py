#!/usr/bin/env python
import sys
import time
import collections
from functools import reduce

_dbg = '-d' in sys.argv[1:]

def out(s):
    sys.stdout.write(s)
    sys.stdout.flush()

if _dbg:
    def dbg(s):
        if isinstance(s, str):
            out(s)
        else:
            out(str(s) + '\n')
else:
    def dbg(s):
        pass

def readline():
    return sys.stdin.readline().strip()

def readfloat():
    return float(readline())

def readfloats():
    return [float(x) for x in readline().split()]

def readint():
    return int(readline())

def readints():
    return [int(x) for x in readline().split()]

class Party(object):
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def dec(self):
        self.count -= 1

    def __str__(self):
        return '{0.name}:{0.count}'.format(self)

def foo(l):
    dbg(' '.join([str(p) for p in l]) + '\n')

def solve_case():
    N = readint()
    Np = readints()
    S = sum(Np)
    P = [Party(chr(ord('A') + i), p) for i, p in enumerate(Np)]
    r = []
    while S:
        P.sort(key=lambda x: -x.count)
        foo(P)
        if S == 3:
            r.append(P[0].name)
            P[0].dec()
            S -= 1
        elif (P[1].count > 1) or (S == 2):
            r.append(P[0].name + P[1].name)
            P[0].dec()
            P[1].dec()
            S -= 2
        else:
            r.append(P[0].name)
            P[0].dec()
            S -= 1
    return ' '.join(r)

def main():
    fmt = 'Case #{0:d}: {1}\n'
    cases = readint()
    if _dbg:
        for c in range(1, cases + 1):
            t0 = time.time()
            out(fmt.format(c, solve_case()))
            dbg('{:.6f}\n'.format(time.time() - t0))
    else:
        for c in range(1, cases + 1):
            out(fmt.format(c, solve_case()))

if __name__ == '__main__':
    main()

