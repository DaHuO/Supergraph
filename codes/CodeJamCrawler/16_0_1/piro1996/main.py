#!/usr/bin/env python

T = input()
for t in xrange(T):
    s = raw_input()
    r = s[0]

    for i in xrange(1, len(s)):
        if r[0] > s[i]:
            r += s[i]
        else:
            r = s[i] + r

    print 'Case #%d: %s' % (t + 1, r)
