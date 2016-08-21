def solve():
    n = int(raw_input())
    if n == 0:
        print "INSOMNIA"
    else:
        s = set()
        i = 0
        while len(s) < 10:
            i += 1
            map(s.add, list("%s" %(n*i)))
        print n*i

T = int(raw_input())

for t in range(1, T+1):
    print "Case #%d:" %t,
    solve()
