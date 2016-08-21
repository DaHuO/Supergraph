for t in range(int(input())):
    print('Case #{}: '.format(t+1), end='')
    x = n = int(input())
    if n == 0:
        print('INSOMNIA'.format(t))
    else:
        seen = set(str(n))
        while len(seen) < 10:
            x += n
            seen |= set(str(x))
        print(x)
