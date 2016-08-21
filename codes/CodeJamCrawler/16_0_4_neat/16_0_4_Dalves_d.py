import math
from itertools import izip, cycle, izip_longest

def find_solution(k, c, s):
    minimum = math.ceil(k/float(c))
    result = []
    if s < minimum:
        return
    pos = 0
    level = 0
    for x in xrange(k):
        pos = pos*k + x
        level += 1
        if level == c:
            level = 0
            result.append(pos+1)
            pos = 0
    if pos+1 not in result:
        result.append(pos+1)
    return result

t = int(raw_input())

for i in xrange(t):
    line = raw_input()
    (k, c, s) = (int(x) for x in line.split())
    print "Case #%d:" % (i+1),
    sol = find_solution(k, c, s)
    if sol:
        for n in sol:
            print n,
        print
    else:
        print "IMPOSSIBLE"
