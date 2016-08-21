# -*- coding: utf-8 -*-
import fileinput
import itertools
import sys

sys.setrecursionlimit(2000)

best_combo = None

def try_combination(so_far, chars_list, position):
    if  position == len(chars_list):
        global best_combo
        if best_combo is None or so_far > best_combo:
            best_combo = so_far
        return
    try_combination(so_far + chars_list[position], chars_list, position+1)
    try_combination(chars_list[position] + so_far, chars_list, position+1)


def run():
    in_stream = fileinput.input()
    cases_count = int(in_stream.readline())

    for case in xrange(cases_count):
        line = in_stream.readline().strip()
        global best_combo
        best_combo = None
        try_combination("", line, 0)

        print("Case #{0}: {1}".format(case+1, best_combo))


if __name__ == "__main__":
    run()
