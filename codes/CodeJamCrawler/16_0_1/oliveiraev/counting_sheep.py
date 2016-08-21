# -*- coding: utf-8 -*-
"""
"""

import sys


class Parser(object):
    def __init__(self, test_suite=None):
        if test_suite is None:
            test_suite = sys.argv[1]
        if isinstance(test_suite, str):
            test_suite = open(test_suite)
        self.suite = test_suite
        self.remaining_cases = int(self.suite.readline())

    def __len__(self):
        return self.remaining_cases

    @property
    def case(self):
        return Case(self.suite.readline())


class Case(int):
    pass

class Insomnia(StopIteration):
    pass


class Asleep(StopIteration):
    pass


class Sheep(object):
    current_number = None

    def __init__(self, initial_number=0):
        self.multiplier = 1
        self.initial_number = abs(int(initial_number))
        self.remaining_digits = list("0123456789")

    @property
    def awaken(self):
        return bool(self.remaining_digits)

    def __iter__(self):
        return self

    def count(self):
        self.current_number = self.initial_number * self.multiplier
        self.multiplier += 1
        for digit in set(str(self.current_number)):
            if digit in self.remaining_digits:
                self.remaining_digits.remove(digit)
        if not self.awaken:
            raise Asleep()
        if self.current_number * self.multiplier != self.current_number:
            return self.current_number
        raise Insomnia()

    __next__ = count


if __name__ == "__main__":
    tests = Parser()
    for case in range(len(tests)):
        print("Case #{}: ".format(case + 1), end="")
        sheep = Sheep(tests.case)
        try:
            while sheep.awaken:
                sheep.count()
        except Asleep:
            print(sheep.current_number)
        except Insomnia:
            print("INSOMNIA")
