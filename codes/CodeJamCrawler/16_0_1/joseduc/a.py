def solve(n):
    seen = set()
    if n == 0:
        print "INSOMNIA"
    else:
         j = n
         while True:
            for i in str(n):
                seen.add(i)
                if len(seen) == 10:
                    print n
                    return
            n += j         
        

t = int(raw_input())

for i in xrange(t):
    n = int(raw_input())
    print "Case #%s:" % (i + 1),
    solve(n)
    
