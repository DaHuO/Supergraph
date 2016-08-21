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
		tc['N'] = int(input_file.readline())

		tc_list.append(tc)

	return tc_list

def sleeping_pills(tc):
    is_sleeping = False
    sleeping_number = tc['N']

    if sleeping_number == 0:
        print "Case #%i: INSOMNIA" % tc['x']
    else:
        i = 0
        number_report = {}

        while not is_sleeping:
            i += 1
            sleeping_number = i * tc['N']

            for c in str(sleeping_number):
                number_report[c] = True

            if len(number_report) == 10:
                is_sleeping = True
                print "Case #%i: %i" % (tc['x'], sleeping_number)

def main(argv):
	"""
        I already felt asleep Zzz....
	"""
	filename = argv[0]
	tc_list = parse_input(filename)

	for tc in tc_list:
            sleeping_pills(tc)

if __name__ == "__main__":
	main(sys.argv[1:])

