def solve(num, t) : 
    if(num == 0): 
        print "Case #%d: INSOMNIA" % t
    else: 
        seen = set()
        cnum = 0;
        for i in xrange(1, 100):
            cnum += num 
            seen = seen.union(set(list(str(cnum))))
            if(len(seen) == 10) : 
                print "Case #%d: %d" % (t, cnum)
                break

def reader(): 
    num = int(raw_input())
    for i in xrange(num):
        a = int(raw_input())
        solve(a, i + 1)

reader()

