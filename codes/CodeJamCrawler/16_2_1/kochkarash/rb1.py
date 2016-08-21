import sys
fileinput = sys.stdin

import StringIO
#fileinput = StringIO.StringIO(inputstr)

digits=("ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE")
mapping=(("Z",0), ("W",2 ), ("X",6), ("S",7),("V",5), ("F",4),("R",3), ("G",8),("O",1), ("N",9))


T=int(fileinput.readline().strip())
for t in range(T):
    S=fileinput.readline().strip()
    ps=list(S)
    n=[]
    while(True):
        if not ps:
            break
        for m in mapping:
            if m[0] in ps:
                n=n+[m[1]]
                #print list(digits[m[1]]), ps
                for c in list(digits[m[1]]):
                    ps.remove(c)
                break
    n = sorted(n)
    n=(str(c) for c in n)
    n="".join(n)
    print "Case #%s: %s" % (t+1, n)