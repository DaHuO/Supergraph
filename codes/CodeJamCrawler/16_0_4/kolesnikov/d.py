import sys

T = int(sys.stdin.next())

for i in range(T):
    [K, C, S] = map(int, sys.stdin.next().split(' '))

    print(('Case #%i: ' % (i + 1)) + ' '.join(map(str, range(1, K + 1))))
