#!/usr/bin/python2


def f(s):
    res = s[0]
    for i in s[1:]:
        if i >= res[0]:
            res = i + res
        else:
            res = res + i
    return res


import sys
fd = open(sys.argv[1], "rb")
t = int(fd.readline().strip())
for i in xrange(1, t + 1):
    line = fd.readline().strip()
    res = f(line)
    print "Case #%d: %s" % (i, res)
fd.close()
