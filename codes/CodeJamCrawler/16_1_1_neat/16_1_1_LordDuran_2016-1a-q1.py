# from __future__ import division
from pprint import pprint
import time
inputfile = file("in", "rb")
outputfile = file("out", "wb")
out_s = "Case #%d: %s"
parse_line = lambda: [int(a) for a in inputfile.readline().split()]
rl = lambda: inputfile.readline().replace("\n","")


from collections import deque

def do_case(ncase):
    S = list(rl())
    new_S = deque([S[0]])
    S.remove(S[0])
    for c in S:
        if ord(c) >= ord(new_S[0]):
            new_S.appendleft(c)
        else:
            new_S.append(c)
    print >>outputfile, out_s % (ncase, str(''.join(new_S)))

start_time = time.time()
T = int(inputfile.readline())
for ncase in xrange(1,T+1):
    print "Doing case", ncase
    do_case(ncase)
    print "Done, time", time.time()-start_time
    