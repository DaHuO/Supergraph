#! /usr/bin/env python
import sys, re
import operator as op
import math

""" START TEMPLATE JCHAOISAAC """

# some reading functions
lolfile = open(sys.argv[1]) # open file
getline = lambda: lolfile.readline().strip()
gettoken = lambda: re.split("\s+", getline())
getint = lambda: int(getline())
getints = lambda: map(int, gettoken())


""" END TEMPLATE JCHAOISAAC """

[T] = getints()
for cases in xrange(1, T + 1): # loop over cases
    ans = 0
    # main
    s = getline()
    p, ans = '+', 0
    for v in s[::-1]:
        if v != p: ans += 1
        p = v
    # main
    print "Case #%d: %d" % (cases, ans) # answer output
