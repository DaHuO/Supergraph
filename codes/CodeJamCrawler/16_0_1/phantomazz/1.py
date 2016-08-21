# -*- coding: utf-8 -*-

import sys


def load_input_data():
    with open(sys.argv[1], "r") as input_file:
        input_data = input_file.readlines()
        return input_data[1:]


def process_found_digits(found_digits, current_number):
    result = found_digits
    for digit in str(current_number):
        result[int(digit)] = 1
    return result


def get_last_number(first_number):
    found_digits = [0] * 10
    current_multiplier = 1

    while found_digits.count(1) != 10:
        found_digits = process_found_digits(
            found_digits, first_number * current_multiplier)
        current_multiplier = current_multiplier + 1
    return first_number * (current_multiplier - 1)


def solve_case(index, input_case):
    if input_case == "0":
        print("Case #{0}: INSOMNIA".format(index))
        return
    print("Case #{0}: {1}".format(index, get_last_number(int(input_case))))


def solve(input_data):
    for index, input_case in enumerate(input_data):
        solve_case(index + 1, input_case.strip())


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Invalid arguments"
        sys.exit
    solve(load_input_data())
