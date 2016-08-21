#!/usr/bin/python2.7

import sys

T = int(sys.stdin.readline())

for i in xrange(T):
    S      = sys.stdin.readline().strip()
    upper  = [S[0]]
    lower  = []

    for j in xrange(1,len(S)):
        if S[j] > upper[-1]:
            upper.append(S[j])
        elif S[j] < upper[-1]:
            lower.append(S[j])
        else:
            added = False
            for k in xrange(len(upper)-1,-1,-1):
                if upper[k] < S[j]:
                    upper.append(S[j])
                    added = True
                    break
                elif upper[k] > S[j]:
                    lower.append(S[j])
                    added = True
                    break
            if not added:
                for k in xrange(0, len(lower)):
                    if lower[k] < S[j]:
                        upper.append(S[j])
                        added = True
                        break
                    elif lower[k] > S[j]:
                        lower.append(S[j])
                        added = True
                        break
            if not added:
                upper.append(S[j])


    print "Case #{0}: ".format(i+1),
    for j in xrange(len(upper)-1,-1,-1):
        sys.stdout.write(upper[j])
    for j in xrange(0, len(lower)):
        sys.stdout.write(lower[j])
    print
    


