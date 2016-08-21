import sys

CASES = 0
CURRENT_CASE = 1
CASE_LINE_FORMAT = r"Case #%s: %s"


def get_input():
	with open(sys.argv[1], "rb") as fd:
		fd.readline()
		while True:
			line = fd.readline()
			if line == '':
				break 
			
			yield line.strip()


for line in get_input():
	count = 0
	current_char = line[0]
	for c in line:
		if c != current_char:
			current_char = c
			count += 1

	if line[-1] == '-':
		count += 1

	print CASE_LINE_FORMAT % (CURRENT_CASE, count)
	CURRENT_CASE += 1