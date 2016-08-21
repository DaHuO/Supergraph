#!/usr/bin/env python3.4
import sys

lines = iter(sys.stdin)
next(lines)  # throw away first line

for case, line in enumerate(lines, 1):
    N = int(line.strip())
    if N == 0:
        i = 'INSOMNIA'
    else:
        s = set()
        i = 0
        while len(s) != 10:
            i += N
            s.update(str(abs(i)))
    print('Case #%i: %s' % (case, i))
