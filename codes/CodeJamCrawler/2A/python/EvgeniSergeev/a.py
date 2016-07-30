#from math import *
#from collections import Counter
def rl(s): return xrange(len(s))

INF = 2147483647


import sys
stdin = sys.stdin

T =        int( stdin.readline().strip() )

def rotateLex(s):
    length = 1
    while length < len(s):
        for k in range(0, len(s), 2*length):
            if s[k:k+length] > s[k+length: k+2*length]:
                s[k+length:k+2*length], s[k:k+length] = (s[k:k+length],
                                                         s[k+length:k+2*length])
        length *= 2

    return s

must_have = {'R' : ['R', 'S'],
             'P' : ['P', 'R'],
             'S' : ['S', 'P']}

for icase in range(1, T+1):
    N, R, P, S = map(int, stdin.readline().strip().split())

    best = None
    for seed in 'RPS':
        s = [seed]
        while len(s) < (1 << N):
            s2 = []
            for letter in s:
                s2.extend(must_have[letter])
            s = s2
        rs = s.count('R')
        ps = s.count('P')
        #print rs, ps, (1 << N) - rs-ps
        if rs == R and ps == P:
            here = rotateLex(s)
            if None is best or best > here:
                best = here

    rr = "IMPOSSIBLE" if best is None else ''.join(best)
    print 'Case #%d:' % icase, rr

