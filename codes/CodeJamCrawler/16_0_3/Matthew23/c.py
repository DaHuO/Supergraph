#!/usr/bin/python3
# -*- coding: utf8 -*-
# Google Code Jam 2016 - Qualification Round - Problem B - Mateusz Kurek

import numpy as np


def main():
    t = int(input())
    for i in range(1, t+1):
        n, j = map(int, input().split())
        print('Case #{}:'.format(i))
        for num, dividers in find_complex_numbers(n):
            print(' '.join(map(str, [num] + dividers)))
            j -= 1
            if j == 0:
                break


# def get_dividers(n):
#     np1 = n + 1
#     s = list(range(np1))
#     sqrtn = int(round(n**0.5)) + 1
#     # print('looking for dividers from 2 to {} (n={})'.format(sqrtn, n))
#     for i in range(2, sqrtn):
#         if s[i] > 0:
#             s[i*i: np1: i] = [-i] * len(range(i*i, np1, i))
#     return dict([(k, -v) for k, v in enumerate(s) if v < 0])


# def get_dividers(n):
#     result = []
#     for base in range(2, 10):
#         num = int(np.base_repr(n, base=base))
#         divider = get_divider(num)
#     return True, [2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_divider(n):
    sqrtn = int(round(n**0.5)) + 1
    for i in range(2, sqrtn):
        if n % i == 0:
            return i


def log(*s):
    pass


def find_complex_numbers(binary_number_length):
    # dividers = get_dividers(10**binary_number_length)
    # for k, v in sorted(dividers.items()):
    #     print('{} -> {}'.format(k, v))
    for i in range(2**(binary_number_length-1) + 1, 2**(binary_number_length), 2):
        base2 = np.base_repr(i, base=2)
        idividers = []
        log(i, base2)
        for base in range(2, 11):
            num_base = int(base2, base=base)
            divider = get_divider(num_base)
            log(base, num_base, divider)
            if divider:
                idividers.append(divider)
            else:
                break
        log(i, len(idividers), idividers)
        if len(idividers) == 9:
            log("ok!")
            yield base2, idividers
        log('=======')


if __name__ == '__main__':
    # for k, v in sorted(get_dividers(20).items()):
    #     print('{} -> {}'.format(k, v))
    # get_dividers(2**23)

    # for x in get_dividers_2(2**5).items():
    #     print(x)
    # get_dividers_2(2**16)
    main()
