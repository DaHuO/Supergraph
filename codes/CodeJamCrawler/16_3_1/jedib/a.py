#!/usr/bin/python

tests = int(raw_input())

for test in xrange(1, tests+1):
    N = int(raw_input())
    senators = raw_input().split()
    senators = [ int(s) for s in senators[:]]
    #print 'test', test
    #print 'senators', senators

    out = []
    while sum(senators):
        if sum(senators) == 3:
            idx = senators.index(max(senators))
            senators[idx] -= 1
            idx2 = -1
            out.append((idx, idx2))
            continue
        idx = senators.index(max(senators))
        senators[idx] -= 1
        if sum(senators):
            idx2 = senators.index(max(senators))
            senators[idx2] -= 1
        else:
            idx2 = -1
        out.append((idx, idx2))
    res = []
    for a, b in out:
        if b == -1:
            res.append( chr(ord('A')+a) )
        else:
            res.append( chr(ord('A')+a) + chr(ord('A')+b) )

    #print res


    print "Case #%i:" % (test), " ".join(elt for elt in res)
    #print "Case #%i: %s" % (test, res) 

