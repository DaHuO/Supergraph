# -*- coding: utf-8 -*-
n = int(raw_input())
for i in xrange(n):
    x = int(raw_input())
    if not x:
        print 'INSOMNIA'
    else:
        s = set(str(x))
        nxt = 2
        while len(s) != 10:
            s = s.union(set(str(nxt * x)))
            nxt += 1
        print 'Case #{}: {}'.format(i + 1, (nxt - 1) * x)
