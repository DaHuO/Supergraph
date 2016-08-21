def analysis():
    t = int(raw_input())
    if t == 0:
        return "INSOMNIA"
    a = set()
    c = t
    while True:
        a = a.union(set(list(str(t))))
        if (len(a) == 10):
            return str(t)
        t += c

cases = int(raw_input())

for i in xrange(cases):
    output = "Case #%i: %s" % (i+1, analysis())
    print output
