N = input()
def solve(m):
    if m == 0:
        return "INSOMNIA"
    s = set()
    i = 1
    while True:
        s.update(set(str(i*m)))
        if len(s) == 10:
            return i*m
        i += 1
    raise

for tc in xrange(1, N+1):
    m = input()
    print "Case #{}: {}".format(tc, solve(m))
