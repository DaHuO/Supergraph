__author__ = 'pcjjman'
test_input = \
"""5
0
1
2
11
1692"""
test_output = \
"""Case #1: INSOMNIA
Case #2: 10
Case #3: 90
Case #4: 110
Case #5: 5076"""

import itertools
import math
import sys
test = False
line_number = 0


def get_numbers(input_number, previously_seen):
    for i in range(0, 10):
        if str(i) not in previously_seen and str(i) in str(input_number):
            previously_seen.add(str(i))


def get_input():
    global line_number
    if not test:
        return raw_input("")
    else:
        output = test_input.split("\n")[line_number]
        line_number += 1
        return output

if __name__ == "__main__":
    cases = int(get_input())
    for case in range(cases):
        number = int(get_input())
        if number == 0:
            print "Case #{}: Insomnia".format(case + 1)
            continue
        previously_seen = set()
        first = True
        multiplier = 1
        while len(previously_seen) != 10:
            if not first:
                multiplier += 1
            first = False
            current_number = number * multiplier
            get_numbers(current_number, previously_seen)
        print "Case #{}: {}".format(case + 1, current_number)


