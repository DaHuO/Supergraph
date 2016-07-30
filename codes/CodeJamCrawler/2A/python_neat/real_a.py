import sys, itertools, collections
sys.setrecursionlimit(10000)

read_ints = lambda: map(int, raw_input().split())
read_int  = input


def gen(win, level):
    if level == 0:
        return ['RPS'[win]]
    s1 = gen(win, level - 1)
    s2 = gen((win + 2) % 3, level - 1)
    return min(s1, s2) + max(s1, s2)


for no_t in xrange(1, read_int() + 1):
    n, r, p, s = read_ints()

    for win in xrange(3):
        tmp = gen(win, n)
        counter = collections.Counter(tmp)
        if counter['R'] == r and counter['P'] == p and counter['S'] == s:
            ans = ''.join(tmp)
            break
    else:
        ans = 'IMPOSSIBLE'
    print 'Case #%d: %s' % (no_t, ans)
