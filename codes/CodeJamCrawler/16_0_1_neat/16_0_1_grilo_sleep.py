#!/usr/bin/env python

import sys
import os


cache = {}

def has_all_digits(number_list):
    if len(number_list) < 10: return False
    for idx, number in enumerate(number_list):
        if idx != number: return False
    return True

def number_to_digits(number):
    return [int(i) for i in str(number)]


def count_sheep(number, multiplier, zero_nine):
    if number == 0: return "INSOMNIA"

    count = number * multiplier
    for digit in number_to_digits(count):
        zero_nine[digit] = ''

    if has_all_digits(zero_nine.keys()):
        return str(count)
    else:
        return count_sheep(number, multiplier + 1, zero_nine)
    
input = None
if os.path.isfile(sys.argv[1]):
    with open(sys.argv[1]) as file:
        input = file.readlines()[1:]
else:
    input = list(sys.argv[1])

for idx, n in enumerate(input):
    idx += 1
    if n in cache: 
        count = cache[n]
    else:
        count = count_sheep(int(n), 1, {})
        cache[n] = count
    print "Case #" + str(idx) + ": " + count
