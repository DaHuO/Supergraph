from itertools import combinations, product
for t in xrange(input()):
    print "Case #%d:"%(t+1),

    n, k = map(int, raw_input().split())
    P = map(float, raw_input().split())
    k2 = k/2

    ps = []
    ans = 0
    for p in combinations(P, k):
        su = 0
        for q in product(range(2), repeat=k):
            if sum(q)==k2:
                tmp = 1.
                for i, e in enumerate(q):
                    if e:
                        tmp *= p[i]
                    else:
                        tmp *= 1.-p[i]
                su += tmp
        if ans < su:
            ps = p
            ans = su
    print ans


