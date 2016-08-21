
import sys
f = sys.stdin
cases = int(f.readline())
for case in range (1,1+cases):
    K,C,S = map(int,f.readline().split(" "))
    cur = range(1,K+1)
    level = 1
    while level < C:
        next = []
        if len(cur) >1:
            for i in range(len(cur)-1):
                base = (cur[i]-1)*K
                incr = level + i + 1
                next.append(base+incr)
        else:
            next.append((cur[0]-1)*K+1)
        cur = next
        level += 1
    if len(cur) > S:
        print "Case #%d: IMPOSSIBLE" % (case)
    else:
        print "Case #%d: %s" % (case," ".join(map(str,cur)))        
