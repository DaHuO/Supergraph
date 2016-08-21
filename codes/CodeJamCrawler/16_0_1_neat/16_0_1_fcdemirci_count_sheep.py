#!/usr/bin/env python
ALL_DIGITS = set(range(10))


def get_digits(number):
    return [int(i) for i in str(number)]


def get_last_number(start_number):
    already_seen = set()
    last_seen = None
    N = 1
    while True:
        current_number = start_number * N
        digits = get_digits(current_number)
        already_seen.update(digits)
        if already_seen == ALL_DIGITS:
            return current_number
        if last_seen is not None:
            if digits == last_seen:
                return None
        last_seen = digits
        N += 1

if __name__ == "__main__":
    num_test_cases = int(input())
    for test_case in range(1, num_test_cases+1):
        number = int(input())
        last_number = get_last_number(number)
        if last_number is None:
            print('Case #{}: INSOMNIA'.format(test_case))
        else:
            print('Case #{}: {}'.format(test_case, last_number))
