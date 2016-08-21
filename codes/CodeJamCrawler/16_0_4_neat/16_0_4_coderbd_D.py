#!/usr/bin/python

t = int(raw_input())
for case_no in xrange(1, t+1):
    k, c, s = map(int, raw_input().split())
    print 'Case #%d: %s' % (case_no, ' '.join(map(str,range(1, s+1))))
