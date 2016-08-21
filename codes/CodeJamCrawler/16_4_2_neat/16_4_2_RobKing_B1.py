from sys import *
from numpy import *
import itertools

def getprobability(inlist, result):
    p = 0
    for combo in itertools.combinations(range(len(inlist)), result):
        currentP = 1
        for i in range(len(inlist)):
            if i in combo:
                currentP *= inlist[i]
            else:
                currentP *= 1 - inlist[i]
        p += currentP
    return p

def solve(T, N, K, L):
    bestp = 0
    for combo in itertools.combinations(L, K):
        p = getprobability(combo, K/2)
        if p > bestp:
            bestp = p
    print "Case #%d: %f" %(T+1, bestp)


cases = int(raw_input())
for T in xrange(cases):
    N, K = raw_input().split()
    N = int(N)
    K = int(K)
    L = raw_input().split()
    L = map(float, L)
    solve(T, N, K, L)
