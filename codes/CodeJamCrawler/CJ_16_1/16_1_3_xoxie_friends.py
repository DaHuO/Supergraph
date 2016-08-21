import sys
from collections import defaultdict, deque

f = open(sys.argv[1])
f.readline()

l = f.readline()
casenum = 1
while l != "":
    n = int(l)
    bffs = [int(x)-1 for x in f.readline().split()]
    revbff = defaultdict(list)

    for i,j in zip(range(n),bffs):
        revbff[j].append(i)

    maxF = 0
    circles = deque([[i] for i in range(n)])

    while circles:
        t = circles.popleft()

        nextbff = bffs[t[-1]]

        try:
            x = t.index(nextbff)
            if x == len(t)-2:
                maxF = max(maxF,len(t))
                newI = set(range(n)) - set(t)
                for i in newI:
                    circles.append( t+[i] )
            elif x == 0:
                maxF = max(maxF,len(t))
        except ValueError:
            t.append( nextbff )
            circles.append(t)
                      
    output = maxF
    

    print "Case #{}: {}".format(casenum,output)
    l = f.readline()
    casenum += 1
