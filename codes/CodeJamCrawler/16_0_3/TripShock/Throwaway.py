#!/usr/bin/env python

# https://pypi.python.org/pypi/primefac
import primefac


def convert_to_base(num, base):
    if base == 2:
        return num

    multiply = 1
    result = 0
    while num != 0:
        result += multiply * (num % 2)
        num /= 2
        multiply *= base
    return result


def find_prime_factor(num):
    return next(primefac.primefac(num, methods=(primefac.ecm,)))


def check_and_print_jamcoin(trial_num):
    if trial_num % 2 == 0:
        return False

    factors = []
    for base in range(2, 11):
        num = convert_to_base(trial_num, base)
        prime_factor = find_prime_factor(num)
        if prime_factor == num:
            return False
        factors.append(prime_factor)

    print("{:b} {}".format(trial_num, " ".join(str(f) for f in factors)))
    return True


if __name__ == "__main__":

    num_test_cases = int(raw_input())

    for test_case in range(1, num_test_cases + 1):
        # j = num_jamcoins
        # n = jamcoin_length

        jamcoin_length, num_jamcoins = (int(x) for x in raw_input().split())

        print("Case #{}:".format(test_case))

        trial_num = int("1" + ("0" * (jamcoin_length - 2)) + "1", base=2)
        found_num_jamcoins = 0

        while found_num_jamcoins < num_jamcoins:
            if check_and_print_jamcoin(trial_num):
                found_num_jamcoins += 1
            trial_num += 1
