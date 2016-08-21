#!/usr/bin/python

import sys
from multiprocessing import Process

input_file = sys.argv[1] if len(sys.argv) > 1 else 'b_sample.in'
decimal_digits = set(str(i) for i in range(0, 10))

def flip_at_index(string, index):
    for i in xrange(0, index):
        if string[i] is '-':
            string[i] = '+'
        else:
            string[i] = '-'
    return ''.join(string)


def fix_pancakes(stack_string):
    flips = 0
    while stack_string != len(stack_string) * '+':
        if stack_string[0] is '+' and stack_string[-1] is '-':
            stack_string = stack_string[::-1]
            flips += 1
        elif stack_string[0] is '+':
            stack_string = flip_at_index(list(stack_string), stack_string.index('-'))
            flips += 1
        else:
            stack_string = flip_at_index(list(stack_string), stack_string.index('+'))
            flips += 1

    return flips


def parallel_pancakes(test, stack_string):
    if stack_string == len(stack_string) * '+':
        print "Case #{}: {}".format(test+1, 0)
    elif stack_string == len(stack_string) * '-':
        print "Case #{}: {}".format(test+1, 1)
    else:
        fix_pancakes(stack_string)
        print "Case #{}: {}".format(test+1, fix_pancakes(stack_string))


with open(input_file, 'r') as f:
    test_cases = int(f.readline())
    assert(1<=test_cases<=100)

    for test in xrange(0, test_cases):
        S = f.readline().rstrip('\n')
        flip_pancakes = Process(target=parallel_pancakes(test, S))
        flip_pancakes.start()

f.close()
