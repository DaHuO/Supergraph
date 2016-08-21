#!/usr/bin/env python2.7
import sys
lines = iter(sys.stdin)
cases = int(lines.next())
for case in range(1,cases+1):
    K, C, S = lines.next().split()
    K, C, S = map(int, (K, C, S))
    if S < K / C:
        out = "IMPOSSIBLE"
    else:
        current = 0
        curr_C = 0
        results = []
        for i in range(0,K):
            current = K * current + i
            curr_C += 1
            if curr_C == C:
                results.append(current + 1)
                current = 0
                curr_C = 0
            elif i == K-1:
                while curr_C < C:
                    current = current*K
                    curr_C += 1
                results.append(current + 1)
        out = ' '.join(map(str, results))
        if len(results) > S:
            out = "IMPOSSIBLE"
    print "Case #{case}: {out}".format(case=case, out=out.strip())
