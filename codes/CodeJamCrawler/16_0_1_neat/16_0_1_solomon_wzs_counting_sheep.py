#!/usr/bin/python2

import sys


def f(n):
    if n == 0:
        return "INSOMNIA"

    s = set()
    d = n
    while True:
        for i in str(n):
            s.add(int(i))
        if len(s) == 10:
            return n
        else:
            n += d


fd = open(sys.argv[1], "rb")

t = int(fd.readline().strip())
for i in xrange(1, t + 1):
    n = int(fd.readline().strip())
    ans = f(n)
    print "Case #%d: %s" % (i, ans)

fd.close()
