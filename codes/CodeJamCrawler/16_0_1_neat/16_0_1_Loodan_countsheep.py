
# Process the inputs into a list
def pre_process(file):

	data = []

	f = open(file, 'r')

	for line in f:

		data.append(int(line))

	return data


# Get digits in a number
def get_digits(num):

	digits = []

	for d in str(num):

		digits.append(d)

	return digits



# Count sheep
def count_sheep(N):

	digits = []

	for i in range(1, 101):

		count = N * i

		temp = get_digits(count)

		# Find a new digit
		for d in temp:

			if not (d in digits):

				digits.append(d)

		if len(digits) == 10:

			return count, digits

	return count, digits


if __name__ == "__main__":

	sol = open("./count_sheep.out", "r+")

	data = pre_process("./A-large.in")

	for i in range(data[0]):

		count, digits = count_sheep(data[i+1])

		if len(digits) < 10:

			sol.write("Case #{}: {}\n".format(i+1, "INSOMNIA"))

		else:

			sol.write("Case #{}: {}\n".format(i+1, count))

	sol.close()