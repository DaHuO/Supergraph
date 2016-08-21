#! /usr/bin/env python3
import sys


def swap_stack(pancake_stack, end):
    new_stack = ""
    for i in range(end + 1):
        if pancake_stack[i] == '-':
            new_stack += '+'
        else:
            new_stack += '-'
    return new_stack[::-1] + pancake_stack[end + 1:]


def b_revenge_of_the_pancakes(pancake_stack):
    swaps = 0
    while True:
        last_negative = pancake_stack.rfind('-')
        if -1 == last_negative:
            break

        if pancake_stack[0] == '-':
            pancake_stack = swap_stack(pancake_stack, last_negative)
            swaps += 1
            continue

        pos = pancake_stack.find('+')
        if -1 != pos and pos < last_negative:
            while pos + 1 < last_negative and pancake_stack[pos + 1] == '+':
                pos += 1
            pancake_stack = swap_stack(pancake_stack, pos)
            swaps += 1

        pancake_stack = swap_stack(pancake_stack, last_negative)
        swaps += 1
    return swaps


def main():
    test_cases = int(sys.stdin.readline())

    for test_case in range(test_cases):
        print("Case #{}: {}".format(test_case + 1,
                                    b_revenge_of_the_pancakes(sys.stdin.readline().strip())))


if __name__ == "__main__":
    main()
