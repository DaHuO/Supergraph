import re
from itertools import izip

def split(l, string):
	first = string[0]
	for i in range(1, len(string)):
		if string[i] != first:
			break
	else:
		return l + [first]
	l.append(string[:i])
	return split(l, string[i:])

input_file = "input"
output_file = "output"

content = open(input_file).readlines()
cases = content[1:]

regex = re.compile(r"((?<=-)\+)|((?<=\+)-)") # Split splits string around char
results = []
for case in cases:
	cakes = split([], case.strip())
	length = len(cakes)
	results.append(length - 1 if cakes[length-1][0] == "+" else length)

output = open(output_file, "w+")
for i in range(len(cases)):
	output.write("Case #" + str(i+1) + ": " + str(results[i]) + "\n")
