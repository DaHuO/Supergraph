for tc in range(1, int(input())+1):
    n = int(input())
    print('Case #{}: '.format(str(tc)), end='')
    if n==0:
        print('INSOMNIA')
        continue
    a = set(range(10))
    for i in range(1, 10000000):
        a -= set([int(x) for x in str(i*n)])
        if not len(a):
            print(i*n)
            break
