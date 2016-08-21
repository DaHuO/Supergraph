import sys


def get_divisor(n):
	if (n < 1):
		return None
	else:
		potential_divisor = 2

		while (potential_divisor * potential_divisor < n):
			if (n % potential_divisor == 0):
				return potential_divisor
			potential_divisor += 1

		return None


input = open(sys.argv[1], 'r')

t = input.readline()
lines = input.readlines()

for line_index in range(len(lines)):
	if (lines[line_index][-1] == '\n'):
		lines[line_index] = lines[line_index][:-1]

	[n, j] = lines[line_index].split()
	n = int(n)
	j = int(j)

	print('Case #' + str(line_index + 1) + ':')

	jamcoins_count = 0

	for potential_jamcoin in range((1 << (n - 1)) + 1, 1 << n, 2):

		is_jamcoin = True
		potential_jamcoin_bin = bin(potential_jamcoin)[2:]
		potential_jamcoin_alt_base_divisors = []

		for base in range(2, 11):
			potential_jamcoin_alt_base = int(potential_jamcoin_bin, base)

			divisor = get_divisor(potential_jamcoin_alt_base)

			if (not divisor):
				is_jamcoin = False
				break
			else:
				potential_jamcoin_alt_base_divisors.append(divisor)

		if (is_jamcoin):
			divisor_string = ' '.join(map(str, potential_jamcoin_alt_base_divisors))

			print(str(potential_jamcoin_bin) + ' ' + divisor_string)

			jamcoins_count += 1

			if (jamcoins_count >= j):
				break

input.close()
