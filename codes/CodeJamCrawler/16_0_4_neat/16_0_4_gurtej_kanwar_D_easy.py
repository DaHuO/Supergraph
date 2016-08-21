import sys

T = int(sys.stdin.readline())
for i in range(T):
    K,C,S = map(int, sys.stdin.readline().strip().split(" "))
    print "Case #%d: %s" % (i+1, " ".join(map(str, range(1,K+1))))
