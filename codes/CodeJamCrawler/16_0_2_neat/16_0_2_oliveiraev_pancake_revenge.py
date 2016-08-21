# -*- coding: utf-8 -*-
"""
"""

import sys


class CaseReader(object):
    def __init__(self, cases=None):
        if cases is None:
            cases = sys.argv[1]
        if isinstance(cases, str):
            cases = open(cases)
        self.cases = cases
        self.total_cases = abs(int(self.cases.readline()))

    def __len__(self):
        return self.total_cases

    def __iter__(self):
        return self

    def __next__(self):
        return self.cases.readline().replace("\n", "")


class Stack(object):
    def __init__(self, pancakes):
        self.pancakes = list(pancakes)
        self.flips = 0

    @property
    def heads_up(self):
        return "-" not in self.pancakes

    def flip(self, pancakes=1):
        stack_slice = reversed(self.pancakes[:pancakes])
        stack_slice = [pancake is "+" and "-" or "+" for pancake in stack_slice]
        if stack_slice[0] == "+" and stack_slice[-1] == "-":
            return self.flip(pancakes - 1)
        self.pancakes = stack_slice + self.pancakes[pancakes:]
        self.flips += 1


if __name__ == "__main__":
    tests = CaseReader()
    for case in range(len(tests)):
        print("Case #{}: ".format(case + 1), end="")
        stack = Stack(next(tests))
        while not stack.heads_up:
            stack.flip("".join(stack.pancakes).rfind("-") + 1)
        print(stack.flips)
