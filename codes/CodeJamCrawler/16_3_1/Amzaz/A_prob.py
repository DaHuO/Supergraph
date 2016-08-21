        
import sys
f = sys.stdin
T = int(f.readline())
for case in xrange(1, T+1):
    N = int(f.readline())
    P = map(int, f.readline().split())
    evac = []
    count = sum(P)
    while count > 0:
        maximal = max(P)
        senators = [i for i in xrange(N) if P[i] == maximal]
        if len(senators) % 2 == 1:
            evac.append(chr(ord('A') + senators[-1]))
            P[senators[-1]] -= 1
            count -= 1
            senators = senators[:-1]
        for p in P:
            assert p * 2 <= count, P
        for i in xrange(0, len(senators), 2):
            evac.append(chr(ord('A') + senators[i]) + chr(ord('A') + senators[i + 1]))
            P[senators[i]] -= 1
            P[senators[i + 1]] -= 1
            count -= 2
            
            for p in P:
                assert p * 2 <= count, (P, evac)
        
    print "Case #%d: %s" % (case, " ".join(evac))
        