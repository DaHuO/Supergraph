from random import randint

def rand_coin(n):
    s = '1'
    for _ in range(n - 2):
        s += str(randint(0, 1))
    s += '1'
    return s

t = int(raw_input())
for cas in range(1, t + 1):
    n, j = map(int, raw_input().split())
    ans = {}
    while len(ans) < j:
        c = rand_coin(n)
        if c in ans:
            continue
        f = []
        for i in range(2, 10 + 1):
            x = int(c, i)
            if is_prime(x):
                break
            f.append(factor(x)[0][0])
        if len(f) == 9:
            ans[c] = f
    print 'Case #%d:' % cas
    for k, v in ans.iteritems():
        print k, ' '.join(map(str, v))
