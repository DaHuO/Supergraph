#!/usr/bin/env python3
import sys


def doit(input_str):
    stack = [s is '+' for s in input_str]
    rotations = 0
    while True:
        try:
            first_other = stack.index(not stack[0])
        except ValueError:
            rotations += not stack[0]
            return str(rotations)
        else:
            stack[:first_other] = [not stack[0]] * first_other
            rotations += 1


def main():
    line_count = int(sys.stdin.readline().strip())
    for case_no in range(1, line_count + 1):
        value_str = sys.stdin.readline().strip()
        result = doit(value_str)
        sys.stdout.write('Case #{}: {}\n'.format(case_no, result))


if __name__ == '__main__':
    main()
