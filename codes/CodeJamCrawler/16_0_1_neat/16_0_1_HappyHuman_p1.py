for i in xrange(int(raw_input().strip())):
    n = int(raw_input().strip())

    if n == 0:
        print "Case #%s: INSOMNIA"%(i+1, )
    else:
        k = n
        dig = set(str(n))
        while len(dig) < 10:
            k += n
            dig |= set(str(k))
        print "Case #%s: %s"%(i+1, k)