T = int(raw_input())

for i in xrange(T):
    K, C, S = [int(x) for x in raw_input().split()]

    list_students = [k for k in xrange(1, K + 1)]

    for k in xrange(1, C):
        shift = K**k
        for j in xrange(S):
            list_students[j] += j * shift

    print "Case #%d: %s" % (i + 1, " ".join([str(i) for i in list_students]))
