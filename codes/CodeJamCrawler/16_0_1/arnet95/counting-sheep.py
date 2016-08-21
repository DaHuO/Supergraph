def f(n):
    if n == 0:
        return "INSOMNIA"
    k = len(str(n))
    m = max(10, max([(x+1)*10**k-1 for x in xrange(1, 10)]))
    l = range(10)
    i = 1
    while l != []:
        for digit in [int(c) for c in str(i*n)]:
            if digit in l:
                l.remove(digit)
        i += 1
    return (i-1)*n

for i in xrange(1, int(raw_input())+1):
    print "Case #%d: %s" % (i, str(f(int(raw_input()))))
