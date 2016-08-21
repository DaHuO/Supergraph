#  -*- coding: utf-8 -*-
import logging
import sys


def setup_logging():
    if len(sys.argv) > 1 and 'debug' in sys.argv[1]:
        level = logging.DEBUG
    else:
        level = logging.ERROR
    logging.basicConfig(format='[%(levelname)s]: %(message)s', level=level)


def line():
    return next(sys.stdin).strip()


M = {
    "ZERO": 0,
    "ONE": 1,
    "TWO": 2,
    "THREE": 3,
    "FOUR": 4,
    "FIVE": 5,
    "SIX": 6,
    "SEVEN": 7,
    "EIGHT": 8,
    "NINE": 9
}


M1 = {
    'Z': 'ZERO',
    # ('ONE', set([]))
    'W': 'TWO',
    # ('THREE', set([]))
    'U': 'FOUR',
    # ('FIVE', set([]))
    'X': 'SIX',
    # ('SEVEN', set([]))
    'G': 'EIGHT',
    # ('NINE', set([]))
}

M2 = {
    'O': 'ONE',
    'H': 'THREE',
    'F': 'FIVE',
    'S': 'SEVEN'
}


def replace(L, mapping):
    numbers = []
    for k, v in mapping.iteritems():
        c = L.count(k)
        if c > 0:
            numbers.extend(str(M[v]) for _ in xrange(c))
            for l in v:
                L = L.replace(l, '', c)
    return L, numbers


def solution(L):
    logging.debug('%s', L)
    L, n1 = replace(L, M1)
    L, n2 = replace(L, M2)
    assert len(L) == 0 or (len(L) % 4 == 0 and set(L) == {'N', 'I', 'E'}), L
    n3 = ['9' for _ in xrange(len(L) / 4)]
    return ''.join(sorted(n1 + n2 + n3))


def main():
    T = int(line())  # num test cases
    for case_num in range(1, T + 1):
        # A = map(int, line().split(' '))
        print "Case #%s:" % case_num, solution(line())


if __name__ == '__main__':
    setup_logging()
    main()
