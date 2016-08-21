import sys
from collections import deque

f = open(sys.argv[1])
f.readline()
casenum = 1
for l in f:
    l = l.strip()
    words = deque([l[0]])
    tested = set()
    finished = set()

    while words:
        w = words.popleft()
        if w in tested:
            continue
        tested.add(w)
        i = len(w)
        if i == len(l):
            finished.add(w)
        else:
            if l[i] >= w[0]:
                words.append( l[i]+w )
            else:
                words.append( w+l[i] )
    finished = list(finished)
    finished.sort()
    output = finished[-1]

    print "Case #{}: {}".format(casenum,output)
    casenum += 1
f.close()
