T = int(raw_input())

for t in range(T):
    k, c, s = map(int, raw_input().split())
    if c*s < k:
        print('Case #%d: IMPOSSIBLE' % (t+1))
    else:
        l = range(k)
        if k % c != 0:
            l += [0] * (c - k%c)
        l.reverse()
        out = []
        while len(l):
            num = 0
            for _ in range(c):
                num = num*k + l.pop()
            out.append(num+1)
        print('Case #%d: ' % (t+1) + ' '.join(map(str, out)))
