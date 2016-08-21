def solve(N, R, P, S):
    # P -> R -> S
    sP = 'P'
    sR = 'R'
    sS = 'S'

    def f (a, b):
        return ''.join(sorted([a,b]))

    #print P, R, S
    #print sP, sR, sS

    for i in range(N):
        t = P + S - R

        if t < 0 or t % 2 != 0:
            return

        t = t / 2
        P = P - t
        R = S - t
        S = t

        if P < 0 or R < 0 or S < 0:
            return

        sP, sR, sS = f(sP,sR), f(sR, sS), f(sP, sS)
        #print P, R, S
        #print sP, sR, sS

    if P < 0 or R < 0 or S < 0:
        return

    if sum([P, R, S]) == 1:
        if P:
            return sP;
        if R:
            return sR;
        return sS;

import sys
sys.stdin = open('A-large.in', 'rt')
sys.stdout = open('A-large.out', 'wt')

T = int(raw_input().strip())
for t in range(1, T+1):
    N, R, P, S = map(int, raw_input().split(' '))
    print 'Case #{}:'.format(t), (solve(N, R, P, S) or "IMPOSSIBLE")
