t = int(raw_input())

for tt in range(1,t + 1):
    n = int(raw_input())
    m = n
    d = {}
    
    for it in range(1,201):
        for x in str(m):
            d[x] = True
        if all(x in d for x in '0123456789'):
            break
        m += n
    if all(x in d for x in '0123456789'):
        print "Case %s%d: %d" % ('#',tt,m)
    else:
        print "Case %s%d: INSOMNIA" % ('#',tt)