#!/usr/bin/python
# -*- coding: utf-8 -*-

def solve(N, R, P, S):
    if N == 1:
        if R == 0:
            return "PS"
        elif P == 0:
            return "RS"
        else:
            return "PR"
    else:
        if R%2 == 0:
            return solve(N-1, R/2, P/2+1, S/2) + solve(N-1, R/2, P/2, S/2+1)
        elif P%2 == 0:
            return solve(N-1, R/2+1, P/2, S/2) + solve(N-1, R/2, P/2, S/2+1)
        else:
            return solve(N-1, R/2, P/2+1, S/2) + solve(N-1, R/2+1, P/2, S/2)

T = int(raw_input().strip())

for t in xrange(0, T):
    N, R, P, S = tuple(map(int, raw_input().strip().split()))

    if {R, P, S} == {2**N / 3, 2**N / 3 + 1}:
        answer = solve(N, R, P, S)
    else:
        answer = "IMPOSSIBLE"
    
    print "Case #%i: %s\n" % (t+1, answer)


