def single(func):
    return func(raw_input())

def row(func):
    return map(func, raw_input().split())

def printcase(case, out, pattern='Case #%d: %s'):
    print pattern % (case, out)

def repeat(func, times):
    return [func() for _ in xrange(times)]

def digits(n):
    res = set()
    while n:
        n, d = divmod(n, 10)
        res.add(d)
    return res

def a(N, max=1000):
    seen = set()
    for x in xrange(1, max):
        seen |= digits(x * N)
        if len(seen) == 10:
            return x * N

T = single(int)
for t in xrange(1, T + 1):
    N = single(int)
    printcase(t, a(N) or 'INSOMNIA')
