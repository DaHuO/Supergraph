#!/usr/bin/env python

T = int(input())

ii = 1

def make_possible(arr, s=None):
    if s is None:
        s = ''
    elif len(s) == len(arr):
        return [s]

    combs = []
    for elem in arr[len(s)]:
        for x in elem:
            # print('s , x', s, x)
            combs.extend(make_possible(arr, s + x))

    return combs



while ii <= T:
    C, J = input().split()

    C_1, J_1 = [None] * len(C), [None] * len(C)
    for j in range(len(C)):
        if C[j] == '?' and J[j] == '?':
            C_1[j] = [str(x) for x in range(0, 10)] # ['9', '0', '1']
            J_1[j] = [str(x) for x in range(0, 10)] # ['9', '0', '1']
        elif C[j] == '?' and J[j] != '?':
            C_1[j] = [str(x) for x in range(0, 10)] # [str(x % 10) for x in [int(J[j]) - 1, int(J[j]), int(J[j]) + 1]]
            J_1[j] = [J[j]]
        elif C[j] != '?' and J[j] == '?':
            C_1[j] = [C[j]]
            J_1[j] = [str(x) for x in range(0, 10)] # [str(x % 10) for x in [int(C[j]) - 1, int(C[j]), int(C[j]) + 1]]
        else:
            C_1[j] = [C[j]]
            J_1[j] = [J[j]]

    C_all = sorted([(int(x), x) for x in make_possible(C_1)])
    J_all = sorted([(int(x), x) for x in make_possible(J_1)])

    C_final, J_final = '', ''
    diff_min = 10 ** 20
    for (c, cstr) in C_all:
        for (j, jstr) in J_all:
            d = abs(c - j)
            if d < diff_min:
                C_final, J_final, diff_min = cstr, jstr, d

    print('Case #{}: {} {}'.format(ii, C_final, J_final))
    ii += 1
