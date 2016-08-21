#! /usr/bin/env python

t = int(raw_input())
for i in xrange(1, t+1):
    N = raw_input()
    N1 = N
    track = set()
    if N == '0':
        print "Case #%s: " % i + "INSOMNIA"
        continue
    count = 2
    while len(track) !=10:
        temp = set(x for x in N1)
        track = temp | track
        N1 = str(count*int(N))
        count +=1
    print "Case #%s: %d" % (i, int(N1) - int(N))

