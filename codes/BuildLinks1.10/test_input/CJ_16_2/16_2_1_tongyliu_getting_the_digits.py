#!/usr/bin/env python

import sys

# Zero: Z
# Two: W 
# Four: U
# Six: X
# Eight: G

# Five: F
# Seven: S
# Three: R

# Nine: I
# One: O

def get_all_tha(str, digit, digit_str, indicator):
    digits = []
    while str.find(indicator) != -1:
        for c in digit_str:
            str = str.replace(c, '', 1)
        digits.append(digit)
    return str, digits

def get_tha_digits(str):
    digits = []
    str, new_digits = get_all_tha(str, '0', 'ZERO', 'Z')
    digits.extend(new_digits)
    str, new_digits = get_all_tha(str, '2', 'TWO', 'W')
    digits.extend(new_digits)
    str, new_digits = get_all_tha(str, '4', 'FOUR', 'U')
    digits.extend(new_digits)
    str, new_digits = get_all_tha(str, '6', 'SIX', 'X')
    digits.extend(new_digits)
    str, new_digits = get_all_tha(str, '8', 'EIGHT', 'G')
    digits.extend(new_digits)
    str, new_digits = get_all_tha(str, '3', 'THREE', 'R')
    digits.extend(new_digits)
    str, new_digits = get_all_tha(str, '5', 'FIVE', 'F')
    digits.extend(new_digits)
    str, new_digits = get_all_tha(str, '7', 'SEVEN', 'S')
    digits.extend(new_digits)
    str, new_digits = get_all_tha(str, '9', 'NINE', 'I')
    digits.extend(new_digits)
    str, new_digits = get_all_tha(str, '1', 'ONE', 'O')
    digits.extend(new_digits)
    return ''.join(sorted(digits))

i = 0
for line in sys.stdin:
    if i > 0:
        print 'Case #%d: %s' % (i, get_tha_digits(line))
    i += 1
