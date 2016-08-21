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

# global data



# global data

[T] = getints()
for cases in xrange(1, T + 1): # loop over cases
    ans = 'INSOMNIA'
    # main

    N = getint()
    d = len(str(N)) # lazy way to get number of digits
    n = N

    c = 10
    arr = [False] * 10
    for i in xrange(1, 10 ** (d + 1)):
        m = n
        while m > 0:
            m, r = divmod(m, 10)
            if not arr[r]:
                arr[r] = True
                c -= 1
        if c == 0:
            ans = str(n)
            break
        n += N

    # main
    print "Case #%d: %s" % (cases, ans) # answer output
