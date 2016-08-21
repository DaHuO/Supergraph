from sys import *

def getexpectedcount(N):
    if N == 1:
        return [1, 1, 0]
    else:
        expectedcounts = getexpectedcount(N- 1)
        P = expectedcounts[0]
        R = expectedcounts[1]
        S = expectedcounts[2]
        P_new = P + S
        R_new = R + P
        S_new = R + S
        return [P_new, R_new, S_new]

def sortseed(seed):
    if len(seed) == 1:
        return seed
    else:
        if seed[len(seed) / 2: len(seed)] < seed[0: len(seed) / 2]:
            newseed = ''
            newseed += sortseed(seed[len(seed) / 2 : len(seed)])
            newseed += sortseed(seed[0: len(seed) / 2])
            seed = newseed
        else:
            newseed = ''
            newseed += sortseed(seed[0: len(seed) / 2])
            newseed += sortseed(seed[len(seed) / 2 : len(seed)])
        return newseed

def expandlist(seed):
    newlist = ''
    for i in range(len(seed)):
        if seed[i] == 'P':
            newlist += 'PR'
        if seed[i] == 'R':
            newlist += 'RS'
        if seed[i] == 'S':
            newlist += 'PS'
    return newlist
    
def solve(T, N, R, P, S):

    ecounts = getexpectedcount(N)
    if P == ecounts[0] and R == ecounts[1] and S == ecounts[2]:
        seed = 'PR'
        for i in range(N - 1):
            seed = expandlist(seed)
        seed = sortseed(seed)
        print "Case #%d: %s" % (T + 1, seed)
    elif R == ecounts[0] and S == ecounts[1] and P == ecounts[2]:
        seed = 'SR'
        for i in range(N - 1):
            seed = expandlist(seed)
        seed = sortseed(seed)
        print "Case #%d: %s" % (T + 1, seed)
    elif S == ecounts[0] and P == ecounts[1] and R == ecounts[2]:
        seed = 'PS'
        for i in range(N - 1):
            seed = expandlist(seed)
        seed = sortseed(seed)
        print "Case #%d: %s" % (T + 1, seed)
    else:
        print "Case #%d: IMPOSSIBLE" % (T + 1)

cases = int(raw_input())

for T in xrange(cases):
    N, R, P, S = raw_input().split()
    N = int(N)
    R = int(R)
    P = int(P)
    S = int(S)
    solve(T, N, R, P, S)

