#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
from math import sqrt
from itertools import count, islice

def parse_input(filename):
	"""
	Parse the input according to the following format

	#Test cases

	The input may of course have several test cases
	"""
	input_file = open(filename, "r")

	tc_number = int(input_file.readline())
	tc_list = []

	for i in range(tc_number):
		tc = {}
		tc['x'] = i + 1
		tc['N'], tc['J'] = [int(x) for x in
                        input_file.readline().split(' ')]

		tc_list.append(tc)

	return tc_list

def generation(n, i, coin, c, candidates):
    coin += c
    if n - 1 == i:
        candidates.append(coin + '1')
    else:
        generation(n, i + 1, coin, '0', candidates)
        generation(n, i + 1, coin, '1', candidates)

def generate_candidates(n):
    candidates = []
    generation(n, 2, '1', '0', candidates)
    generation(n, 2, '1', '1', candidates)

    if n == 2:
        return ['11']
    else:
        return candidates

def is_prime(n):
    prime = False

    if n <= 1:
        return prime, 0

    candidate_divisor = [i for i in range(2, int(sqrt(n) + 1))]
    highest_divisor = 1
    smallest_divisor = 1
    for divisor in candidate_divisor:
        if n % divisor == 0:
            smallest_divisor = divisor
            highest_divisor = n / smallest_divisor
            break

    return not (smallest_divisor > 1), highest_divisor

def jam_coins(tc):
    chosen = 0
    candidates = generate_candidates(tc['N'])

    print "Case #%i:" % tc['x']
    for candidate in candidates:
        prime = False
        result = candidate
        for b in range(2,11):
            candidate_value = int(candidate, b)
            prime, divisor = is_prime(candidate_value)

            if prime:
                break
            else:
                result = result + ' ' + str(divisor)
        if not prime:
            chosen += 1
            print result
        if chosen >= tc['J']:
            break


def main(argv):
	"""
        Give me coins with jam on top
	"""
	filename = argv[0]
	tc_list = parse_input(filename)

	for tc in tc_list:
            jam_coins(tc)

if __name__ == "__main__":
	main(sys.argv[1:])

