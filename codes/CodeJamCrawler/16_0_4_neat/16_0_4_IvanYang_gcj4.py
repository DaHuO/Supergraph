t = int(raw_input())

for i in xrange(1,t + 1):
    tmp = raw_input().split()
    K = int(tmp[0])
    C = int(tmp[1])
    S = int(tmp[2])

    interval = pow(K,C-1)
    now = 1
    print "case #{}:".format(i),
    for i in range(K):
        print "{}".format(now),
        now += interval

    print
