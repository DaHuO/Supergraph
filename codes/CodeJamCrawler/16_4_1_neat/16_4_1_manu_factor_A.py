#!/bin/python
import sys
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')
    
T = int(input.readline())

def sol(s, N):
    print "sol", s, N
    while N>0:
        r = ''
        for c in s:
            r += {"R": "RS", "P": "PR", "S": "SP"}[c]
        s = r
        N -= 1
    print "=", s
    return s

def order(s):
    n = len(s)
    if n==1:
        return s
    assert n % 2 == 0
    s1 = order(s[:n/2])
    s2 = order(s[n/2:])
    if s1 < s2:
        return s1 + s2
    else:
        return s2 + s1

def solve():
    N, R, P, S = map(int, input.readline().strip().split())
    assert 2**N == R + P + S
    for c in "RPS":
        s = sol(c, N)
        if s.count('R') == R and s.count('P') == P and s.count('S') == S:
            return order(s)
    return 'IMPOSSIBLE'

for t in range(T):
    print >> output, 'Case #%s: %s' % (t+1,solve())

