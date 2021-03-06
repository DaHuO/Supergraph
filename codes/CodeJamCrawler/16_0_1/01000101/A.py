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
	start_num = chunk
	temp_num = start_num 
	ans = 0
	full_count = [False, False, False, False, False, False, False, False, False, False,]
	true_count = 0

	for i in range(1,200):
		temp_num = int(start_num[0]) * i
		numlst = list(str(temp_num))
		for x in numlst:
			if full_count[int(x)] == False:
				full_count[int(x)] = True
				true_count += 1

		if true_count == 10:
			ans = temp_num
			return ans

	return "INSOMNIA"

lines_per_case = 1
chunks = get_chunks(lines, lines_per_case)

for i, chunk in enumerate(chunks):
	print "Case #%s: %s" % (i+1, get_answer(chunk))
