#!/usr/bin/env python
#python 2.x
T = int(raw_input())

for cas in xrange(1, T + 1):
    S = raw_input()
    n = len(S)
    sl = ""
    sr = ""
    for i in xrange(n - 1, 0, -1):
        if S[i] >= max(S[:i]):
            sl += S[i] 
        else:
            sr = S[i] + sr
    print "Case #%s: %s"%(cas, sl + S[0] + sr)
