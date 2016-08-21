#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import math
from bisect import *

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
		tc['S'] = input_file.readline()

		tc_list.append(tc)

	return tc_list

def swap(c, n):
    result = False if c == '-' else True

    for i in range(1, n+1):
        result = not(result)

    return result

def pancake_service(tc):
    swap_number = 0

    for c in reversed(tc['S']):
        if not swap(c, swap_number):
            swap_number += 1

    print "Case #%i: %i" % (tc['x'], swap_number)

def main(argv):
	"""
        So hungry, just woke up
	"""
	filename = argv[0]
	tc_list = parse_input(filename)

	for tc in tc_list:
            pancake_service(tc)

if __name__ == "__main__":
	main(sys.argv[1:])

