rl = lambda: map(int, raw_input().split())


def sol(k, c, s):
    r = []
    p = 0
    x = 0
    i = 0
    while i < k or x > 0:
        p += min(i, k - 1)
        x += 1
        if x == c:
            r.append(p + 1)
            x = 0
            p = 0
        p *= k
        i += 1
    if len(r) > s:
        return "IMPOSSIBLE"
    return " ".join(map(str, r))

t = input()
for i in xrange(t):
    k, c, s = rl()
    print "Case #%d:" % (i + 1), sol(k, c, s)
