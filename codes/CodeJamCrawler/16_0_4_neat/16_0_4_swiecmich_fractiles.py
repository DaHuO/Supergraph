t = int(raw_input())
for i in xrange(1, t + 1):
    k, c, s = [int(s) for s in raw_input().split(" ")]
    print "Case #{}: {}".format(i, " ".join(str(j + 1) for j in range(k)))
