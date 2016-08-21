# @see

import sys


def print_result(case_number, data):
    print('Case #{}: {}'.format(
        case_number + 1,
        data
    ))


LIMIT = 1000

tests_numbers = int(input().strip())

for i in range(tests_numbers):
    N = int(input().strip())

    if N == 0:
        print_result(i, 'INSOMNIA')
    else:
        k = 1
        NN = N
        arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        while k < LIMIT:
            tmp = NN

            while tmp:
                arr[int(tmp % 10)] = 1
                tmp //= 10

            if sum(arr) == 10:
                break
            else:
                k += 1
                NN += N

        if k < LIMIT:
            print_result(i, NN)
        else:
            print_result(i, 'INSOMNIA')
