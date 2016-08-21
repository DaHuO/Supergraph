#!/usr/local/bin/python
DEBUG = False

import re

def dedup(s):
    if DEBUG:
        print 'Original: {}'.format(s)

    deplussed = re.sub('\++', '+', s)
    dedupped = re.sub('\-+', '-', deplussed)

    if DEBUG:
        print 'Dedupped: {}'.format(dedupped)

    return dedupped

def count_flips(s):
    flips = 0
    s = dedup(s)
    while s != '+':
        if s[0] == '+':
            s = '-' + s[1:]
        else:
            s = '+' + s[1:]
        s = dedup(s)
        flips += 1
    return flips 

t = int(raw_input())
for i in xrange(1, t + 1):
    s = raw_input()
    print "Case #{}: {}".format(i, count_flips(s))
