#!/usr/bin/env python
import string

f = open('/dev/stdin', 'r')
T = int(f.readline())

for t in range(T):
    N = int(f.readline())
    r = set(string.digits)
    i = 0

    if N != 0:
        while len(r) > 0:
            i += 1
            r = r - set(str(i * N))

        print('Case #%d: %d' % (t + 1, i * N))
    else:
        print('Case #%d: INSOMNIA' % (t + 1))
