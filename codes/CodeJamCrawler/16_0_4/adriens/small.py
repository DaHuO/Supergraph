import math

def solu(K,C,S):
    if S<math.ceil(K/C): return 'IMPOSSIBLE'

    if C<K: 
        l = [sum([(p*C+i)*K**(C-i-1) for i in range(0,C)])+1 for p in range(0, int(K/C))] + [K**C-sum([ i*K**(C-i-1)  for i in range(C)])]
        if l[-1]==l[-2]:
           l = l[:-1]
        return ' '.join(map(str,l))

    else:
        l = sum([i*K**(K-i-1) for i in range(1,K)])+1
        return l

import sys

T = int(sys.stdin.readline())
for t in range(T):
    K,C,S = map(int, sys.stdin.readline().split())
    print "Case #%i:"%(t+1), solu(K,C,S)
