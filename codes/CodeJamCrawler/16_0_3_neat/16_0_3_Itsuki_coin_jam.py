#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def make_digits(i):
    digits = []
    while i > 0:
        r = i % 2
        digits.append(r)
        i = i // 2
    digits.reverse()
    return digits


def findDivisor(n):
    if n % 2 == 0:
        return 2

    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return -1


def convert(digits, base):
    result = 0
    power = len(digits) - 1
    for digit in digits:
        result += digit * (base ** power)
        power -= 1
    return result


def convert2baseExpression(i):
    digits = []
    while i > 0:
        r = i % 2
        digits.append(r)
        i = i // 2
    digits.reverse()
    return ''.join(digits)


def print_coin_jam(n, j):
    begin = 1 + 2 ** (n - 1)
    end = 2 ** n - 1
    count = 0
    for i in range(begin, end + 1, 2):
        digits = make_digits(i)
        divisors = []
        for base in range(2, 11):
            converted = convert(digits, base)
            divisor = findDivisor(converted)
            if divisor == -1:
                break
            divisors.append(divisor)
        if len(divisors) == 9:
            result = ''
            for digit in digits:
                result += str(digit)
            for divisor in divisors:
                result += ' '
                result += str(divisor)
            print(result)
            count += 1
            if count >= j:
                return


if __name__ == '__main__':
    test_cases = int(input())
    for t in range(1, test_cases + 1):
        in_data = input().split(' ')
        n = int(in_data[0])
        j = int(in_data[1])
        print('Case #{}:'.format(t))
        print_coin_jam(n, j)
