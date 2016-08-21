T = int(raw_input())

for i in xrange(T):
    K, C, S = [int(x) for x in raw_input().split()]
    print "Case #" + str(i+1) + ": " + " ".join([str(x) for x in range(1,K+1)])
