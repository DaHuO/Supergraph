#!/usr/bin/env python

import util
# util.DEBUG = True


NUMBERS = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']


def pick(s, n):
    s = s[:]
    number = NUMBERS[n]
    for c in number:
        if c not in s:
            return False
        s.remove(c)
    return s


class Trying(object):

    def __init__(self, s, digits):
        self.s = s
        self.digits = digits

    def __repr__(self):
        return '<{} {}>'.format(self.s, self.digits)


pool = []


def search(s):
    pool.append(Trying(s, []))
    while pool:
        trying = pool.pop()
        if trying.s == []:
            return ''.join(map(str, sorted(trying.digits)))
        for i in range(0, 10):
            picked = pick(trying.s, i)
            if picked is False:
                continue
            pool.append(Trying(picked, trying.digits + [i]))
    assert False


def solution(idx):
    string = list(raw_input())
    digits = search(string)
    util.print_case(idx, digits)


if __name__ == '__main__':
    count = util.int_input()  # float_input, list_input
    util.loop(count, solution)