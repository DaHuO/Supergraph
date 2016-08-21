#! /usr/bin/env python
"""
Name: Sravan Bhamidipati
Date: 8th April, 2016
Purpose: https://code.google.com/codejam/contest/6254486/dashboard#s=p0
"""

import string
import sys

sleep = frozenset(string.digits)

def count_to_sleep(num):
    orig = int(num)
    prev = orig
    seen = set(num)
    for i in xrange(100):
        if seen == sleep:
            return prev

        prev += orig
        seen |= set(str(prev))
    if seen == sleep:
        return prev
    else:
        return 'INSOMNIA'


with open(sys.argv[1]) as fd:
    for line_no, line in enumerate(fd):
        if line_no == 0:
            continue
        else:
            print 'Case #%s: %s' % (line_no, count_to_sleep(line.strip()))
