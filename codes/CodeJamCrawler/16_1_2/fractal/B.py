import collections

T = int(raw_input())


L = []
l = []
for t in range(1, T+1):
    N = int(raw_input())
    del L[:]
    for _ in range(2*N-1):
        k = map(int, raw_input().split())
        L.extend(k)
    cnts = collections.Counter(L)
    del l[:]
    for (a,b) in cnts.most_common():
        if b%2:
            l.append(a)
    l.sort()
    print "Case #%d: %s" % (t, ' '.join([str(x) for x in l]))

