from collections import defaultdict

def counting_sheep(num):

	MAX_ITERATIONS = 10000000

	# Handle fringe cases for speed:
	if num == 0:
		return 'INSOMNIA'

	# Create a dictionary for each digit initialised to False
	# to keep track of which elements have been seen.
	digits = map(str, range(10))
	seen_digits = dict(zip(digits, [False]*len(digits)))

	iteration = 0
	all_digits_seen = False
	while iteration < MAX_ITERATIONS and not all_digits_seen:

		# Compute value
		n = (iteration+1)*num


		# Flag digits as seen
		for d in str(n):
			seen_digits[d] = True


		# Check if all digits have been seen
		all_digits_seen = True
		for d in seen_digits.keys():
			if not seen_digits[d]:
				all_digits_seen = False

			
		iteration += 1

	if all_digits_seen:
		return str(n)
	else:
		return 'INSOMNIA'


if __name__ == '__main__':

	num_test_cases = int(raw_input())

	for i in xrange(1, num_test_cases+1):

		n = int(raw_input())

		result_string = counting_sheep(n)

		print 'Case #{}: {}'.format(i, result_string)