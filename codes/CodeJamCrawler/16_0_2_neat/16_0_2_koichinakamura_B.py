from numpy import *

def solve(S):
    c = 0
    p = S[0]
    for i in range(1, len(S)):
        if p != S[i]:
            c += 1
            p = S[i]
    if S[-1] == '-':
        c += 1
    return c

for case in range(input()):
    ans = solve(raw_input())
    print 'Case #{}: {}'.format(case+1, ans)
