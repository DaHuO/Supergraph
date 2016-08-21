# from __future__ import division
from pprint import pprint
import time
inputfile = file("in", "rb")
outputfile = file("out", "wb")
out_s = "Case #%d: %s"
parse_line = lambda: [int(a) for a in inputfile.readline().split()]
rl = lambda: inputfile.readline().replace("\n","")

import itertools

def do_case(ncase):
    N, = parse_line()
    bffs = {}
    bffline = parse_line()
    bffline = [x-1 for x in bffline]
    for i in xrange(N):
        bffs[i] = bffline[i]
    maxi = 0
    for n in xrange(2, N+1):
        for perm in itertools.permutations(range(N), n):
            for i in xrange(n):
                if bffs[perm[i]] != perm[(i+1)%n] and bffs[perm[i]] != perm[(i-1)%n]:
                    break
            else:
                maxi = max(maxi, n)
    print >>outputfile, out_s % (ncase, str(maxi))

start_time = time.time()
T = int(inputfile.readline())
for ncase in xrange(1,T+1):
    print "Doing case", ncase
    do_case(ncase)
    print "Done, time", time.time()-start_time
    