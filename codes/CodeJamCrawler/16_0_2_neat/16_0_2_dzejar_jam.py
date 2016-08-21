#!/bin/env python
#coding: utf8

import sys
import time


class PancakeStack():
    def __init__(self, str):
        self._stack = map(lambda x: x == '+', list(str.strip()))

    @property
    def size(self):
        return len(self._stack)

    def __repr__(self):
        return ''.join(map(lambda x: '+' if x else '-', self._stack))

    def __getitem__(self, item):
        return self._stack[item]

    def is_ready(self):
        return set(self._stack) == set([True])

    def flip(self, n):
        assert n <= self.size
        self._stack[:n] = map(lambda x: not x, reversed(self._stack[:n]))

    def lower_sad_index(self):
        return self.size - self._stack[::-1].index(False)

    def upper_sad_index(self):
        return self.size - self._stack.index(False)

    def first_change_index(self):
        c = self._stack[0]
        for i, x in enumerate(self._stack):
            if x != c:
                return i
        return i + 1


def parse_input():
    count = int(sys.stdin.readline())
    for n in range(count):
        x = sys.stdin.readline()
        yield n + 1, x


def solve_task(input):
    ps = PancakeStack(input)
    # print ps, ps.is_ready(), ps[0:ps.size]
    steps = 0
    while not ps.is_ready():
        # print ps, ps.first_change_index()
        ps.flip(ps.first_change_index())
        steps += 1
    return steps


for i, n in parse_input():
    print "Case #%s: %s" % (i, solve_task(n))

