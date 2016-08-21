#!/usr/bin/python

import sys
from multiprocessing import Process

input_file = sys.argv[1] if len(sys.argv) > 1 else 'a_sample.in'
decimal_digits = set(str(i) for i in range(0, 10))

def count_sheep(initial_number):
    seen_digits = set(str(initial_number))
    i = 0
    while seen_digits != decimal_digits:
        latest_number = str(initial_number * (i+1))
        for char in set(latest_number):
            seen_digits.add(char)
        i += 1
    return latest_number

def parallel_sheep(test, initial_number):
    if initial_number is 0:
        print "Case #{}: {}".format(test+1, 'INSOMNIA')
    else:
        print "Case #{}: {}".format(test+1, count_sheep(initial_number))


with open(input_file, 'r') as f:
    test_cases = int(f.readline())
    assert(0<=test_cases<=1000000)

    for test in xrange(0, test_cases):
        N = int(f.readline().rstrip('\n'))
        build_sheeps = Process(target=parallel_sheep(test, N))
        build_sheeps.start()

f.close()
