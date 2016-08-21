n = int(raw_input())
for __ in xrange(n):
    i = int(raw_input())
    if i==0:
        print "Case #" + str(__+1) + ": INSOMNIA"
        continue
    t = set(list(str(i)))
    for _ in xrange(1,101):
        t = t | set(list(str(i*_)))
        if len(t)==10:
            print "Case #" + str(__+1) + ": " + str(i*_)
            break
