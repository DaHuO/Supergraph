t = int(input())
for i in range(t):
    k, c, s = map(int, input().split())
    print('Case #{}: {}'.format(i+1, ' '.join(map(str, range(1, s+1)))))
