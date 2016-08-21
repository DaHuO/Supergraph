#  -*- coding: utf-8 -*-
import logging
import sys

import heapq

sys.setrecursionlimit(10000)


def setup_logging():
    if len(sys.argv) > 1 and 'debug' in sys.argv[1]:
        level = logging.DEBUG
    else:
        level = logging.ERROR
    logging.basicConfig(format='[%(levelname)s]: %(message)s', level=level)


def line():
    return next(sys.stdin).strip()

def add_to_heap(L, prio, val):
    if prio == 0:
        return
    heapq.heappush(L, (prio, val))


def solution(P):
    L = [(-x, chr(ord('A') + i)) for i, x in enumerate(P)]
    heapq.heapify(L)
    sol = []
    while L:
        s = ''
        x = heapq.heappop(L)
        s += x[1]
        add_to_heap(L, x[0] + 1, x[1])
        if not(len(L) == 2 and sum(abs(x[0]) for x in L) == 2):
            x = heapq.heappop(L)
            s += x[1]
            add_to_heap(L, x[0] + 1, x[1])
        sol.append(s)
    return ' '.join(sol)


def main():
    T = int(line())  # num test cases
    for case_num in range(1, T + 1):
        line()
        P = map(int, line().split(' '))
        print "Case #%s:" % case_num, solution(P)


if __name__ == '__main__':
    setup_logging()
    main()
