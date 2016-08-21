#!/usr/bin/python2


def gl(s, c):
    if c == 0:
        return s

    s1 = [s]
    for i in xrange(c - 1):
        s2 = []
        for ch in "".join(s1):
            if ch == 'G':
                s2.append('G' * len(s))
            else:
                s2.append(s)
        s1 = s2
    return s1

def pos(k, c, p):
    n = 0
    gc = p
    for i in xrange(c - 1):
        n = gc
        gc = n * k + p
    return n

def f(k, c, s):
    if c == 1:
        res = [str(x) for x in xrange(1, k + 1)]
    else:
        res = []
        i = 0
        while i < k - 1:
            p = pos(k, c, i)
            res.append(str(p * k + i + 2))
            i += 2
        if i < k:
            res.append(str(k))

    if len(res) > s:
        return "IMPOSSIBLE"
    else:
        return " ".join(res)

import sys
fd = open(sys.argv[1], "rb")
t = int(fd.readline().strip())
for i in xrange(1, t + 1):
    line = fd.readline().strip()
    k, c, s = [int(x) for x in line.split(" ")]
    res = f(k, c, s)
    print "Case #%d: %s" % (i, res)
fd.close()
