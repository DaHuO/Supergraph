#!/usr/bin/env python2.7
import sys
lines = iter(sys.stdin)
cases = int(lines.next())
for case in range(1, cases + 1):
    N = int(lines.next())
    if N == 0:
        out = "INSOMNIA"
    else:
        current = N
        values = set(str(current))
        while len(values) < 10:
            current += N
            values.update(set(str(current)))
        out = str(current)

    print "Case #{case}: {out}".format(case=case, out=out.strip())
