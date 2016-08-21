import os, sys
import math, itertools, random

# get problem letter from script name
problem_letter = sys.argv[0].split('.')[0]
data_set = sys.argv[1]


input_filename = "%s-%s.in" % (problem_letter, data_set)
input_file = open(input_filename)
lines = [line[:-1] for line in input_file.readlines()[1:]][:]

output_filename = "%s.out" % problem_letter
output_file = open(output_filename, "w+")
sys.stdout = output_file

def get_chunks(lines, n):
	for i in range(0, len(lines), n):
		yield lines[i:i+n]

def get_answer(chunk):
	numy = chunk[0]
	num = int(numy)
	numbers = [1,2,3,4,5,6,7,8,9,0]
	for b in range(1,1000001):
		solution = num * b
		sleep = b
		list_num = [int(char) for char in str(solution)]
		for i in range(0, len(list_num)):
			if list_num[i] in numbers:
				numbers.remove(list_num[i])
		if numbers == []:
			return solution
		if sleep == 1000000:
			sleepy = "INSOMNIA"
			return sleepy

				
lines_per_case = 1
chunks = get_chunks(lines, lines_per_case)

for i, chunk in enumerate(chunks):
	print "Case #%s: %s" % (i+1, get_answer(chunk))
