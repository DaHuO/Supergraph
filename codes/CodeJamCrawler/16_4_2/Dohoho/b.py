import itertools

n = int(raw_input())

cur = []
cached = {}

def prob(x, n):
    global cached
    global cur

    if x == len(cur):
        return (1 if n == 0 else 0)

    if (x,n) in cached:
        return cached[(x,n)]
    res = cur[x] * prob(x+1, n-1) + (1-cur[x]) * prob(x+1, n+1)
    cached[(x,n)] = res
    return res

for nn in xrange(n):
    [l, s] = map(int, raw_input().split())
    inp = map(float, raw_input().split())
    inp.sort()
    inp += inp

    best = 0.0
    for i in xrange(l-s, l+1):
        cached = {}
        cur = inp[i:i+s]
        rr = prob(0, 0)
        if rr > best:
            best = rr

    print "Case #{}: {}".format(nn+1, best)