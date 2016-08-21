#!/usr/bin/env python

import sys
import re

# Cases
f = open(sys.argv[1])
cases = f.readlines()
len_cases = int(cases[0])

def countvariations(stack):
    return len(re.findall('[\+]+', stack)) + len(re.findall('[\-]+', stack))

# Processing each case
for i in range(1, len_cases+1):
    stack = cases[i].split('\n')[0]
    variations = countvariations(stack)
    # print "Variations:", variations
    # print "Stack:", stack
    if variations == 1 and stack[0] == '-':
        print "Case #%d: %d" % (i, 1)
    elif variations == 1 and stack[0] == '+':
        print "Case #%d: %d" % (i, 0)
    elif stack[-1] == '-':
        print "Case #%d: %d" % (i, variations)
    else:
        print "Case #%d: %d" % (i, variations-1)
