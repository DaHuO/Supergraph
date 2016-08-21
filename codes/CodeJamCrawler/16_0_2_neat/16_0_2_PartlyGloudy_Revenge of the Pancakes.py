import os

input_file = open("input_large.in", "r")
output_file = open("output_large.txt", "w")

cases = int(input_file.readline())

for i in range(cases):
	stack = list(input_file.readline()[0:-1])
	last = ""
	clean_stack = []
	for p in stack:
		if p != last:
			clean_stack.append(p)
		last = p

	frowns = clean_stack.count("-") * 2
	if clean_stack[0] == "-":
		frowns -= 1

	output_file.write("Case #" + str(i+1) + ": " + str(frowns) + "\n")