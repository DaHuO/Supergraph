n = int(raw_input())
for i in xrange(n):
    line = raw_input().split()
    K = int(line[0])
    C = int(line[1])
    S = int(line[2])
    if K == S:
        print "Case #" + str(i + 1) + ": " + " ".join([str(x + 1) for x in range(S)])