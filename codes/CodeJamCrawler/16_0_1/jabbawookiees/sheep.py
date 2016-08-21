cases = int(raw_input())

for ctr in xrange(cases):
    base = int(raw_input())
    found = set()
    last = None
    if base == 0:
        answer = "INSOMNIA"
    else:
        cc = 1
        while len(found) < 10:
            last = cc * base
            cc += 1
            found |= set(str(last))
        answer = last
    print "Case #%d: %s" % (ctr + 1, answer)
