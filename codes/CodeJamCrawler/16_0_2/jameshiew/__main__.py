#!/usr/bin/env python3
"""https://code.google.com/codejam/contest/6254486/dashboard"""

HAPPY = '+'
SAD = '-'


def number_of_flips_needed_to_make_all_pancakes_happy_side_up(pancakes: str) -> int:
    number_of_flips_needed = 0 if pancakes[-1] is HAPPY else 1
    for i in range(len(pancakes)-1):
        a, b = pancakes[i], pancakes[i+1]
        if a != b:
            number_of_flips_needed += 1
    return number_of_flips_needed

if __name__ == '__main__':
    import fileinput

    stdin = fileinput.input()
    T = int(next(stdin).rstrip())

    for case_no in range(1, T+1):
        S = next(stdin).rstrip()
        print('Case #{}: {}'.format(case_no, number_of_flips_needed_to_make_all_pancakes_happy_side_up(S)))
