#!/usr/bin/env python

def solve(K, C, S):
    assert K == S  # Solving the small set only
    return [1+i*K**(C-1) for i in range(K)]

T = int(raw_input().strip())
for t in range(T):
    K, C, S = [int(n) for n in raw_input().strip().split()]
    sol = solve(K, C, S)
    print 'Case #%d: %s' % (t+1, ' '.join(str(d) for d in sol) if sol else 'IMPOSSIBLE')
