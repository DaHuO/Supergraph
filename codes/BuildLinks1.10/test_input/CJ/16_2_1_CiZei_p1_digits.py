#!/usr/bin/env python
from collections import defaultdict
import sys

digits = [
    'ZERO',
    'ONE',
    'TWO',
    'THREE',
    'FOUR',
    'FIVE',
    'SIX',
    'SEVEN',
    'EIGHT',
    'NINE',
]

digit_check_order = [0, 2, 6, 8, 7, 5, 4, 3, 1, 9]


def get_letter_count(input_str):
    ret = defaultdict(int)
    for letter in input_str:
        ret[letter] += 1
    return ret

def has_letters(letter_count, digit):
    for letter in digits[digit]:
        if not letter_count[letter] > 0:
            return False
    return True

def decrement_letter_count(letter_count, digit):
    for letter in digits[digit]:
        letter_count[letter] -= 1

def solve_case(input_str):
    letter_count = get_letter_count(input_str)
    existing_nums = []
    for digit in digit_check_order:
        while has_letters(letter_count, digit):
            existing_nums.append(digit)
            decrement_letter_count(letter_count, digit)
    return sorted(existing_nums)

def read_and_solve():
    case_count = int(sys.stdin.readline().strip())
    for case in xrange(1, case_count + 1):
        input_str = sys.stdin.readline().strip()
        solution = solve_case(input_str)
        print "Case #{}: {}".format(case, ''.join(map(str, solution)))

if __name__ == '__main__':
    read_and_solve()
