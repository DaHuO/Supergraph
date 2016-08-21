t = int(raw_input())
for case in xrange(t):
    n = int(raw_input())
    if n == 0:
        ret = "INSOMNIA"
    else:
        s = set()
        c = 0
        while len(s) < 10:
            c += n
            s = s | set(iter(str(c)))
        ret = c

    print "Case #%d: %s" % (case + 1, ret)
