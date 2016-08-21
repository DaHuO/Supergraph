T = int(input())

for t in range(1, T + 1):
    N = int(input())
    if N == 0:
        print('Case #{0}: INSOMNIA'.format(t))
    else:
        res = 0
        temp = N
        count = 1
        while res != (1 << 10) - 1:
            temp = str(temp)
            for i in temp:
                x = int(i)
                res |= 1 << x
            count += 1
            temp = N * count
        print('Case #{0}: {1}'.format(t, temp - N))

