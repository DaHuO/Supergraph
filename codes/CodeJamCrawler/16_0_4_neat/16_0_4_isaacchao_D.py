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
    K, C, S = getints()
    ans = ' '.join([str(x) for x in xrange(1, K + 1)])
    print "Case #%d: %s" % (cases, ans) # answer output

