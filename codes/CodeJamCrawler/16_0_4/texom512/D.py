__author__ = 'texom512'

t = int(input())
for i in range(t):
    k, c, s = map(int, input().split())
    # print(k, c, s)

    print('Case #{}: '.format(i + 1) + ' '.join(str(1 + i * k ** (c - 1)) for i in range(k)))
