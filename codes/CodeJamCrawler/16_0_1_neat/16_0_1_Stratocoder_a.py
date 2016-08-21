t = int(raw_input())

for tt in xrange(t):
    n = int(raw_input())
    if n == 0:
        ans = 'INSOMNIA'
    else:
        dig = set()
        mul = 0
        while len(dig) < 10:
            mul += 1
            map(dig.add, str(n * mul))
        ans = n * mul
    print 'Case #{}: {}'.format(tt + 1, ans)
