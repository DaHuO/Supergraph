import sys

CASES = 0
CURRENT_CASE = 1

def get_input():
	with open(sys.argv[1], "rb") as fd:
		fd.readline()
		while True:
			line = fd.readline()
			if line == '':
				break 
			
			yield line.strip()





MAX_TIMEOUT = 10000
CASE_LINE_FORMAT = r"Case #%s: %s"

CASES = get_input()

for line in get_input():
	original_number = int(line)
	number = original_number
	current_timeout = 1
	new_digits = list(line)
	seen_digits = set([])

	while True:	
		number = original_number * current_timeout
		#print "%s " % (number),
		new_digits = list(str(number))
		seen_digits = seen_digits.union(new_digits)

		if seen_digits == set(['0','1','2','3','4','5','6','7','8','9']):
			print CASE_LINE_FORMAT % (CURRENT_CASE, number)
			CURRENT_CASE += 1;
			break
		elif current_timeout == MAX_TIMEOUT:
			print CASE_LINE_FORMAT % (CURRENT_CASE, "INSOMNIA")
			CURRENT_CASE += 1;
			break
		else:
			current_timeout += 1;
			
