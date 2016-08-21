def doit(n):
    if n == 0:
        return "INSOMNIA"
    current_n = n
    mask = 0
    target = 0x3ff
    while mask != target:
        for c in str(current_n):
            mask |= 1 << (ord(c) - ord('0'))
        current_n += n
    return current_n - n

nb_tests = int(raw_input())
for i in xrange(nb_tests):
    n = int(raw_input())
    res = doit(n)
    print "Case #%d: %s" % (i + 1, res)
