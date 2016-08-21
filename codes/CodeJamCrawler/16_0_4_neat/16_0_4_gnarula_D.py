T = int(input())

for t in range(1, T + 1):
    K, C, S = list(map(int, input().split()))
    print('Case #{0}:'.format(t), end=' ')
    for i in range(1, K):
        print(i, end=' ')
    print(K)
