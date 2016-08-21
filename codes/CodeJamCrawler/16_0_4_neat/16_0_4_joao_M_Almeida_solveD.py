def solveD(K,C,S):
    l = []
    for j in xrange(K):
            l = l + [1 + j*K**(C-1)]
    return l

with open("D-small-attempt0.in") as f:
    T = int(f.next())
    for i in xrange(T):
        K, C, S = [int(s) for s in f.next().split(" ")]  # read a list of integers, 2 in this case
        l = solveD(K,C,S)
        to_print = ' '.join([str(x) for x in l])
        print "Case #%d: %s" % (i+1,to_print)
