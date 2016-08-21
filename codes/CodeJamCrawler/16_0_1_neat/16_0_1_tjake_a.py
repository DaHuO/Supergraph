IMP = "INSOMNIA"
for t in xrange(input()):
    n = input()
    print "Case #" + str(t+1) + ":",
    if not n:
        print IMP
        continue
    c = 0
    d = [0] * 10
    for p in xrange(10**4):
        c += n
        for m in str(c):
            d[int(m)] = 1
        if sum(d)==10:
            print c
            break
    if sum(d)<10:
        print IMP
