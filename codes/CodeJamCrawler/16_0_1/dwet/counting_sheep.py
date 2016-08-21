cases = int(raw_input())
for case in xrange(cases):
    n = int(raw_input())
    seen = {str(x): False for x in range(10)}
    for x in xrange(1, 1000000):
        y = n * x

        # update seen
        for c in str(y):
            seen[c] = True

        if all(seen.values()):
            print "Case #%s: %s" % (case + 1, y)
            break
    else:
        print "Case #%s: INSOMNIA" % (case + 1)
