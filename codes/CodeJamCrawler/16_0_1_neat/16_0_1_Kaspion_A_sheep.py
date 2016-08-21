import sys

def parse(lines):
	"""Parse the input file, return a generator of N's"""
	next(lines) # Get rid of the first lines, containing the number of tests

	for line in lines:
		yield int(line)

def get_digits(n):
	"""Get all decimal digits of a positive integer as a set"""
	if n == 0:
		return set([0])

	digits = set()

	# Continue until no digits left or saw all digits
	while n != 0 and len(digits) < 10:
		digits.add(n%10)
		n = n//10

	return digits

def solve(N):
	"""Find the number of times to count for a given N before falling asleep"""
	if N == 0:
		return 'INSOMNIA'

	digits_found = [False]*10
	n = 0 # holds the last number counted

	# Iterate over all i's until found 10 unique digits
	while not all(digits_found):
		n += N
		current_digits = get_digits(n)
		for digit in current_digits:
			digits_found[digit] = True

	return n

def main():
	# Expect to receive the input file name
	if len(sys.argv) < 2:
		print('Missing input file argument')
		sys.exit(1)

	input_file = sys.argv[1]
	with open(input_file) as ifile:
		for i, N in enumerate(parse(ifile)):
			counts = solve(N)
			result_line = 'Case #{i}: {counts}'.format(i=i+1, counts=counts)
			print(result_line)

if __name__=='__main__':
	main()
