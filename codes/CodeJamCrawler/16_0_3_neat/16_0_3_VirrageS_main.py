from math import sqrt
from itertools import count, islice
import random


def power_it(x, b):
    a = x
    x = 1

    for i in range(0, b):
        x = x * a

    return x

def is_prime(n):
    return n > 1 and all(n%i )

def check_in_base(s, base):
    s = s[::-1]

    tmp = 0
    for idx, c in enumerate(s):
        if c == '0':
            continue

        tmp += power_it(base, idx)

    for i in range(2, min(100000, int(sqrt(tmp) - 1))):
        if tmp % i == 0:
            return i

    return -1


n = int(input()) + 1

for i in range(1, n):
    a, b = map(int, input().split())

    print('Case #' + str(i) + ':')

    found = 0
    remember = []
    while found < b:

        s = '1'
        for i in range(0, a - 2):
            s += random.choice(['0', '1'])
        s += '1'

        if s in remember:
            continue

        remember.append(s)

        result = []
        for base in range(2, 10 + 1):
            res = check_in_base(s, base)
            if res < 0:
                break

            result.append(res)

        if len(result) == 9:
            print(s, end="")

            for x in result:
                print(' ' + str(x), end="")

            print('')
            found = found + 1
