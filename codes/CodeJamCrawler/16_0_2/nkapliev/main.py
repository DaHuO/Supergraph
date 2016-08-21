

# @see

import sys


def print_result(case_number, data):
    print('Case #{}: {}'.format(
        case_number + 1,
        data
    ))


tests_numbers = int(input().strip())

for i in range(tests_numbers):
    res = 0
    pancakes = input().strip()

    for pIndex in range(len(pancakes)):
        if pIndex > 0 and pancakes[pIndex] != pancakes[pIndex - 1]:
            res += 1

    if pancakes[-1] == '-':
        res += 1

    print_result(i, res)
