#!/usr/bin/env python3
import sys


def main():
    input_file = sys.argv[1]
    solve(input_file)


def solve(input_file):
    with open(input_file) as f_in:
        t = int(next(f_in))
        for case in range(t):
            ins = next(f_in).rstrip()
            large = solve_instance(ins)
            print("Case #%d: %s" % (case + 1, large))


def solve_instance(large):
    first = [large[0]]
    second = []
    for c in large[1:]:
        if c >= first[-1]:
            first.append(c)
        else:
            second.append(c)
    first.reverse()
    return "".join(first) + "".join(second)


if __name__ == '__main__':
    main()
