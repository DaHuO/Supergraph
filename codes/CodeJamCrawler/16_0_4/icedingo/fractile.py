T = int(input())

for t in range(1, T+1):
    K, C, S = map(int, input().split())

    print('Case #{}: {}'.format(t, ' '.join(str(i*(sum(K**(P) for P in range(C))) + 1) for i in range(K))))
