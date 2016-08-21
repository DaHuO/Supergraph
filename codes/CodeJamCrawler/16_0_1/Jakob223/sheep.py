def f(n):
    # print n
    alld = set('1234567890')
    for i in xrange(100000):
        if not alld:
            return str(n*i)
        alld -= set(str((i+1)*n))
    return "INSOMNIA"
        
        
T = int(raw_input())
for i in xrange(1,T+1):
    print "Case #%d: %s" % (i, f(int(raw_input())))
    
    # 5
    # 0
    # 1
    # 2
    # 11
    # 1692