# @see

import sys


def print_result(case_number, data):
    print('Case #{}: {}'.format(
        case_number + 1,
        data
    ))


tests_numbers = int(input().strip())

for i in range(tests_numbers):
    K, C, S = [int(x) for x in input().strip().split(' ')]

    print_result(i, ' '.join([str(x + 1) for x in range(K)]))
