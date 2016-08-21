import os, sys
import math, itertools, random

# get problem letter from script name
problem_letter = sys.argv[0].split('.')[0]
data_set = sys.argv[1]
attempt_number = sys.argv[2]

input_filename = "%s-%s-%s.in" % (problem_letter, data_set, attempt_number)
input_file = open(input_filename)
lines = [line[:-1] for line in input_file.readlines()[1:]][:]

output_filename = "%s.out" % problem_letter
output_file = open(output_filename, "w+")
sys.stdout = output_file

def get_chunks(lines, n):
	for i in range(0, len(lines), n):
		yield lines[i:i+n]

def get_answer(chunk):
	chunk = ''.join(chunk)
	orig = int(chunk)
	n = 1
	known = range(10)
	while int(chunk) < 10**6 and chunk != '0':
		for char in chunk:
			known[int(char)] = 1 
			if len(set(known)) <= 1:
				return chunk
		chunk = str(orig*n)
		n += 1
	return 'INSOMNIA'
	return chunk

lines_per_case = 1
chunks = get_chunks(lines, lines_per_case)

for i, chunk in enumerate(chunks):
	print "Case #%s: %s" % (i+1, get_answer(chunk))
