# -*- coding: utf-8 -*-
#
# Copyright 2013 Eric Shtivelberg
#

import sys

problem = 'A-large'


# Open the input file
input_file_name = problem + '.in'
input_file = open(input_file_name)
lines = map(str.strip, input_file.readlines())
input_file.close()

# print output
# print "Closed input file..."

# lines = '''5
# 0
# 1
# 2
# 11
# 1692'''.split('\n')

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
	N = read_int()

	need_to_see = set(xrange(10))

	max_iters = 100
	for i in range(1, max_iters+1):
		digits = set(map(int, str(i * N)))
		# print N, i*N
		# print digits
		# print need_to_see
		need_to_see -= digits
		# print need_to_see
		if not need_to_see:
			break

	if not need_to_see:
		output.append(str(i * N))
	else:
		output.append('INSOMNIA')


########## Contest Specific End ##########

cases = ['Case #{}: {}'.format(i+1, output[i]) for i in range(len(output))]
output_file.write('\n'.join(cases))

output_file.close()
# print "Closed output file..."