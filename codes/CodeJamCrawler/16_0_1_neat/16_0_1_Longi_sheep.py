#!/usr/bin/python3

import sys


def main():
    with open(sys.argv[1]) as input_file:
        content = [line.strip('\n') for line in input_file.readlines()]

    case_count = int(content[0])

    with open('output', 'w') as output_file:
        for case_number in range(1, case_count + 1):
            input_number = int(content[case_number])

            result = count_sheep(input_number)

            output_file.write('Case #' + str(case_number) + ": " + result + '\n')


def count_sheep(n):
    if n == 0:
        return 'INSOMNIA'

    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    multiplier = 0

    while len(digits) > 0:
        multiplier += 1
        current = multiplier * n

        while current > 0 and len(digits) > 0:
            digit = current % 10
            if digit in digits: digits.remove(digit)
            current //= 10

    return str(multiplier * n)


if __name__ == '__main__':
    main()
