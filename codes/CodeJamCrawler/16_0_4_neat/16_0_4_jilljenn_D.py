T = int(input())
for t in range(T):
    K, C, S = map(int, input().split())
    print('Case #%d: %s' % (t + 1, ' '.join(map(str, range(1, K + 1)))))
