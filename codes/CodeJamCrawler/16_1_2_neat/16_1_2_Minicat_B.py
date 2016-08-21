from collections import defaultdict

def solve(n, lists):
    # {height: {index: count}}}
    cat = {}
    for l in lists:
        for i, h in enumerate(l):
            if h not in cat:
                cat[h] = defaultdict(int)
            cat[h][i] += 1

    meow = []
    for height, mapping in cat.iteritems():
        total = 0
        for index, count in mapping.iteritems():
            total += count
        if total % 2 == 1:
            meow.append(height)

    return ' '.join([str(x) for x in sorted(meow)])

inp = open('B-large.in')
outp = open('Blarge.out', 'w')

T = int(inp.readline())

for ii in range(1, T+1):
    n = int(inp.readline())
    lists = []
    for i in range(0, 2*n-1):
        lists.append([int(x) for x in inp.readline().rstrip().split()])
    ans = solve(n, lists)
    outp.write('Case #{}: {}\n'.format(ii, ans))
    print 'Case #{}: {}'.format(ii, ans)

inp.close()
outp.close()
