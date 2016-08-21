#!/usr/bin/python
import sets
import sys

f = open(sys.argv[1], 'r')
N = int(f.readline())

for t in range(0, N):
    s = f.readline().split()
    K = int(s[0])
    C = int(s[1])-1
    S = int(s[2])

    if C == 0:
        if S >= K:
            print "Case #" + str(t+1) + ": " + ' '.join(map(str, range(1, K+1)))
        else:
            print "Case #" + str(t+1) + ": IMPOSSIBLE"
        continue

    if K % 2 == 1:
        if ((K/2) + 1) > S:
            print "Case #" + str(t+1) + ": IMPOSSIBLE"
    else:
        if K/2 > S:
            print "Case #" + str(t+1) + ": IMPOSSIBLE"

    res = []
    for i in xrange(0, K, 2):
        res.append((K**C)*i + (i + 1))

    if K % 2 == 1:
        res[len(res) - 1] = res[len(res) - 1] - 1

    
    print "Case #" + str(t+1) + ": " + ' '.join(map(lambda x : str(x+1), res))
