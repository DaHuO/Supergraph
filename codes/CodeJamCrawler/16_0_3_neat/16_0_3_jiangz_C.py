#!/usr/bin/env python3
import math
import itertools


def factor(n):
    m = int(math.sqrt(n)) + 2
    for i in range(2, m):
        if n % i == 0:
            return i
    return 0

T = input()
N, J = map(int, input().split())


print('Case #1:')

s = {'{:0>{}s}'.format(bin(x)[2:], N-2) for x in range(2**(N-2))}

print(s)

cnt = 0

for perm in s:
    num = ''.join(['1', *perm, '1'])
    res = []
    for base in range(2, 11):
        x = int(num, base)
        f = factor(x)
        if f == 0:
            break
        res.append(f)
    if len(res) == 9:
        print(num, *res)
        cnt += 1
    # print(cnt)
    if cnt >= J:
        break

