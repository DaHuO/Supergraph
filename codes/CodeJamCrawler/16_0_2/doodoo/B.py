def solve(S):
    uniqS = []

    cur = None
    for c in S:
        if c != cur:
            cur = c
            uniqS.append(c)

    N = len(uniqS)
    if uniqS[0] == '-':
        N = N - 1
        return (N / 2) * 2 + 1

    return (N / 2) * 2

T = int(raw_input())

for i in xrange(T):
    S = raw_input()

    print 'Case #%d: %d' % (i + 1, solve(S))
