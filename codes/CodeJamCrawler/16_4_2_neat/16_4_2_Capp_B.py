#!/usr/bin/env python

from sys import stdin, stderr
from itertools import combinations

def Solve(N, K, Ps):
    ret = 0.
    for Ks in combinations(Ps, K):
        val = 0.
        for Ksub in combinations(Ks, K / 2):
            Ksub2 = list(Ks)
            for v in Ksub: Ksub2.remove(v)
            val_tmp = 1.
            for pp in Ksub  : val_tmp *= pp
            for pp in Ksub2 : val_tmp *= (1 - pp)
            val += val_tmp
            pass
        ret = max(ret, val)
    return ret

#print Solve(12, 1365, 1365, 1366)
for T in range(int(stdin.readline())):
    print 'Case #%d:' % (T+1),

    N, K = [int(w) for w in stdin.readline().split()]
    Ps = [float(w) for w in stdin.readline().split()]
    
    #print N, R, P, S
    print Solve(N, K, Ps)
