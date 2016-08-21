import os, sys

with open(sys.argv[1], 'r') as infile:
    N = int(infile.readline().strip())
    for x in xrange(1, N+1):
        T = infile.readline().strip()
        cases = set(list(T))
        intT = int(T)
        current = intT
        count = 2
        stablecount = 0
        while len(cases) < 10:
            current = count*intT
            count += 1
            cur_num = len(cases)
            cases.update(list(str(current)))
            if cur_num == len(cases):
                stablecount += 1
            else:
                stablecount = 0
            if stablecount > 100:
                current = 'INSOMNIA'
                break
            
        if isinstance(current, int):
            current = str(current)
        print "Case #%s: %s" % (x, current)