T = int(input())
for t in range(T):
    K, C, S = [int(x) for x in input().split()]
    print('Case #{}:'.format(t+1), end='')
    for k in range(K):
        print(' {}'.format(k+1), end='')
    print()
