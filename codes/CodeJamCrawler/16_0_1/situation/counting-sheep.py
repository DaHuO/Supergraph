#!/usr/bin/env python3
__author__ = 'Alessandro Puccetti'


import sys


def get_digits(n):
    n = str(n)
    return [_ for _ in n]


def update_digits(digits, n):
    n_digits = (get_digits(n))
    for d in n_digits:
        if d not in digits:
            digits.add(d)
    return digits


def main():

    input_file_name = sys.argv[1]
    f = open(input_file_name, 'r')
    test_cases = int(f.readline())
    input_tests = []

    digits = set()

    for t in range(test_cases):
        n = int(f.readline())
        if n == 0:
            print ('Case #' + str(t + 1) + ': INSOMNIA')
            continue
        n_digits = (get_digits(n))
        i = 1
        digits = set()
        while len(digits) < 10:
            # print (n * i)
            digits = update_digits(digits, n * i)
            # print (digits)
            i += 1
        i -= 1
        print ('Case #' + str(t + 1) + ': ' + str(n * i))

    return

if __name__ == '__main__':
    main()
