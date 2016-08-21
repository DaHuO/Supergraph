T = int(input())
for _ in range(1, T+1):
    N = int(input())
    D = {}
    flag = 0
    for k1 in range(1, 1000):
        X = N*k1
        for k2 in str(X):
            D[k2] = 1
        if sum(D.values())==10:
            flag=1
            break
    print('Case #{}: {}'.format(_, X) if flag==1 else 'Case #{}: Insomnia'.format(_))


