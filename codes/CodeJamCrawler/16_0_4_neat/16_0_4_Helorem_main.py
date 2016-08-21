def doit(k, c, s):
    res = []
    if k == s:
        for i in xrange(k):
            res.append(str(i + 1))
    else:
        return "IMPOSSIBLE"
    return " ".join(res)

nb_tests = int(raw_input())
for i in xrange(nb_tests):
    line = raw_input()
    k, c, s = line.split(" ")
    res = doit(int(k), int(c), int(s))
    print "Case #%d: %s" % (i + 1, res)
