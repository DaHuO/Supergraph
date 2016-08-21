import sys
import os

output_format = 'Case #{0}: {1}\n'
# riddle #1
def solve_riddle(input):
	#ord(char)-97
	counter = dict()
	for i in range(26):
		counter[chr(65+i)] = 0
	for c in input:
		if c in counter:
			counter[c] += 1
		else:
			counter[c] = 1
	digits = [0]*10
	digits[0] = counter['Z']
	digits[8] = counter['G']
	digits[6] = counter['X']
	digits[7] = counter['S'] - digits[6]
	digits[2] = counter['W']
	digits[3] = counter['T'] - digits[2] - digits[8]
	digits[4] = counter['U']
	digits[5] = counter['F'] - digits[4]
	digits[9] = counter['I'] - digits[8] - digits[6] - digits[5]
	digits[1] = counter['N'] - digits[9]*2 - digits[7]
	s = ''
	for i in range(10):
		s = s + ((chr(48+i))*digits[i])
	return s

# read the input
file = open(sys.argv[1])
output = open('output.txt', 'w')
lines = file.readlines()
# the number of cases.
n = int(lines[0])
cur_line = 1
# solve the riddle and write to the output file.
for i in range(n):
	answer = solve_riddle(lines[i+1])
	output.write(output_format.format(i+1,answer))