cases = int(raw_input())
for case in xrange(1, cases + 1):
    k, c, s = (int(x) for x in raw_input().split())
    ans = " ".join(str(x) for x in range(1, k + 1))
    print "Case #%s: %s" % (case, ans)
