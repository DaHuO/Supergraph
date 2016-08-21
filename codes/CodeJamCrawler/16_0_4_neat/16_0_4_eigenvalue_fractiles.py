def solve(k, c):
    diff = k ** (c - 1)
    ans = [str(i * diff) for i in xrange(1, k + 1)]
    return " ".join(ans)

def reader() : 
    n = int(raw_input())
    for t in xrange(1, n + 1):
        k, c, s = [int(x) for x in raw_input().split()]
        print "Case #%d: %s" %(t, solve(k, c))

reader()
