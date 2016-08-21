from __future__ import print_function

t = int(raw_input())

for i in xrange(1, t + 1):
    N = int(raw_input())
    P = [int(s) for s in raw_input().split(" ")]
    assert(N == len(P))
    s = sum(P)
    
    print("Case #{}:".format(i), end="")
    
    while s > 0:
        m = max(P)
        A = ''
        # find first max
        for j in xrange(0, len(P)):
            if P[j] == m:
                A = chr(ord('A') + j)
                P[j] -= 1
                s -= 1
                break
        if s > 2 or s == 1:
            # find last max
            m = max(P)
            maxi = 0
            for j in xrange(0, len(P)):
                if P[j] == m:
                    maxi = j
            B = chr(ord('A') + maxi)
            P[maxi] -= 1
            s -= 1
            print(" {}{}".format(A, B), end="")
        else:
            print(" {}".format(A), end="")
    print("")
