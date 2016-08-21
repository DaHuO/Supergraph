t = int(raw_input())
for case in range(1, t+1):
    (k, c, s) = map(int, raw_input().split(" "))
    print "Case #%d:" % case,
    for i in range(1, s+1):
        print i,
    print ""
