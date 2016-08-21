T = input()
for x in range(T):
    print "Case #%d:" % (x+1),
    K, C, S = map(int, raw_input().split())
    for i in range(1, K+1):
        t = i
        for y in range(C-1):
            t = K*(t-1)+i
        print t,
    print 
