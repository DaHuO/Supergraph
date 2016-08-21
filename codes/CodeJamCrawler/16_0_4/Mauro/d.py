from itertools import *

def solve(K,C,S):
    step = K**(C-1)
    return [str(i+1) for i in xrange(0,K**C,step)]

for case in range(int(raw_input())):
    K, C, S = map(int,raw_input().split())
    ans = solve(K, C, S)
    print "Case #%d: %s" % (case+1,' '.join(ans))
