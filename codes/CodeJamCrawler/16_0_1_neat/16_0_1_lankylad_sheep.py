N = int(raw_input())

for t in xrange(1,N+1):
    n = int(raw_input())
    if n == 0:
        print "Case #{}: {}".format(t, "INSOMNIA")
        continue
    x = 0
    digits = set()
    while len(digits) < 10:
        x += 1
        digits |= set(str(n*x))
    print "Case #{}: {}".format(t, n*x)