# -*- coding: utf-8 -*-
#
# Copyright 2013 Eric Shtivelberg
#

import sys

problem = 'B-large'


# # Open the input file
input_file_name = problem + '.in'
input_file = open(input_file_name)
lines = map(str.strip, input_file.readlines())
input_file.close()

# print "Closed input file..."

# lines = '''5
# -
# -+
# +-
# +++
# --+-
# '''.split('\n')

def read_line(): return lines.pop(0)
def read_parts(): return lines.pop(0).split(' ')
def read_int(): return int(lines.pop(0))
def read_ints(): return map(int, lines.pop(0).split(' '))
def read_float(): return int(lines.pop(0))
def read_floats(): return map(float, lines.pop(0).split(' '))

# Write the output
output_file_name = problem + '.out'
output_file = open(output_file_name, 'w')
# output_file = sys.stdout

########## Contest Specific ##########

# The output list
output = []

T = read_int()

for t in range(1, T+1):
	S = read_line()
	moves_num = 0
	while '-' in S:
		last_non_happy = S.rindex('-')
		S = S[:last_non_happy+1]

		# Flip
		S = S.replace('-', '/').replace('+', '-').replace('/', '+')

		# print last_non_happy
		# print S, S[:last_non_happy+1]

		moves_num += 1

	output.append(str(moves_num))


########## Contest Specific End ##########

# print output
cases = ['Case #{}: {}'.format(i+1, output[i]) for i in range(len(output))]
output_file.write('\n'.join(cases))

output_file.close()
# print "Closed output file..."