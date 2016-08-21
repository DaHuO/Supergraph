import os

input_file = open("input_large.in", "r")
output_file = open("output_large.txt", "w")

cases = int(input_file.readline())

all_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for i in range(cases):
	n = long(input_file.readline())

	# If n is zero, no answer will ever be found, return failure
	if n == 0:
		output_file.write("Case #" + str(i+1) + ": " + "INSOMNIA" + "\n")

	# Otherwise, keep multiplying and adding digits until all have been seen
	else:
		digits_seen = []
		j = 1
		while len(digits_seen) != 10:

			# multiply number and get list of the result's digits
			k = n * j
			new_digits = list(str(k))

			# Add any new digits to the list of digits seen so far
			for digit in new_digits:
				if digit not in digits_seen:
					digits_seen.append(digit)

			# Increment j
			j += 1

		# All digits have been seen, return n
		output_file.write("Case #" + str(i+1) + ": " + str(k) + "\n")