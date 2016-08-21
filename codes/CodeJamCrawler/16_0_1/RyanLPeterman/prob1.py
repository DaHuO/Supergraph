import sys

def main():
	with open(sys.argv[1]) as file_handler:
		test_cases = file_handler.read().splitlines()

		# for each test case
		for j in range(1, int(test_cases[0])+ 1):

			N = int(test_cases[j])
			original_N = int(test_cases[j])

			digits_dict = create_dict()

			# Store first iter
			store_digits(original_N, digits_dict)

			# Note: is never possible to have first num cause sleep
			# Since at most the numbers have 7 digits
			N += original_N
			done = False

			while not done:

				# store first iter
				store_digits(N, digits_dict)

				if is_full(digits_dict):
					ans = N
					done = True

				elif N == original_N:
					ans = "INSOMNIA"
					done = True

				N += original_N

			print "Case #" + str(j) + ": " + str(ans)

# creates empty dict full of False values
def create_dict():
	digit_dict = {}

	for i in xrange(0, 10):
		digit_dict[str(i)] = False

	return digit_dict

# stores digits into dict
def store_digits(N ,digits_dict):
	digit_str = str(N)

	for char in digit_str:
		digits_dict[char] = True

# returns true if all digits have been seen
def is_full(digits_dict):

	for key, value in digits_dict.iteritems():
		# if any are false return false
		if not value:
			return False

	return True


if __name__ == '__main__':
	main()