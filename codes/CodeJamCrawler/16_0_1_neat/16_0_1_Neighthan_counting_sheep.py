def main(size):
	"""
	@param size = string; small or large
	"""
	infile = size + ".in"
	# infile = "large.in"

	output = ""

	with open(infile) as file:
		num_cases = int(file.readline())
		for case in range(1, num_cases+1):
			last = find_last_number(file.readline())
			output += "Case #%s: %s\n" % (case, last)

	with open(size + ".out", 'w') as outfile:
		outfile.write(output)


def find_last_number(first):
	digits_not_seen = [str(i) for i in range(10)]
	current_number = first
	for i in xrange(2, 10000):
		digits_not_seen = find_last_helper(current_number, digits_not_seen)
		if len(digits_not_seen) == 0:
			return current_number
		current_number = str(int(first) * i)
	return "INSOMNIA"
	

def find_last_helper(current_number, digits_not_seen):
	return [digit for digit in digits_not_seen if digit not in current_number]
			

main("large")

