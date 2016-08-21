T = input()
for t in range(T):
    K, C, S = map(int, raw_input().split())
    print "Case #%d: %s" % (t + 1, ' '.join(str(i + 1) for i in range(K)))
