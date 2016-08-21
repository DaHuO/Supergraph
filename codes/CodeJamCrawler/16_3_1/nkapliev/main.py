# @see

import sys


def print_result(case_number, data):
    print('Case #{}: {}'.format(
        case_number + 1,
        data
    ))


tests_numbers = int(input().strip())

for i in range(tests_numbers):
    res = ''
    N = int(input().strip())
    P = [int(p) for p in input().strip().split(' ')]

    while True:
        maxP = max(P)

        if maxP == 0:
            break

        maxIndex = P.index(maxP)
        P[maxIndex] -= 1
        res += chr(maxIndex + 65)

        if sum(P) == 2:
            res += ' '
            continue

        maxP = max(P)

        if maxP == 0:
            break

        maxIndex = P.index(maxP)
        P[maxIndex] -= 1
        res += chr(maxIndex + 65)

        res += ' '

    print_result(i, res.strip())
