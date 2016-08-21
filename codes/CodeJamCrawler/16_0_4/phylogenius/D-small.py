import sys
for x in range(1, int(sys.stdin.readline()) + 1):
    K, C, S = map(int, sys.stdin.readline().strip().split())
    print('Case #{}: {}'.format(x, ' '.join(map(str, range(1, K+1)))))
