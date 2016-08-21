#!/usr/bin/env python2

def all_happy(S):
    for x in S:
        if x == '-':
            return False
    return True

def flipped(S, n):
    m = {'-':'+', '+':'-'}
    return ''.join([m[x] for x in S[:n][::-1]]) + S[n:]

def solve(S):
    V = set()

    Q = [(S, 0)]
    while Q:
        s, d = Q[0]
        Q = Q[1:]
        V.update([s])

        if all_happy(s):
            return d

        for i in xrange(1, len(S)+1):
            f = flipped(s, i)
            if f not in V:
                Q.append((f, d+1))

    raise Exception()

T = int(raw_input())
for i in xrange(1, T+1):
    S = raw_input().strip()
    print "Case #%s: %s" % (i, solve(S))
