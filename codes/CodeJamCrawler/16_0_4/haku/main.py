with open('/Users/sigma/Downloads/D-small-attempt0.in.txt') as inf,\
        open('/Users/sigma/Documents/output.txt', 'w') as ouf:
    tn = int(inf.readline())
    for ti in range(tn):
        k, c, s = map(int, inf.readline().split())
        if s < k:
            ans = 'IMPOSSIBLE'
        else:
            ans = ' '.join([str(i * (k ** (c - 1)) + 1) for i in range(k)])
        print('Case #{}: {}'.format(ti + 1, ans), file=ouf)