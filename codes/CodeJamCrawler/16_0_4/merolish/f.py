for t in range(int(input())):
    k, c, s = map(int, input().split())
    print('Case #{}:'.format(t + 1), end='')
    if s < k:
        print(' IMPOSSIBLE')
    else:
        for i in range(1, k ** c + 1, k ** (c - 1)):
            print(' {}'.format(i), end='')
        print()

