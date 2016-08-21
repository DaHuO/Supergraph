# -*- coding: utf-8 -*-
import fileinput
import itertools

replacements = {"+": "-", "-": "+"}


def _find_rightmost(values_list, value):
    return next((len(values_list) - idx - 1 for idx, v in enumerate(reversed(values_list)) if v == value), None)


def _ensure_plus_on_position(sequence, position):
    flips_count = 0
    if not sequence or sequence[position] == '+':
        return flips_count

    left_plus_count = len(list(itertools.takewhile(lambda x: x == '+', sequence)))
    if left_plus_count:
        # flip all leftmost pluses to minus so that they become pluses after another flip
        flips_count += 1
        for idx in xrange(left_plus_count):
            sequence[idx] = "-"

    for idx, v in enumerate(list(reversed(sequence[:position+1]))):
        sequence[idx] = replacements[v]
    flips_count += 1
    return flips_count


def sort_cakes(sequence):
    total_flips = 0
    rightmost_minus = _find_rightmost(sequence, "-")
    while rightmost_minus is not None:
        total_flips += _ensure_plus_on_position(sequence, rightmost_minus)
        rightmost_minus = _find_rightmost(sequence, "-")
    return total_flips

def run():
    in_stream = fileinput.input()
    cases_count = int(in_stream.readline())

    for case in xrange(cases_count):
        sequence = list(in_stream.readline().strip())
        flips_count = sort_cakes(sequence)

        print("Case #{0}: {1}".format(case+1, flips_count))

if __name__ == "__main__":
    run()
