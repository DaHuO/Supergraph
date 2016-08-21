# run with PyPy 2.6.1

typ = {0: 'P', 1: 'R', 2: 'S'}


def winner(x, y):
    if x > y:
        return winner(y, x)
    # x <= y
    if x == 'P' and y == 'R':
        return 'P'
    if x == 'P' and y == 'S':
        return 'S'
    if x == 'R' and y == 'S':
        return 'R'
    raise ValueError

def good(a):
    if len(a) == 1:
        return True
    b = []
    for i in xrange(0, len(a), 2):
        if a[i] == a[i + 1]:
            return False
        else:
            b.append(winner(a[i], a[i+1]))
    return good(b)

def valid(a, r, p, s):
    return (
        (sum(1 for x in a if x == 'R') == r) and
        (sum(1 for x in a  if x == 'P' ) == p) and
        (sum(1 for x in a if x == 'S' ) == s)
        )

def f(n, r, p, s):
    ans = ''
    for mask in xrange(3**(2**n)):
        t = mask
        a = []
        for i in xrange(2**n):
            a.append(typ[t % 3])
            t = t / 3
        # print a, valid(a, r, p, s), good(a)
        if valid(a, r, p, s) and good(a):
            # print '!!!!!!!!!!', a
            if (not ans) or a < ans:
                ans = a
    if not ans:
        return "IMPOSSIBLE"
    return ''.join(ans)

loser = {
    'P': 'R',
    'R': 'S',
    'S': 'P',
}

def build(n, root):
    if n == 0:
        return root
    u = loser[root]
    c1 = build(n - 1, root)
    c2 = build(n - 1, u)
    if c1 < c2:
        return c1 + c2
    else:
        return c2 + c1

def g(n, r, p, s):
    ans = 'ZZZ'
    pp = build(n, 'P')
    rr = build(n, 'R')
    ss = build(n, 'S')
    for uu in [pp, rr, ss]:
        if valid(uu, r, p ,s):
            ans = min(ans, uu)
    if ans == 'ZZZ':
        return 'IMPOSSIBLE'
    return ans

test_count = int(raw_input().strip())
for test in xrange(1, test_count + 1):
    line = raw_input().strip().split(' ')
    n, r, p, s = [int(x) for x in line]
    print 'Case #{}: {}'.format(test, g(n, r, p, s))