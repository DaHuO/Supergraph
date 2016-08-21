# -*- coding: utf-8 -*-


def solve(pancakes):
    from_bottom = reversed(pancakes)

    flip_counter = 0
    good = '+'
    while True:
        pancake = next(from_bottom, None)
        if pancake != good:
            if pancake is None:
                return flip_counter
            good = pancake
            flip_counter += 1


if __name__ == '__main__':
    cases_number = int(input())
    for case_number in range(1, cases_number + 1):
        input_args = input()
        print('Case #%s: %s' % (case_number, solve(input_args)))
