#!/usr/bin/env python3


import sys


DIGITS = ("ZERO",
          "ONE",
          "TWO",
          "THREE",
          "FOUR",
          "FIVE",
          "SIX",
          "SEVEN",
          "EIGHT",
          "NINE")


def get_cases():
    num_cases = int(sys.stdin.readline())
    for _ in range(num_cases):
        yield sys.stdin.readline().strip()


def solve_case(case):
    combos = dict(combinations_for_length(len(case)))
    return combos[tuple(sorted(case))]


def combinations_for_length(length, current=(), current_len=0, digits=DIGITS):
    if current_len == length:
        yield (tuple(sorted("".join(current))),
               "".join(str(DIGITS.index(s)) for s in current))
        return

    if not digits:
        return

    if current_len + len(digits[0]) <= length:
        yield from combinations_for_length(length,
                                           current + (digits[0],),
                                           current_len + len(digits[0]),
                                           digits)

    yield from combinations_for_length(length,
                                       current,
                                       current_len,
                                       digits[1:])


def main():
    for index, case in enumerate(get_cases(), start=1):
        print("Case #{}: {}".format(index, solve_case(case)))


if __name__ == '__main__':
    main()
