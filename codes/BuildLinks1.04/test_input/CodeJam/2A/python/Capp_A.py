#!/usr/bin/env python

from sys import stdin, stderr
from struct import pack

def Solve(N, R, P, S):
    a = max([R, P, S])
    b = min([R, P, S])
    if a - b > 1: return 'IMPOSSIBLE'
    clist = []
    if R == a: clist += ['R']
    if P == a: clist += ['P']
    if S == a: clist += ['S']
    for c in ['R', 'P', 'S']:
        if not c in clist: clist += [c]
        pass
    Nval = 2 ** N
    ret = (clist[0] + clist[1] + clist[2]) * (Nval / 3)
    if Nval % 3 == 1: ret += clist[0]
    if Nval % 3 == 2: ret += clist[0] + clist[1]
    for n in range(N):
        pos  = 0
        ret2 = ''
        while pos < 2 ** N:
            s1 = ret[pos        : pos + 2**n    ]
            s2 = ret[pos + 2**n : pos + 2**n * 2]
            if s1 < s2: ret2 += s1 + s2
            else:       ret2 += s2 + s1
            pos += 2**n * 2
            pass
        ret = ret2
    return ret

#print Solve(12, 1365, 1365, 1366)
for T in range(int(stdin.readline())):
    print 'Case #%d:' % (T+1),

    N, R, P, S = [int(w) for w in stdin.readline().split()]
    #print N, R, P, S
    print Solve(N, R, P, S)
