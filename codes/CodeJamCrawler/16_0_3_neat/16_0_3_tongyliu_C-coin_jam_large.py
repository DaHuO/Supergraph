#!/usr/bin/env python

import sys
import math

N = int(sys.argv[1])
J = int(sys.argv[2])

print 'Case #1:'

found = 0
inner_num = 0

while found < J:
    num_str = '1' + format(inner_num, '0' + str(N - 2) + 'b') + '1'
    print_str = num_str
    is_prime = False

    for base in range(2, 11):
        num = int(num_str, base)
        for divisor in xrange(2, int(math.sqrt(num))):
            if divisor > 100000:
                is_prime = True
                break
            if num % divisor == 0:
                print_str += ' ' + str(divisor)
                break
        else:
            is_prime = True

    if not is_prime:
        print print_str
        found += 1

    inner_num += 1
