# -*- coding: utf-8 -*-

import pdb
from collections import deque

def solve(line):
	digit_num = [0] * 10
	letter = dict()
	for x in line:
	  letter[x] = letter.get(x, 0) + 1
	# 0
	num = letter.get('Z', 0)
	if num != 0:
		digit_num[0] = num
		letter['Z'] -= num
		letter['E'] -= num
		letter['R'] -= num
		letter['O'] -= num
	# 6
	num = letter.get('X', 0)
	if num != 0:
		digit_num[6] = num
		letter['S'] -= num
		letter['I'] -= num
		letter['X'] -= num
	# 2
	num = letter.get('W', 0)
	if num != 0:
		digit_num[2] = num
		letter['T'] -= num
		letter['W'] -= num
		letter['O'] -= num
	# 4
	num = letter.get('U', 0)
	if num != 0:
		digit_num[4] = num
		letter['F'] -= num
		letter['O'] -= num
		letter['U'] -= num
		letter['R'] -= num
	# 8
	num = letter.get('G', 0)
	if num != 0:
		digit_num[8] = num
		letter['E'] -= num
		letter['I'] -= num
		letter['G'] -= num
		letter['H'] -= num
		letter['T'] -= num
	# 3
	num = letter.get('H', 0)
	if num != 0:
		digit_num[3] = num
		letter['T'] -= num
		letter['H'] -= num
		letter['R'] -= num
		letter['E'] -= num
		letter['E'] -= num
	# 5
	num = letter.get('F', 0)
	if num != 0:
		digit_num[5] = num
		letter['F'] -= num
		letter['I'] -= num
		letter['V'] -= num
		letter['E'] -= num
	# 9
	num = letter.get('I', 0)
	if num != 0:
		digit_num[9] = num
		letter['N'] -= num
		letter['I'] -= num
		letter['N'] -= num
		letter['E'] -= num
	# 1
	num = letter.get('O', 0)
	if num != 0:
		digit_num[1] = num
		letter['O'] -= num
		letter['N'] -= num
		letter['E'] -= num
	# 7
	num = letter.get('S', 0)
	if num != 0:
		digit_num[7] = num
		letter['S'] -= num
		letter['E'] -= num
		letter['V'] -= num
		letter['E'] -= num
		letter['N'] -= num

	result = ''
	for i in range(10):
		result += str(i) * digit_num[i]
	return result

def main():
	# pdb.set_trace()

	input_file = 'A-large.in.txt'
	output_file = 'out'
	output_format = 'Case #{0}: {1}\n'

	results = []

	with open(input_file, 'r') as f:
		case_total = str_to_int(f.readline())
		# for each case:
		for i in range(case_total):
			# some code . reading
			line = f.readline().strip()
			results.append(solve(line))
			
	with open(output_file, 'w') as f:
		for i in range(len(results)):
			# for each result
			f.write(output_format.format(i+1, results[i]))	


# --------------------------------------------

# '1\n' => 1
def str_to_int(s):
    return int(s.strip())

# '1 2 3' => [1, 2, 3]
def str_to_int_list(s, delimiter = ' '):
    return [int(x) for x in s.strip().split(delimiter)]

if __name__ == '__main__':
	main()



