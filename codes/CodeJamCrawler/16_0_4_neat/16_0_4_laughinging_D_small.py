f = open("D-small-attempt0.in", "r")
t = int(f.readline().strip())

#t = 10
def pos(p, k, c):
    u = 0
    for i in xrange(c):
        u = u*k + p
    return u

for i in xrange(t):
    print "Case #" + str(i+1) + ":",
    K,C,S = [int(i) for i in f.readline().split()]
    #K, C, S = [int(i) for i in raw_input().split()]
    for j in xrange(K):
        print pos(j, K, C)+1,
    print

