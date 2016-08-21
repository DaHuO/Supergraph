#!/usr/bin/python3

import sys

def digits(v):
    return list(str(v))

def repl(N):
    if N == 0:
        return "INSOMNIA"
    current = N
    seen = set(digits(N))
    while len(seen) < 10:
        current += N
        seen = seen.union(set(digits(current)))
    return str(current)

T = int(sys.stdin.readline().strip())
for i in range(T):
    N = int(sys.stdin.readline().strip())
    print ("Case #%d: %s" % (i+1, repl(N)))
