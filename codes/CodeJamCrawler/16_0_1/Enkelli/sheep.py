#!/usr/bin/env python3

import sys


def get_file_content(f):
    with open(f, 'r') as input_file:
        return input_file.read()


def sheep_count(start_number):
    if start_number == 0:
        return 'INSOMNIA'

    digits = ['X' for i in range(10)]
    number = start_number
    
    while True:
        for i in str(number):
            digits[int(i)] = i
        if digits == ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return number
        number += start_number


def main(argc, argv):
    if argc < 2:
        print("Hey man, give me some file.")
        sys.exit(1)

    numbers = get_file_content(argv[1]).split()
    # 1 <= T <= 100
    for i, num in enumerate(numbers[1:], 1):
        n = sheep_count(int(num))
        print("Case #{}: {}".format(i, n))
    


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
