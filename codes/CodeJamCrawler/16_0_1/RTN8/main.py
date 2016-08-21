# -*- coding: utf-8 -*-

ETALON = set(range(10))


def get_numbers(number):
    numbers = {number % 10}
    while True:
        number //= 10
        if number == 0:
            break
        numbers.add(number % 10)
    return numbers


def solve(input_args):
    number = int(input_args)

    if number == 0:
        return 'INSOMNIA'
    numbers = get_numbers(number)
    multiplier = 1
    while numbers != ETALON:
        multiplier += 1
        next_number = number * multiplier
        numbers |= get_numbers(next_number)
    return next_number


if __name__ == '__main__':
    cases_number = int(input())
    for case_number in range(1, cases_number + 1):
        input_args = input()
        print('Case #%s: %s' % (case_number, solve(input_args)))
