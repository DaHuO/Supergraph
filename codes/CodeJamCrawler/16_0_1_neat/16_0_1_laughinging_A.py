#f = open("A-small-attempt1.in", "r")
f = open("A-large.in", "r")
t = int(f.readline().strip())
for i in xrange(t):
    u = [0 for j in xrange(10)]
    n = int(f.readline().strip())
    s = 0
    while sum(u) != 10:
        s += n
        for j in str(s):
            u[int(j)] = 1
        if s >= n * 1000:
            break
    print "Case #" + str(i+1) + ":" ,
    if sum(u) == 10:
        print str(s)
    else:
        print "INSOMNIA"

