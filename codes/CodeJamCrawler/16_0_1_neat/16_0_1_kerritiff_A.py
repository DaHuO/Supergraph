def solve(x):
    if x == 0:
        return 'INSOMNIA'
    s = set()
    for i in range(10):
        s.add(i)
    i = 1
    while s:
        y = x * i
        z = y
        while z:
            s.discard(z % 10)
            z = z // 10
        i += 1
    return y

t = int(input())

for i in range(t):
    x = int(input())
    print('Case #%d: %s' % (i + 1, solve(x)))
