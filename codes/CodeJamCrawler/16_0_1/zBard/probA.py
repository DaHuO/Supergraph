from itertools import groupby
import sys

w = int(sys.stdin.readline().strip())
i = 1
for line in sys.stdin:
    orig = int(line)
    #print inp
    if orig is not 0 :
        mp = {}
        cnt = 0
        inp = orig
        while len(mp) != 10:
            cnt += 1
            inp = orig * cnt
            #print inp
            vv = list(str(inp))
            #print vv
            for c in vv :
                if not c in mp : mp[c] = 1
            #print mp
        print "Case #"+str(i)+":",inp
    else :
        print "Case #"+str(i)+":","INSOMNIA"

    i+=1

