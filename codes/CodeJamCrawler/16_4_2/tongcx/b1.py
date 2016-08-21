from sys import stdin

T = int(stdin.readline())

def mul(v, x):
    return [y*x for y in v]

def add(u, v):
    return [x+y for x, y in zip(u,v)]

for case in xrange(T):
    N, K = map(int, stdin.readline().split())
    P = map(float, stdin.readline().split())
    ans = 0
    for mask in xrange(2**N):
        mask = ('{:0' + str(N) + 'b}').format(mask)
        if mask.count('1') == K:
            # print mask
            acc = [1, 0]
            for i, x in enumerate(mask):
                if x == '1':
                    acc = add([0] + mul(acc, P[i]), mul(acc, (1-P[i])) + [0])
                    # print acc
            if acc[K/2] > ans:
                ans = acc[K/2]
    print 'Case #{}: {}'.format(case+1, ans)
