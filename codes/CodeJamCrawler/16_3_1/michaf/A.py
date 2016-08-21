#!/usr/bin/env python3

import sys, os, re
import collections
import math
import operator

sys.setrecursionlimit(200)

def debug(x):
    print(x, file=sys.stderr) 

def solve(p, q):
    ans = ''
    while len(q) > 0:
        maxes = sorted(q, key=lambda x: q[x[0]], reverse=True)
        #debug(maxes)
        m = maxes[0]
        if len(q) != 2 or (len(q) == 2 and q[maxes[0]] > q[maxes[1]]):
            ans += m + ' '
            q[m] -= 1
        else:
            m2 = maxes[1] 
            ans += m + m2 + ' '
            q[m] -= 1
            q[m2] -= 1
            if q[m2] <= 0:
                del q[m2]

        if q[m] <= 0:
            del q[m]

    ans = ans.strip() 
    return ans

def main():
    inp = [x.strip() for x in sys.stdin.readlines()]
    T = int(inp[0])
    P = inp[1::2]
    Q = inp[2::2]

    debug(T)
    debug(P)
    debug(Q)

    for numinput, (p, q) in enumerate(zip(P, Q), 1):
        p = int(p)
        q = {chr(d+ord('A')): int(x) for d, x in enumerate(q.split(" "))}
        debug("p: %s, q: %s" % (p, q))
        ans = solve(p, q)
        print("Case #%d: %s" % (numinput, ans))

if __name__ == '__main__':
    main()
