def reduc(l):
    P, S, R = l
    N = (P + S + R) // 2
    return [N - S, N - R, N - P]

def build(letter, n):
    c = {'P': 'PR', 'R': 'RS', 'S': 'PS'}
    if n == 0:
        return [letter]
    bundle = []
    for l in c[letter]:
        bundle.append(build(l, n - 1))
    return bundle

def reduction(tree):
    if len(tree) == 1:
        return tree[0]
    else:
        t1, t2 = tree
        x = reduction(t1)
        y = reduction(t2)
        if x < y:
            return x + y
        else:
            return y + x

T = int(input())
for t in range(T):
    N, R, P, S = map(int, input().split())
    l = [P, S, R]
    stuff = []
    for _ in range(N):
        stuff.append(l)
        l = reduc(l)
    stuff.append(l)
    if any(x < 0 for x in l):
        sol = 'IMPOSSIBLE'
    else:
        sol = reduction(build('PSR'[l.index(1)], N))
    print('Case #%d: %s' % (t + 1, sol))

reduc([1, 2, 1])
