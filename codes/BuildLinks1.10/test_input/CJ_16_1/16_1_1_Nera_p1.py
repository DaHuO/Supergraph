import sys

MAX_ATTEMPTS = 1000

if len(sys.argv) != 3:
	print "Usage: problem1 <input file> <output file>"
	exit();

cases = []
inputFile = open(sys.argv[1], "r")
lines = inputFile.readlines()
for i in range(1, len(lines)):
	cases += [lines[i].strip()]


def find_max_index(word, start_index):
	max_char = word[start_index]
	max_index = start_index
	for i in range(start_index, -1, -1):
		if word[i] > max_char:
			max_index = i
			max_char = word[i]
	return max_index

output = open(sys.argv[2], "w")

for c in range(0, len(cases)):
	word = cases[c]
	solution = word[0]
	maxes = []

	current_index = len(word) - 1
	while current_index != 0:
		next_max = find_max_index(word, current_index)
		maxes += [next_max]
		if next_max != current_index:
			current_index = next_max
		else:
			current_index -=1
	for i in range(1, len(word)):
		if i in maxes:
			solution = word[i] + solution
		else:
			solution += word[i]
	output.write("Case #%d: %s\n" % (c + 1, solution))
output.close()

