f = open("B-large.in", "r")
t = int(f.readline().strip())
for i in xrange(t):
    u = 0
    s = f.readline().strip()
    for j in xrange(len(s)-1):
        if s[j] != s[j+1]:
            u += 1
    if s[-1] == '-':
        u += 1
    print "Case #" + str(i+1) + ": " + str(u)
