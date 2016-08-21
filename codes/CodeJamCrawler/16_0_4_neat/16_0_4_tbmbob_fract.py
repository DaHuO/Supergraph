for i in range(int(input())):
    k, c, s = map(int, input().split())
    print('Case #%d: ' % (1+i), end='')
    if k != s:
        print('IMPOSSIBLE')
        continue
    ans = [str(1 + j * k**(c-1)) for j in range(s)]
    print(' '.join(ans))
