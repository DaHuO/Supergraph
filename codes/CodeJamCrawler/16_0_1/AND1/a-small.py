
T = int(input())

for t in range(0, T):
    N = int(input())
    vis = [False] * 10
    last = 0
    for i in range(0, 101):
        r = last + N
        last = r
        while r > 0:
            d = r % 10
            vis[d] = True
            r //= 10
        if vis == [True] * 10:
            break
    if vis == [True] * 10:
        print('Case #{0}: {1}'.format(t + 1, last))
    else:
        print('Case #{0}: INSOMNIA'.format(t + 1))



