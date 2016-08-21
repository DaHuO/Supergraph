#!/usr/bin/python2


def f(s, target='+'):
    is_same = True
    for i in xrange(len(s)-2, -1, -1):
        if s[i] != s[-1]:
            is_same = False
            break

    if is_same:
        if s[-1] == target:
            return 0
        else:
            return 1

    if s[-1] == target:
        return f(s[0:i + 1], s[i + 1])
    else:
        return f(s[0:i + 1], s[i + 1]) + 1


import sys
fd = open(sys.argv[1], "rb")
t = int(fd.readline().strip())
for i in xrange(1, t + 1):
    s = fd.readline().strip()
    ans = f(s)
    print "Case #%d: %s" % (i, ans)
fd.close()
