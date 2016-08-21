from math import sqrt, pow, log, ceil, log10
from sys import stdin
import random

debug = False

def check(P, ans):
    sums = sum(P)
    maxs = max(P)

    if maxs > sums / 2:
        print "Error", ans, P
        print P
        exit(-1)

def sol(N,P):

    if debug:
        print " ->", P

    ans = ""

    while True:

        sums = sum(P)
        maxs = max(P)

        if maxs == 0:
            break

        if debug:
            print "h", P, maxs, sums

        if sums % 2 == 0: 
            ind = P.index(maxs)
            ans += " " + chr(65 + ind)
            P[ind] -= 1

            maxs = max(P)
            ind = P.index(maxs)
            ans += chr(65 + ind)
            P[ind] -= 1
        else:
            ind = P.index(maxs)
            ans += " " + chr(65 + ind)
            P[ind] -= 1

        # Check
        check(P, ans)

    return ans

T = int(stdin.readline())

for i in range(1,T+1):

    N, = map(int, stdin.readline().split())
    P = map(int, stdin.readline().split())
    
    print "Case #" + str(i) + ":", 

    print sol(N,P)