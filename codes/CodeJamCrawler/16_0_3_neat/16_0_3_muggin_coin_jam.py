#! /usr/bin/python
import sys
import math
import itertools as it
import numpy as np
import struct
import pickle
from threading import Thread

def find_non_trivial_divisor(number):
    first_divisor = -1

    for divisor in xrange(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            first_divisor = divisor
            break

    return first_divisor

def switch_to_dec(num_arr, in_base):
    return sum([digit * in_base**pow for (pow, digit) in enumerate(num_arr[::-1])])

def check_for_base(num_arr, in_base, known_primes, result):
    # switch to dec
    num_dec = switch_to_dec(num_arr, in_base)
    #print '{} ~ {} (base{})'.format(str(num_arr), num_dec, in_base)

    divisor = -1
    if num_dec not in known_primes:
        # search for divisor
        divisor = find_non_trivial_divisor(num_dec)

    # return (base, divisor)
    result[in_base] = divisor
    #return (in_base, divisor)

if __name__ == '__main__':
    # get path to input file
    data_file = sys.argv[1]

    # load input data
    with open(data_file) as fd:
        fd.readline()
        NJs = [(int(line.split()[0]), int(line.split()[1])) for line in fd] 

    N, J = NJs[0]

    known_primes = set([])

    cached = False
    if not cached:
        min_primes = min([switch_to_dec([1] + [0]*30 + [1], base) for base in xrange(2, 11)])
        max_primes = max([switch_to_dec([1]*32, base) for base in xrange(2, 11)])
        print 'Min primes: {} Max primes: {}'.format(min_primes, max_primes)

        with open('primes.32b', 'r') as fd:
            known_primes = set(filter(lambda prime: min_primes <= prime <= max_primes, np.fromfile(fd, dtype=np.uint32)))
            print 'Loaded {} primes!'.format(len(known_primes))

        with open('primes.cache', 'w') as fd:
            pickle.dump(known_primes, fd)
            print 'Pickled prime set!'
    else:
        with open('primes.cache', 'r') as fd:
            known_primes = pickle.load(fd)
            print 'Unpickled prime set!'



    solutions = []
    middle_generator = it.product([1, 0], repeat=(N-2))

    while len(solutions) < J:
        next_arr = [1] + list(middle_generator.next()) + [1]

        current_solution_dict = {}
        threads = []
        for base in range(2, 10):
            thread = Thread(target=check_for_base, args=(next_arr, base, known_primes, current_solution_dict))
            threads.append(thread)
            thread.start()
            #check_for_base(next_arr, base, known_primes, current_solution_dict)

        for thread in threads:
            thread.join()

        current_solution = list(current_solution_dict.iteritems())
        if all(map(lambda (base, divisor): divisor > -1, current_solution)):
            #print '{} ~ {}'.format(next_arr, ' \/ '.join(map(lambda (x, y): 'B: ' + str(x) + ' D: ' + str(switch_to_dec(next_arr, x)) + ' Div: ' + str(y), current_solution)))
            sorted_divisors = map(lambda (_, divisor): divisor, sorted(current_solution, key=lambda x:x[0]))
            solutions.append((next_arr, sorted_divisors))
            print 'SOLUTION {} ~ {} {}'.format(len(solutions), ''.join(map(str, next_arr)), ' '.join(map(lambda (_, divisor): str(divisor), current_solution)))

    #print known_primes

    with open('coin_jam_result.txt', 'w') as fd:
        fd.write('Case #1:\n')

        for (arr, divisors) in solutions:
            fd.write('{} {}\n'.format(''.join(map(str, arr)), ' '.join(map(str,divisors))))
