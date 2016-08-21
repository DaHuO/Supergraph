#!/usr/bin/env python3

def i_th(k, c, i):
    res = 0
    for j in range(1, c):
        res += (i-1) * (k**(j))
    res += i
    return res

# print(i_th(3, 3, 2))
# print(i_th(2, 2, 2))
# print(i_th(4, 5, 1))

def solve_small(k, c):
    res = []
    for i in range(1, k+1):
        res.append(i_th(k, c, i))
    return map(str, res)


T = int(input())

for i in range(T):
    K, C, S = map(int, input().split())
    if K == S:
        res = ' '.join(solve_small(K, C))
    else:
        res = ''
    print('Case #{}: {}'.format(i+1, res))
