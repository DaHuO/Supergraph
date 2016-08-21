t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    c = set()
    j=1
    if n==0:
        print "Case #{}: {}".format(i, 'INSOMNIA')
        continue
        
    while(True):
        x = j*n
        c = c.union(set(list(str(x))))
        if len(c)==10:
            break
        j+=1

    print "Case #{}: {}".format(i, j*n)
