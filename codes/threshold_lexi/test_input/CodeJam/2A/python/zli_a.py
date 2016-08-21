import numpy
from numpy import array as ar
import sys
from collections import Counter

#http://www.ics.uci.edu/~eppstein/PADS/
#David Eppstein's python library
#from pads import DFS

def xl(l):
    return xrange(len(l))

def next_line():
    return input_file.readline().rstrip()

rewrite = {'r': 'rs', 'p': 'pr', 's': 'ps'}
#rewrites = {'r': ['rs', 'sr'], 'p': ['pr', 's': 'ps'}

rps = []
#rps.append([ar(1, 0, 0), ar(0, 1, 0), ar(0, 0, 1)])
#rps.append(["p", "r", "s"])
rps.append({'p': 'p', 'r': 'r', 's': 's'})
for i in range(13):
    new = {}
    for c in rewrite:
        substr = [rps[-1][c2] for c2 in rewrite[c]]
        if substr[0] < substr[1]:
            new[c] = substr[0] + substr[1]
        else:
            new[c] = substr[1] + substr[0]
    """
    for s in rps[-1]:
        #new.append(s + numpy.roll(s, 1)
        #'ps' -> 'prps'
        #'sp' -> 'pspr'
        #'rs' -> 'rsps'
        #'sr' -> 'psrs'
        rps[-1][0]
        new.append("".join(rewrite[c] for c in s))
    """
    rps.append(new)

input_file = open(sys.argv[1])
for case in range(1, int(next_line())+1):
    print "Case #%s:" % (case),
    N, R, P, S = map(int, next_line().split())
    counts = {'r': R, 'p': P, 's': S}
    for c in 'rps':
        if counts[c] == 0:
            del counts[c]
    #print counts
    for s in rps[N].values():
        if dict(Counter(s)) == counts:
            print s.upper()
            break
    else:
        print "IMPOSSIBLE"
