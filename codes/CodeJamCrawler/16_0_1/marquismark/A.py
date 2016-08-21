#!/usr/bin/env python

TEST="""5
0
1
2
11
1692"""
#raw_input = iter(TEST.splitlines()).next

ALL = set("0123456789")

def solve(N):
    if N == 0:
        return "INSOMNIA"
    sN = str(N)
    i = 1
    SEEN = set(sN)
    while SEEN != ALL:
        i += 1
        SEEN.update( set(str(i*N)) )
    return i*N


T = int(raw_input())
for case in range(1,T+1):
    N = int(raw_input().strip())
    print("Case #%s: %s" % (case, solve(N)))
