#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

# standard module
import os
import sys

# install required

# from local script

class Codejam1Solver:

    def __init__(self, chosen):
        self.N = int(chosen)

    def __separate_digits(self, value):
        return set([digit for digit in str(value)])

    def __iter_chosen(self):
        cnt = 1
        while True:
            yield cnt * self.N
            cnt += 1

    def __has_fall_sleep(self, seen):
        for item in [str(n) for n in range(10)]:
            if item not in set(seen):
                return False
        return True

    def get_answer(self):

        if self.N == 0:
            return "INSOMNIA"

        seen = []

        for i, v in enumerate(self.__iter_chosen()):

            seen += self.__separate_digits(v)
            if self.__has_fall_sleep(seen):
                return v

lines = [line.strip() for line in open(sys.argv[1])]
target = lines[1:int(lines[0])+1]
for i, N in enumerate(target):
    solver = Codejam1Solver(N)
    print("Case #{0}: {1}".format(i + 1 , solver.get_answer()))
