import sys
cases = int(sys.stdin.readline())
for c in range(1, cases+1):
    n = int(sys.stdin.readline())
    if n == 0:
        print "Case #" + str(c) + ": INSOMNIA"
    else:
        s = set(str(n))
        nn = n
        while len(s)<10:
            nn += n
            s  = s.union(set(str(nn)))
        print "Case #" + str(c) + ": " + str(nn)
