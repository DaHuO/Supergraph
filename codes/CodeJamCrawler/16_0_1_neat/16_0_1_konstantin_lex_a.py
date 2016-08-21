def solve(n):
    if not n:
        return -1
    r = n
    s = set(str(n))
    while len(s) < 10:
        n += r
        s.update(set(str(n)))
        #print '>>>', s

    return n

f = open('in.txt', 'r')
t = int(f.readline().strip())
for i in range(t):
    n = int(f.readline().strip())
    res = solve(n)
    if res == -1:
        print "Case #{}: INSOMNIA".format(i+1)
    else:
        print "Case #{}: {}".format(i+1, res)
