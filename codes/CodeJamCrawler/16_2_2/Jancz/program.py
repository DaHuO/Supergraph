#!/usr/bin/env python

from sys import argv


def get_list_of_integers(a):
    values = []
    index = a.find('?')
    if index >= 0:
        for i in range(0, 10):
            values.extend(get_list_of_integers(a[:index] + str(i) + a[index + 1:]))
        return values
    else:
        return [int(a)]


def solve(a, b):
    possible_as = get_list_of_integers(a)
    possible_bs = get_list_of_integers(b)

    min_a = possible_as[0]
    min_b = possible_bs[0]
    min_abs_diff = abs(min_a - min_b)
    for i in possible_as:
        for j in possible_bs:
            new_abs_diff = abs(i - j)
            if new_abs_diff < min_abs_diff:
                min_a = i
                min_b = j
                min_abs_diff = new_abs_diff
            elif new_abs_diff == min_abs_diff and i < min_a:
                min_a = i
                min_b = j
                min_abs_diff = new_abs_diff
            elif new_abs_diff == min_abs_diff and i == min_a and j < min_b:
                min_a = i
                min_b = j
                min_abs_diff = new_abs_diff

    return '%s %s' % ((str(min_a).zfill(len(a))), (str(min_b).zfill(len(b))))


input_file = open(argv[1], 'r')
number_of_cases = int(input_file.readline())
for current_case_number in range(1, number_of_cases + 1):
    input_text = input_file.readline().strip().split(' ')
    print('Case #%i: %s' % (current_case_number, solve(input_text[0], input_text[1])))
