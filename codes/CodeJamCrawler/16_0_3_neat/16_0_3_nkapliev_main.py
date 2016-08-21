# @see

import sys
import random


base_cache = [[base ** x for x in range(32)] for base in range(11)]
prime_limit = 1000


def print_result(case_number, data):
    print('Case #{}: {}'.format(
        case_number + 1,
        data
    ))


def get_div(num):
    for i in range(prime_limit):
        if i > 1 and int(num % i) == 0:
            return i

    return False


def get_random_num(length):
    return random.randint(2 ** (length - 2), 2 ** (length - 1) - 1) * 2 + 1

    # return '1' + ''.join([str(x) for x in range(length - 2)]) + '1'


def get_based_num(new_num, base):
    res = 0
    i = 0

    while new_num > 0:
        tmp = int(new_num % 2)

        if tmp == 1:
            res += base_cache[base][i]

        new_num //= 2
        i += 1

    return res

tests_numbers = int(input().strip())

for i in range(tests_numbers):
    N, J = [int(x) for x in input().strip().split(' ')]

    numbers = []
    numbers_divs = []
    prime_numbers = []

    while J != 0:
        new_num = get_random_num(N)

        if new_num in numbers or new_num in prime_numbers:
            continue

        is_not_prime_in_all_bases = True
        divs = []

        for base in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            based_num = get_based_num(new_num, base)
            div = get_div(based_num)

            if not div:
                is_not_prime_in_all_bases = False
                break
            else:
                divs.append(str(div))

        if is_not_prime_in_all_bases:
            numbers.append(new_num)
            numbers_divs.append(divs)
            J -= 1
        else:
            prime_numbers.append(new_num)

    print('Case #{}:'.format(i + 1))

    for number_index in range(len(numbers)):
        print('{0:b} {1}'.format(numbers[number_index], ' '.join(numbers_divs[number_index])))
