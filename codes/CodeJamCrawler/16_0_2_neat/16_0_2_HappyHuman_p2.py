for i in xrange(int(raw_input().strip())):
    panks = raw_input().strip()
    dif = sum([panks[m] != panks[m+1] for m in range(len(panks) - 1)])
    if panks[-1] == '-':
        dif += 1
    print "Case #%s: %s"%(i+1, dif)