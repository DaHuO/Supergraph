#!/usr/bin/python


all_di = set(range(10))

nb = int(raw_input())

for n in xrange(1, nb+1):
    N = int(raw_input())
    res = "INSOMNIA"
    if N != 0:
        newd = set()
        for i in xrange(1, 1000000):
            this = "%d" % (N*i)
            newd.update(set(this))

            if len(newd) == 10:
                res = this
                break

    print "Case #%d:" % (n), res
