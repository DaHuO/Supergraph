def f(n):
    count = 0
    n += '+'
    for i in xrange(len(n)-1):
        if n[i] != n[i+1]:
            count += 1 
    return count
        
        
T = int(raw_input())
for i in xrange(1,T+1):
    print "Case #%d: %s" % (i, f((raw_input())))
    
    # 5
    # 0
    # 1
    # 2
    # 11
    # 1692Square Brackets [ ] | English Club