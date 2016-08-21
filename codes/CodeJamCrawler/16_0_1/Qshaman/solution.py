def sol(S):
    re = S[0]
    for c in S[1:]:
        if c >= re[0]:
            re = c + re
        else:
            re = re + c
    return re

T = int(raw_input())
for i in xrange(T):
    S = raw_input()
    print 'Case #%d: %s' % (i+1, sol(S))
