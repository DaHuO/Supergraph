# -*- coding: utf-8 -*-
"""
"""

import sys
import multiprocessing


class CaseReader(object):
    def __init__(self, cases=None):
        if cases is None:
            cases = sys.argv[1]
        if isinstance(cases, str):
            cases = open(cases)
        cases.seek(0)
        coin_length, total_cases = cases.readlines().pop().split(" ")
        self.coin_length = abs(int(coin_length))
        self.total_cases = abs(int(total_cases))
        self._value = int("1{:0>#0{}}".format(1, self.coin_length - 1), 2)
        while len(self.value) < self.coin_length:
            next(self)

    def __len__(self):
        return self.total_cases

    def __iter__(self):
        return self

    def __next__(self):
        self._value += 2
        value = self.value
        if len(value) > self.coin_length:
            raise StopIteration()
        return value

    @property
    def value(self):
        return str(bin(self._value)).replace("0b", "", 1)


def get_divisor(number):
    number = abs(int(number))
    if number <= 1:
        return None
    if not number % 2:
        return 2
    if not number % 3:
        return 3

    def multipliers(value=5):
        while True:
            yield value
            value += 6

    def find(divisors):
        """
        https://en.wikipedia.org/wiki/Primality_test#Pseudocode
        """
        while True:
            value = next(divisors)
            if pow(value, 2) > number:
                return None
            if not number % value:
                return value
            value += 2
            if not number % value:
                return value
    return find(multipliers())


def iter_cases(tests):
    for item in range(tests.total_cases):
        iter_values(tests)


def iter_values(tests):
    for value in tests:
        if iter_bases(value):
            return


def iter_bases(value):
    divisors = [value, None]
    for base in range(2, 11):
        base_value = int(value, base)
        divisors.insert(base, get_divisor(base_value))
        if divisors[base] is None:
            return False
    print("{0} {2} {3} {4} {5} {6} {7} {8} {9} {10}".format(*divisors))
    return True


if __name__ == "__main__":
    print("Case #1:")
    iter_cases(CaseReader())
