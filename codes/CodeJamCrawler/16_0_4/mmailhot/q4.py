import sys

n = int(sys.stdin.readline())

for i in range(n):
    k, c, s = map(int, sys.stdin.readline().split(' '))
    print("Case #{}: {}".format( i + 1, ' '.join(map(str, range(1, k + 1)))))
