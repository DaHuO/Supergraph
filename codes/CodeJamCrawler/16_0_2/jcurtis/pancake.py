def group(s):
    s = list(s)
    l = len(s)
    g = []
    old = ''
    while l > 0:
        tmp = s.pop()
        l -= 1
        if tmp != old:
            old = tmp
            g.append(old)
    return g

def solve(s):
    g = group(s)
    c = g.count('-') * 2
    if s[0] == '-':
        c -= 1
    return c

def test():
    tmp = '+' * 100
    for i in range(1, 101):
        assert(solve(tmp[0:i]) == 0)
    tmp = '-' * 100
    for i in range(1, 101):
        assert(solve(tmp[0:i]) == 1)

T = int(raw_input())

test()

for n in range(1, T+1):
    s = solve(raw_input())
    print('Case #{}: {}'.format(n, s))
