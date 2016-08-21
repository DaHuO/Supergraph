#!/bin/python
from itertools import combinations
import sys
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')
    
T = int(input.readline())

cache = {}

def p(n, ps):
    if (n, ps) in cache:
        return cache[(n, ps)]

    if len(ps)==1:
        if n==1:
            return ps[0]
        if n==0:
            return 1.0-ps[0]
        return 0.0

    r = p(n, ps[:-1])*(1.0-ps[-1]) + p(n-1, ps[:-1])*ps[-1]
    cache[(n,ps)] = r
    print "p", n, ps, "=", r
    return r

def compute_p(ps):
    assert len(ps) % 2 == 0
    print ps
    return p(len(ps)/2, ps)

def solve():
    N, K = map(int, input.readline().strip().split())
    ps = map(float, input.readline().strip().split())

    assert len(ps) == N

    print "*" , K, ps

    best_p = 0.0
    for subs in combinations(ps, K):
        print "sub", subs
        assert len(subs) == K
        p = compute_p(subs)
        if p > best_p:
            best_p = p

    return best_p

for t in range(T):
    print >> output, 'Case #%s: %s' % (t+1,solve())

