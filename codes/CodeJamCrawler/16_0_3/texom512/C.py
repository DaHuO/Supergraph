__author__ = 'texom512'

from math import sqrt

bases = range(2, 11)


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if not n % i:
            return i
    return n > 1


# print(is_prime(2038074743))

t = input()
n, j = map(int, input().split())

print('Case #1 ')

num = 2 ** (n - 1) + 1
# print('{0:b}'.format(num))

founds = 0
while founds != j:
    l = [is_prime(int('{0:b}'.format(num), base)) for base in bases]
    # print([int('{0:b}'.format(num), base) for base in bases])
    # print(l)
    if True not in l:
        print(*(['{0:b}'.format(num)] + l))
        founds += 1
    num += 2
